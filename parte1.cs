label continuacao:
    hide screen quick_button
    hide screen quick_button1
    hide screen quick_button2
    hide screen quick_button3
    hide E
    hide P
    hide T
    hide Y
        
    scene patio
    $ style.say_window = style.window
    n"X"

    show prota at center:
        zoom 0.35
    with dissolve
    
    p"X"

    $ style.say_window = style.window
    n"X"

    #(LIBERA MOVIMENTAÇÃO DE NOVO DA ESCOLA)

    #(QUANDO ELE CHEGA NA SALA DE AULA:)

    n"X"

    show fernando at center:
        zoom 0.2
    with dissolve
    $ style.say_window = style.window_cg
    
    e"Pode se sentar no seu lugar"

    show prota at center:
        zoom 0.35
    with dissolve

    p" Tudo bem…"

    $ style.say_window = style.window

    n"Arrumo minhas coisas no meu lugar, ainda com os olhares dos meus colegas"

    $ style.say_window = style.window
    
    e"[nomeP]"

    n"X"

    show prota at center:
        zoom 0.35
    with dissolve

    p" …"

    $ style.say_window = style.window

    n"X"

    show prota at center:
        zoom 0.35
    with dissolve
    
    p"X"
    
    e"Jonas, Ana e [nomeP]"
    hide fernando
    show jonas at center:
        zoom 0.38
    with dissolve

    j"Jonas dá uma piscadela para Ana, que faz um sinal de positivo com o dedão para Jonas"
    hide jonas

    show prota at center:
        zoom 0.35
    with dissolve

    p"O que?!?!?!?!"

    n"X"

    #(AQUI A GENTE MOSTRA O CELULAR COM AS MENSAGENS DO WHATSAPP COM O CHAT DO GRUPO COM O JONAS E A ANA ABERTO)

    #(ENCERRA A CONVERSA NO WHATSAPP AQUI)

    n"Coloco a mão na testa, como se algo inconveniente estivesse sendo forçado em mim"

    show prota at center:
        zoom 0.35
    with dissolve
    
    p"X"

    show prota at center:
        zoom 0.35
    with dissolve

    p"(Sinto como se eu estivesse sendo arrastado pelos meus dois melhores amigos de novo...)"

    n"Eu suspiro"

    show prota at center:
        zoom 0.35
    with dissolve
    
    p "X"

    #(A PARTIR DE AGR VOU COLOCAR UM "(...)" TODA VEZ QUE FOR MESMA FRASE MAS FOR PRA SER COLOCADA EM CLIQUES DIFERENTES NO JOGO, PRA N FICAR MUITO GRANDE AS FRASES NA TEXTBOX)

    #(4. CHEGANDO NO ASILO...)

    n"Com uma freiada repentina o ônibus para abruptamente"

    n"Acordo assustado e bato minha cabeça no banco da frente sem querer"

    show prota at center:
        zoom 0.35
    with dissolve
    
    p" AI!!"

    n"Irritado olho ao redor para tentar entender o que aconteceu"

    show prota at center:
        zoom 0.35
    with dissolve
    
    p "X"

    show ana at left:
        zoom 0.2
    with dissolve
    
    A"Esse motorista idiota que dormiu no volante, parece!"
    hide ana

    show prota at center:
        zoom 0.35
    with dissolve

    p"Muito sem noção"
    hide prota

    show jonas at right:
        zoom 0.38
    with dissolve

    j"X"

    show jonas at right:
        zoom 0.38
    with dissolve
    
    j"X"
    hide jonas
    show ana at left:
        zoom 0.2
    with dissolve

    A"X"
    hide ana

    show prota at center:
        zoom 0.35
    with dissolve

    p"X"
    hide prota

    show jonas at right:
        zoom 0.38
    with dissolve

    j"Tem eu, ué!"
    hide jonas

    show ana at left:
        zoom 0.2
    with dissolve

    A"Ele falou Ser humano normal Jonas"
    hide ana

    show jonas at right:
        zoom 0.38
    with dissolve

    j "Ei!"

    n"Ele dá uma cotovelada na cintura da Ana, que começa a rir, já que ela sente cócegas"

    show ana at left:
        zoom 0.2
    with dissolve
    
    A"X"

    n"X"

    show jonas at right:
        zoom 0.38
    with dissolve
    
    j"X"

    show ana at left:
        zoom 0.2
    with dissolve
    
    A"X"

    show jonas at right:
        zoom 0.38
    with dissolve
    
    j"Eu sei que não sou formado em logística, mas alguém consegue me explicar como eu fui parar com dois caras que mal vem pra escola?"
    
    hide jonas

    show prota at center:
        zoom 0.35
    with dissolve

    p"Tá reclamando do que? Pelo menos você tem colega de quarto"
    hide prota

    show ana at left:
        zoom 0.2
    with dissolve

    A "Hehehe, parece que quem tá com a sorte grande aqui sou eu"

    n"Ela aponta para a sua colega de quarto, discretamente"

    show ana at left:
        zoom 0.2
    with dissolve
    
    A"Meus pêsames pra vocês dois, porque eu farei amizade com a novinha bonitinha ali enquanto vocês sofrem de solidão"

    n"Ela se vira e corre na direção da menina, que parecia estar aguardando por ela"

    show ana at left:
        zoom 0.2
    with dissolve
    
    A "Ow novinha~"

    n"Enquanto isso, os dois seniores do clube de basquete chamavam o Jonas"

    show jonas at right:
        zoom 0.38
    with dissolve
    
    j" Foi mal. Estão me chamando ali, te vejo mais tarde!"
    hide jonas

    show prota at center:
        zoom 0.35
    with dissolve

    p "X"

    #(LIBERA MOVIMENTAÇÃO NO CENÁRIO PARA O JOGADOR)

    #"SE ACHOU E CLICOU NA FOLHA DE MOVIMENTO DO QUARTO"

    show prota at center:
        zoom 0.35
    with dissolve
    
    p"(Quarto 208… É aqui!)"

    #(DEPOIS DESSE DIÁLOGO, REDIRECIONA ELE PRA DENTRO DO QUARTO)

    n"Ando pelo quarto e começo a analisar o local, tentando me familiarizar com o ambiente estranho"

    n"Eu suspiro, Desanimado"

    show prota at center:
        zoom 0.35
    with dissolve
    
    p"(Muito bem, o que eu devia fazer a seguir?)"

    #OPÇÃO: 1. Arrumar minhas coisas
    #OPÇÃO: 2. Ir explorar
    #SE ESCOLHEU 1:

    n"Colocando cada coisa no seu devido lugar até que minha mochila esteja praticamente vazia, eu suspiro e me deito na cama, cansado"

    show prota at center:
        zoom 0.35
    with dissolve
    
    p "X"

    show prota at center:
        zoom 0.35
    with dissolve
    
    p"(Será que eu devia ir explorar, só pra variar...?)"

    #(LIBERA A MOVIMENTAÇÃO NO CENÁRIO PARA O JOGADOR)
    #SE ESCOLHEU 2:

    show prota at center:
        zoom 0.35
    with dissolve

    p"(Até amanhã dá tempo de guardar essas coisas, então depois eu vejo isso!)"

    #(LIBERA A MOVIMENTAÇÃO NO CENÁRIO PARA O JOGADOR)
    #CONTINUANDO A PARTIR DO FIM DESSAS DUAS OPÇÕES, O DIÁLOGO RETOMA QUANDO O PROTA ACHA O SENHOR IDOSO NO LADO DE FORA DO ASILO, ENCARANDO A FLORESTA:

    show prota at center:
        zoom 0.35
    with dissolve

    p "X"

    show prota at center:
        zoom 0.35
    with dissolve
    
    p "A monitora disse que podemos ficar fazendo companhia para um hóspede em especial do asilo, se assim preferirmos"

    n"Ele não responde"

    show prota at center:
        zoom 0.35
    with dissolve
    
    p "X"

    show prota at center:
        zoom 0.35
    with dissolve

    p"X"

    show prota at center:
        zoom 0.35
    with dissolve
    
    p "!!!"

    n"Olho para baixo e mexo com meus dedos de nervosismo, enquanto ele apenas continuou assim, do mesmo jeito em silêncio de novo"

    show prota at center:
        zoom 0.35
    with dissolve
    
    p "X"

    show prota at center:
        zoom 0.35
    with dissolve
    
    p"X"

    #(AQUI FAZEMOS UMA TRANSIÇÃO DE TELA PARA O PERÍODO NOTURNO)

    n"X"

    show prota at center:
        zoom 0.35
    with dissolve
    
    p"X"

    show prota at center:
        zoom 0.35
    with dissolve
    
    p " Do que o senhor tá falando?"

    n"Eu sorrio para disfarçar, mas ele apenas me encara, sem mais nem menos"

    n"Eu suspiro em desistência"

    show prota at center:
        zoom 0.35
    with dissolve
    
    p" Eu não queria falar nada, porque você provavelmente pensaria que eu estou ficando louco"

    n"O senhor apenas me dá um sorriso terno e permanece em silêncio"

    n"Eu encaro a paisagem, incapaz de olhar em seus olhos"

    show prota at center:
        zoom 0.35
    with dissolve
    
    p "X"

    show prota at center:
        zoom 0.35
    with dissolve
    
    p "Nada vem fácil pra mim, né? Pqp"

    n"Reviro os olhos de irritação e fecho a cara"

    n"Quando pensei em finalmente ir deitar, fui interrompido pela visão de uma sombra branca em meio à mata"

    show prota at center:
        zoom 0.35
    with dissolve
    
    p "X"

    show prota at center:
        zoom 0.35
    with dissolve
    
    p " Haa...Droga…!Pra onde… aquela coisa...foi…? Haa…"

    n"Quando recuperei um pouco do meu cérebro e parei para pensar, percebi que estou em um lugar estranho"

    show prota at center:
        zoom 0.35
    with dissolve
    
    p "Hmm…"

    n"Olho ao redor, sem ver nenhum sinal de luz ou pessoas por perto"

    #(DESCULPA, MAS COMO BRASILEIRA EU FUI OBRIGADA A COLOCAR ESSE TERMO AQUI MESMO EU ME SEGURANDO PRA N COLOCAR NADA DO TIPO DESDE O COMEÇO. QUALQUER COISA SÓ COLOCAR "LINGUAGEM IMPRÓPRIA NA CLASSIFICAÇÃO INDICATIVA DO JOGO)

    show prota at center:
        zoom 0.35
    with dissolve
    
    p "X"

    show prota at center:
        zoom 0.35
    with dissolve
    
    p"X"

    show prota at center:
        zoom 0.35
    with dissolve
    
    p" (E se as sombras voltaram? Elas vieram me enterrar no abismo de novo?)"

    n"Fecho os olhos apertado"

    show prota at center:
        zoom 0.35
    with dissolve

    p" (Já era! Sinto que dessa vez eu não seria capaz de escapar…)"


label escola:
    scene patio
    jump qboton