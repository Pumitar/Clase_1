#pgzero
from turtle import Screen
import pgzrun 
import random
import time

WIDTH = 288 # Ancho de la ventana
HEIGHT = 512 # Altura de la ventana

TITLE = "FLAPPY BIRD" # Título para la ventana de juego
FPS = 30 # Número de fotogramas por segundo
salto_fps = 0 

bird_images = {"mid":"bird-midflap", "down":"bird-downflap", "up":"bird-upflap"} 
tubo_images = {"down": "pipe-green", "up": "pipe-green-reverse"}
count = 0
speed = 5

#Actores
fondo = Actor("background-day")
suelo = Actor("base", (144,490))
bird = Actor(bird_images.get("mid"), (40,256))
game_overs = Actor("gameover", (144,260))
title = Actor ("title",(144,200))
star = Actor("star", (144,280))
reset = Actor("reset", (144,320))
tubo_1 = None
tubo_2 = None

game_over = 0
game_star = 0
mode_obstacle =  ["up","down"]
def create_obstacle():
    mode = random.randint(0,1)
    if mode == 0:
        y = random.randint(0,160)
    else:
        y = random.randint(360,512)
    
    image = tubo_images.get(mode_obstacle[mode]) # "pipe-green-reverse" |  "pipe-green"
    new_tubo = Actor(image, (315, y))
    return new_tubo


def draw():
    global count
    #Actores
    fondo.draw()
    suelo.draw()
    screen.draw.text(str(count), pos=(10, 10), color="white", fontsize = 24)
    
    # bird_mid.draw()
    bird.draw()
    #Otros
    
    if tubo_1 != None:
        tubo_1.draw()
    if tubo_2 != None:
        tubo_2.draw()
    
    if game_over == 1:
        game_overs.draw()
        
        reset.draw()

    if game_star == 0:
        title.draw()
        star.draw()
        bird.pos = (144,330)  
        
    
 # Controles
def update():
    global game_over
    global salto_fps
    global FPS
    global count, speed, game_star
    
    if game_star == 1 and game_over == 0:
        colisiones()
        if  keyboard.space and salto_fps < FPS:
            salto_fps = salto_fps + 3
            clock.schedule_unique(play_sound_wing, 0.2)
            bird.image = bird_images.get("up")
            bird.y= bird.y - 8
            clock.schedule_unique(set_bird_mid, 0.3)
            animate(bird,tween="accelerate",duration = 1 ,y = 425) 
        
        else:
            salto_fps = salto_fps - 1
        
        global tubo_1
        global tubo_2
        global count
    #tubo_1    
        if tubo_1 == None:    
            tubo_1 = create_obstacle()
        elif tubo_1.x < -15:
            tubo_1 = None
        else:
            tubo_1.x = tubo_1.x - 2
        
    #tubo_2
        if tubo_2 == None:
            if tubo_1.x < 144:    
                tubo_2 = create_obstacle()
                
        elif tubo_2.x < -15:
            tubo_2 = None
        else:
            tubo_2.x = tubo_2.x - 2

    #tubos
        if tubo_1 != None and tubo_1.x == bird.x-1:
            count = count + 1
            clock.schedule_unique(play_sound_point, 0.2)
            speed = speed + 1
            
        if tubo_2 != None and tubo_2.x == bird.x-1:
            count = count + 1
            clock.schedule_unique(play_sound_point, 0.2)
            speed = speed + 1
    

def on_mouse_down(button,pos):
    global reset
    global game_over
    global tubo_1, tubo_2, count, game_star
    print(button, pos)
    if reset != None and button == reset.collidepoint(pos):
        game_over = 0 
        count = 0
        bird.pos = (40,256)  
        tubo_1 = None
        tubo_2 = None
        #reset = None
        
    if game_star == 0 and button == star.collidepoint(pos):
        game_star = 1
        
def set_bird_mid():
    bird.image = bird_images.get("mid")
    
def play_sound_wing():
    sounds.wing.play()
    
def play_sound_die():
    sounds.die.play()
    
def play_sound_point():
    sounds.point.play()
    
def colisiones():
    global game_over

    if tubo_1 != None:
        if bird.colliderect(tubo_1):
            game_over = 1
            
            clock.schedule_unique(play_sound_die, 0.01)
                       
    if tubo_2 != None:
        if bird.colliderect(tubo_2):
            game_over = 1
            clock.schedule_unique(play_sound_die, 0.01)
             
    if bird.colliderect(suelo):
        game_over = 1
        clock.schedule_unique(play_sound_die, 0.01)
            
 
 
