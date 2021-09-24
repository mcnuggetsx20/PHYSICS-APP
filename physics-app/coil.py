import pygame
import sys
import variables
import functions


def coil():
    pygame.quit()
    pygame.__init__
    screen = pygame.display.set_mode(variables.resolution_main)
    clock = pygame.time.Clock()

    coil_start_pos = (0,0)
    coil_end_pos = (0,0)
    coil_actual_start_pos = (0,0)
    coil_actual_end_pos = (0,0)
    actual_coil_draw = False
    mousebutton_clicked = False
    ended_coil = False
    selected_box = False
    vibrations = True
    time = 0

    list_of_coils = []
    #coil loop

    while True:
        shift_pressed = False
        #drawing background
        screen.blit(variables.image_coil_background,(0,0))

        



        #collecting events

        if pygame.key.get_pressed()[pygame.K_RSHIFT] == 1:
            shift_pressed = True
        if pygame.key.get_pressed()[pygame.K_LSHIFT] == 1:
            shift_pressed = True
        for event in pygame.event.get():


            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if vibrations == False:
                        vibrations = True
                    else:
                        vibrations = False


                if pygame.key.get_pressed()[pygame.K_LCTRL] == 1:
                    if event.key == pygame.K_z:
                        if len(list_of_coils) >= 1:
                            del list_of_coils[-1]

                if event.key == pygame.K_ESCAPE:
                    import menu
                    list_of_coils = []
                    menu.menu()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    shift_pressed = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = event.pos[0]
                y = event.pos[1]
                if x>variables.coil_rect_width+variables.coil_coil_link_radius:
                    coil_actual_start_pos = event.pos
                    coil_start_pos = event.pos
                    mousebutton_clicked = True
                else:
                    if x>variables.coil_square_coil_position[0] and y>variables.coil_square_coil_position[1] and x<variables.coil_square_coil_position[0]+variables.coil_square_coil_size[0] and y<variables.coil_square_coil_position[1]+variables.coil_square_coil_size[1]:
                        if selected_box == 'coil':
                            selected_box = False
                        else:
                            selected_box = 'coil'
                    if x>variables.coil_square_weight_position[0] and y>variables.coil_square_weight_position[1] and x<variables.coil_square_weight_position[0]+variables.coil_square_weight_size[0] and y<variables.coil_square_weight_position[1]+variables.coil_square_weight_size[1]:
                        if selected_box == 'weight':
                            selected_box = False
                        else:
                            selected_box = 'weight'
            if mousebutton_clicked == True:
                if event.type == pygame.MOUSEMOTION:
                    x = event.pos[0]
                    if x>variables.coil_rect_width+variables.coil_coil_link_radius:
                        coil_end_pos = event.pos
                        actual_coil_draw = True
                        coil_actual_end_pos = event.pos
            if event.type == pygame.MOUSEBUTTONUP:
                x = event.pos[0]
                if x>variables.coil_rect_width+variables.coil_coil_link_radius:
                    coil_end_pos = event.pos
                    ended_coil = True
            
        #checking if shift is pressed
        if shift_pressed == True:
            print("...")
            print(coil_start_pos)
            coil_end_pos = functions.draw_straight_line(coil_start_pos[0],coil_start_pos[1],coil_end_pos[0],coil_end_pos[1])
            coil_actual_end_pos = functions.draw_straight_line(coil_actual_start_pos[0],coil_actual_start_pos[1],coil_actual_end_pos[0],coil_actual_end_pos[1])
            print(coil_end_pos)
        #checking if coil has ended
        if ended_coil == True:
            coil_actual_start_pos = (0,0)
            coil_actual_end_pos = (0,0)
            list_of_coils.append([coil_start_pos, coil_end_pos, 0, 0])
            ended_coil = False
            mousebutton_clicked = False
            actual_coil_draw = False
        print(list_of_coils)    

        #drawing coils
        for coordinates in list_of_coils:
            #3 - czas sprezyny
            #2 - wychylenie
            coordinates[3] += 1/variables.coil_screen_fps
            coordinates[2] = functions.x_t(variables.amplitude, variables.elastic_idx, variables.mass, coordinates[3], variables.phase)

            coil_lenght = ((coordinates[0][1]-coordinates[1][1])**2+(coordinates[1][0]-coordinates[0][0])**2)**0.5
            coil_lenght = coil_lenght+coordinates[2]
            end_pos_after_move = functions.circle_line(coordinates[0],coordinates[1],coil_lenght)
            functions.draw_coil(screen,coordinates[0],end_pos_after_move,variables.coil_coil_line_width,variables.coil_coil_lenght_of_first_line, variables.coil_coil_number_of_links,variables.coil_coil_link_radius,variables.coil_coil_link_width, variables.color_coil_coil)
        if actual_coil_draw == True:
            functions.draw_coil(screen,coil_actual_start_pos,coil_actual_end_pos,variables.coil_coil_line_width,variables.coil_coil_lenght_of_first_line,variables.coil_coil_number_of_links,variables.coil_coil_link_radius,variables.coil_coil_link_width, variables.color_coil_coil)


        #drawing screen (first boxes behind small boxes on left side)
        pygame.draw.rect(screen,variables.color_coil_rect,(variables.coil_rect_start_position,variables.coil_rect_size))
        if selected_box == "coil":
            pygame.draw.rect(screen,variables.color_coil_bigsquare, (variables.coil_square_coil_position[0]-variables.coil_square_frame,variables.coil_square_coil_position[1]-variables.coil_square_frame,variables.coil_square_coil_size[0]+2*variables.coil_square_frame,variables.coil_square_coil_size[1]+2*variables.coil_square_frame))
        if selected_box == "weight":
            pygame.draw.rect(screen,variables.color_coil_bigsquare, (variables.coil_square_weight_position[0]-variables.coil_square_frame,variables.coil_square_weight_position[1]-variables.coil_square_frame,variables.coil_square_weight_size[0]+2*variables.coil_square_frame,variables.coil_square_weight_size[1]+2*variables.coil_square_frame))
        pygame.draw.rect(screen,variables.color_coil_square,(variables.coil_square_weight_position,variables.coil_square_weight_size))
        pygame.draw.rect(screen,variables.color_coil_square,(variables.coil_square_coil_position,variables.coil_square_coil_size))
        screen.blit(variables.image_coil_weight,(variables.coil_square_weight_position))
        screen.blit(variables.image_coil_coil,(variables.coil_square_coil_position))




        clock.tick(variables.coil_screen_fps)
        time += 1 / variables.coil_screen_fps
        pygame.display.update()







