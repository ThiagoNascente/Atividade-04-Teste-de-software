"""Chama, em sequencia, os executores locais dos 24 mutantes."""
import argparse
from pathlib import Path
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--caso", type=int, choices=range(25), default=0,
                        metavar="0..24", help="0 executa os 24 casos (padrao)")
    parser.add_argument("--compilador", help="GCC/Clang: nome ou caminho completo")
    args = parser.parse_args()
    raiz = Path(__file__).resolve().parent
    for numero in range(25):
        pasta = raiz / (f"Mutante{numero:02d}" if numero else "Original")
        comando = [sys.executable, str(pasta / "executar.py"), "--caso", str(args.caso)]
        if numero:
            comando.append("--reutilizar-original")
        if args.compilador:
            comando.extend(["--compilador", args.compilador])
        print(f"\n=== {pasta.name} ({numero}/24) ===", flush=True)
        try:
            processo = subprocess.run(comando, cwd=str(raiz))
        except OSError as erro:
            print(f"ERRO ao iniciar {pasta.name}: {erro}", file=sys.stderr)
            return 1
        if processo.returncode:
            print(f"Execucao interrompida: {pasta.name} retornou codigo {processo.returncode}.",
                  file=sys.stderr)
            return 1
    print("\nConcluido: os 24 executores de mutantes terminaram com sucesso.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
