import pygame
class GerenciadorSom:
    
    def __init__(self):
        self.caminhos_musica = {
            "som_menu":"assets/som/c_pixelado_menu.mp3",
            "som_acerto":"assets/som/acerto.wav",
            "som_jogo":"assets/som/musica_jogo.wav",
            "som_derrota":"assets/som/derrota.wav",
            "som_erro":"assets/som/error.wav"
        }

        pygame.mixer.init()
        self.sons = {}
        self.carregar_sons()

    def carregar_sons(self):
        try:
            for nome_som, caminho_som in self.caminhos_musica.items():
                self.sons[nome_som] = pygame.mixer.Sound(caminho_som)
            
            return 0
        except Exception as e:
            print("Erro ao carregar som:", e)
            return 1
        
    def tocar(self, nome:str):
        if nome in self.sons:
            self.sons[nome].play()
    
    def parar_todos(self):
        pygame.mixer.stop()