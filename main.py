from jogo import Jogo
import os
import time
from jogador import GerenciadorJogador
from palavra import GerenciadorPalavras
from som import GerenciadorSom
adm_sons = GerenciadorSom()
adm_jogadores = GerenciadorJogador()
adm_palavras = GerenciadorPalavras()

def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def forca(erro):
    match erro:
        case 0:
            print("-------")
            print("|     |")
            print("|")
            print("|")
            print("|")
            print("|")
        case 1:
            print("-------")
            print("|     |")
            print("|     O")
            print("|")
            print("|")
            print("|")
        case 2:
            print("-------")
            print("|     |")
            print("|     O")
            print("|     |")
            print("|")
            print("|")
        case 3:
            print("-------")
            print("|     |")
            print("|     O")
            print("|    /|")
            print("|")
            print("|")
        case 4:
            print("-------")
            print("|     |")
            print("|     O")
            print("|    /|\\")
            print("|")
            print("|")
        case 5:
            print("-------")
            print("|     |")
            print("|     O")
            print("|    /|\\")
            print("|    /")
            print("|")
        case 6:
            print("-------")
            print("|     |")
            print("|     O")
            print("|    /|\\")
            print("|    / \\")
            print("|")

def definir_categoria():
    print("Escolha a categoria da palavra")
    cont = 1
    for i in adm_palavras.categorias:
        print(f"{cont} - {i}")
        cont = cont + 1

    entrada_categoria = input("\nEntrada: ")
    try:
        return adm_palavras.categorias[int(entrada_categoria)-1]
    except:
        return None

def definir_jogador():
    print("Escolha o jogador da vez")
    cont = 1
    for i in adm_jogadores.jogadores:
        print(f"{cont} - {i.nome}")
        cont = cont + 1
    
    entrada_jogador = input("\nEntrada: ")
    try:
        return adm_jogadores.jogadores[int(entrada_jogador)-1]
    except:
        None

def adicionar_jogador():
    while True:
        limpar_terminal()
        print("ADICIONAR JOGADOR      -1 = VOLTAR")
        nome = input("Informe um nome: ")
        limpar_terminal()
        if nome == "-1":
            return "-1"
        certeza = input(f"Tem certeza que deseja adicionar o jogador:  {nome}\n\n1 - SIM\n0 - NAO\n")
        if certeza == "0":
            pass
        elif certeza == "1":
            return nome
        else:
            limpar_terminal()
            print("Opção invalida selecionada")

som_menu = adm_sons.sons["som_menu"]
som_jogo = adm_sons.sons["som_jogo"]
while True:
    limpar_terminal()
    if som_menu.get_num_channels() == 0:
        som_menu.play(loops=-1)
        som_menu.set_volume(0.2)
    print("MENU")
    print("1 - Jogar\n2 - Ranking\n3 - Adicionar jogador\n0 - Sair\n" )
    entrada = input("Entrada: ")
    match entrada:
        case "1": #entra no jogo
            cont_erro = 0
            limpar_terminal()
            categoria_da_palavra = definir_categoria()
            if categoria_da_palavra:
                limpar_terminal()
                jogador = definir_jogador()
                if jogador:
                    print(jogador.nome)
                    palavra_aleatoria = adm_palavras.palavra_aleatoria(categoria_da_palavra)
                    jogo = Jogo(palavra_aleatoria, jogador)
                    adm_sons.parar_todos()
                    if som_jogo.get_num_channels() == 0:
                        som_jogo.play(loops=-1)
                        som_jogo.set_volume(0.2)
                    limpar_terminal()
                    print("Para sair digite (1) a qualquer momento.")
                    time.sleep(2)
                    while True:
                        limpar_terminal()
                        print(f"{categoria_da_palavra.upper()}                      letras erradas: {" ".join(jogo.letras_erradas)}")

                        forca(cont_erro)
                        estado = jogo.estado_atual()
                        print(estado)
                        letra = input("\nDigite uma letra: ")
                        if letra == "-1":
                            adm_sons.parar_todos()
                            break
                        retorno_tentativa = jogo.tentar_letra(letra)
                        if retorno_tentativa == "erro":
                            cont_erro = cont_erro + 1
                            adm_sons.sons["som_erro"].play().set_volume(0.3)
                        elif retorno_tentativa == "derrota":
                            adm_sons.parar_todos()
                            adm_sons.sons["som_derrota"].play().set_volume(0.2)
                            print(f"Voce nao acertou a palavra era --> {palavra_aleatoria.texto}")
                            input("Precione enter para voltar ao menu...")
                            adm_sons.parar_todos()
                            break
                        elif retorno_tentativa == "vitoria":
                            limpar_terminal()
                            adm_jogadores.adicionar_ponto(jogador, 10)
                            forca(cont_erro)
                            estado = jogo.estado_atual()
                            print(estado)
                            print(f"Parabens voce acertou a palavra!")
                            input("Precione enter para voltar ao menu...")
                            adm_sons.parar_todos()
                            break
                        elif retorno_tentativa == "nao_letra":
                            limpar_terminal()
                            print("Digige uma letra valida.")
                            input("Enter para continuar...")
                        elif retorno_tentativa == "repetida":
                            limpar_terminal()
                            print("Letra repetida.")
                            input("Enter para continuar...")
                        elif retorno_tentativa == "acerto":
                            adm_jogadores.adicionar_ponto(jogador, 5)
                            adm_sons.sons["som_acerto"].play().set_volume(0.3)
                        else:
                            print("erro inesperado")
                            time.sleep(3)
                            break
                else:
                    limpar_terminal()
                    print("Valor invalido para a categoria!")
                    time.sleep(1)
            else:
                limpar_terminal()
                print("Valor invalido para a categoria!")
                time.sleep(1)
        case "2": #mostra ranking dos jogadores cadastrado
            limpar_terminal()
            print("RANKING DOS JOGADORES\n")
            ranking = adm_jogadores.ranking()
            cont = 1
            for i in ranking:
                print(f"{cont} - {i.nome} --> {i.pontuacao}")
                cont = cont + 1
            
            input("Precione enter para continuar...")
        case "3": #adiciona mais jogadores
            nome = adicionar_jogador()
            if nome != "-1" and nome != "":
                adm_jogadores.adicionar_jogador(nome)
                print("Nome adicionar com sucesso!")
                input("PRECIONE ENTER PARA CONTINUAR...")

        case "0": # salva jogadores e termina o programa
            limpar_terminal()
            adm_jogadores.salvar_jogadores()
            adm_palavras.salvar_palavras()
            break
        case _: # usado quando a entrada não for valida
            limpar_terminal()
            print("Opção invalida!")
            time.sleep(1)