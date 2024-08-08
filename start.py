# The script of the game goes in this file.
# Declare characters used by this game. The color argument colorizes the
# name of the character.
# The game starts here.
init python:
    senhaCerta = "258322"
    senhaDigitada = ""
    estudante = False
    chavedoescritorio = False
    garrafinha = False 
    caderno = False
    mensagens = False

default timeout = 1.0
$ arr_keys = ["q", "w", "r", "t", "y"]

label start:
    $ quick_menu=False
    stop music
    scene black
    with Pause(1)
    show text "{font=fonts/SketchGothicSchool.ttf}{size=80}{color=#1b0f87}Apresentamos{/size}{/color}{/font}" with fade
    $ renpy.pause(3.0)
    show text "{font=fonts/SketchGothicSchool.ttf}{size=80}{color=#1b0f87}Anhangá{/size}{/color}{/font}" with fade
    $ renpy.pause(3.0)

    scene prologo with fade
    $ renpy.pause(3.0)

    scene black with fade
    $ renpy.pause(2.0)

    #prologo
    label nome:
        $ quick_menu=True 
        $nomeP = renpy.input ("Escolha um nome para o protagonista:",length=10)
        menu:
            "Continuar como {color=#d235db}([nomeP]){/color}?":
                jump keep
            "Refazer Nome?":
                jump nome

label keep:
    scene black with fade
    $ renpy.pause(2.0)

    play music "audio/musicaJogo.mp3"
    #$renpy.block_rollback()
    $ style.say_window = style.window
    n "X"

    scene meuquarto at center with fade
    n "X"
    show mãe at center:
        zoom 0.2
        #linear 0.7 zoom 0.2
    with dissolve

    $ style.say_window = style.window_cg
    m "X"

    hide mãe
    show protaMeno at center:
        zoom 0.2
    with dissolve

    p "X"

    hide protaMeno
    show mãe at center:
        zoom 0.2
    with dissolve

    m "Não, querido. Já está tarde, você tem que sair cedo amanhã."

    hide mãe
    show protaMeno at center:
        zoom 0.2
    with dissolve

    p "Só mais uminha, por favorrrr! Eu juro que vou dormir depois dela!"

    hide protaMeno
    show mãe at center:
        zoom 0.2
    with dissolve

    m "Está bem..."
    m "Era uma vez… porque todas as histórias que se tornaram lendas, que se tornaram contos de fadas, se iniciam assim…"
    hide mãe
    show inimigosNeutros with dissolve
    #
    $ style.say_window = style.window
    n "Havia uma pequena tribo indígena que era como uma grande família…"
    scene Floresta_noite at center
    show inimigosNeutros
    n "X"
    scene meuquarto at center with fade
    hide inimigosNeutros
    hide mãe
    show protaMeno at center:
        zoom 0.2
    with dissolve

    $ style.say_window = style.window_cg

    p "Sério mamãe?"

    hide protaMeno
    show mãe at center:
        zoom 0.2
    with dissolve

    m " Sim, querido!"

    hide mãe
    show protaMeno at center:
        zoom 0.2
    with dissolve

    p "Então se eu cuidar bem da natureza, o senhor Deus vai cuidar de vocês para que vocês voltem logo para casa quando forem viajar?"
    $ style.say_window = style.window
    n "Ela faz uma expressão triste, mas sorri logo depois..."

    hide protaMeno
    show mãe at center:
        zoom 0.2
    with dissolve
    $ style.say_window = style.window_cg
    m "Claro, querido. Se você desejar com toda sua força, com certeza irá se realizar, mesmo sem pedir para divindade alguma."

    hide mãe
    show protaMeno at center:
        zoom 0.2
    with dissolve

    p "Entendi, mamãe!"
    $ style.say_window = style.window
    n "Ele sorri de forma meiga para sua mãe."
    n "E ela continua a historia..."

    hide protaMeno


    scene Floresta_noite at center with fade
    show inimigosNeutros with dissolve

    n "''Entre as divindades que cuidavam daquela grande família, havia um em especial que se mostrou extremamente ligado a eles, o que era uma coisa muito rara, já que ele não gostava de humanos e caçadores''."
    show anhanganeutro at center:
        zoom 0.4
    with dissolve

    n "X"

    hide anhanganeutro
    hide inimigosNeutros
    show colono_s_arma01 at center:
        zoom 0.5
    with dissolve

    n "''Os colonizadores chegaram repentinamente durante o dia com seus objetos estranhos e palavras doces e ludibriosas na tribo''."

    hide colono_s_arma01
    show inimigosNeutros at left with dissolve
    n "''No começo não eram muito bem vindos, já que eles eram completos forasteiros, mas depois de um tempo, eles logo conseguiram a atenção da tribo, e consequentemente, a sua confiança''."
    hide inimigosNeutros
    show colono_s_arma01 at center:
        zoom 0.5
    with dissolve
    n "X"
    hide colono_s_arma01
    hide anhanga pajé
    show inimigosNeutros
    show anhanganeutro at right:
        zoom 0.4
    with dissolve
    n "X"
    hide anhanganeutro
    hide inimigosNeutros
    show indios_inimigos_furiosos02
    n "MATA-LOS!!!"
    hide indios_inimigos_furiosos02
    scene meuquarto at center with fade

    $ style.say_window = style.window

    n "A criança se aconchega no colo da mãe, nervoso e triste."

    show mãe at center:
        zoom 0.2
    with dissolve

    $ style.say_window = style.window_cg

    m "O que foi, querido?"

    hide mãe
    show protaMeno at center:
        zoom 0.2
    with dissolve

    p "O senhor divindade vai ficar bem, mamãe?"

    hide protaMeno
    show mãe at center:
        zoom 0.2
    with dissolve

    m "X"

    hide mãe

    #anhanga fugindo
    $ style.say_window = style.window
    scene Floresta_noite
    show indios_inimigos_furiosos02
    show anhanganeutro at center:
        zoom 0.4
        linear 0.2 xalign 1.8
    n "X"
    hide indios_inimigos_furiosos02
    show anhanga pajé at center:
        zoom 0.4
    with dissolve
    $ style.say_window = style.window_cg
    a "X"
    hide anhanga pajé
    $ style.say_window = style.window
    n "X"
    show anhanga pajé at center:
        zoom 0.4
    with dissolve
    $ style.say_window = style.window_cg
    a "X"
    # mostrar paje
    $ style.say_window = style.window
    n "X"
    hide anhanga pajé
    show esposa_bebe_neutro01 at center:
        zoom 0.5
    with dissolve

    $ style.say_window = style.window_cg
    f "''Isso é muito ruim! Precisamos avisá-lo!''"
    hide esposa_bebe_neutro01
    show Raoniexaltado02 at center:
        zoom 0.4
    with dissolve
    i "''Eu vou, você vai para casa e se esconde bem com o nosso filho''."
    scene black
    $ style.say_window = style.window
    n "''Com a permissão dele, o índio se manteve na vila como um apaziguador entre os dois lados, enquanto passava informações a ele para driblar seus planos sem machucar nenhum dos dois''."

    scene meuquarto at center with fade

    show protaMeno at center:
        zoom 0.2
    with dissolve

    $ style.say_window = style.window_cg

    p "Ainda bem que ele está lá para ajudar o senhor divindade contra os homens maus."

    hide protaMeno
    show mãe at center:
        zoom 0.2
    with dissolve

    m "Você parece com sono. Eu devia parar a história aqui?"

    hide mãe
    show protaMeno at center:
        zoom 0.2
    with dissolve
    p "Não, não! Eu aguento, eu sou forte!"

    hide protaMeno
    show mãe at center:
        zoom 0.2
    with dissolve
    m "Haha! tudo bem, querido!"
    scene black

    $ style.say_window = style.window
    n "''Entretanto, naquele dia…''"
    scene forest_bg_01:
        zoom 1.0
    n "''Esse mesmo indígena estava indo até a parte central da floresta, que guardava o local de repouso de Anhangá, mas naquele momento, ele não sabia que estava sendo seguido por um membro de sua tribo para descobrir informações''."

    show Raonineutro01 at center:
        zoom 0.4
    with dissolve
    $ style.say_window = style.window_cg
    i "''Caro amigo, as coisas não estão muito boas daquele lado. Creio que você esteja em perigo!''"
    hide Raonineutro01
    show anhanganeutro at center:
        zoom 0.4
    with dissolve
    d "''Bobagem, eles nunca me machucariam mesmo que nós não estejamos em bons termos agora. Eles são minha família também!''"
    hide anhanganeutro
    show Raonineutro01 at center:
        zoom 0.4
    with dissolve
    i "''Eu sei que eles são como família para você, mas desde que aqueles homens brancos chegaram nesta terra, as coisas mudaram de dentro para fora! Temo por sua segurança, meu amigo!''"
    hide Raonineutro01
    show anhanganeutro at center:
        zoom 0.4
    with dissolve
    d "''Bobagem, eu não irei falar mais nada sobre isso. Você devia voltar para a aldeia, eu vou me retirar...''"
    hide anhanganeutro
    $ style.say_window = style.window
    n "''Disse virando de costas para o índio.''"
    show anhanganeutro:
        zoom 0.4
        xalign 0.1
        linear 1.8 xalign 1.0
    "''Depois de um diálogo com o Deus, o mesmo índio que estava seguindo o amigo dele, esperou a oportunidade em que os dois baixaram a guarda"
    show traidor1:
        zoom 0.4
        xalign 0.1
        linear 1.0 xalign 0.5
    $ style.say_window = style.window
    "e partiu para o ataque à divindade!''."
    $ style.say_window = style.window_cg
    show Raoniexaltado02 at left:
        zoom 0.4
    with dissolve
    i " ''Não, cuidado!!!''"
    hide Raoniexaltado02
    $ style.say_window = style.window
    "''O Deus guardião se vira na direção de sua voz e então...''"
    scene black
    show background_video
    pause 1.0
    "''A haste de madeira em forma de cruz de uma árvore da floresta e a lâmina da lança banhada em castanha de caju, suas maiores fraquezas, acertou em cheio um ponto vital próximo de seu abdômen, entretanto, ele não morreu…''"
    #colocar anhaga ferido
    scene forest_bg_01:
        zoom 1.0
    show furia at right:
        zoom 0.4
    with dissolve
    $ style.say_window = style.window_cg
    d " ''Cof Cof, como pôde? Eu sou da sua família também...''"
    $ style.say_window = style.window
    "''A divindade se contorce, cuspindo um pouco de sangue.''"
    "''O índio manipulado sorriu e disse:"
    $ style.say_window = style.window_cg
    show traidor1 at center:
        zoom 0.4
    r "Você pode ter nos enganado antes, mas isso não funcionará agora, entidade maligna!''"
    scene black
    hide furia
    show furia at center:
        zoom 0.4
        xalign 0.5
        linear 0.1 xalign 0.51
        repeat
    with dissolve
    $ style.say_window = style.window
    n "''Disse, retirando a lança do seu abdômen e jogando no chão perto do outro índio''."
    n "''Consumido pela fúria de ser traído pelos outros indígenas, o Deus guardião partiu para cima do índio que tentou matá-lo, entretanto, não conseguiu machucá-lo graças ao seu melhor amigo que, foi atingido em seu lugar''."
    scene black with fade
    n "''A força foi suficiente para que as mãos do Deus atravessassem seu corpo, sem chance de cura."
    n "Entretanto, isso foi suficiente para que ele recuperasse a consciência e visse o que fez ao seu amigo''."
    n "''Mas era tarde demais...''"
    n "''Ele podia claramente, ver que o brilho dos olhos de seu amigo estava se apagando lentamente, mas não com emoções negativas, sim um grande alívio.''"
    show sentidos at left:
        xalign 0.2
        zoom 0.4
    with dissolve
    $ style.say_window = style.window_cg
    d " ''Não! Por quê? Por quê? POR QUÊ?!''"
    $ style.say_window = style.window
    n "''Gritou o Deus com lágrimas nos olhos e grande desespero para o índio''."
    show Raoniferidochoro03 at center:
        xalign 0.7
        zoom 0.4
    with dissolve
    n "''Seu amigo apenas deu-lhe um sorriso fraco e disse: "
    n "Fazer isso com sua amada família doeria mais em você do que em mim...''"
    n "''Depois disso, os olhos do índio se fecham e qualquer sinal de vida que ele possuía antes, havia desaparecido sem deixar rastros.''"
    # mostrar a morte do anhanga
    scene black
    n " ''Magoado com a sua perda e ferido pela lança, o Deus guardião deitou o corpo de seu amigo ao seu lado para preservá-lo como um túmulo de descanso eterno, e prometeu se vingar de todos aqueles que lhe fizeram mal e seus descendentes''."
    n "''Logo em seguida, a divindidade amaldiçou todos os aldeões e enfim, caiu em um estado de sono profundo em seu local de descanso."
    n "Mas, logo acordaria para realizar sua promessa...''"
    $ style.say_window = style.window_cg
    scene meuquarto at center with fade
    show mãe at center:
        zoom 0.2
    with dissolve

    m "O que achou da história, querido?"

    p " ... "

    m " Filho???"

    $ style.say_window = style.window

    n "A mulher olha para a criança dormindo e a arruma na cama. Ela apaga a luz do abajur e sai discretamente pela porta do quarto, parando para olhar uma última vez."
    jump CAPITULO1
