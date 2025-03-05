from time import sleep

from classes.matriz import Matriz, GerenciadorMatrizes


gerenciador = GerenciadorMatrizes()


def main() -> None:
    menu()


def titulo(texto: str) -> None:
    print("=" * 50)
    print(texto.center(50, ' '))
    print('=' * 50)


def validar_dados(texto: str, criacao_matriz: bool = False) -> int:
    while True:
        try:
            resposta = int(input(texto))
            if criacao_matriz and resposta <= 0:
                print("Não existe matriz com linhas e/ou colunas negativas ou iguais a zero. Digite novamente!")
                continue
            elif criacao_matriz and resposta > 3:
                print("O limite da matriz permitido pelo programa é de ordem 3. Digite novamente!")
                continue
            return resposta
        except:
            print("Valor inválido. Digite um número inteiro!")


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
        soma_matrizes()
    elif resp == 6:
        titulo("Subtração de Matrizes")
        subtracao_matrizes()
    elif resp == 7:
        titulo("Multiplicação de Matrizes")
        multiplicacao_matrizes()
    elif resp == 8:
        titulo("Determinante de Matriz")
        determinante()
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

    linhas: int = validar_dados("Digite o número de linhas da matriz [máximo de 3 linhas]: ", True)
    colunas: int = validar_dados("Digite o número de colunas da matriz [máximo de 3 colunas]: ", True)

    matriz_nova: Matriz = gerenciador.criar_matriz(linhas, colunas)

    matriz_temporaria: list[int] = []
    for i in range(0, linhas):
        matriz_temporaria.append([])
        for j in range(0, colunas):
            matriz_temporaria[i].append(validar_dados(f"Digite o elemento da posição {i+1}x{j+1}: "))
    matriz_nova.matriz = matriz_temporaria

    print(f"A matriz {linhas}x{colunas} foi criada.")
    sleep(3)
    menu()


def listar_matrizes(voltar_menu: bool = True) -> None:
    global gerenciador

    verificar_existencia_de_matrizes()

    gerenciador.exibir_matrizes(1.5)

    if voltar_menu:
        sleep(3)
        menu()


def alteracao_matriz() -> None:
    global gerenciador

    listar_matrizes(False)

    codigo = validar_dados("Digite o código da matriz que deseja alterar: ")

    verificar_matriz_com_codigo(codigo)

    matriz_selecionada: Matriz = pegar_matriz_por_codigo(codigo)

    linha_elemento = obter_posicao("Digite a linha da posição do elemento que deseja alterar: ",
                                   matriz_selecionada.linha,
                                   "linhas")

    coluna_elemento = obter_posicao("Digite a coluna da posição do elemento que deseja alterar: ",
                                    matriz_selecionada.coluna,
                                    "colunas")

    elemento = validar_dados(f"Insira o valor na posição {linha_elemento}x{coluna_elemento}: ")

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

    codigo = validar_dados("Digite o código da matriz que deseja remover: ")

    verificar_matriz_com_codigo(codigo)

    gerenciador.remover_matriz(codigo)

    print(f"A matriz com o código {codigo} foi removida.")

    sleep(3)
    menu()


def verificar_existencia_de_matrizes() -> None:
    global gerenciador

    if not gerenciador.matrizes:  # Dicionário vazio == False.
        print("Não foi criada nenhuma matriz.")
        sleep(2)
        menu()


def verificar_matriz_com_codigo(codigo:int) -> None:
    global gerenciador

    if codigo not in gerenciador.matrizes or codigo <= 0:
        print("Não há uma matriz com esse código.")
        sleep(2)
        menu()


def obter_posicao(entrada_msg: str, limite: int, tipo: str) -> int:
    while True:
        posicao = validar_dados(entrada_msg, True)
        if posicao > limite:
            print(f"A matriz que você selecionou não possui {posicao} {tipo}. Digite novamente!")
            continue
        return posicao


def pegar_matriz_por_codigo(codigo: int) -> Matriz:
    global gerenciador

    for chave in gerenciador.matrizes:
        if chave == codigo:
            return gerenciador.matrizes[chave]


if __name__ == '__main__':
    main()