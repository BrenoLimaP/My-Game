label parte2:
    call screen corredor

    label escritorio:
        scene black
        n "Está trancado?!!"
        n "Parece que preciso de uma senha de 6 digitos! Mas que merda, como vou saber a senha disso?!"
        n "Será que meus pais deixaram alguma coisa pela casa?"
        while senhaDigitada != senhaCerta:
            python:
                senhaDigitada = renpy.input("Qual será a senha? Deixa eu ver...",length=6, allow="1234567890") #pixel_width=200
            if senhaDigitada != senhaCerta:
                "Droga! Não é isso!"
                "Preciso procurar pela casa."
                call screen corredor

            if senhaDigitada == senhaCerta:
                "Consegui!!!"

        scene escritorio at center with fade


    show chave at center:
        zoom 0.1
        yalign 0.65
        xalign 0.45

    show prota at center:
        zoom 0.35
    with dissolve

    # fazer varias reações do prota

    n "X"

    show prota at center:
        zoom 0.35
    with dissolve

    # fazer varias reações do prota

    $ style.say_window = style.window_cg
    p"Acho que a última vez que vi ou entrei nesse escritório foi quando eu era criança…"

    $ style.say_window = style.window

    n"X"

    #(AQUI VOCÊ MOSTRA A FOTO QUE O S/N TA FALANDO)

    $ style.say_window = style.window
    $ style.say_window = style.window_cg
    show prota at center:
        zoom 0.35
    with dissolve
    scene escritoriosombra
    show foto at truecenter:
        zoom 0.0
        linear 0.1 zoom 0.8
    with dissolve
    pause
    hide foto
    scene escritorio at center with dissolve
    show chave at center:
        zoom 0.1
        yalign 0.65
        xalign 0.45

    p"(Eu lembro que fiquei de cara amarrada nesse dia, porque eles me disseram que eu era gordo e fofo, que nem um porquinho)"

    p"(Achei ofensivo, mas olhando bem essa foto, eles até que tinham razão)"

    n"Passo meus dedos pela foto amorosamente"
    $ style.say_window = style.window

    show prota at center:
        zoom 0.35
    with dissolve
    $ style.say_window = style.window_cg
    p"Apesar disso, não fiquei emburrado por muito tempo, já que eles viviam fazendo graça pra mim quando isso acontecia"

    show prota at center:
        zoom 0.35
    with dissolve

    p" Bom, vamos continuar xeretando por aí!"

    #(ESSE DIÁLOGO SOBRE AS FOTOS ACABA AQUI)

    #(SE ACHOU UMA CAIXA ESCONDIDA NUM CANTO DO CHÃO:)

    n"Enquanto estou vasculhando o escritório, bati meu pé em alguma coisa dura no chão"

    $ style.say_window = style.window

    show prota at center:
        zoom 0.35
    with dissolve
    $ style.say_window = style.window_cg
    p" Hã? Uma caixa…?"

    n"X"

    scene quartodospais at center with fade

    #(AQUI VOCÊ REDIRECIONA O JOGADOR DIRETAMENTE PARA O CENÁRIO QUE É O QUARTO DOS PAIS DELE)

    n"Depois de sentar na cama e abrir ela, encontrei vários documentos de uma pesquisa sobre tribos brasileiras antigas"

    show prota at center:
        zoom 0.35
    with dissolve

    $ style.say_window = style.window
    $ style.say_window = style.window_cg
    p"X"

    $ style.say_window = style.window

    show prota at center:
        zoom 0.35
    with dissolve
    $ style.say_window = style.window_cg
    p" X"

    $ style.say_window = style.window

    show prota at center:
        zoom 0.35
    with dissolve
    $ style.say_window = style.window_cg
    p"X"

    $ style.say_window = style.window

    show prota at center:
        zoom 0.35
    with dissolve
    $ style.say_window = style.window_cg
    p"X"

    $ style.say_window = style.window

    show prota at center:
        zoom 0.35
    with dissolve
    $ style.say_window = style.window_cg
    p" Depois eu olho isso, amanhã preciso acordar cedo e resolver algumas coisas da escola pra segunda"

    #(AQUI VOCÊ LIBERA A MOVIMENTAÇÃO DO PERSONAGEM E SÓ ENTÃO VOCÊ FAZ APARECER UM PEQUENO LIVRO EM CIMA DA CAMA DOS PAIS DELE [O DIÁRIO])

    #(QUANDO O JOGADOR CLICA NO DIÁRIO [ISSO É OBRIGATÓRIO PARA LIBERAR OS PRÓXIMOS DIÁLOGOS DE QUANDO ELE VAI PRA ESCOLA E ETC]: )

    show prota at center:
        zoom 0.35
    with dissolve

    p"X"

    $ style.say_window = style.window

    show prota at center:
        zoom 0.35
    with dissolve
    $ style.say_window = style.window_cg
    p"X"

    $ style.say_window = style.window

    show prota at center:
        zoom 0.35
    with dissolve
    $ style.say_window = style.window_cg
    p"X"

    $ style.say_window = style.window

    show prota at center:
        zoom 0.35
    with dissolve
    $ style.say_window = style.window_cg
    p"X"

    #(LIBERA A MOVIMENTAÇÃO PRO JOGADOR E QUANDO ELE ENTRAR NO QUARTO DELE, LIBERA MAIS UM DIÁLOGO:)
    #call screen corredor2

    scene meuquarto at center with fade

    n"Chegando no meu quarto, coloquei meu pijama, deitei na cama e dormi, estranhamente mais rápido que o comum"

    #(AQUI VOCÊ COLOCA UMA TELA BRANCA QUE VAI APARECENDO COM AQUELE EFEITO DE TELA QUE VAI DESINTEGRANDO, E A PARTIR DAÍ O CENÁRIO VAI CONTINUAR COMO SE ESTIVÉSSEMOS VENDO O SONHO DO PROTA)

    n"X"

    $ style.say_window = style.window

    show prota at center:
        zoom 0.35
    with dissolve
    $ style.say_window = style.window_cg
    p" Agh!"  #(SE POSSIVEL AQUI, COLOCA UMA TREMEDEIRA NA TELA E UM BARULHO DE QUANDO ALGUÉM TROPEÇA NO MATO OU COISA DO TIPO)"

    $ style.say_window = style.window

    show prota at center:
        zoom 0.35
    with dissolve
    $ style.say_window = style.window_cg
    p"X"

    $ style.say_window = style.window

    show prota at center:
        zoom 0.35
    with dissolve
    $ style.say_window = style.window_cg
    p" Quem é você?! É você que está me perseguindo?!?!?!"

    s"Shiii~ Se você for tão barulhento assim, ele vai encontrar você..."

    show prota at center:
        zoom 0.35
    with dissolve

    p" QUEM DIABOS É ELE?!?!"

    n"**Crack**"  #(BARULHO DE GALHO QUEBRANDO)

    $ style.say_window = style.window
    $ style.say_window = style.window_cg

    s"X"

    $ style.say_window = style.window

    show prota at center:
        zoom 0.35
    with dissolve
    $ style.say_window = style.window_cg
    p"X"

    $ style.say_window = style.window

    show prota at center:
        zoom 0.35
    with dissolve
    $ style.say_window = style.window_cg
    p" Pai? Mãe?"

    show pai at right:
        zoom 0.15
    with dissolve

    o"Filho, por que você me matou?"

    m"Você nos odiava tanto que tínhamos que morrer?"

    show prota at center:
        zoom 0.35
    with dissolve

    p" NÃO É VERDADE!"

    show mãe at left:
        zoom 0.15
    with dissolve

    m"Foi culpa sua! Você nos matou!"

    show prota at center:
        zoom 0.35
    with dissolve
    $ style.say_window = style.window_cg
    p" Não é verdade, mãe, pai! Eu amava vocês…! Ainda os amo muito!"


    $ style.say_window = style.window
    n" Eu nunca os odiei, desculpa por não ter dito muito que os amava antes!"

    $ style.say_window = style.window
    $ style.say_window = style.window_cg
    k"X"

    $ style.say_window = style.window

    show prota at center:
        zoom 0.35
    with dissolve
    $ style.say_window = style.window_cg
    p"X"

    n"**Crack**"  #(BARULHO DE VIDRO QUEBRANDO)

    n"X"

    #(AQUI O SONHO ACABA)

    $ style.say_window = style.window

    show prota at center:
        zoom 0.35
    with dissolve
    $ style.say_window = style.window_cg
    p" NÃO!!!"

    hide mãe
    hide pai

    $ style.say_window = style.window

    show prota at center:
        zoom 0.35
    with dissolve
    $ style.say_window = style.window_cg
    p" São 4h30 ainda…"


    $ style.say_window = style.window
    n"Desanimado, me levanto da cama e vou tomar um banho para relaxar"

    n"Me olho no espelho e vejo as noites mal dormidas que eu venho tendo desde o acidente, que são claramente visíveis nas bolsas escuras abaixo dos meus olhos"

    $ style.say_window = style.window

    show prota at center:
        zoom 0.35
    with dissolve
    $ style.say_window = style.window_cg
    p" Grande dia!"


    $ style.say_window = style.window
    n"Termino de me arrumar, pego minha mochila e saio, levando o diário e a fotografia dos meus pais junto comigo"

    #(AQUI VOCÊ LIBERA A MOVIMENTAÇÃO DO JOGADOR E FAZ ELE IR PRA ESCOLA)

    call screen corredor1