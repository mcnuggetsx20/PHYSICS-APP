from math import pi
from types import coroutine
import pygame
import sys
from variables import *
import functions
import datetime

coil_start_pos = (0,0)
coil_end_pos = (0,0)
coil_actual_start_pos = (0,0)
coil_actual_end_pos = (0,0)
actual_coil_draw = False
mousebutton_clicked = False
ended_coil = False
selected_box = False
vibrations = False
sinus_box = False
to_delete = []
list_of_added_items = []
time = 0
colored_coil = 0
list_of_coils = []
list_of_weights = []
list_of_weights_params = []
elements_dict = dict()
del_idx = 0
pixels_to_draw = []

def dict_init():
    global list_of_weights  
    global list_of_coils
    global elements_dict
    elements_dict = dict()
    ok = False

    for i in range(len(list_of_weights)):
        elements_dict.update({i : []})

    for i in range(len(list_of_coils)):
        ok = False
        if list_of_coils[i][0] in list_of_weights and list_of_coils[i][1] in list_of_weights:
            for j in range(2):
                idx = list_of_weights.index(list_of_coils[i][j])
                elements_dict[idx].append([i, j])


        else:
            if list_of_coils[i][0] in list_of_weights:
                temp = list_of_coils[i][0]
                temp2 = 0
            else:
                temp = list_of_coils[i][1]
                temp2 = 1
            ok = True

        if ok:
            if temp in list_of_weights:
                print('elo')
                idx = list_of_weights.index(temp)
                elements_dict[idx].append([i,temp2])

def coil():
    pygame.quit()
    pygame.__init__
    screen = pygame.display.set_mode(resolution_main)
    clock = pygame.time.Clock()

    global precision
    global sinus_box
    global coil_start_pos
    global coil_end_pos
    global coil_actual_start_pos
    global coil_actual_end_pos
    global actual_coil_draw
    global mousebutton_clicked
    global ended_coil
    global selected_box
    global vibrations
    global to_delete
    global list_of_added_items
    global time
    global colored_coil
    global list_of_coils
    global list_of_weights
    global list_of_weights_params
    global elements_dict
    global del_idx
    #coil loop

    while True:
        now = datetime.datetime.now()
        shift_pressed = False
        #drawing background
        screen.blit(image_coil_background,(0,0))





        #collecting events

        if pygame.key.get_pressed()[pygame.K_RSHIFT] == 1:
            shift_pressed = True
        if pygame.key.get_pressed()[pygame.K_LSHIFT] == 1:
            shift_pressed = True
        for event in pygame.event.get():


            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == 1073741903: #right arrow
                    colored_coil += -1 * (len(list_of_coils)) * int(colored_coil == len(list_of_coils)-1) + 1
                elif event.key == 1073741904: #right arrow
                    colored_coil += len(list_of_coils) * int(not colored_coil) -1
                #print(event.key)
                if event.key == pygame.K_SPACE:
                    
                    if vibrations == False:
                        vibrations = True
                    else:
                        vibrations = False

                '''if event.key == pygame.K_BACKSPACE:
                    list_of_coils.pop(colored_coil)
                    for i in elements_dict:
                        if len(elements_dict[i]) == 1 and elements_dict[i][0] == colored_coil:
                            print('ayo')
                            list_of_weights.pop(i)
                            list_of_weights_params.pop(i)
                    dict_init()
                    colored_coil = max(colored_coil-1, 0)'''

                if pygame.key.get_pressed()[pygame.K_LCTRL] == 1:
                    if event.key == pygame.K_z:
                        if len(list_of_added_items)>0:
                            to_delete = list_of_added_items[-1]
                            if to_delete[0] == 'c':
                                del list_of_coils[-1]
                                del list_of_added_items[-1]
                                dict_init()
                            if to_delete[0] == 'w':
                                del list_of_weights[-1]
                                del list_of_weights_params[-1]
                                del list_of_added_items[-1]
                                del pixels_to_draw[-1]
                                dict_init()
                if event.key == pygame.K_ESCAPE:
                    import menu
                    menu.menu()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    shift_pressed = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = event.pos[0]
                y = event.pos[1]
                if x>coil_rect_width+coil_coil_link_radius:
                    if selected_box == 'coil':
                        coil_actual_start_pos = event.pos
                        coil_start_pos = event.pos
                        x = coil_start_pos[0]
                        y = coil_start_pos[1]
                        biggest_dist = coil_weight_radius
                        closest_weight_idx = (coil_weight_radius,-1)
                        for i in range (0, len(list_of_weights)):
                            x_weight = list_of_weights[i][0]
                            y_weight = list_of_weights[i][1]
                            dist = ((x-x_weight)**2 + (y-y_weight)**2)**0.5
                            if dist <= biggest_dist and dist<=closest_weight_idx[0]:
                                closest_weight_idx = (dist,i)
                        if closest_weight_idx[1] != -1:
                            coil_start_pos = list_of_weights[closest_weight_idx[1]]
                        coil_actual_start_pos = coil_start_pos
                        mousebutton_clicked = True
                    if selected_box == 'weight':
                        x = event.pos[0]
                        y = event.pos[1]
                        biggest_dist = coil_weight_radius
                        closest_coil_idx = (coil_weight_radius,-1,0)
                        for i in range (0, len(list_of_coils)):
                            coil_coordinate_x = list_of_coils[i][0][0]
                            coil_coordinate_y = list_of_coils[i][0][1]
                            dist = ((x-coil_coordinate_x)**2 + (y-coil_coordinate_y)**2)**0.5
                            if dist <= biggest_dist and dist <= closest_coil_idx[0]:
                                closest_coil_idx = (dist,i,0)
                            coil_coordinate_x = list_of_coils[i][1][0]
                            coil_coordinate_y = list_of_coils[i][1][1]
                            dist = ((x-coil_coordinate_x)**2 + (y-coil_coordinate_y)**2)**0.5
                            if dist <= biggest_dist and dist <= closest_coil_idx[0]:
                                closest_coil_idx = (dist,i,1)
                        if closest_coil_idx[1] != -1:
                            x = list_of_coils[closest_coil_idx[1]][closest_coil_idx[2]][0]
                            y = list_of_coils[closest_coil_idx[1]][closest_coil_idx[2]][1]

                        list_of_weights.append((x,y))
                        list_of_weights_params.append([(x,y), mass, [0, 0]])
                        pixels_to_draw.append([])
                        list_of_added_items.append('w')
                        dict_init()
                else:
                    if x>coil_square_coil_position[0] and y>coil_square_coil_position[1] and x<coil_square_coil_position[0]+coil_square_coil_size[0] and y<coil_square_coil_position[1]+coil_square_coil_size[1]:
                        if selected_box == 'coil':
                            selected_box = False
                        else:
                            selected_box = 'coil'
                    if x>coil_square_weight_position[0] and y>coil_square_weight_position[1] and x<coil_square_weight_position[0]+coil_square_weight_size[0] and y<coil_square_weight_position[1]+coil_square_weight_size[1]:
                        if selected_box == 'weight':
                            selected_box = False
                        else:
                            selected_box = 'weight'
                    if x>coil_square_sinus_position[0] and y>coil_square_sinus_position[1] and x<coil_square_sinus_position[0]+coil_square_sinus_size[0] and y<coil_square_sinus_position[1]+coil_square_sinus_size[1]:
                        if sinus_box:
                            sinus_box = False
                        else:
                            sinus_box = True
            if mousebutton_clicked == True:
                if event.type == pygame.MOUSEMOTION:
                    x = event.pos[0]
                    if x>coil_rect_width+coil_coil_link_radius:
                        actual_coil_draw = True
                        coil_actual_end_pos = event.pos
            if event.type == pygame.MOUSEBUTTONUP:
                x = event.pos[0]
                if x>coil_rect_width+coil_coil_link_radius:
                    if selected_box == 'coil':
                        coil_end_pos = event.pos
                        x = coil_end_pos[0]
                        y = coil_end_pos[1]
                        biggest_dist = coil_weight_radius
                        closest_weight_idx = (coil_weight_radius,-1)
                        for i in range (0, len(list_of_weights)):
                            x_weight = list_of_weights[i][0]
                            y_weight = list_of_weights[i][1]
                            dist = ((x-x_weight)**2 + (y-y_weight)**2)**0.5
                            if dist <= biggest_dist and dist<=closest_weight_idx[0]:
                                closest_weight_idx = (dist,i)
                        if closest_weight_idx[1] != -1:
                            coil_end_pos = list_of_weights[closest_weight_idx[1]]
                        ended_coil = True
                        list_of_added_items.append('c')
            
        #checking if shift is pressed
        if shift_pressed == True:
            coil_end_pos = functions.draw_straight_line(coil_start_pos[0],coil_start_pos[1],coil_actual_end_pos[0],coil_actual_end_pos[1])
            coil_actual_end_pos = functions.draw_straight_line(coil_start_pos[0],coil_start_pos[1],coil_actual_end_pos[0],coil_actual_end_pos[1])
        #checking if coil has ended
        if ended_coil == True:
            coil_actual_start_pos = (0,0)
            coil_actual_end_pos = (0,0)
            length = ((coil_end_pos[0]-coil_start_pos[0])**2 + (coil_end_pos[1]-coil_start_pos[1])**2)**0.5
            list_of_coils.append([coil_start_pos, coil_end_pos, length, elastic_idx])
            ended_coil = False
            mousebutton_clicked = False
            actual_coil_draw = False
            dict_init()
        if vibrations:
            for i in range (0,precision):
                list_of_coils, list_of_weights_params = functions.moving_blocks(list_of_coils, list_of_weights_params, elements_dict, speed_multiplier, coil_screen_fps*precision, gravitation)

        list_of_weights = []
        for i in list_of_weights_params:
            list_of_weights.append(i[0])

        #drawing line 

        if vibrations:
            
            for i in range (len(list_of_weights)):
                pixels_to_draw[i].append([list_of_weights[i][0],list_of_weights[i][1]])
            for i in range (len(pixels_to_draw)):
                for j in range (len(pixels_to_draw[i])):
                        pixels_to_draw[i][j][0] += 1

        if sinus_box:
            for i in range (len(pixels_to_draw)):
                for j in range (len(pixels_to_draw[i])-1):
                    pygame.draw.line(screen,(0,0,0),pixels_to_draw[i][j],pixels_to_draw[i][j+1],4)
        else:
            for i in range (len(pixels_to_draw)):
                pixels_to_draw[i] = []


        #drawing coils
        for coil_idx in list_of_coils:
            functions.draw_coil(screen,coil_idx[0], coil_idx[1], coil_coil_line_width,coil_coil_lenght_of_first_line, coil_coil_number_of_links,coil_coil_link_radius,coil_coil_link_width, color_coil_coil)
        if actual_coil_draw == True:
            functions.draw_coil(screen,coil_actual_start_pos,coil_actual_end_pos,coil_coil_line_width,coil_coil_lenght_of_first_line,coil_coil_number_of_links,coil_coil_link_radius,coil_coil_link_width, color_coil_coil)

        #print(coil_actual_end_pos)

        #drawing screen (first boxes behind small boxes on left side)
        for weight in list_of_weights_params:
            pygame.draw.circle(screen,color_coil_weight,(weight[0][0],weight[0][1]),coil_weight_radius)
        pygame.draw.rect(screen,color_coil_rect,(coil_rect_start_position,coil_rect_size))
        if selected_box == "coil":
            pygame.draw.rect(screen,color_coil_bigsquare, (coil_square_coil_position[0]-coil_square_frame,coil_square_coil_position[1]-coil_square_frame,coil_square_coil_size[0]+2*coil_square_frame,coil_square_coil_size[1]+2*coil_square_frame))
        if selected_box == "weight":
            pygame.draw.rect(screen,color_coil_bigsquare, (coil_square_weight_position[0]-coil_square_frame,coil_square_weight_position[1]-coil_square_frame,coil_square_weight_size[0]+2*coil_square_frame,coil_square_weight_size[1]+2*coil_square_frame))
        if sinus_box:
            pygame.draw.rect(screen,color_coil_bigsquare, (coil_square_sinus_position[0]-coil_square_frame,coil_square_sinus_position[1]-coil_square_frame,coil_square_sinus_size[0]+2*coil_square_frame,coil_square_sinus_size[1]+2*coil_square_frame))
        pygame.draw.rect(screen,color_coil_square,(coil_square_weight_position,coil_square_weight_size))
        pygame.draw.rect(screen,color_coil_square,(coil_square_coil_position,coil_square_coil_size))
        pygame.draw.rect(screen,color_coil_square,(coil_square_sinus_position,coil_square_sinus_size))
        screen.blit(image_coil_weight,(coil_square_weight_position))
        screen.blit(image_coil_coil,(coil_square_coil_position))
        screen.blit(image_coil_sinus,(coil_square_sinus_position))




        
        time += 1 / coil_screen_fps
        '''for i in elements_dict:
            print(i, elements_dict[i])'''
        pygame.display.update()
        after = datetime.datetime.now()
        a = (now.microsecond)
        b = (after.microsecond)
        clock.tick(coil_screen_fps)
        print (b-a)
#coil()
