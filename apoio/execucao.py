"""Executor compartilhado para Windows, Linux e macOS; apenas biblioteca padrao."""
import argparse
import os
from pathlib import Path
import shutil
import subprocess
import sys

RAIZ = Path(__file__).resolve().parent.parent


def salvar(arquivo, texto):
    arquivo.write_text(texto, encoding="utf-8")


def compilar(pasta, nome, compilador):
    executavel = pasta / (nome + (".exe" if os.name == "nt" else ""))
    processo = subprocess.run(
        [compilador, "-std=c11", "-Wall", "-Wextra", "-Werror",
         "-Wno-parentheses", str(pasta / (nome + ".c")), "-o", str(executavel)],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    salvar(pasta / "compilacao.txt", processo.stdout + processo.stderr)
    if processo.returncode:
        raise RuntimeError(f"Falha de compilacao: {pasta}. Consulte compilacao.txt.")
    return executavel


def rodar(executavel, pasta, ct, entrada):
    destino = pasta / "casos_de_teste" / ct
    caminho = destino / f"path_{ct.lower()}.tes"
    for nome in ("saida.txt", "erros.txt", "resultado.txt", caminho.name):
        arquivo = destino / nome
        if arquivo.exists():
            arquivo.unlink()
    try:
        processo = subprocess.run(
            [str(executavel), str(caminho)], cwd=str(destino), input=entrada,
            capture_output=True, text=True, encoding="utf-8", errors="replace",
            timeout=10,
        )  # communicate fecha stdin, incluindo o EOF necessario para CT24.
    except subprocess.TimeoutExpired as erro:
        salvar(destino / "saida.txt", (erro.stdout or b"").decode("utf-8", "replace"))
        salvar(destino / "erros.txt", (erro.stderr or b"").decode("utf-8", "replace"))
        salvar(destino / "resultado.txt", "ERRO: tempo limite de 10 segundos excedido.\n")
        raise RuntimeError(f"Tempo limite excedido: {pasta.name}/{ct}") from erro
    salvar(destino / "saida.txt", processo.stdout)
    salvar(destino / "erros.txt", processo.stderr)
    if processo.returncode or not caminho.is_file() or caminho.stat().st_size == 0:
        salvar(destino / "resultado.txt", f"ERRO DE EXECUCAO; codigo={processo.returncode}\n")
        raise RuntimeError(f"Falha de execucao ou ponta de prova ausente: {pasta.name}/{ct}")
    return processo.stdout


def main(mutante_local):
    parser = argparse.ArgumentParser(description="Compila e executa os casos de teste com ponta de prova.")
    parser.add_argument("--caso", type=int, choices=range(25), default=0,
                        metavar="0..24", help="0 executa todos os casos (padrao)")
    parser.add_argument("--compilador", help="GCC/Clang: nome no PATH ou caminho completo")
    if mutante_local:
        parser.add_argument("--reutilizar-original", action="store_true", help=argparse.SUPPRESS)
    args = parser.parse_args()
    mutante = mutante_local
    pasta_resumo = RAIZ / f"Mutante{mutante:02d}" if mutante else RAIZ / "Original"
    nome_resumo = f"resumo_m{mutante:02d}_ct{args.caso:02d}.md" if mutante else f"resumo_original_ct{args.caso:02d}.md"
    resumo = pasta_resumo / nome_resumo
    try:
        compilador = args.compilador or shutil.which("gcc") or shutil.which("clang")
        if not compilador or not shutil.which(compilador):
            raise RuntimeError("Compilador nao encontrado. Instale GCC/Clang ou use --compilador CAMINHO.")
        casos = [args.caso] if args.caso else list(range(1, 25))
        mutantes = [mutante] if mutante else []
        # Valida todas as entradas antes de substituir evidencias.
        entradas = {}
        for n in casos:
            ct = f"CT{n:02d}"
            entradas[ct] = (RAIZ / "Original" / "casos_de_teste" / ct / "entrada.txt").read_text(encoding="utf-8")
            for m in mutantes:
                arquivo = RAIZ / f"Mutante{m:02d}" / "casos_de_teste" / ct / "entrada.txt"
                if arquivo.read_text(encoding="utf-8") != entradas[ct]:
                    raise RuntimeError(f"Entrada de Mutante{m:02d}/{ct} difere do original.")
        salvar(resumo, "# Execucao em andamento\n\nAinda nao ha resultado final desta tentativa.\n")
        original = RAIZ / "Original"
        referencias = {}
        if mutante and args.reutilizar_original:
            # O executor geral acabou de gerar estas referencias; nao recompilar nem executar.
            for ct in entradas:
                destino = original / "casos_de_teste" / ct
                caminho = destino / f"path_{ct.lower()}.tes"
                if ((destino / "resultado.txt").read_text(encoding="utf-8").strip() != "REFERENCIA ORIGINAL"
                        or not caminho.is_file() or caminho.stat().st_size == 0):
                    raise RuntimeError(f"Referencia original invalida: {ct}. Execute o original primeiro.")
                referencias[ct] = (destino / "saida.txt").read_text(encoding="utf-8")
            print("Referencias do original reutilizadas nesta execucao.")
        else:
            exe_original = compilar(original, "programa", compilador)
            for ct, entrada in entradas.items():
                referencias[ct] = rodar(exe_original, original, ct, entrada)
                salvar(original / "casos_de_teste" / ct / "resultado.txt", "REFERENCIA ORIGINAL\n")
                print(f"Original | {ct} | referencia registrada")
        linhas = ["# Resultado da execucao", "", f"Casos: {len(casos)}. Mutantes: {len(mutantes)}.",
                  "", "| Programa | Caso | Resultado |", "|---|---|---|"]
        if not mutante:
            linhas.extend(f"| Original | {ct} | REFERENCIA ORIGINAL |" for ct in entradas)
        for m in mutantes:
            pasta = RAIZ / f"Mutante{m:02d}"
            exe = compilar(pasta, f"programa{m}", compilador)
            for ct, entrada in entradas.items():
                saida = rodar(exe, pasta, ct, entrada)
                status = "MORTO" if saida != referencias[ct] else "SOBREVIVE NESTE CASO"
                salvar(pasta / "casos_de_teste" / ct / "resultado.txt",
                       f"{status}\nComparacao da saida completa com Original/{ct}; ponta de prova apenas informativa.\n")
                linhas.append(f"| {pasta.name} | {ct} | {status} |")
                print(f"{pasta.name} | {ct} | {status}")
        salvar(resumo, "\n".join(linhas) + "\n")
        print(f"Concluido. Resumo: {resumo}")
        return 0
    except (OSError, RuntimeError) as erro:
        salvar(resumo, f"# Execucao interrompida\n\n{erro}\n\nEvidencias podem estar parciais.\n")
        print(f"ERRO: {erro}", file=sys.stderr)
        return 1



