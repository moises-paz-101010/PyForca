from palavra import Palavra
from jogador import Jogador
class Jogo:
    
    def __init__(self, palavra:Palavra, jogador:Jogador):
        self.palavra_atual = palavra.texto.lower()
        self.letras_certas = []
        self.letras_erradas = []
        self.tentativas_restantes = 6
        self.jogador = jogador.nome
    
    def tentar_letra(self, letra: str):
        letra = letra.lower()

        if len(letra) != 1 or not letra.isalpha():
            return "nao_letra"

        if letra in self.letras_erradas or letra in self.letras_certas:
            return "repetida"

        if letra in self.palavra_atual:
            self.letras_certas.append(letra)
            if self.verificar_vitoria():
                return "vitoria"
            return "acerto"

        # Se chegou aqui, é erro
        self.letras_erradas.append(letra)
        self.tentativas_restantes -= 1

        if self.verificar_derrota():
            return "derrota"

        return "erro"

    def verificar_vitoria(self):
        aux_palavra = set(self.palavra_atual) #uso de conjuntos para não repetir elementos
        aux_letras_certas = set(self.letras_certas)

        if aux_palavra == aux_letras_certas:
            return True
        else:
            return False

    def verificar_derrota(self):
        if self.tentativas_restantes <= 0:
            return True
        else:
            return False
    
    def estado_atual(self):
        string = ""
        for letra in self.palavra_atual:
            if letra in self.letras_certas:
                string = string + letra
            else:
                string = string + "_"

        return string

    def reiniciar(self, nova_palavra):
        self.palavra_atual = nova_palavra.texto.lower()
        self.letras_certas = []
        self.letras_erradas = []
        self.tentativas_restantes = 6