import pygame
from gui_buttom import Button

pygame.init()

#create game window
FPS = 60
ANCHO_PANTALLA = 1280
ALTO_PANTALLA = 720
screen = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Main Menu")

#game variables
game_pause = False

#define fonts
font = pygame.font.SysFont("Gabriola", 40)
#text colours
text_col = (255,255,255)

def draw_text(text, form, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))

#TODO Load buttons images
resume_button_img = pygame.image.load("./buttoms/resume/Resume1.png").convert_alpha()
star_button_img = pygame.image.load("./buttoms/start/Start1.png").convert_alpha()
options_button_img = pygame.image.load("./buttoms/settings/Settings1.png").convert_alpha()
levels_button_img = pygame.image.load("./buttoms/levels/Levels1.png").convert_alpha()
quits_button_img = pygame.image.load("./buttoms/quit/Quit1.png").convert_alpha()
main_menu_button_img = pygame.image.load('./buttoms/main_menu/Main Menu1.png').convert_alpha()
audio_button_img = pygame.image.load('./buttoms/volume/Volume1.png').convert_alpha()
keys_button_img = pygame.image.load('./buttoms/customize/Customize1.png').convert_alpha()
back_button_img = pygame.image.load('./buttoms/left_key/LeftKey1.png').convert_alpha()

# level_one_button_img = pygame.image.load('./buttoms/numbers/0.png').convert_alpha()
# level_two_button_img = pygame.image.load('./buttoms/numbers/1.png').convert_alpha()
# level_three_button_img = pygame.image.load('./buttoms/numbers/2.png').convert_alpha()


#buttoms instances
resume_button = Button(480, 275, resume_button_img, 4)
star_button = Button(480, 275, star_button_img, 4)
levels_button = Button(480, 275, levels_button_img, 4)
options_button = Button(480, 350, options_button_img, 4)
quits_button = Button(480, 425, quits_button_img, 4)

main_menu_button = Button(480, 275, main_menu_button_img, 4)
audio_button = Button(480, 350, audio_button_img, 4)
keys_button = Button(480, 425, keys_button_img, 4)
back_button = Button(5, 660, back_button_img, 4)

# level_one = Button(470, 350, level_one_button_img, 4)
# level_two = Button(480, 350, level_two_button_img, 4)
# level_three = Button(460, 350, level_three_button_img, 4)


menu_state = "main"
game_level = 0
#game loop
run = True
screen.fill((11, 44, 38))
while run:

    if menu_state == "main":
        draw_text("Main Menu", font, text_col, 535, 180)
        # if levels_button.draw(screen):
            # if level_one.draw(screen):
                # game_level = 1
                # # screen.fill(0,0,0)
                # draw_text("LEVEL 1", font, text_col, 475, 320)

                # if game_pause:
        if options_button.draw(screen):
            menu_state = "options"
        if quits_button.draw(screen):
            run = False
    
    if menu_state == "options":
        draw_text("Settings", font, text_col, 545, 180)
        if audio_button.draw(screen):
            pass
        if keys_button.draw(screen):
            menu_state = "keys"
        if main_menu_button.draw(screen):
            menu_state = "main"
    
    if menu_state == "keys":
        keys_img = pygame.image.load("./buttoms/keys_paint.png").convert_alpha()
        screen.blit(keys_img,(0, 75))
        draw_text("Keys", font, text_col, 130, 70)
        draw_text("_________", font, text_col, 130, 70)
        if back_button.draw(screen):
            menu_state = "options"



    print(menu_state)
    # else:
    #     draw_text("Press Esc to continue", font, text_col, 475, 320)

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_pause = True
                
    
    pygame.display.update()
pygame.quit()
