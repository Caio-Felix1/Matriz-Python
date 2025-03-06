from time import sleep

import funcoes.func_auxiliares as aux
from classes.matriz import Matriz, GerenciadorMatrizes
from funcoes.operacao import (soma_ou_subtracao_matrizes,
                              multiplicacao_matrizes,
                              determinante)


gerenciador = GerenciadorMatrizes()


def main() -> None:
    menu()


def titulo(texto: str) -> None:
    print("=" * 50)
    print(texto.center(50, ' '))
    print('=' * 50)


def menu() -> None:
    titulo("Cálculo de Matrizes")

    print("1 - Criar Matriz")
    print("2 - Listar Matrizes")
    print("3 - Alterar elementos de Matriz")
    print("4 - Remover Matriz")
    print("5 - Soma de Matrizes")
    print("6 - Subtração de Matrizes")
    print("7 - Multiplicação de Matrizes")
    print("8 - Determinante da Matriz")
    print("9 - Sair do Programa")

    try:
        resp = int(input("Selecione uma das opções: "))
    except:
        resp: int = 0

    if resp == 1:
        titulo("Criação de Matriz")
        criar_matriz()
    elif resp == 2:
        titulo("Lista de Matrizes")
        listar_matrizes()
    elif resp == 3:
        titulo("Alteração de Matriz")
        alteracao_matriz()
    elif resp == 4:
        titulo("Remoção de Matriz")
        remover_matriz()
    elif resp == 5:
        titulo("Soma de Matrizes")
        chamar_soma_ou_subtracao(resp)
    elif resp == 6:
        titulo("Subtração de Matrizes")
        chamar_soma_ou_subtracao(resp)
    elif resp == 7:
        titulo("Multiplicação de Matrizes")
        chamar_multiplicacao()
    elif resp == 8:
        titulo("Determinante de Matriz")
        chamar_determinante()
    elif resp == 9:
        print("Encerrando o programa...")
        sleep(2)
        exit(0)
    else:
        print("Opção inválida.")
        sleep(2)
        menu()


def criar_matriz() -> None:
    global gerenciador

    linhas: int = aux.validar_dados("Digite o número de linhas da matriz [máximo de 3 linhas]: ", True)
    colunas: int = aux.validar_dados("Digite o número de colunas da matriz [máximo de 3 colunas]: ", True)

    matriz_nova: Matriz = gerenciador.criar_matriz(linhas, colunas)

    matriz_temporaria: list[list[int]] = []
    for i in range(0, linhas):
        matriz_temporaria.append([])
        for j in range(0, colunas):
            matriz_temporaria[i].append(aux.validar_dados(f"Digite o elemento da posição {i+1}x{j+1}: "))
    matriz_nova.matriz = matriz_temporaria

    print(f"A matriz {linhas}x{colunas} foi criada.")
    sleep(3)
    menu()


def listar_matrizes(voltar_menu: bool = True, verificar_existe: bool = True) -> None:
    global gerenciador

    if verificar_existe:
        if not aux.verificar_existencia_de_matrizes(gerenciador):
            menu()

    gerenciador.exibir_matrizes(1.5)

    if voltar_menu:
        sleep(3)
        menu()


def alteracao_matriz() -> None:
    global gerenciador

    listar_matrizes(False)

    codigo = aux.validar_dados("Digite o código da matriz que deseja alterar: ")

    if not aux.verificar_matriz_com_codigo(gerenciador, codigo):
        menu()

    matriz_selecionada: Matriz = aux.pegar_matriz_por_codigo(gerenciador, codigo)

    linha_elemento = aux.obter_posicao("Digite a linha da posição do elemento que deseja alterar: ",
                                   matriz_selecionada.linha,
                                   "linhas")

    coluna_elemento = aux.obter_posicao("Digite a coluna da posição do elemento que deseja alterar: ",
                                    matriz_selecionada.coluna,
                                    "colunas")

    elemento = aux.validar_dados(f"Insira o valor na posição {linha_elemento}x{coluna_elemento}: ")

    matriz_selecionada.matriz[linha_elemento-1][coluna_elemento-1] = elemento

    print(f"O elemento na posição {linha_elemento}x{coluna_elemento} foi alterado.")

    while (resp := input("Deseja alterar outro elemento [S/N]? ").upper().strip()) not in ["S", "N", "SIM", "NÃO", "NAO"]:
        print("Resposta inválida. Digite novamente!")

    if resp in ["SIM", "S"]:
        titulo("Alteração de Matriz")
        alteracao_matriz()
    else:
        sleep(3)
        menu()


def remover_matriz() -> None:
    global gerenciador

    listar_matrizes(False)

    codigo = aux.validar_dados("Digite o código da matriz que deseja remover: ")

    if not aux.verificar_matriz_com_codigo(gerenciador, codigo):
        menu()

    gerenciador.remover_matriz(codigo)

    print(f"A matriz com o código {codigo} foi removida.")

    sleep(3)
    menu()


def chamar_soma_ou_subtracao(num: int) -> None:
    global gerenciador

    if not aux.verificar_duas_matrizes(gerenciador):
        menu()

    listar_matrizes(False, False)

    duas_matrizes = aux.obter_duas_matrizes(gerenciador)
    if duas_matrizes:  # Tupla com elementos == True
        matriz1, matriz2 = duas_matrizes
    else:
        menu()

    soma_ou_subtracao_matrizes(num, matriz1, matriz2)
    menu()


def chamar_multiplicacao() -> None:
    global gerenciador

    if not aux.verificar_duas_matrizes(gerenciador):
        menu()

    listar_matrizes(False, False)

    duas_matrizes = aux.obter_duas_matrizes(gerenciador)
    if duas_matrizes:
        matriz1, matriz2 = duas_matrizes
    else:
        menu()

    multiplicacao_matrizes(matriz1, matriz2)
    menu()


def chamar_determinante() -> None:
    global gerenciador

    listar_matrizes(False)

    codigo = aux.validar_dados("Digite o código da matriz que deseja fazer o determinante: ")

    if not aux.verificar_matriz_com_codigo(gerenciador, codigo):
        menu()

    mat: Matriz = aux.pegar_matriz_por_codigo(gerenciador, codigo)

    determinante(mat)
    menu()


if __name__ == '__main__':
    main()