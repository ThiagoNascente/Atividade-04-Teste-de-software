# Execução dos casos de teste

## Requisitos

- Windows, Linux ou macOS com Python 3.8 ou superior.
- GCC ou Clang instalado e disponível no PATH, ou indicado com `--compilador`.
- Somente a biblioteca padrão do Python, sem pacotes adicionais.

## Executar todos os mutantes

Abra o terminal na raiz de `Nova atividade` e execute:

```bash
python .\executar.py
```

No Linux e macOS:

```bash
python3 ./executar.py
```

O executor geral primeiro chama o executor de `Original`, compilando o original uma vez e executando seus 24 casos uma única vez. Depois chama os executores de `Mutante01` até `Mutante24`, em sequência, reutilizando as referências recém-geradas. Cada mutante é compilado uma vez e executa seus 24 casos. São **600 execuções** no total (24 do original + 24 × 24 dos mutantes), mantendo as evidências e os resumos nas respectivas pastas.

Para executar somente CT03 em todos os mutantes, use `python .\executar.py --caso 3` (Linux/macOS: `python3 ./executar.py --caso 3`). Nesse modo são 25 execuções: uma do original e uma de cada mutante. Também é possível passar `--compilador clang` ou o caminho do compilador; os argumentos são encaminhados a cada executor local.

Se algum executor falhar, o geral interrompe a sequência e retorna código 1. Ao concluir todos, retorna zero. Os executores individuais continuam disponíveis conforme os comandos abaixo.

## Executar a partir da raiz da pasta

No Windows, fica assim executar o Original e o Mutante01:

```bash
python .\Original\executar.py
python .\Mutante01\executar.py
```

Troque `Mutante01` por `Mutante02` até `Mutante24` para selecionar outro.

No Linux e macOS:

```bash
python3 ./Original/executar.py
python3 ./Mutante01/executar.py
```

O executor do original compila e executa somente o original nos 24 casos. O executor de um mutante compila o original e aquele mutante uma vez cada, executa os 24 casos em ambos (48 execuções) e compara as saídas. Os demais mutantes não são executados.

## Executar um caso específico

Para CT03:

```bash
python .\Original\executar.py --caso 3
python .\Mutante01\executar.py --caso 3
```

No Linux e macOS:

```bash
python3 ./Original/executar.py --caso 3
python3 ./Mutante01/executar.py --caso 3
```

## Resultados

- `entrada.txt`: entrada do caso.
- `saida.txt`: saída completa do programa.
- `erros.txt`: saída de erro, normalmente vazia.
- `resultado.txt`: referência original, MORTO ou SOBREVIVE NESTE CASO.
- `path_ct01.tes` até `path_ct24.tes`: ponta de prova de cada execução.
