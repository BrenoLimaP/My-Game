screen saidarua:
    add "rua"
    
    imagebutton:
        xpos 1430
        ypos 620
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textcasa"), Jump("NãoAmigo")#imagem ruim

        hovered Show("textcasa", 
            displayText = "Casa")
        unhovered Hide("textcasa")
    #Quadro
    imagebutton:
        xpos 900
        ypos 580
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textmercadinho"), Jump("ruademanha")

        hovered Show("textmercadinho", 
            displayText = "Mercadinho")
        unhovered Hide("textmercadinho")

    imagebutton:
        xpos 630
        ypos 910
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textestacao"), Jump("estaçãotrem")

        hovered Show("textestacao", 
            displayText = "Estação")
        unhovered Hide("textestacao")
    
screen estaçãotrem:
    add "trem"
    
    imagebutton:
        xpos 1750
        ypos 900
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textvoltar"), Jump("saidarua")

        hovered Show("textvoltar", 
            displayText = "Casa")
        unhovered Hide("textvoltar")
    #Quadro
    imagebutton:
        xpos 1150
        ypos 200
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textquadro"), Jump("NãoAmigo")

        hovered Show("textquadro", 
            displayText = "Trem")
        unhovered Hide("textquadro")
    
screen ruadomercado:
    add "ruade"
    
    imagebutton:
        xpos 1750
        ypos 900
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textparque"), Jump("saidarua")

        hovered Show("textparque", 
            displayText = "Parque{p}Entrada")
        unhovered Hide("textparque")
    #Quadro
    imagebutton:
        xpos 900
        ypos 500
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textcasa1"), Jump("saidarua")

        hovered Show("textcasa1", 
            displayText = "Casa")
        unhovered Hide("textcasa1")

    imagebutton:
        xpos 320
        ypos 750
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textcaixa"), Jump("mercado")#imagem ruim

        hovered Show("textcaixa", 
            displayText = "Esquina")
        unhovered Hide("textcaixa")

screen mercado:
    add "mercadinho"
    
    imagebutton:
        xpos 1750
        ypos 900
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textvoltar"), Jump("pontodeonibus")#imagem ruim

        hovered Show("textvoltar", 
            displayText = "Ponto de Ônibus")
        unhovered Hide("textvoltar")
    #Quadro
    imagebutton:
        xpos 1150
        ypos 200
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textquadro"), Jump("ruademanha")

        hovered Show("textquadro", 
            displayText = "Mercadinho")
        unhovered Hide("textquadro")
    imagebutton:
        xpos 320
        ypos 750
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textcaixa"), Jump("rodoanel")#imagem ruim

        hovered Show("textcaixa", 
            displayText = "Rodovia A")
        unhovered Hide("textcaixa")

screen rodoanel:
    add "rodovia"
    
    imagebutton:
        xpos 1750
        ypos 900
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textvoltar"), Jump("mercado")

        hovered Show("textvoltar", 
            displayText = "esquina")
        unhovered Hide("textvoltar")
    #Quadro
    imagebutton:
        xpos 1150
        ypos 200
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textquadro"), Jump("quadro")

        hovered Show("textquadro", 
            displayText = "Rodovia B")
        unhovered Hide("textquadro")

screen pontodeonibus:
    add "ponto"
    
    imagebutton:
        xpos 1750
        ypos 900
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textvoltar"), Jump("mercado")

        hovered Show("textvoltar", 
            displayText = "esquina")
        unhovered Hide("textvoltar")
    #Quadro
    imagebutton:
        xpos 1150
        ypos 200
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textquadro"), Jump("quadro")

        hovered Show("textquadro", 
            displayText = "Ponto de Ônibus")
        unhovered Hide("textquadro")

    imagebutton:
        xpos 320
        ypos 750
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textcaixa"), Jump("parquediadema")

        hovered Show("textcaixa", 
            displayText = "Passarela")
        unhovered Hide("textcaixa")

screen parquediadema:
    add "parque"
    
    imagebutton:
        xpos 1750
        ypos 900
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textvoltar"), Jump("pontodeonibus")

        hovered Show("textvoltar", 
            displayText = "Ponto de Ônibus")
        unhovered Hide("textvoltar")
    #Quadro
    imagebutton:
        xpos 1150
        ypos 200
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textquadro"), Jump("viela")

        hovered Show("textquadro", 
            displayText = "Beco")
        unhovered Hide("textquadro")
    imagebutton:
        xpos 320
        ypos 750
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textcaixa"), Jump("cafezis")

        hovered Show("textcaixa", 
            displayText = "café Memória")
        unhovered Hide("textcaixa")

screen viela:
    add "beco"
    #Quadro
    imagebutton:
        xpos 1150
        ypos 200
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textquadro"), Jump("portao")

        hovered Show("textquadro", 
            displayText = "Portão da Escola")
        unhovered Hide("textquadro")
    imagebutton:
        xpos 320
        ypos 750
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textcaixa"), Jump("parquediadema")

        hovered Show("textcaixa", 
            displayText = "Passarela")
        unhovered Hide("textcaixa")

screen portao:
    add "portaoescolafundo"
    
    imagebutton:
        xpos 1750
        ypos 900
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textvoltar"), Jump("viela")

        hovered Show("textvoltar", 
            displayText = "Beco")
        unhovered Hide("textvoltar")
    #Quadro
    imagebutton:
        xpos 1150
        ypos 200
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textquadro"), Jump("quadro")

        hovered Show("textquadro", 
            displayText = "Portão da Escola{p}(Fundos)")
        unhovered Hide("textquadro")

screen cafezis:
    add "cafezin"
    
    imagebutton:
        xpos 1750
        ypos 900
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textvoltar"), Jump("parquediadema")

        hovered Show("textvoltar", 
            displayText = "Passarela")
        unhovered Hide("textvoltar")
    #Quadro
    imagebutton:
        xpos 1150
        ypos 200
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textquadro"), Jump("starbucks")

        hovered Show("textquadro", 
            displayText = "Café Memória")
        unhovered Hide("textquadro")
    imagebutton:
        xpos 320
        ypos 750
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textcaixa"), Jump("portaofrente")

        hovered Show("textcaixa", 
            displayText = "Potão da Escola")
        unhovered Hide("textcaixa")

screen starbucks:
    add "starbuks"
    
    imagebutton:
        xpos 1750
        ypos 900
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textvoltar"), Jump("entradastarbucks")

        hovered Show("textvoltar", 
            displayText = "Fundos do Café")
        unhovered Hide("textvoltar")
    #Quadro
    imagebutton:
        xpos 1150
        ypos 200
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textquadro"), Jump("dentrodastarbucks")

        hovered Show("textquadro", 
            displayText = "Entrada do Café")
        unhovered Hide("textquadro")
    imagebutton:
        xpos 320
        ypos 750
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textcaixa"), Jump("cafezis")

        hovered Show("textcaixa", 
            displayText = "Café Memória (Frente)")
        unhovered Hide("textcaixa")

screen entradastarbucks:
    add "entradastar"
    
    imagebutton:
        xpos 1750
        ypos 900
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textvoltar"), Jump("starbucks")

        hovered Show("textvoltar", 
            displayText = "Frente do Café")
        unhovered Hide("textvoltar")
    #Quadro
    imagebutton:
        xpos 1150
        ypos 200
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textquadro"), Jump("dentrodastarbucks")

        hovered Show("textquadro", 
            displayText = "Entrada do Café(Fundos)")
        unhovered Hide("textquadro")

screen dentrodastarbucks:
    add "dentrostar"
    
    imagebutton:
        xpos 1750
        ypos 900
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textvoltar"), Jump("entradastarbucks")

        hovered Show("textvoltar", 
            displayText = "Saída (Fundos)")
        unhovered Hide("textvoltar")
    #Quadro
    imagebutton:
        xpos 1150
        ypos 200
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textquadro"), Jump("starbucks")

        hovered Show("textquadro", 
            displayText = "Saída (Frente)")
        unhovered Hide("textquadro")

screen portaofrente:
    add "portaoescolafrente"
    
    imagebutton:
        xpos 1750
        ypos 900
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textvoltar"), Jump("cafezis")

        hovered Show("textvoltar", 
            displayText = "Café Memória")
        unhovered Hide("textvoltar")
    #Quadro
    imagebutton:
        xpos 1150
        ypos 200
        idle "cenarioshover/folha_idle.png"
        hover "cenarioshover/folha_hover.png"
        action Hide("textquadro"), Jump("quadro")

        hovered Show("textquadro", 
            displayText = "Portão Principal")
        unhovered Hide("textquadro")