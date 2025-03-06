from time import sleep

from classes.matriz import Matriz


def soma_ou_subtracao_matrizes(num: int, mat1: Matriz, mat2: Matriz) -> None:
    if mat1.linha == mat2.linha and mat1.coluna == mat2.coluna:
        matriz_resultado: Matriz = Matriz(0, mat1.linha, mat1.coluna)

        matriz_temp: list[list[int]] = []
        for i in range(mat1.linha):
            matriz_temp.append([])
            for j in range(mat1.coluna):
                if num == 5:
                    matriz_temp[i].append(mat1.matriz[i][j] + mat2.matriz[i][j])
                else:
                    matriz_temp[i].append(mat1.matriz[i][j] - mat2.matriz[i][j])
        matriz_resultado.matriz = matriz_temp

        if num == 5:
            print("Matriz resultante da soma: ")
        else:
            print("Matriz resultante da subtração: ")
        print(matriz_resultado.mostrar_matriz())
        sleep(5)
    else:
        if num == 5:
            print("Só é possível fazer a soma entre matrizes com linhas e colunas iguais.")
        else:
            print("Só é possível fazer a subtração entre matrizes com linhas e colunas iguais.")
        sleep(3)


def multiplicacao_matrizes(mat1: Matriz, mat2: Matriz) -> None:
    if mat1.coluna == mat2.linha:
        matriz_resultado: Matriz = Matriz(0, mat1.linha, mat2.coluna)

        matriz_temp: list[list[int]] = []
        for i in range(mat1.linha):
            matriz_temp.append([])
            for j in range(mat2.coluna):
                soma = 0
                for k in range(mat1.coluna):
                    soma += mat1.matriz[i][k] * mat2.matriz[k][j]
                matriz_temp[i].append(soma)

        matriz_resultado.matriz = matriz_temp

        print("Matriz resultante da multiplicação: ")
        print(matriz_resultado.mostrar_matriz())
        sleep(5)
    else:
        print("Só é possível fazer a multiplicação entre matrizes quando\n"
              "o número de colunas da primeira matriz for igual ao número de linhas da segunda matriz.")
        sleep(4)


def determinante(mat: Matriz) -> None:
    if mat.linha == mat.coluna:
        mat_calc: list[lis[int]] = mat.matriz

        if mat.linha == 1:
            determinante = mat_calc[0][0]
        elif mat.linha == 2:
            determinante = mat_calc[0][0] * mat_calc[1][1] - mat_calc[0][1] * mat_calc[1][0]
        else: # Regra de Sarrus para determinante 3x3
            determinante = (mat_calc[0][0] * mat_calc[1][1] * mat_calc[2][2] +
                            mat_calc[0][1] * mat_calc[1][2] * mat_calc[2][0] +
                            mat_calc[0][2] * mat_calc[1][0] * mat_calc[2][1])

            determinante -= (mat_calc[0][2] * mat_calc[1][1] * mat_calc[2][0] +
                             mat_calc[0][0] * mat_calc[1][2] * mat_calc[2][1] +
                             mat_calc[0][1] * mat_calc[1][0] * mat_calc[2][2])

        print(f"O determinante da matriz com o código {mat.codigo}: {determinante}")
        sleep(5)
    else:
        print("Só é possível fazer o determinante de matriz quadrada\n(número de linhas igual ao número de colunas).")
        sleep(4)