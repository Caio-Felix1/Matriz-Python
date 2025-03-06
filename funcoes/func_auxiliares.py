from time import sleep
from typing import Union

from classes.matriz import Matriz, GerenciadorMatrizes


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


def verificar_existencia_de_matrizes(gerenc: GerenciadorMatrizes) -> bool:
    if not gerenc.matrizes:  # Dicionário vazio == False.
        print("Não foi criada nenhuma matriz.")
        sleep(2)
        return False
    return True


def verificar_matriz_com_codigo(gerenc: GerenciadorMatrizes, codigo:int) -> bool:
    if codigo not in gerenc.matrizes or codigo <= 0:
        print(f"Não há uma matriz com o código {codigo}.")
        sleep(2)
        return False
    return True


def obter_posicao(entrada_msg: str, limite: int, tipo: str) -> int:
    while True:
        posicao = validar_dados(entrada_msg, True)
        if posicao > limite:
            print(f"A matriz que você selecionou não possui {posicao} {tipo}. Digite novamente!")
            continue
        return posicao


def pegar_matriz_por_codigo(gerenc: GerenciadorMatrizes, codigo: int) -> Matriz:
    for chave in gerenc.matrizes:
        if chave == codigo:
            return gerenc.matrizes[chave]


def verificar_duas_matrizes(gerenc: GerenciadorMatrizes) -> bool:
    if len(gerenc.matrizes) < 2:
        print("É necessário ter no mínimo duas matrizes para fazer essa operação.")
        sleep(2)
        return False
    return True


def obter_duas_matrizes(gerenc: GerenciadorMatrizes) -> Union[tuple[Matriz, Matriz], tuple[()]]:
    codigo1: int = validar_dados("Digite o código da primeira matriz: ")
    if not verificar_matriz_com_codigo(gerenc, codigo1):
        return ()

    codigo2: int = validar_dados("Digite o código da segunda matriz: ")
    if not verificar_matriz_com_codigo(gerenc, codigo2):
        return ()

    matriz1: Matriz = pegar_matriz_por_codigo(gerenc, codigo1)
    matriz2: Matriz = pegar_matriz_por_codigo(gerenc, codigo2)

    return matriz1, matriz2