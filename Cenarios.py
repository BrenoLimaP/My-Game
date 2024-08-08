screen estaçãotrem:
    add "trem"
    imagebutton:
        xpos 1450
        ypos 950
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textvoltar"), Jump("saidarua")

        hovered Show("textvoltar",
            displayText = "Casa")
        unhovered Hide("textvoltar")
    #Quadro
    imagebutton:
        xpos 350
        ypos 650
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textquadro"), Jump("NãoAmigo")

        hovered Show("textquadro",
            displayText = "Trem")
        unhovered Hide("textquadro")
#esse aqui
screen ruadomercado:
    add "ruade"

    imagebutton:
        xpos 1750
        ypos 800
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textparque"), Jump("saidarua")

        hovered Show("textparque",
            displayText = "Parque{p}Entrada")
        unhovered Hide("textparque")
    #Quadro
    imagebutton:
        xpos 900
        ypos 600
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textcasa1"), Jump("saidarua")

        hovered Show("textcasa1",
            displayText = "Casa")
        unhovered Hide("textcasa1")

    imagebutton:
        xpos 320
        ypos 850
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textcaixa"), Jump("mercado")#imagem ruim

        hovered Show("textcaixa",
            displayText = "Esquina")
        unhovered Hide("textcaixa")
#esse aqui
screen mercado:
    add "mercadinho"

    imagebutton:
        xpos 1700
        ypos 920
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textvoltar"), Jump("pontodeonibus")#imagem ruim

        hovered Show("textvoltar",
            displayText = "Ponto de Ônibus")
        unhovered Hide("textvoltar")
    #Quadro
    imagebutton:
        xpos 1400
        ypos 600
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textquadro"), Jump("ruademanha")

        hovered Show("textquadro",
            displayText = "Mercadinho")
        unhovered Hide("textquadro")
    imagebutton:
        xpos 100
        ypos 620
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textcaixa"), Jump("rodoanel")#imagem ruim

        hovered Show("textcaixa",
            displayText = "Rodovia A")
        unhovered Hide("textcaixa")
# esse aqui
screen rodoanel:
    add "rodovia"

    imagebutton:
        xpos 350
        ypos 1000
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textvoltar"), Jump("mercado")

        hovered Show("textvoltar",
            displayText = "esquina")
        unhovered Hide("textvoltar")
    #Quadro
    imagebutton:
        xpos 950
        ypos 450
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textquadro"), Jump("quadro")

        hovered Show("textquadro",
            displayText = "Rodovia B")
        unhovered Hide("textquadro")
#esse
screen pontodeonibus:
    add "ponto"

    imagebutton:
        xpos 1350
        ypos 900
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textvoltar"), Jump("mercado")

        hovered Show("textvoltar",
            displayText = "esquina")
        unhovered Hide("textvoltar")
    #Quadro
    imagebutton:
        xpos 1000
        ypos 650
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textquadro"), Jump("quadro")

        hovered Show("textquadro",
            displayText = "Ponto de Ônibus")
        unhovered Hide("textquadro")

    imagebutton:
        xpos 320
        ypos 650
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textcaixa"), Jump("parquediadema")

        hovered Show("textcaixa",
            displayText = "Passarela")
        unhovered Hide("textcaixa")
#esse
screen parquediadema:
    add "parque"

    imagebutton:
        xpos 1100
        ypos 1000
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textvoltar"), Jump("pontodeonibus")

        hovered Show("textvoltar",
            displayText = "Ponto de Ônibus")
        unhovered Hide("textvoltar")
    #Quadro
    imagebutton:
        xpos 1200
        ypos 650
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textquadro"), Jump("viela")

        hovered Show("textquadro",
            displayText = "Beco")
        unhovered Hide("textquadro")
    imagebutton:
        xpos 200
        ypos 650
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textcaixa"), Jump("cafezis")

        hovered Show("textcaixa",
            displayText = "café Memória")
        unhovered Hide("textcaixa")
#esse
screen viela:
    add "beco"
    #Quadro
    imagebutton:
        xpos 1220
        ypos 720
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textquadro"), Jump("portao")

        hovered Show("textquadro",
            displayText = "Portão da Escola")
        unhovered Hide("textquadro")
    imagebutton:
        xpos 1050
        ypos 950
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textcaixa"), Jump("parquediadema")

        hovered Show("textcaixa",
            displayText = "Passarela")
        unhovered Hide("textcaixa")