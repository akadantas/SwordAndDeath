from time import sleep
import os
import sys
import random

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')
    sys.stdout.flush()

def menuinicial(msg):
    print("-"*30)
    print(msg.center(30))
    print("-"*30)
    print("[1] Novo Jogo\n[2] Carregar Jogo\n[3] Sair ")

def luta(player, inimigo_nome, inimigo_hp, inimigo_atk):
    hp_inimigo=inimigo_hp
    player_inventario = {"pocoes": 1}
    while hp_inimigo > 0 and player['hp_atual'] > 0:
        limpar()
        print(f"--- ARENA: {player['nome']} VS {inimigo_nome} ---")
        print(f"Seu HP: {player['hp_atual']} | HP inimigo: {hp_inimigo}")
        print("-"*30)
        print("[1] Ataque Rapido\n[2] Ataque Pesado\n[3] Inventario")

        e=input("Escolha: ")

        if e=="1":
            dano = player ['forca'] + random.randint(1,3)
            hp_inimigo-=dano
            print(f"Você acertou! {dano} de dano")

        elif e=="2":
            if random.random() > 0.4:
                dano = player['forca'] + random.randint(7, 10)
                hp_inimigo-=dano
                print(f"GOLPE CRITICO! {dano} de dano!")
            else:
                print("Você errou o golpe")

        elif e=="3":
            print(">>> INVENTARIO <<<")
            print(player_inventario)
            if player_inventario['pocoes'] > 0:
                es = input("Deseja usar poção? S/N: ").upper()
                if es == "S":
                    print("Você tomou a poção!")
                    player['hp_atual'] = player['hp_max']
                    player_inventario['pocoes'] -= 1
                    sleep(2.5)
                else:
                    print("Saindo do inventario...")
                    sleep(1.5)

        sleep(1)

        if hp_inimigo > 0:
            dano_in = max(1, inimigo_atk + random.randint(-1, 2))
            player['hp_atual'] -= dano_in
            print(f"O inimigo te atacou! Causando {dano_in} de dano.")
            sleep(1)

    if player['hp_atual'] > 0:
        print(f'\nVocê venceu!')
        sleep(1)
        return True
    return False


def jogar():
    player= {
        "nome": "Iluminado",
        "hp_atual": 20, "hp_max": 20,
        "forca": 5, "vitorias": 0,
        "ouro": 0
    }
    nomes_inimigos=["Mata-rindo", "Querô", "Você", "Azazel", "Donald Trump", "Java", "Apocalipse", "Liza"]
    player_inventario={"pocoes": 1}

    while True:
        limpar()
        print(f"--- CIDADE DOS GLADIADORES ---")
        print(f"Nome: {player['nome']} | HP: {player['hp_atual']}/{player['hp_max']}")
        print(f"Ouro: {player['ouro']} | Vitorias: {player['vitorias']}")
        print("-"*30)
        print("[1] Ir para arena (Lutar)")
        print("[2] Ferreiro (Melhorar espada -20 ouros.)")
        print("[3] Descanso (Curar -5 ouros.)")
        print("[4] Inventario")
        print("[5] Sair")

        e=input("\nOque você quer fazer? > ")

        if e=="1":
            inimigo_atual=random.choice(nomes_inimigos)
            inimigo_hp = 15 + (player['vitorias'] * 3)
            inimigo_atk = 3 + (player['vitorias'] // 2)
            venceu = luta(player, inimigo_atual, inimigo_hp, inimigo_atk)
            if venceu:
                player['vitorias']+=1
                player['ouro']+=15
                print("\nVocê ganhou 15 de ouro.")
            else:
                print("\nVocê foi derrotado... Ouro Perdido.")
                player['hp_atual']=1
                sleep(2)

        elif e=="2":
            if player['ouro']>=20:
                player['ouro']-=20
                player['forca']+=3
                print("Você melhorou sua espada! (+3 de força)")
            else:
                print("Ouro Insuficiente")
            sleep(3)

        elif e=="3":
            if player['ouro']>=5:
                player['ouro']-=5
                player['hp_atual']= player['hp_max']
                print("HP completamente restaurando.")
            else:
                print("Você não tem ouro suficiente.")
                sleep(3)

        elif e=="4":
            print(">>> INVENTARIO <<<")
            print(player_inventario)
            if player_inventario['pocoes'] > 0:
                es=input("Deseja usar poção? S/N: ").upper()
                if es=="S":
                    print("Você tomou a poção!")
                    player['hp_atual']=player['hp_max']
                    player_inventario['pocoes']-=1
                    sleep(2.5)
                else:
                    print("Saindo do inventario...")
                    sleep(1.5)

            else:
                print("Você não tem poções!")
                sleep(2.5)


        elif e == "5":
            print("SAINDO")
            break

#inicio
while True:
    limpar()
    menuinicial("RPG 0.1.0 alpha")

    try:
        e=int(input("ESCOLHA: "))
    except ValueError:
        print("Digite um número valido!")
        sleep(1.5)
        continue

    if e==1:
        limpar()
        print("INICIANDO...")
        sleep(1.5)
        input("Aperte ENTER para continuar!")
        jogar()

    elif e==2:
        print("EM BREVE")

    elif e==3:
        print("SAINDO...")
        sleep(1.5)
        break

