#include <stdio.h>

/* Registra os blocos executados, como no exemplo do triangulo. */
#define ponta_de_prova(num) do { \
    if (++printed_nodes % 10) fprintf(path, " %2d ", (num)); \
    else fprintf(path, " %2d\n", (num)); \
} while (0)

int main(void)
{
    FILE *path = fopen("path.tes", "w");
    int printed_nodes = 0;
    int nota1, nota2, frequencia;
    double media;

    if (path == NULL) {
        perror("Erro ao abrir path.tes");
        return 1;
    }

    /* 1: leitura das duas notas inteiras (0 a 10) e da frequencia (0 a 100). */
    ponta_de_prova(1);
    printf("Digite duas notas inteiras (0 a 10) e a frequencia (0 a 100): ");
    if (scanf("%d %d %d", &nota1, &nota2, &frequencia) != 3) {
        /* 2: entrada nao numerica ou incompleta. */
        ponta_de_prova(2);
        printf("Entrada invalida.\n");
    } else {
        /* 3: validacao dos limites. */
        ponta_de_prova(3);
        if (nota1 < 0 || nota1 > 10 || nota2 < 0 || nota2 > 10 ||
            frequencia < 0 || frequencia > 100) {
            /* 4: valores fora dos limites. */
            ponta_de_prova(4);
            printf("Notas devem estar entre 0 e 10 e frequencia entre 0 e 100.\n");
        } else {
            /* 5: calculo da media e classificacao do aluno. */
            ponta_de_prova(5);
            media = (nota1 + nota2) / 2.0;
            printf("Media: %.1f\n", media);

            if (frequencia < 75) {
                /* 6: frequencia insuficiente, independentemente da media. */
                ponta_de_prova(6);
                printf("REPROVADO POR FALTA\n");
            /* MUTANTE 16 - Relacional: operador >= substituido por <=.
             * Original: } else if (media >= 7) {
             * A seta abaixo identifica a unica linha alterada. */
            /* --> */ } else if (media <= 7) {
                /* 7: frequencia suficiente e media de pelo menos 7. */
                ponta_de_prova(7);
                printf("APROVADO\n");
            } else if (media >= 5) {
                /* 8: frequencia suficiente e media de 5 ate menos de 7. */
                ponta_de_prova(8);
                printf("RECUPERACAO\n");
            } else {
                /* 9: frequencia suficiente e media abaixo de 5. */
                ponta_de_prova(9);
                printf("REPROVADO POR NOTA\n");
            }
        }
    }

    /* 10: encerramento. */
    ponta_de_prova(10);
    fclose(path);
    return 0;
}
