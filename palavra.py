import json
import random

class Palavra:
    def __init__(self, texto:str, categoria:str):
        self.texto = texto
        self.categoria = categoria
    
    def __str__(self):
        return f"Palavra(texto = {self.texto}, categoria = {self.categoria})"
    
    def __len__(self):
        return len(self.texto)


class GerenciadorPalavras:
    
    def __init__(self):
        self.arquivo_palavra = "dados/palavra.json"
        self.palavras = []
        self.categorias = []
        self.carregar_palavras()

    def carregar_palavras(self):
        try:
            with open(self.arquivo_palavra, "r", encoding="utf-8") as arquivo:
                conteudo = json.load(arquivo)
                for categoria, palavras in conteudo.items():
                    self.categorias.append(categoria)
                    for palavra in palavras:
                        aux_palavra = Palavra(palavra, categoria)
                        self.palavras.append(aux_palavra)

            return 0

        except FileNotFoundError:
            print(f"Arquivo {self.arquivo_palavra} não encontrado!")
            return 1

        except json.JSONDecodeError:
            print(f"Arquivo {self.arquivo_palavra} corrompido ou vazio")
            return 1

    def buscar_palavra(self, palavra:str):
        for obj_palavra in self.palavras:
            if obj_palavra.texto == palavra:
                return obj_palavra
        return None

    def buscar_categoria(self, categoria:str):
        for obj_palavra in self.palavras:
            if obj_palavra.categoria == categoria:
                return obj_palavra
        return None

    def salvar_palavra(self, palavra:Palavra):
        valida_categoria = self.buscar_categoria(palavra.categoria) != None
        valida_palavra = self.buscar_palavra(palavra.texto) == None

        if valida_palavra and valida_categoria:
            self.palavras.append(palavra)
            return 0
        else:
            
            return 1
    def filtrar_por_categoria(self, lista:list, categoria:str):
        return [p for p in lista if p.categoria == categoria] #compresão de listas

    def palavra_aleatoria(self, categoria:str):
        por_categoria = self.filtrar_por_categoria(self.palavras, categoria)
        if por_categoria != []:
            return random.choice(por_categoria)

        return None

    def salvar_palavras(self):
        conteudo = {}
        for obj in self.palavras:
            categoria = obj.categoria
            palavra = obj.texto

            if categoria not in conteudo:
                conteudo[categoria] = []

            conteudo[categoria].append(palavra)
        
        try:
            with open(self.arquivo_palavra, "w", encoding="utf-8") as arquivo:
                json.dump(conteudo, arquivo, indent=4)
        except:
            print(f"Algum error ocorreu ao tentar gravar no arquivo {self.arquivo_palavra}")