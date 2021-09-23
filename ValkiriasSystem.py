import time

"""Armazenamento de dados"""
qtd_ttl = 0
listageral = []


# Funções

def adic_aluna(name, nickname, numtel, game, classelo, normcomp):
    linha = [name, nickname, numtel, game, classelo, normcomp]
    listageral.append(linha)


def remover_listageral(nomealuna):
    for a in listageral:
        if a[0] == nomealuna:
            listageral.remove(a)


def edit_nome(nomepraeditar, newname):
    for b in listageral:
        if b[0] == nomepraeditar:
            b[0] = newname


def edit_nick(nomealuna1, newnickname):
    for c in listageral:
        if c[0] == nomealuna1:
            c[1] = newnickname


def edit_telefone(nomealuna3, novotel):
    for d in listageral:
        if d[0] == nomealuna3:
            d[2] = novotel


def edit_jogo(nomealuna4, newgame):
    for e in listageral:
        if e[0] == nomealuna4:
            e[3] = newgame


def edit_elo(nomealuna5, newelo):
    for f in listageral:
        if f[0] == nomealuna5:
            f[4] = newelo


def edit_categoria(nomealuna6, novacategoria):
    for g in listageral:
        if g[0] == nomealuna6:
            g[5] = novacategoria


# Código

print("--------------------------\n-----VALKÍRIAS SYSTEM-----\n--------------------------")
print("Bem vindas ao VALKÍRIAS SYSTEM!")
time.sleep(2)

cond1 = True
while cond1:
    print("----------------------------")
    menu = int(input(
        "1 - Adicionar aluna\n2 - Remover aluna\n3 - Buscar aluna\n4 - Editar dados\n5 - Verificar dados\n6 - Sair"
        "\nQual ação deseja realizar agora?"))
    print("----------------------------")


    if menu == 1:

        condAdd = True

        while condAdd:
            AddOuSair = int(input("1 - Adicionar\n2 - Voltar\nInsira o código:"))
            print("----------------------------")

            if AddOuSair == 2:
                condAdd = False
            else:
                nome = input("Nome da aluna:")

                nick = input("Nick da aluna:")

                telefone = input("Número de telefone:")
                print("----------------------------")

                codjogo = int(input("1 - League of legends\n2 - Valorant\n3 - Free Fire\nInsira o código do jogo:"))
                print("----------------------------")

                elo = ""
                jogo = ""
                if codjogo == 1:

                    jogo = "League of Legends"

                    elocod = int(
                        input("1 - Ferro\n2 - Bronze\n3 - Prata\n4 - Ouro\n5 - Platina\n6 - Diamante\n7 - Mestre"
                              "\n8 - Grão-Mestre\n9 - Desafiante\n10 - Unranked\nInsira o código do elo:"))

                    if elocod == 1:
                        ramificacao = int(input("1 - I\n2 - II\n3 - III\n4 - IV\nDigite o código da ramificação:"))
                        if ramificacao == 1:
                            elo = "Ferro I"
                        elif ramificacao == 2:
                            elo = "Ferro II"
                        elif ramificacao == 3:
                            elo = "Ferro III"
                        elif ramificacao == 4:
                            elo = "Ferro IV"
                        else:
                            print("A ação não pode ser concluída.")
                            continue

                    elif elocod == 2:
                        ramificacao = int(input("1 - I\n2 - II\n3 - III\n4 - IV\nDigite o código da ramificação:"))
                        if ramificacao == 1:
                            elo = "Bronze I"
                        elif ramificacao == 2:
                            elo = "Bronze II"
                        elif ramificacao == 3:
                            elo = "Bronze III"
                        elif ramificacao == 4:
                            elo = "Bronze IV"
                        else:
                            print("A ação não pode ser concluída.")
                            continue

                    elif elocod == 3:
                        ramificacao = int(input("1 - I\n2 - II\n3 - III\n4 - IV\nDigite o código da ramificação:"))
                        if ramificacao == 1:
                            elo = "Prata I"
                        elif ramificacao == 2:
                            elo = "Prata II"
                        elif ramificacao == 3:
                            elo = "Prata III"
                        elif ramificacao == 4:
                            elo = "Prata IV"
                        else:
                            print("A ação não pode ser concluída.")
                            continue

                    elif elocod == 4:
                        ramificacao = int(input("1 - I\n2 - II\n3 - III\n4 - IV\nDigite o código da ramificação:"))
                        if ramificacao == 1:
                            elo = "Ouro I"
                        elif ramificacao == 2:
                            elo = "Ouro II"
                        elif ramificacao == 3:
                            elo = "Ouro III"
                        elif ramificacao == 4:
                            elo = "Ouro IV"
                        else:
                            print("A ação não pode ser concluída.")
                            continue

                    elif elocod == 5:
                        ramificacao = int(input("1 - I\n2 - II\n3 - III\n4 - IV\nDigite o código da ramificação:"))
                        if ramificacao == 1:
                            elo = "Platina I"
                        elif ramificacao == 2:
                            elo = "Platina II"
                        elif ramificacao == 3:
                            elo = "Platina III"
                        elif ramificacao == 4:
                            elo = "Platina IV"
                        else:
                            print("A ação não pode ser concluída.")
                            continue

                    elif elocod == 6:
                        ramificacao = int(input("1 - I\n2 - II\n3 - III\n4 - IV\nDigite o código da ramificação:"))
                        if ramificacao == 1:
                            elo = "Diamante I"
                        elif ramificacao == 2:
                            elo = "Diamante II"
                        elif ramificacao == 3:
                            elo = "Diamante III"
                        elif ramificacao == 4:
                            elo = "Diamante IV"
                        else:
                            print("A ação não pode ser concluída.")
                            continue

                    elif elocod == 7:
                        ramificacao = int(input("1 - I\n2 - II\n3 - III\n4 - IV\nDigite o código da ramificação:"))
                        if ramificacao == 1:
                            elo = "Mestre I"
                        elif ramificacao == 2:
                            elo = "Mestre II"
                        elif ramificacao == 3:
                            elo = "Mestre III"
                        elif ramificacao == 4:
                            elo = "Mestre IV"
                        else:
                            print("A ação não pode ser concluída.")
                            continue

                    elif elocod == 8:
                        ramificacao = int(input("1 - I\n2 - II\n3 - III\n4 - IV\nDigite o código da ramificação:"))
                        if ramificacao == 1:
                            elo = "Grão-Mestre I"
                        elif ramificacao == 2:
                            elo = "Grão-Mestre II"
                        elif ramificacao == 3:
                            elo = "Grão-Mestre III"
                        elif ramificacao == 4:
                            elo = "Grão-Mestre IV"
                        else:
                            print("A ação não pode ser concluída.")
                            continue

                    elif elocod == 9:
                        elo = "Desafiante"

                    elif elocod == 10:
                        elo = "Unranked"
                    else:
                        print("A ação não pode ser concluída.")
                        continue

                elif codjogo == 2:

                    jogo = "Valorant"

                    elocod = int(input(
                        "1 - Ferro\n2 - Bronze\n3 - Prata\n4 - Ouro\n5 - Platina\n6 - Diamante\n7 - Imortal"
                        "\n8 - Radiante\n9 - Unranked\nInsira o código do elo:"))

                    if elocod == 1:
                        ramificacao = int(input("1 - I\n2 - II\n3 - III\nDigite o código da ramificação:"))
                        if ramificacao == 1:
                            elo = "Ferro I"
                        elif ramificacao == 2:
                            elo = "Ferro II"
                        elif ramificacao == 3:
                            elo = "Ferro III"
                        else:
                            print("A ação não pode ser concluída.")
                            continue

                    elif elocod == 2:
                        ramificacao = int(input("1 - I\n2 - II\n3 - III\nDigite o código da ramificação:"))
                        if ramificacao == 1:
                            elo = "Bronze I"
                        elif ramificacao == 2:
                            elo = "Bronze II"
                        elif ramificacao == 3:
                            elo = "Bronze III"
                        else:
                            print("A ação não pode ser concluída.")
                            continue

                    elif elocod == 3:
                        ramificacao = int(input("1 - I\n2 - II\n3 - III\nDigite o código da ramificação:"))
                        if ramificacao == 1:
                            elo = "Prata I"
                        elif ramificacao == 2:
                            elo = "Prata II"
                        elif ramificacao == 3:
                            elo = "Prata III"
                        else:
                            print("A ação não pode ser concluída.")
                            continue

                    elif elocod == 4:
                        ramificacao = int(input("1 - I\n2 - II\n3 - III\nDigite o código da ramificação:"))
                        if ramificacao == 1:
                            elo = "Ouro I"
                        elif ramificacao == 2:
                            elo = "Ouro II"
                        elif ramificacao == 3:
                            elo = "Ouro III"
                        else:
                            print("A ação não pode ser concluída.")
                            continue

                    elif elocod == 5:
                        ramificacao = int(input("1 - I\n2 - II\n3 - III\nDigite o código da ramificação:"))
                        if ramificacao == 1:
                            elo = "Platina I"
                        elif ramificacao == 2:
                            elo = "Platina II"
                        elif ramificacao == 3:
                            elo = "Platina III"
                        else:
                            print("A ação não pode ser concluída.")
                            continue

                    elif elocod == 6:
                        ramificacao = int(input("1 - I\n2 - II\n3 - III\nDigite o código da ramificação:"))
                        if ramificacao == 1:
                            elo = "Diamante I"
                        elif ramificacao == 2:
                            elo = "Diamante II"
                        elif ramificacao == 3:
                            elo = "Diamante III"
                        else:
                            print("A ação não pode ser concluída.")
                            continue

                    elif elocod == 7:
                        ramificacao = int(input("1 - I\n2 - II\n3 - III\nDigite o código da ramificação:"))
                        if ramificacao == 1:
                            elo = "Imortal I"
                        elif ramificacao == 2:
                            elo = "Imortal II"
                        elif ramificacao == 3:
                            elo = "Imortal III"
                        else:
                            print("A ação não pode ser concluída.")
                            continue

                    elif elocod == 8:
                        elo = "Radiante"

                    elif elocod == 9:
                        elo = "Unranked"
                    else:
                        print("A ação não pode ser concluída.")
                        continue

                elif codjogo == 3:

                    jogo = "Free Fire"
                    elocod = int(input("1 - Bronze\n2 - Prata\n3 - Ouro\n4 - Platina\n5 - Diamante\n6 - Mestre"
                                       "\n7 - Desafiante\n8 - Unranked\nInsira o código do elo:"))

                    if elocod == 1:
                        ramificacao = int(input("1 - I\n2 - II\n3 - III\nDigite o código da ramificação:"))
                        if ramificacao == 1:
                            elo = "Bronze I"
                        elif ramificacao == 2:
                            elo = "Bronze II"
                        elif ramificacao == 3:
                            elo = "Bronze III"
                        else:
                            print("A ação não pode ser concluída.")
                            continue

                    elif elocod == 2:
                        ramificacao = int(input("1 - I\n2 - II\n3 - III\nDigite o código da ramificação:"))
                        if ramificacao == 1:
                            elo = "Prata I"
                        elif ramificacao == 2:
                            elo = "Prata II"
                        elif ramificacao == 3:
                            elo = "Prata III"
                        else:
                            print("A ação não pode ser concluída.")
                            continue

                    elif elocod == 3:
                        ramificacao = int(input("1 - I\n2 - II\n3 - III\n4 - IV\nDigite o código da ramificação:"))
                        if ramificacao == 1:
                            elo = "Ouro I"
                        elif ramificacao == 2:
                            elo = "Ouro II"
                        elif ramificacao == 3:
                            elo = "Ouro III"
                        elif ramificacao == 4:
                            elo = "Ouro IV"
                        else:
                            print("A ação não pode ser concluída.")
                            continue

                    elif elocod == 4:
                        ramificacao = int(input("1 - I\n2 - II\n3 - III\n4 - IV\nDigite o código da ramificação:"))
                        if ramificacao == 1:
                            elo = "Platina I"
                        elif ramificacao == 2:
                            elo = "Platina II"
                        elif ramificacao == 3:
                            elo = "Platina III"
                        elif ramificacao == 4:
                            elo = "Platina IV"
                        else:
                            print("A ação não pode ser concluída.")
                            continue

                    elif elocod == 5:
                        ramificacao = int(input("1 - I\n2 - II\n3 - III\n4 - IV\nDigite o código da ramificação:"))
                        if ramificacao == 1:
                            elo = "Diamante I"
                        elif ramificacao == 2:
                            elo = "Diamante II"
                        elif ramificacao == 3:
                            elo = "Diamante III"
                        elif ramificacao == 4:
                            elo = "Diamante IV"
                        else:
                            print("A ação não pode ser concluída.")
                            continue

                    elif elocod == 6:
                        elo = "Mestre"

                    elif elocod == 7:
                        elo = "Desafiante"

                    elif elocod == 8:
                        elo = "Unranked"
                    else:
                        print("A ação não pode ser concluída.")
                        continue

                normaloucomp = int(input("1 - Competitivo\n2 - Normal\nInsira o código:"))

                tipo = ""
                if normaloucomp == 1:
                    tipo = "Competitivo"
                elif normaloucomp == 2:
                    tipo = "Normal"
                else:
                    print("A ação não pode ser concluída.")
                    continue

                qtd_ttl += 1
                adic_aluna(nome, nick, telefone, jogo, elo, tipo)
    elif menu == 2:
        condRemove = True

        while condRemove:
            RemoverOuSair = int(input("1 - Remover\n2 - Voltar\nInsira o código:"))

            if RemoverOuSair == 2:
                condRemove = False

            else:
                nomeAluna = input("Nome da Aluna a ser removida:")

                for h in listageral:
                    if h[0] == nomeAluna:
                        remover_listageral(nomeAluna)
                        qtd_ttl -= 1
                        time.sleep(2)
                        print("Aluna Removida com Sucesso")
                        break
                    else:
                        print("Aluna não encontrada")
                        continue
    elif menu == 3:
        alunabuscar = input("Nome da aluna a ser buscada:")

        for aluna in listageral:
            if aluna[0] == alunabuscar:
                print("Orientação: [Nome],[Nick],[Telefone],[Jogo],[Elo],[Categoria]")
                print(aluna)

    elif menu == 4:
        condEdit = True

        while condEdit:
            editOuSair = int(input("1 - Editar\n2 - Voltar\nInsira o código:"))

            if editOuSair == 2:
                condEdit = False
            else:

                infoedit = int(input(
                    "1 - Nome\n2 - Nick\n3 - Telefone\n4 - Jogo\n5 - Elo\n6 - Categoria de jogo"
                    "\nQual informação deseja alterar?"))
                nomeeditar = input("Insira o nome da Aluna a qual deseja editar as informações:")

                if infoedit == 1:
                    novonome = input("Novo nome a ser inserido:")
                    edit_nome(nomeeditar, novonome)

                elif infoedit == 2:
                    novonick = input("Novo nick a ser inserido:")
                    edit_nick(nomeeditar, novonick)

                elif infoedit == 3:
                    novotelefone = input("Novo telefone a ser inserido:")
                    edit_telefone(nomeeditar, novotelefone)

                elif infoedit == 4:
                    novojogo = input("Novo jogo a ser inserido:")
                    edit_jogo(nomeeditar, novojogo)

                elif infoedit == 5:
                    novoelo = ""
                    for i in listageral:
                        if i[0] == nomeeditar:
                            if i[3] == "League of Legends":
                                novoelocod = int(input("1 - Ferro\n2 - Bronze\n3 - Prata\n4 - Ouro\n5 - Platina"
                                                       "\n6 - Diamante\n7 - Mestre\n8 - Grão-Mestre\n9 - Desafiante"
                                                       "\n10 - Unranked\nInsira o código do elo a ser inserido:"))

                                if novoelocod == 1:
                                    ramificacao = int(
                                        input("1 - I\n2 - II\n3 - III\n4 - IV\nDigite o código da ramificação:"))
                                    if ramificacao == 1:
                                        novoelo = "Ferro I"
                                    elif ramificacao == 2:
                                        novoelo = "Ferro II"
                                    elif ramificacao == 3:
                                        novoelo = "Ferro III"
                                    elif ramificacao == 4:
                                        novoelo = "Ferro IV"
                                    else:
                                        print("A ação não pode ser concluída.")
                                        continue

                                elif novoelocod == 2:
                                    ramificacao = int(
                                        input("1 - I\n2 - II\n3 - III\n4 - IV\nDigite o código da ramificação:"))
                                    if ramificacao == 1:
                                        novoelo = "Bronze I"
                                    elif ramificacao == 2:
                                        novoelo = "Bronze II"
                                    elif ramificacao == 3:
                                        novoelo = "Bronze III"
                                    elif ramificacao == 4:
                                        novoelo = "Bronze IV"
                                    else:
                                        print("A ação não pode ser concluída.")
                                        continue

                                elif novoelocod == 3:
                                    ramificacao = int(
                                        input("1 - I\n2 - II\n3 - III\n4 - IV\nDigite o código da ramificação:"))
                                    if ramificacao == 1:
                                        novoelo = "Prata I"
                                    elif ramificacao == 2:
                                        novoelo = "Prata II"
                                    elif ramificacao == 3:
                                        novoelo = "Prata III"
                                    elif ramificacao == 4:
                                        novoelo = "Prata IV"
                                    else:
                                        print("A ação não pode ser concluída.")
                                        continue

                                elif novoelocod == 4:
                                    ramificacao = int(
                                        input("1 - I\n2 - II\n3 - III\n4 - IV\nDigite o código da ramificação:"))
                                    if ramificacao == 1:
                                        novoelo = "Ouro I"
                                    elif ramificacao == 2:
                                        novoelo = "Ouro II"
                                    elif ramificacao == 3:
                                        novoelo = "Ouro III"
                                    elif ramificacao == 4:
                                        novoelo = "Ouro IV"
                                    else:
                                        print("A ação não pode ser concluída.")
                                        continue

                                elif novoelocod == 5:
                                    ramificacao = int(
                                        input("1 - I\n2 - II\n3 - III\n4 - IV\nDigite o código da ramificação:"))
                                    if ramificacao == 1:
                                        novoelo = "Platina I"
                                    elif ramificacao == 2:
                                        novoelo = "Platina II"
                                    elif ramificacao == 3:
                                        novoelo = "Platina III"
                                    elif ramificacao == 4:
                                        novoelo = "Platina IV"
                                    else:
                                        print("A ação não pode ser concluída.")
                                        continue

                                elif novoelocod == 6:
                                    ramificacao = int(
                                        input("1 - I\n2 - II\n3 - III\n4 - IV\nDigite o código da ramificação:"))
                                    if ramificacao == 1:
                                        novoelo = "Diamante I"
                                    elif ramificacao == 2:
                                        novoelo = "Diamante II"
                                    elif ramificacao == 3:
                                        novoelo = "Diamante III"
                                    elif ramificacao == 4:
                                        novoelo = "Diamante IV"
                                    else:
                                        print("A ação não pode ser concluída.")
                                        continue

                                elif novoelocod == 7:
                                    ramificacao = int(
                                        input("1 - I\n2 - II\n3 - III\n4 - IV\nDigite o código da ramificação:"))
                                    if ramificacao == 1:
                                        novoelo = "Mestre I"
                                    elif ramificacao == 2:
                                        novoelo = "Mestre II"
                                    elif ramificacao == 3:
                                        novoelo = "Mestre III"
                                    elif ramificacao == 4:
                                        novoelo = "Mestre IV"
                                    else:
                                        print("A ação não pode ser concluída.")
                                        continue

                                elif novoelocod == 8:
                                    ramificacao = int(
                                        input("1 - I\n2 - II\n3 - III\n4 - IV\nDigite o código da ramificação:"))
                                    if ramificacao == 1:
                                        novoelo = "Grão-Mestre I"
                                    elif ramificacao == 2:
                                        novoelo = "Grão-Mestre II"
                                    elif ramificacao == 3:
                                        novoelo = "Grão-Mestre III"
                                    elif ramificacao == 4:
                                        novoelo = "Grão-Mestre IV"
                                    else:
                                        print("A ação não pode ser concluída.")
                                        continue

                                elif novoelocod == 9:
                                    novoelo = "Desafiante"

                                elif novoelocod == 10:
                                    novoelo = "Unranked"
                                else:
                                    print("A ação não pode ser concluída.")
                                    continue

                            elif i[3] == "Valorant":
                                novoelocod = int(input(
                                    "1 - Ferro\n2 - Bronze\n3 - Prata\n4 - Ouro\n5 - Platina\n6 - Diamante"
                                    "\n7 - Imortal\n8 - Radiante\n9 - Unranked\nInsira o código do elo:"))

                                if novoelocod == 1:
                                    ramificacao = int(input("1 - I\n2 - II\n3 - III\nDigite o código da ramificação:"))
                                    if ramificacao == 1:
                                        novoelo = "Ferro I"
                                    elif ramificacao == 2:
                                        novoelo = "Ferro II"
                                    elif ramificacao == 3:
                                        novoelo = "Ferro III"
                                    else:
                                        print("A ação não pode ser concluída.")
                                        continue

                                elif novoelocod == 2:
                                    ramificacao = int(input("1 - I\n2 - II\n3 - III\nDigite o código da ramificação:"))
                                    if ramificacao == 1:
                                        novoelo = "Bronze I"
                                    elif ramificacao == 2:
                                        novoelo = "Bronze II"
                                    elif ramificacao == 3:
                                        novoelo = "Bronze III"
                                    else:
                                        print("A ação não pode ser concluída.")
                                        continue

                                elif novoelocod == 3:
                                    ramificacao = int(input("1 - I\n2 - II\n3 - III\nDigite o código da ramificação:"))
                                    if ramificacao == 1:
                                        novoelo = "Prata I"
                                    elif ramificacao == 2:
                                        novoelo = "Prata II"
                                    elif ramificacao == 3:
                                        novoelo = "Prata III"
                                    else:
                                        print("A ação não pode ser concluída.")
                                        continue

                                elif novoelocod == 4:
                                    ramificacao = int(input("1 - I\n2 - II\n3 - III\nDigite o código da ramificação:"))
                                    if ramificacao == 1:
                                        novoelo = "Ouro I"
                                    elif ramificacao == 2:
                                        novoelo = "Ouro II"
                                    elif ramificacao == 3:
                                        novoelo = "Ouro III"
                                    else:
                                        print("A ação não pode ser concluída.")
                                        continue

                                elif novoelocod == 5:
                                    ramificacao = int(input("1 - I\n2 - II\n3 - III\nDigite o código da ramificação:"))
                                    if ramificacao == 1:
                                        novoelo = "Platina I"
                                    elif ramificacao == 2:
                                        novoelo = "Platina II"
                                    elif ramificacao == 3:
                                        novoelo = "Platina III"
                                    else:
                                        print("A ação não pode ser concluída.")
                                        continue

                                elif novoelocod == 6:
                                    ramificacao = int(input("1 - I\n2 - II\n3 - III\nDigite o código da ramificação:"))
                                    if ramificacao == 1:
                                        novoelo = "Diamante I"
                                    elif ramificacao == 2:
                                        novoelo = "Diamante II"
                                    elif ramificacao == 3:
                                        novoelo = "Diamante III"
                                    else:
                                        print("A ação não pode ser concluída.")
                                        continue

                                elif novoelocod == 7:
                                    ramificacao = int(input("1 - I\n2 - II\n3 - III\nDigite o código da ramificação:"))
                                    if ramificacao == 1:
                                        novoelo = "Imortal I"
                                    elif ramificacao == 2:
                                        novoelo = "Imortal II"
                                    elif ramificacao == 3:
                                        novoelo = "Imortal III"
                                    else:
                                        print("A ação não pode ser concluída.")
                                        continue

                                elif novoelocod == 8:
                                    novoelo = "Radiante"

                                elif novoelocod == 9:
                                    novoelo = "Unranked"
                                else:
                                    print("A ação não pode ser concluída.")
                                    continue

                            elif i[3] == "Free Fire":
                                novoelocod = int(
                                    input("1 - Bronze\n2 - Prata\n3 - Ouro\n4 - Platina\n5 - Diamante\n6 - Mestre"
                                          "\n7 - Desafiante\n8 - Unranked\nInsira o código do elo:"))

                                if novoelocod == 1:
                                    ramificacao = int(input("1 - I\n2 - II\n3 - III\nDigite o código da ramificação:"))
                                    if ramificacao == 1:
                                        novoelo = "Bronze I"
                                    elif ramificacao == 2:
                                        novoelo = "Bronze II"
                                    elif ramificacao == 3:
                                        novoelo = "Bronze III"
                                    else:
                                        print("A ação não pode ser concluída.")
                                        continue

                                elif novoelocod == 2:
                                    ramificacao = int(input("1 - I\n2 - II\n3 - III\nDigite o código da ramificação:"))
                                    if ramificacao == 1:
                                        novoelo = "Prata I"
                                    elif ramificacao == 2:
                                        novoelo = "Prata II"
                                    elif ramificacao == 3:
                                        novoelo = "Prata III"
                                    else:
                                        print("A ação não pode ser concluída.")
                                        continue

                                elif novoelocod == 3:
                                    ramificacao = int(
                                        input("1 - I\n2 - II\n3 - III\n4 - IV\nDigite o código da ramificação:"))
                                    if ramificacao == 1:
                                        novoelo = "Ouro I"
                                    elif ramificacao == 2:
                                        novoelo = "Ouro II"
                                    elif ramificacao == 3:
                                        novoelo = "Ouro III"
                                    elif ramificacao == 4:
                                        novoelo = "Ouro IV"
                                    else:
                                        print("A ação não pode ser concluída.")
                                        continue

                                elif novoelocod == 4:
                                    ramificacao = int(
                                        input("1 - I\n2 - II\n3 - III\n4 - IV\nDigite o código da ramificação:"))
                                    if ramificacao == 1:
                                        novoelo = "Platina I"
                                    elif ramificacao == 2:
                                        novoelo = "Platina II"
                                    elif ramificacao == 3:
                                        novoelo = "Platina III"
                                    elif ramificacao == 4:
                                        novoelo = "Platina IV"
                                    else:
                                        print("A ação não pode ser concluída.")
                                        continue

                                elif novoelocod == 5:
                                    ramificacao = int(
                                        input("1 - I\n2 - II\n3 - III\n4 - IV\nDigite o código da ramificação:"))
                                    if ramificacao == 1:
                                        novoelo = "Diamante I"
                                    elif ramificacao == 2:
                                        novoelo = "Diamante II"
                                    elif ramificacao == 3:
                                        novoelo = "Diamante III"
                                    elif ramificacao == 4:
                                        novoelo = "Diamante IV"
                                    else:
                                        print("A ação não pode ser concluída.")
                                        continue

                                elif novoelocod == 6:
                                    novoelo = "Mestre"

                                elif novoelocod == 7:
                                    novoelo = "Desafiante"

                                elif novoelocod == 8:
                                    novoelo = "Unranked"
                                else:
                                    print("A ação não pode ser concluída.")
                                    continue
                            else:
                                print("A ação não pode ser concluída.")
                                continue

                        edit_elo(nomeeditar, novoelo)

    elif menu == 5:
        conddados = True

        while conddados:
            verDadosouN = int(input("1 - Verificar Dados\n2 - Voltar\nInsira o código:"))

            if verDadosouN == 2:
                conddados = False
            else:
                tipodedado = int(input("1 - Dados gerais do projeto\n2 - Dados League of Legends\n3 - Dados Valorant"
                                       "\n4 - Dados Free Fire\nQuais Dados deseja exibir?"))

                if tipodedado == 1:
                    dadogeral = int(input("1 - Quantidade total de Alunas\n2 - Lista geral de alunas"
                                          "\n3 - Quantidade geral de alunas no competitivo"
                                          "\n4 - Quantidade geral de alunas no modo normal"
                                          "\nQuais Dados deseja exibir agora?"))

                    if dadogeral == 1:
                        print("Quantidade total de alunas inscritas no projeto:", qtd_ttl)

                    elif dadogeral == 2:
                        print("Lista geral de alunas:")
                        print("Orientação: [Nome],[Nick],[Telefone],[Jogo],[Elo],[Categoria]")
                        for j in listageral:
                            print(j, end="\n")

                    elif dadogeral == 3:
                        qtdcomp = 0
                        for k in listageral:
                            if k[5] == "Competitivo":
                                qtdcomp += 1
                        print("Quantidade de alunas do modo Normal:", qtdcomp,
                              "\n***Para a lista, verificar em seus respectivos jogos***")

                    elif dadogeral == 4:
                        qtdnorm = 0
                        for l in listageral:
                            if l[5] == "Normal":
                                qtdnorm += 1
                        print("Quantidade de alunas do modo Competitivo:", qtdnorm,
                              "\n***Para a lista, verificar em seus respectivos jogos***")
                    else:
                        print("A ação não pode ser concluída.")
                        continue

                elif tipodedado == 2:
                    dadogeral = int(input("1 - Quantidade total de Alunas no League of Legends"
                                          "\n2 - Lista geral de alunas do League of Legends"
                                          "\n3 - Quantidade geral de alunas no modo competitivo do League of Legends"
                                          "\n4 - Quantidade geral de alunas no modo normal do League of Legends"
                                          "\n5 - Lista geral de alunas no modo normal do League of Legends"
                                          "\n6 - Lista geral de alunas no modo competitivo do League of Legends"
                                          "\nQuais Dados deseja exibir agora?"))

                    if dadogeral == 1:
                        qtdlol = 0
                        for m in listageral:
                            if m[3] == "League of Legends":
                                qtdlol += 1
                        print("Quantidade de alunas do League of Legends:", qtdlol)

                    elif dadogeral == 2:
                        print("Lista de alunas de League of legends:")
                        print("Orientação: [Nome],[Nick],[Telefone],[Jogo],[Elo],[Categoria]")
                        for n in listageral:
                            if n[3] == "League of Legends":
                                print(n, end="\n")

                    elif dadogeral == 3:
                        qtdcomplol = 0
                        for o in listageral:
                            if o[3] == "League of Legends" and o[5] == "Competitivo":
                                qtdcomplol += 1
                        print("Quantidade de alunas do modo Competitivo no League of Legends:", qtdcomplol)

                    elif dadogeral == 4:
                        qtdnormlol = 0
                        for p in listageral:
                            if p[3] == "League of Legends" and p[5] == "Normal":
                                qtdnormlol += 1
                        print("Quantidade de alunas do modo Normal no League of Legends:", qtdnormlol)

                    elif dadogeral == 5:
                        print("Lista de alunas do modo competitivo em League of Legends:")
                        print("Orientação: [Nome],[Nick],[Telefone],[Jogo],[Elo],[Categoria]")
                        for q in listageral:
                            if q[3] == "League of Legends" and q[5] == "Competitivo":
                                print(q, end="\n")

                    elif dadogeral == 6:
                        print("Lista de alunas do modo normal em League of Legends:")
                        print("Orientação: [Nome],[Nick],[Telefone],[Jogo],[Elo],[Categoria]")
                        for r in listageral:
                            if r[3] == "League of Legends" and r[5] == "Normal":
                                print(r, end="\n")
                    else:
                        print("A ação não pode ser concluída.")
                        continue

                elif tipodedado == 3:
                    dadogeral = int(input("1 - Quantidade total de Alunas no Valorant"
                                          "\n2 - Lista geral de alunas do Valorant"
                                          "\n3 - Quantidade geral de alunas no competitivo do Valorant"
                                          "\n4 - Quantidade geral de alunas no modo normal do Valorant"
                                          "\n5 - Lista geral de alunas no modo normal do Valorant"
                                          "\n6 - Lista geral de alunas no modo competitivo do Valorant"
                                          "\nQuais Dados deseja exibir agora?"))

                    if dadogeral == 1:
                        qtdval = 0
                        for s in listageral:
                            if s[3] == "Valorant":
                                qtdval += 1
                        print("Quantidade de alunas do Valorant:", qtdval)

                    elif dadogeral == 2:
                        print("Lista de alunas de Valorant:")
                        print("Orientação: [Nome],[Nick],[Telefone],[Jogo],[Elo],[Categoria]")
                        for t in listageral:
                            if t[3] == "Valorant":
                                print(t, end="\n")

                    elif dadogeral == 3:
                        qtdcompval = 0
                        for u in listageral:
                            if u[3] == "Valorant" and u[5] == "Competitivo":
                                qtdcompval += 1
                        print("Quantidade de alunas do modo Competitivo de Valorant:", qtdcompval)

                    elif dadogeral == 4:
                        qtdnormval = 0
                        for v in listageral:
                            if v[3] == "Valorant" and v[5] == "Normal":
                                qtdnormval += 1
                        print("Quantidade de alunas do modo Normal no Valorant:", qtdnormval)

                    elif dadogeral == 5:
                        print("Lista de alunas do modo competitivo em Valorant:")
                        print("Orientação: [Nome],[Nick],[Telefone],[Jogo],[Elo],[Categoria]")
                        for w in listageral:
                            if w[3] == "Valorant" and w[5] == "Competitivo":
                                print(w, end="\n")

                    elif dadogeral == 6:
                        print("Lista de alunas do modo normal em Valorant:")
                        print("Orientação: [Nome],[Nick],[Telefone],[Jogo],[Elo],[Categoria]")
                        for x in listageral:
                            if x[3] == "Valorant" and x[5] == "Normal":
                                print(x, end="\n")
                    else:
                        print("A ação não pode ser concluída.")
                        continue

                elif tipodedado == 4:
                    dadogeral = int(input("1 - Quantidade total de Alunas no Free Fire"
                                          "\n2 - Lista geral de alunas do Free Fire"
                                          "\n3 - Quantidade geral de alunas no competitivo do Free Fire"
                                          "\n4 - Quantidade geral de alunas no modo normal do Free Fire"
                                          "\n5 - Lista geral de alunas no modo normal do Free Fire"
                                          "\n6 - Lista geral de alunas no modo competitivo do Free Fire"
                                          "\nQuais Dados deseja exibir agora?"))

                    if dadogeral == 1:
                        qtdff = 0
                        for y in listageral:
                            if y[3] == "Free Fire":
                                qtdff += 1
                        print("Quantidade de alunas do Free Fire:", qtdff)

                    elif dadogeral == 2:
                        print("Lista de alunas de Free Fire:")
                        print("Orientação: [Nome],[Nick],[Telefone],[Jogo],[Elo],[Categoria]")
                        for z in listageral:
                            if z[3] == "Free Fire":
                                print(z, end="\n")

                    elif dadogeral == 3:
                        qtdcompff = 0
                        for aa in listageral:
                            if aa[3] == "Free Fire" and aa[5] == "Competitivo":
                                qtdcompff += 1
                        print("Quantidade de alunas do modo Competitivo de Free Fire:", qtdcompff)

                    elif dadogeral == 4:
                        qtdnormff = 0
                        for ab in listageral:
                            if ab[3] == "Free Fire" and ab[5] == "Normal":
                                qtdnormff += 1
                        print("Quantidade de alunas do modo Normal no Free Fire:", qtdnormff)

                    elif dadogeral == 5:
                        print("Lista de alunas do modo competitivo em Free Fire:")
                        print("Orientação: [Nome],[Nick],[Telefone],[Jogo],[Elo],[Categoria]")
                        for ac in listageral:
                            if ac[3] == "Free Fire" and ac[5] == "Competitivo":
                                print(ac, end="\n")

                    elif dadogeral == 6:
                        print("Lista de alunas do modo normal em Free Fire:")
                        print("Orientação: [Nome],[Nick],[Telefone],[Jogo],[Elo],[Categoria]")
                        for ad in listageral:
                            if ad[3] == "Free Fire" and ad[5] == "Normal":
                                print(ad, end="\n")
                    else:
                        print("A ação não pode ser concluída.")
                        continue
                else:
                    print("A ação não pode ser concluída.")
                    continue

    elif menu == 6:
        print("Saindo...")
        time.sleep(3)
        cond1 = False
    else:
        print("A ação não pode ser concluída.")
        continue
