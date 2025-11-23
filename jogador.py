import json

class Jogador:

    def __init__(self, nome:str, pontuacao:int = 0):
        self.nome = nome
        self.pontuacao = pontuacao
    
    def adicionar_pontos(self, pontos:int):
        self.pontuacao = self.pontuacao + pontos

    def __str__(self):
        return f"Jogador(nome = {self.nome}, pontuacao = {self.pontuacao})"
    
    def __lt__(self, outro):
        return self.pontuacao < outro.pontuacao
    
    def __gt__(self, outro):
        return self.pontuacao > outro.pontuacao


class GerenciadorJogador:

    def __init__(self):
        self.arquivo_jogador = "dados/jogador.json"
        self.jogadores = []
        self.dados_sobrescreveu = 0
        self.carregar_jogadores()

    def carregar_jogadores(self):
        try:
            with open(self.arquivo_jogador, "r", encoding="utf-8") as arquivo:
                conteudo = json.load(arquivo)
                for i in conteudo:
                    aux_jogador = Jogador(i["nome"], i["pontuacao"])
                    self.jogadores.append(aux_jogador)

            return 0

        except FileNotFoundError:
            print(f"Arquivo {self.arquivo_jogador} não encontrado!")
            return 1

        except json.JSONDecodeError:
            print(f"Arquivo {self.arquivo_jogador} corrompido ou vazio")
            return 1


    def adicionar_jogador(self, nome:str):
        verificar = self.buscar_jogador(nome)
        if verificar == None:
            aux_jogador = Jogador(nome, 0)
            self.jogadores.append(aux_jogador)
            return 0
        else:
            return 1
        

    def buscar_jogador(self, nome:str):
        jogador = next((i for i in self.jogadores if i.nome == nome), None) #compresão de listas
        return jogador

    def atualizar_pontuacao(self, jogador:Jogador, ponto:int):
        jogador.adicionar_pontos(ponto)
        return jogador
    
    def adicionar_ponto(self, jogador:Jogador, ponto:int):
        for i in self.jogadores:
            if i.nome == jogador.nome:
                i.pontuacao = i.pontuacao + ponto
                return 0
        return 1
        
    def ranking(self):
        return sorted(self.jogadores, reverse=True)


    def salvar_jogadores(self):
        conteudo = [i.__dict__ for i in self.jogadores]
        try:
            with open(self.arquivo_jogador, "w", encoding="utf-8") as arquivo:
                json.dump(conteudo, arquivo, indent=4)
        except Exception as erro:
            print(f"Algum error ocorreu ao tentar gravar no arquivo {self.arquivo_jogador}. Erro: {erro}")