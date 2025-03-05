from time import sleep

from typing import Dict

class Matriz:

    def __init__(self: object, codigo: int, linha: int, coluna: int) -> None:
        self.__codigo: int = codigo
        self.__matriz: list[int] = []  # futuramente vai receber uma lista com inteiros
        self.__linha: int = linha
        self.__coluna: int = coluna

    @property
    def codigo(self: object) -> int:
        return self.__codigo

    @property
    def matriz(self: object) -> list[int]:  # futuramente vai receber uma lista com inteiros
        return self.__matriz

    @matriz.setter
    def matriz(self: object, matriz_nova: list[int]) -> None:
        self.__matriz = matriz_nova

    @property
    def linha(self: object) -> int:
        return self.__linha

    @property
    def coluna(self: object) -> int:
        return self.__coluna

    def mostrar_matriz(self: object) -> str:
        return "\n".join(" ".join(map(str, elemento)) for elemento in self.matriz)

    def __str__(self: object) -> str:
        return f'Código: {self.codigo} | Linha(s): {self.linha} | Coluna(s): {self.coluna} \n' \
               f'Matriz:\n{self.mostrar_matriz()}'


class GerenciadorMatrizes:

    qtd_remocao_matriz: int = 0

    def __init__(self: object) -> None:
        self.__matrizes: Dict[int, Matriz] = {}  # código: matriz
        self.__proximo_codigo: int = 1
        self.__codigos_disponiveis: list[int] = []

    @property
    def matrizes(self: object) -> Dict[int, Matriz]:
        return self.__matrizes

    def criar_matriz(self: object, linha: int, coluna: int) -> Matriz:
        if self.__codigos_disponiveis:
            if len(self.__codigos_disponiveis) > 1:
                self.__codigos_disponiveis.sort()
            codigo: int = self.__codigos_disponiveis.pop(0)
        else:
            codigo: int = self.__proximo_codigo
            self.__proximo_codigo += 1

        matriz: Matriz = Matriz(codigo, linha, coluna)
        self.__matrizes[codigo] = matriz
        if GerenciadorMatrizes.qtd_remocao_matriz > 0:
            self.__matrizes = {chave: valor for chave, valor in sorted(self.__matrizes.items(), key=lambda item: item[0])}
            GerenciadorMatrizes.qtd_remocao_matriz -= 1
        return matriz

    def remover_matriz(self: object, codigo: int) -> None:
        if codigo in self.__matrizes:
            del self.__matrizes[codigo]
            self.__codigos_disponiveis.append(codigo)
            GerenciadorMatrizes.qtd_remocao_matriz += 1

    def exibir_matrizes(self: object, tempo_pausa: float) -> None:
        for codigo in self.__matrizes:
            print(self.__matrizes[codigo])
            print('-' * 50)
            sleep(tempo_pausa)