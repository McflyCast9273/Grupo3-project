import pygame, pygame_menu, os, subprocess

pygame.init()
surface = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Menu de inicio')

# FUNCIONES

def start():
    os.chdir("inserte ruta/") #Ruta de los archivos del juego (imagenes, musica, etc)
    subprocess.call(['python', 'inserte ruta/']) #Ruta del proyecto a ejecutar

 
def change_resolution(value, resolution):
    global surface
    surface = pygame.display.set_mode(resolution)
 
resolutions = [('800x600', (800, 600)), ('1024x768', (1024, 768)), ('1280x720', (1280, 720))]


def music():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
    else:
        pygame.mixer.music.load("fallen.mp3")
        pygame.mixer.music.play(-1)
    
def credits():
    menu.disable()
    credits_menu = pygame_menu.Menu(600, 800, 'INTEGRANTES DEL GRUPO 3', theme=menu_theme)
    credits_menu.add_label('Jesús Daniel Flores                       ')
    credits_menu.add_label('Josue Berrocal Romani                     ')
    credits_menu.add_label('Luis Lenon de la Cruz                     ')
    credits_menu.add_label('Jimena Carrillo Azaña                     ')
    credits_menu.add_label('Faridh Castillo Jaramillo                 ')
    credits_menu.add_label('Jarol Carrascal Mejia                     ')
    credits_menu.add_label('')
    credits_menu.add_button('Volver', pygame_menu.events.EXIT)
    credits_menu.mainloop(surface)
    menu.enable()

 # ERROR al ingresar a creditos, no se puede volver a la ventana anterior   
   
    
# DISEÑO DEL MENU (TEMA, FUENTES, IMAGENES)

menu_theme = pygame_menu.themes.THEME_DARK.copy()
menu_theme.title_font = "determinationmonowebregular"
menu_theme.widget_font = "determinationmonowebregular"

menu = pygame_menu.Menu(600, 800, 'BIENVENIDO',
                       theme=menu_theme)

menu.add_selector('Resolución: ', resolutions, onchange=change_resolution)
menu.add_image("pytale.png", angle=0, scale=(1, 1))
menu.add_button('Empezar', start)
menu.add_button('Salir', pygame_menu.events.EXIT)
menu.add_image("grupo3.png", angle=0, scale=(0.5, 0.5))
menu.add_image("escudo.png", angle=0, scale=(0.5, 0.5))
menu.add_button('Musica', music)
menu.add_button('Créditos', credits)

# Reproducir sonido de fondo
pygame.mixer.music.load("fallen.mp3")
pygame.mixer.music.play(-1)
    
    
    #BUCLE PRINCIPAL DEL PROGRAMA
while True:
   
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()  
            exit()
            
    menu.update(events)
    menu.draw(surface)
    pygame.display.update()