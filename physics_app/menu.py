import variables
import coil
import pygame
import sys
def menu():
    if pygame.get_init != True:
        pygame.quit()
    pygame.__init__
    screen = pygame.display.set_mode(variables.resolution_menu)
    where_mouse = ''
    clock = pygame.time.Clock()
    #main menu loop
    while True:

        #drawing
        screen.blit(variables.image_menu_background,(0,0))
        if where_mouse == 'coil':
            pygame.draw.rect(screen,variables.color_highlighted_rect,(variables.menu_coil_highlighted_rect_position, variables.menu_coil_highlighted_rect_size))
        pygame.draw.rect(screen,variables.color_rect,(variables.menu_coil_rect_position, variables.menu_coil_rect_size))

        screen.blit(variables.text_menu_menu,variables.menu_menu_word_position)
        screen.blit(variables.text_menu_coil,variables.menu_coil_word_position)
    
        #collecting events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit(0)
            if event.type == pygame.MOUSEMOTION:
                if event.pos[0] >= variables.menu_coil_rect_position[0] and event.pos[0] <= variables.menu_coil_rect_position[0]+variables.menu_coil_rect_size[0] and event.pos[1] >= variables.menu_coil_rect_position[1] and event.pos[1] <= variables.menu_coil_rect_position[1]+variables.menu_coil_rect_size[1]:
                    where_mouse = 'coil'
                else:
                    where_mouse = ''
            if event.type == pygame.MOUSEBUTTONUP:
                if event.pos[0] >= variables.menu_coil_rect_position[0] and event.pos[1] <= variables.menu_coil_rect_position[1]+variables.menu_coil_rect_size[1] and event.pos[1] >= variables.menu_coil_rect_position[1] and event.pos[1] <= variables.menu_coil_rect_position[1]+variables.menu_coil_rect_size[1]:
                    coil.coil()
        clock.tick(variables.coil_screen_fps)
        pygame.display.update()
        

menu()
