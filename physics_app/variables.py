import pygame

#set up menu screen
width_menu = 600
height_menu = 600
resolution_menu = (width_menu, height_menu)

#colors
color_menu_background = (153, 204, 255)
color_rect = (126, 252, 206)
color_highlighted_rect = (0, 255, 162)
color_menu_other_words = (13, 161, 158)
color_menu_menu = (255, 102, 0)
color_coil_background = (255,255,255)
color_coil_rect = (247,188,91)
color_coil_coil = (128,128,128)
color_coil_coil_red = (200, 104, 104)
color_coil_square = (255,225,100)
color_coil_bigsquare = (245, 144, 66)
color_coil_weight = (69, 71, 71)

#coil variables
coil_screen_fps = 60
coil_coil_line_width = 4
coil_coil_lenght_of_first_line = 10
coil_rect_start_position = (0,0)
coil_rect_width = 100
coil_rect_height = 700
coil_rect_size = (coil_rect_width,coil_rect_height)
coil_coil_number_of_links = 30
coil_coil_link_radius = 15
coil_coil_link_width = 2
coil_square_weight_size = (80,80)
coil_square_weight_position = (10,110)
coil_square_coil_position = (10,10)
coil_square_coil_size = (80,80)
coil_square_sinus_position = (10,210)
coil_square_sinus_size = (80,80)
coil_square_frame = 8
coil_weight_radius = 18
coil_start_pos = (0,0)
coil_end_pos = (0,0)
coil_actual_start_pos = (0,0)
coil_actual_end_pos = (0,0)


#word "menu"
pygame.font.init()
font_menu_menu = pygame.font.SysFont("comicsansms",100)
text_menu_menu = font_menu_menu.render("MENU",True, color_menu_menu)
menu_menu_word_position = (160,0)

#other menu words
font_menu_menu = pygame.font.SysFont("comicsansms",40)
text_menu_coil = font_menu_menu.render("SPRĘŻYNA",True, color_menu_other_words)
menu_coil_word_position = (210,150)
menu_coil_rect_position = (200,150)
menu_coil_rect_size = (230,60)
difference_between_rects = 5
menu_coil_highlighted_rect_position = (menu_coil_rect_position[0]-difference_between_rects,menu_coil_rect_position[1]-difference_between_rects)
menu_coil_highlighted_rect_size = (menu_coil_rect_size[0]+2*difference_between_rects,menu_coil_rect_size[1]+2*difference_between_rects)


#set up main variables
width_main = 1000
height_main = 700
resolution_main = (width_main,height_main)

#images
image_coil_background = pygame.image.load('image_coil_background.png')
image_menu_background = pygame.image.load('menu_background.jpg')
image_coil_weight = pygame.image.load('weight.png')
image_coil_weight = pygame.transform.scale(image_coil_weight,coil_square_weight_size)
image_coil_coil = pygame.image.load('coil.png')
image_coil_coil = pygame.transform.scale(image_coil_coil,coil_square_coil_size)
image_coil_sinus = pygame.image.load('sinus.png')
image_coil_sinus = pygame.transform.scale(image_coil_sinus,coil_square_sinus_size)

#yooo
elastic_idx = 15
mass = 50
phase = 0
speed_multiplier = 50
gravitation = 10
