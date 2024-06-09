from vpython import *
#Web VPython 3.2


scene = canvas(width=640, height=480, center=vector(8,5,0),range=8, background=color.blue)
#cena
ground = box(pos=vector(8,-5,0), length=100, height=10, width=0.5, color=color.green)
#chão
dist = 5 + random()*10 
target = box(pos=vector(dist,1,0), length=0.5, height=2, width=0.5, color=color.red)
height = 1
platform = box(pos=vector(-2,height-0.25,0), length=4, height=0.5, width=0.5, color=color.white)
bird = sphere(pos=vector(0,height+0.3,0), radius=0.3, color=color.yellow)


hit = 0
while hit == 0: 

    #parâmetros iniciais
    v0 = float(input('Diga a velocidade:'))
    dtheta = float(input('Diga o angulo:'))
    theta = radians(dtheta) #converte graus em radianus
    
    
    
    

    #Desenha a seta
    px = 0.1*v0*cos(theta) #calcula a posição inicial de x
    py = 0.1*v0*sin(theta) #calcula a posição inicial de y
    momentum = arrow(pos=bird.pos, axis=vector(px,py,0), shaftwidth=0.1, color=color.orange) #draw arrow representing projectiles initial momentum

 

 
    g1 = input('Diga um nome de um planeta do sistema solar') 
    if g1 == 'terra':
        g = 9.81
    elif g1 == 'marte':
        g = 3.72
    elif g1 == 'jupiter':
        g = 24.79
    elif g1 == 'mercurio':
        g = 3.7
    elif g1 =='saturno':
        g = 10.44
    elif g1 == 'venus':
        g = 8.87
    elif g1 == 'neptuno':
        g = 11.13
    elif g1 == 'uranus':
        g = 8.87
    else : g = 69.69
    
    
    
    #Define parâmetros iniciais
    x = x0 = 0
    y = y0 = height 
    dt = 0.0001 #timestep
    t = 0





    #condições que deixam a animação correr se não bater no alvo
    while (y > 0 and (x < dist-0.25 or x > dist+0.25)) or (y > 2 and x >= dist-0.25 and x<= dist+0.25):

            rate(5000) #fram-rate

            x = x0 + v0*t*cos(theta) # calcula nova posição x
            y = y0 + v0*t*sin(theta)-0.5*g*t**2 # calcula nova posição y
            bird.pos = vector(x,y,0) # redesenha a posição da bola no programa

            px = 0.1*v0*cos(theta) # calcula a posição em x da seta
            py = 0.1*v0*sin(theta)-0.1*g*t #calculate a posição em y da seta 
            momentum.pos = bird.pos #redesenha a seta
            momentum.axis = vector(px,py,0) #redesenha com as posições

            t += dt # incrementa o tempo

    momentum.visible = False #Se falhar o alvo, tira a seta

    #é definida uma condição inversa que define se o alvo voi acertado ou não
    if y >= 0 and y <= 2 and x >= dist-0.25 and x <= dist+0.25:

        #calcula se o alvo cai ou não
        trest = 0.5*100*g*0.5 #calcula o torque do alvo para a bola
        contact_t = 0.01 #define quanto tempo a bola está em contacto com o alvo
        fapp = vector(px, py, 0) / contact_t #calcula a força aplicada ao alvo
        tapp = cross(fapp, vector((dist+0.25)-x, -y, 0)) #calcula torque exercida pela bola ao alvo
        tappm = mag(tapp) #calcula a magnitude da força aplicada

        if tappm > trest: #alvo caiu
        
            target.pos = vector(dist+1.25,0.25,0)
            target.length = 2
            target.height =0.5
            print('Acertou, sheshh!')
            hit = 1

        else: #acertou mas não caiu
            print('Acertou mas não caiu, lol.')

        #anima a bola a cair
        t=0 #reset do tempo
        y0=y #set do y0 para zero
        while y > 0.3:
            rate(5000)
            y = y0 - 0.5*g*t**2            
            bird.pos = vector(x,y,0)
            t += dt

    else:
        print('Falhou, tente de novo.')
