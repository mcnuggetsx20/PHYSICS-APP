import math
import pygame

def circle_line(start_pos,end_pos, lenght_of_first_line):
    x1 = start_pos[0]
    y1 = start_pos[1]
    x2 = end_pos[0]
    y2 = end_pos[1]
    if x2-x1 == 0:
        x2_solved1 = x1
        y2_solved1 = y1-lenght_of_first_line
        x2_solved2 = x1
        y2_solved2 = y1+lenght_of_first_line
    else:
        a_parameter = (y2-y1)/(x2-x1)
        b_parameter = y1-a_parameter*x1
        r = lenght_of_first_line
        delta = (2*a_parameter*b_parameter-2*x1-2*y1*a_parameter)**2-4*(1+a_parameter**2)*(x1**2+b_parameter**2+y1**2-2*y1*b_parameter-r**2)
        delta_sqrt = math.sqrt(delta)
        x2_solved1 = (-(2*a_parameter*b_parameter-2*x1-2*y1*a_parameter)+delta_sqrt)/(2*(1+a_parameter**2))
        x2_solved2 = (-(2*a_parameter*b_parameter-2*x1-2*y1*a_parameter)-delta_sqrt)/(2*(1+a_parameter**2))
        y2_solved1 = a_parameter*x2_solved1 + b_parameter
        y2_solved2 = a_parameter*x2_solved2 + b_parameter
    if (x2-x2_solved1)**2 + (y2-y2_solved1)**2 > (x2-x2_solved2)**2 + (y2-y2_solved2)**2:
        x2_solved = x2_solved2
        y2_solved = y2_solved2
    else:
        x2_solved = x2_solved1
        y2_solved = y2_solved1
    return (x2_solved,y2_solved)

def draw_coil (screen,start_pos,end_pos, line_width, lenght_of_first_line, number_of_links,link_radius,link_width,coil_color):
    (x1,y1) = start_pos
    (x2,y2) = end_pos
    full_line_lenght = math.sqrt((y2-y1)**2+(x2-x1)**2)-2*lenght_of_first_line-2*link_radius

    space_between_link = full_line_lenght/(number_of_links-1)

    if space_between_link >0:
        for space_id in range (0,number_of_links):
            circle = circle_line(start_pos,end_pos,lenght_of_first_line+link_radius+space_between_link*space_id)
            pygame.draw.circle(screen,coil_color,circle,link_radius,link_width)
        x2_solved,y2_solved = circle_line(start_pos,end_pos,lenght_of_first_line)
        x3_solved,y3_solved = circle_line(end_pos,start_pos,lenght_of_first_line)
        pygame.draw.line(screen,coil_color,(x3_solved,y3_solved),end_pos,line_width)
        pygame.draw.line(screen,coil_color,start_pos,(x2_solved,y2_solved),line_width)
    else:
        circle = circle_line(start_pos,end_pos,lenght_of_first_line+link_radius)
        pygame.draw.circle(screen,coil_color, circle,link_radius,link_width)
        line_pos1 = circle_line(start_pos,end_pos,lenght_of_first_line)
        line_pos2 = circle_line(start_pos,end_pos,lenght_of_first_line+2*link_radius)
        line_pos3 = circle_line(start_pos,end_pos,2*lenght_of_first_line+2*link_radius)
        pygame.draw.line(screen,coil_color,start_pos,line_pos1,line_width)
        pygame.draw.line(screen,coil_color,line_pos2,line_pos3,line_width)

def draw_straight_line(x_s, y_s, x_m, y_m):
    if abs(y_s - y_m) < abs(x_s - x_m):
        return (x_m, y_s)
    else:
        return (x_s, y_m)

def x_t(A,k,m,t, fi):
    omega = (k/m)**0.5
    x = A*math.sin(omega*t+fi)
    return x
def v_t(A,k,m,t,fi):
    omega = (k/m)**0.5
    v = A*omega*maath.cos(omega*t + fi)
    return v
def a_t(A,k,m,t,fi):
    omega = (k/m)**0.5
    a = -A*omega*omega*math.sin(omega*t + fi)
    return a







