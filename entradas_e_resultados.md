# Teste de mutantes: programa.c

## Programa e regras

O programa recebe duas notas inteiras entre 0 e 10 e uma frequência inteira entre 0 e 100. Calcula a média aritmética das notas. Frequência menor que 75 reprova por falta. Com frequência suficiente, média maior ou igual a 7 aprova; média de 5 até menos de 7 leva à recuperação; média abaixo de 5 reprova por nota. Valores fora dos intervalos ou entrada incompleta/não numérica são rejeitados.

## Procedimento de execução

- Foram compilados o original e os 24 mutantes com GCC, usando `-std=c11 -Wall -Wextra -Werror -Wno-parentheses`.
- `-Wno-parentheses` permite a mistura intencional de `&&` e `||` em M22, M23 e M24. A precedência normal da linguagem C foi preservada.
- Cada caso foi executado primeiro no original e depois em M1 até M24, sempre com a mesma entrada. Foram realizadas **600 execuções**: 24 casos × 25 programas.
- As saídas da planilha foram obtidas das execuções reais. Somente a pergunta inicial, comum a todos os programas, e os espaços externos foram removidos. A média impressa faz parte da comparação, além da classificação.
- Um mutante é **MORTO** por um caso quando a saída difere da saída do original. **SOBREVIVE** indica saída igual naquele caso; o mutante ainda pode ser morto por outro caso.
- O caminho registrado pela ponta de prova foi coletado para todas as execuções. Ele é apresentado aqui para o original, mas não foi usado como critério de morte. Uma mudança na média pode matar um mutante sem mudar o caminho.
- Os executáveis e arquivos `path.tes` foram gerados em pasta temporária. Nenhum código-fonte foi alterado.

## Entradas usadas e resultados do original

Ordem da entrada: `nota1 nota2 frequencia`. As notas e a frequência são inteiros; a frequência é informada de 0 a 100, sem o símbolo `%`. Em CT24, a entrada termina após `8 8` (fim de arquivo, EOF).

| Caso | Entrada literal | Objetivo | Saída original | Caminho original | Mutantes mortos pelo caso |
|---|---|---|---|---|---|
| CT01 | `8 8 80` | Aprovação com média acima de 7. | Media: 8.0<br>APROVADO | `1 3 5 7 10` | M1, M2, M3, M11, M12, M14, M16, M17, M18 |
| CT02 | `7 7 80` | Limite exato de aprovação: média 7. | Media: 7.0<br>APROVADO | `1 3 5 7 10` | M1, M2, M3, M11, M12, M14, M15, M17, M19 |
| CT03 | `6 7 80` | Recuperação com média 6,5, imediatamente abaixo de 7. | Media: 6.5<br>RECUPERACAO | `1 3 5 8 10` | M1, M2, M3, M11, M12, M14, M16, M17, M19, M21 |
| CT04 | `5 5 80` | Limite exato de recuperação: média 5. | Media: 5.0<br>RECUPERACAO | `1 3 5 8 10` | M1, M2, M3, M11, M12, M14, M16, M17, M19, M20 |
| CT05 | `4 5 80` | Reprovação com média 4,5, imediatamente abaixo de 5. | Media: 4.5<br>REPROVADO POR NOTA | `1 3 5 9 10` | M1, M2, M3, M11, M12, M14, M16, M17, M19, M21 |
| CT06 | `0 8 80` | Menor nota 1 válida: zero. | Media: 4.0<br>REPROVADO POR NOTA | `1 3 5 9 10` | M1, M2, M3, M4, M11, M12, M14, M16, M17, M19, M21 |
| CT07 | `10 8 80` | Maior nota 1 válida: dez. | Media: 9.0<br>APROVADO | `1 3 5 7 10` | M1, M2, M3, M5, M11, M12, M14, M16, M17, M18 |
| CT08 | `8 0 80` | Menor nota 2 válida: zero. | Media: 4.0<br>REPROVADO POR NOTA | `1 3 5 9 10` | M2, M3, M6, M11, M12, M14, M16, M17, M19, M21 |
| CT09 | `8 10 80` | Maior nota 2 válida: dez. | Media: 9.0<br>APROVADO | `1 3 5 7 10` | M1, M2, M3, M7, M11, M12, M14, M16, M17, M18 |
| CT10 | `8 8 0` | Menor frequência válida: 0%. | Media: 8.0<br>REPROVADO POR FALTA | `1 3 5 6 10` | M1, M2, M3, M8, M11, M12, M13 |
| CT11 | `8 8 100` | Maior frequência válida: 100%. | Media: 8.0<br>APROVADO | `1 3 5 7 10` | M1, M2, M3, M9, M11, M12, M14, M16, M17, M18 |
| CT12 | `8 8 74` | Frequência imediatamente abaixo do mínimo: 74%. | Media: 8.0<br>REPROVADO POR FALTA | `1 3 5 6 10` | M1, M2, M3, M11, M12, M13 |
| CT13 | `8 8 75` | Limite exato de frequência suficiente: 75%. | Media: 8.0<br>APROVADO | `1 3 5 7 10` | M1, M2, M3, M10, M12, M13, M16, M17, M18 |
| CT14 | `8 8 76` | Frequência imediatamente acima do mínimo: 76%. | Media: 8.0<br>APROVADO | `1 3 5 7 10` | M1, M2, M3, M11, M12, M14, M16, M17, M18 |
| CT15 | `-1 8 80` | Nota 1 abaixo do limite permitido. | Notas devem estar entre 0 e 10 e frequencia entre 0 e 100. | `1 3 4 10` | M22 |
| CT16 | `11 8 80` | Nota 1 acima do limite permitido. | Notas devem estar entre 0 e 10 e frequencia entre 0 e 100. | `1 3 4 10` | M22, M23 |
| CT17 | `8 -1 80` | Nota 2 abaixo do limite permitido. | Notas devem estar entre 0 e 10 e frequencia entre 0 e 100. | `1 3 4 10` | M23, M24 |
| CT18 | `8 11 80` | Nota 2 acima do limite permitido. | Notas devem estar entre 0 e 10 e frequencia entre 0 e 100. | `1 3 4 10` | M24 |
| CT19 | `8 8 -1` | Frequência abaixo do limite permitido. | Notas devem estar entre 0 e 10 e frequencia entre 0 e 100. | `1 3 4 10` | Nenhum |
| CT20 | `8 8 101` | Frequência acima do limite permitido. | Notas devem estar entre 0 e 10 e frequencia entre 0 e 100. | `1 3 4 10` | Nenhum |
| CT21 | `0 0 80` | Duas notas no mínimo válido: média zero. | Media: 0.0<br>REPROVADO POR NOTA | `1 3 5 9 10` | M4, M6, M11, M12, M14, M16, M17, M19, M21 |
| CT22 | `10 10 80` | Duas notas no máximo válido: média dez. | Media: 10.0<br>APROVADO | `1 3 5 7 10` | M1, M2, M3, M5, M7, M11, M12, M14, M16, M17, M18 |
| CT23 | `abc 8 80` | Entrada não numérica: scanf não lê três inteiros. | Entrada invalida. | `1 2 10` | Nenhum |
| CT24 | `8 8` | Entrada incompleta, encerrada por EOF após duas notas. | Entrada invalida. | `1 2 10` | Nenhum |

## Correspondência e detecção dos mutantes

`Original` corresponde a `programa.c`. Cada coluna `Mn` corresponde a `programan.c`; por exemplo, M24 corresponde a `programa24.c`. Cada mutante contém uma única troca de operador em relação ao original.

| Mutante | Arquivo | Categoria | Linha original | Linha alterada | Casos que matam o mutante |
|---|---|---|---|---|---|
| M1 | programa1.c | Aritmetica | `media = (nota1 + nota2) / 2.0;` | `media = (nota1 - nota2) / 2.0;` | CT01, CT02, CT03, CT04, CT05, CT06, CT07, CT09, CT10, CT11, CT12, CT13, CT14, CT22 |
| M2 | programa2.c | Aritmetica | `media = (nota1 + nota2) / 2.0;` | `media = (nota1 * nota2) / 2.0;` | CT01, CT02, CT03, CT04, CT05, CT06, CT07, CT08, CT09, CT10, CT11, CT12, CT13, CT14, CT22 |
| M3 | programa3.c | Aritmetica | `media = (nota1 + nota2) / 2.0;` | `media = (nota1 + nota2) * 2.0;` | CT01, CT02, CT03, CT04, CT05, CT06, CT07, CT08, CT09, CT10, CT11, CT12, CT13, CT14, CT22 |
| M4 | programa4.c | Relacional | `if (nota1 < 0 &#124;&#124; nota1 > 10 &#124;&#124; nota2 < 0 &#124;&#124; nota2 > 10 &#124;&#124;` | `if (nota1 <= 0 &#124;&#124; nota1 > 10 &#124;&#124; nota2 < 0 &#124;&#124; nota2 > 10 &#124;&#124;` | CT06, CT21 |
| M5 | programa5.c | Relacional | `if (nota1 < 0 &#124;&#124; nota1 > 10 &#124;&#124; nota2 < 0 &#124;&#124; nota2 > 10 &#124;&#124;` | `if (nota1 < 0 &#124;&#124; nota1 >= 10 &#124;&#124; nota2 < 0 &#124;&#124; nota2 > 10 &#124;&#124;` | CT07, CT22 |
| M6 | programa6.c | Relacional | `if (nota1 < 0 &#124;&#124; nota1 > 10 &#124;&#124; nota2 < 0 &#124;&#124; nota2 > 10 &#124;&#124;` | `if (nota1 < 0 &#124;&#124; nota1 > 10 &#124;&#124; nota2 <= 0 &#124;&#124; nota2 > 10 &#124;&#124;` | CT08, CT21 |
| M7 | programa7.c | Relacional | `if (nota1 < 0 &#124;&#124; nota1 > 10 &#124;&#124; nota2 < 0 &#124;&#124; nota2 > 10 &#124;&#124;` | `if (nota1 < 0 &#124;&#124; nota1 > 10 &#124;&#124; nota2 < 0 &#124;&#124; nota2 >= 10 &#124;&#124;` | CT09, CT22 |
| M8 | programa8.c | Relacional | `frequencia < 0 &#124;&#124; frequencia > 100) {` | `frequencia <= 0 &#124;&#124; frequencia > 100) {` | CT10 |
| M9 | programa9.c | Relacional | `frequencia < 0 &#124;&#124; frequencia > 100) {` | `frequencia < 0 &#124;&#124; frequencia >= 100) {` | CT11 |
| M10 | programa10.c | Relacional | `if (frequencia < 75) {` | `if (frequencia <= 75) {` | CT13 |
| M11 | programa11.c | Relacional | `if (frequencia < 75) {` | `if (frequencia > 75) {` | CT01, CT02, CT03, CT04, CT05, CT06, CT07, CT08, CT09, CT10, CT11, CT12, CT14, CT21, CT22 |
| M12 | programa12.c | Relacional | `if (frequencia < 75) {` | `if (frequencia >= 75) {` | CT01, CT02, CT03, CT04, CT05, CT06, CT07, CT08, CT09, CT10, CT11, CT12, CT13, CT14, CT21, CT22 |
| M13 | programa13.c | Relacional | `if (frequencia < 75) {` | `if (frequencia == 75) {` | CT10, CT12, CT13 |
| M14 | programa14.c | Relacional | `if (frequencia < 75) {` | `if (frequencia != 75) {` | CT01, CT02, CT03, CT04, CT05, CT06, CT07, CT08, CT09, CT11, CT14, CT21, CT22 |
| M15 | programa15.c | Relacional | `} else if (media >= 7) {` | `} else if (media > 7) {` | CT02 |
| M16 | programa16.c | Relacional | `} else if (media >= 7) {` | `} else if (media <= 7) {` | CT01, CT03, CT04, CT05, CT06, CT07, CT08, CT09, CT11, CT13, CT14, CT21, CT22 |
| M17 | programa17.c | Relacional | `} else if (media >= 7) {` | `} else if (media < 7) {` | CT01, CT02, CT03, CT04, CT05, CT06, CT07, CT08, CT09, CT11, CT13, CT14, CT21, CT22 |
| M18 | programa18.c | Relacional | `} else if (media >= 7) {` | `} else if (media == 7) {` | CT01, CT07, CT09, CT11, CT13, CT14, CT22 |
| M19 | programa19.c | Relacional | `} else if (media >= 7) {` | `} else if (media != 7) {` | CT02, CT03, CT04, CT05, CT06, CT08, CT21 |
| M20 | programa20.c | Relacional | `} else if (media >= 5) {` | `} else if (media > 5) {` | CT04 |
| M21 | programa21.c | Relacional | `} else if (media >= 5) {` | `} else if (media <= 5) {` | CT03, CT05, CT06, CT08, CT21 |
| M22 | programa22.c | Logica | `if (nota1 < 0 &#124;&#124; nota1 > 10 &#124;&#124; nota2 < 0 &#124;&#124; nota2 > 10 &#124;&#124;` | `if (nota1 < 0 && nota1 > 10 &#124;&#124; nota2 < 0 &#124;&#124; nota2 > 10 &#124;&#124;` | CT15, CT16 |
| M23 | programa23.c | Logica | `if (nota1 < 0 &#124;&#124; nota1 > 10 &#124;&#124; nota2 < 0 &#124;&#124; nota2 > 10 &#124;&#124;` | `if (nota1 < 0 &#124;&#124; nota1 > 10 && nota2 < 0 &#124;&#124; nota2 > 10 &#124;&#124;` | CT16, CT17 |
| M24 | programa24.c | Logica | `if (nota1 < 0 &#124;&#124; nota1 > 10 &#124;&#124; nota2 < 0 &#124;&#124; nota2 > 10 &#124;&#124;` | `if (nota1 < 0 &#124;&#124; nota1 > 10 &#124;&#124; nota2 < 0 && nota2 > 10 &#124;&#124;` | CT17, CT18 |

## Resultado do conjunto

- Mutantes avaliados: **24**.
- Mutantes mortos por pelo menos um caso: **24**.
- Mutantes sobreviventes ao conjunto: **0**.
- Escore de mutação observado: **24 / 24 = 100%**.
- Todos os 24 mutantes tiveram uma diferença observável em pelo menos uma entrada; portanto, nenhum deles foi equivalente ao original nestes testes. O conjunto não pretende esgotar todas as possíveis entradas.

## Organização do Excel

- **Resultados:** mesmo esquema da planilha do triângulo, com `Caso de Teste`, `Original` e `M1` até `M24`. Todas as combinações foram preenchidas. Células de mutantes diferentes do original recebem destaque vermelho.
- **Detecção:** compara, por fórmulas, cada saída com a do original. Mostra MORTO/SOBREVIVE por caso, quantos casos matam cada mutante e o escore do conjunto.
- **Entradas:** valores usados, objetivo de cada caso, caminho original e relação entre mutantes, arquivos e alterações.
- As saídas são registros fixos das execuções. Alterar uma entrada no Excel não executa os programas C novamente. Para atualizar os resultados, é necessário recompilar/executar e substituir as saídas coletadas.

## Referências locais

- Estrutura de tabela: `Exemplos/Mutacao_triangulo_mais_atual/casos_de_teste_triangulo_mutation.ods`.
- Operadores permitidos: `Operacoes_validas/operadores_mutacao.pdf`.
- Código avaliado: `Nova atividade/programa.c` e `Nova atividade/programa1.c` a `programa24.c`.

## Identificação dos códigos avaliados

SHA-256 dos arquivos usados, para identificar a versão exata destas execuções:

| Arquivo | SHA-256 |
|---|---|
| programa.c | `feb91edb36315b6ecd4c9bf75121de6e52df4bec55070c38ca97bd95cb2dad94` |
| programa1.c | `dcf7a22d59ab3d2dc25ebc2853446ebd2c87525a5ea6e66b5c91c150209a9b14` |
| programa2.c | `ee5da9619ff2f967e2ca1a1ed062182cd8a084f03ec91e2c61266a2496cb16aa` |
| programa3.c | `712deb8aac2422ee62fb9c78cbae16fb7da32f724859c24eb5d0f9381c131b8a` |
| programa4.c | `7bc24cca27fd5cc211446492f1892cb4f5b0c834aa2a5780ce49589bac8a54fa` |
| programa5.c | `894e81f52d563d1b1d31f9aca19c73854d7efd03d26efab17e3bd4ee0836ea41` |
| programa6.c | `3b68f4515116c84b071549b62338b8a8be920466ec8de7a628fe58938aa2b54d` |
| programa7.c | `d3d147b8dd54156d297f45307c160c19882b6a53ef1bee44e19a6c145b6ed087` |
| programa8.c | `2e2fdf29840997b3ccf11a86dba545f7e68c6e85ed806fb9c02407e169dc81ea` |
| programa9.c | `6fb7ad6752ee973d5eacd6a11a4332b9141ffb1e86e7c47f3af093d4d79bb3c4` |
| programa10.c | `82ca076166f0f66e8dde90229b8e5790aa530768378fe72e0a0f6a6fc74e5fc3` |
| programa11.c | `87cc50647a6ebca7a8cfc4782ca9b8c268f828b55c0b3fefa8c3a87ab327b30f` |
| programa12.c | `a148201082c2051d2d30d1be300f4f849d462187940487368fa21dd3f5cfe946` |
| programa13.c | `5ce0a6bbb70f5c3ab76dda13391f62b59f791792f1c8fa1ded7fde45dcbfd580` |
| programa14.c | `f0ff4a6e20a026f1a6d779475edc2bc7c955ba527b8eb81b1b2c0b834144e739` |
| programa15.c | `6ad5356f5cbba87449db2baea200dd5837a64942475bcacaf186d3a4a6a70405` |
| programa16.c | `0b3fa7f4824f412410e70124bf0231d317c07601ea285f4973e6ec7f6f5f71f6` |
| programa17.c | `c7a6b4916656b83ee15caf95970a35824ec21e024393df586e3606f807031425` |
| programa18.c | `92a9fe63a15e0707a16a7609fdab23717d75a78b2c55c93961fa23dbf4da7ccf` |
| programa19.c | `2a6dc7c48313ef27b3007e69234560c714c331f4bb2786a88642815f9d1de514` |
| programa20.c | `cb64d2c32513f88a7b30ebcc2d571e85b27cf2de638f667d2b1824c9dd6e68db` |
| programa21.c | `6d120b8d4f7a36befb2ddb650867b2177ee717d3d0c9e0615ae3dd0c6a16a4d5` |
| programa22.c | `ea5453838c1c3321c605855c0274a2a95a196f9d76fb9c8fe7c577a34770a755` |
| programa23.c | `694d3ed13f3af271a07cabb45ad1525875c5be9e3fb65c4c50e49367e2d0da1a` |
| programa24.c | `c3d08a9f52310cc76bf978c4671071bf53f8db0274c81ddb0b0e11dfa5c49c80` |
