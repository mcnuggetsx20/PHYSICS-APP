import math
import pygame


def circle_line(start_pos, end_pos, lenght_of_first_line):
    x1 = start_pos[0]
    y1 = start_pos[1]
    x2 = end_pos[0]
    y2 = end_pos[1]
    r = lenght_of_first_line
    if x2-x1 == 0:
        x2_solved1 = x1
        y2_solved1 = y1-lenght_of_first_line
        x2_solved2 = x1
        y2_solved2 = y1+lenght_of_first_line
    else:
        a_parameter = (y2-y1)/(x2-x1)
        b_parameter = y1-a_parameter*x1
        delta = (2*a_parameter*b_parameter-2*x1-2*y1*a_parameter)**2-4 * \
            (1+a_parameter**2)*(x1**2+b_parameter**2+y1**2-2*y1*b_parameter-r**2)
        if delta < 0:
            delta = 0
        delta_sqrt = math.sqrt(delta)
        x2_solved1 = (-(2*a_parameter*b_parameter-2*x1-2*y1 *
                      a_parameter)+delta_sqrt)/(2*(1+a_parameter**2))
        x2_solved2 = (-(2*a_parameter*b_parameter-2*x1-2*y1 *
                      a_parameter)-delta_sqrt)/(2*(1+a_parameter**2))
        y2_solved1 = a_parameter*x2_solved1 + b_parameter
        y2_solved2 = a_parameter*x2_solved2 + b_parameter
    if r > 0:
        if (x2-x2_solved1)**2 + (y2-y2_solved1)**2 > (x2-x2_solved2)**2 + (y2-y2_solved2)**2:
            x2_solved = x2_solved2
            y2_solved = y2_solved2
        else:
            x2_solved = x2_solved1
            y2_solved = y2_solved1
    else:
        if (x2-x2_solved1)**2 + (y2-y2_solved1)**2 < (x2-x2_solved2)**2 + (y2-y2_solved2)**2:
            x2_solved = x2_solved2
            y2_solved = y2_solved2
        else:
            x2_solved = x2_solved1
            y2_solved = y2_solved1
    return (x2_solved, y2_solved)


def draw_coil(screen, start_pos, end_pos, line_width, lenght_of_first_line, number_of_links, link_radius, link_width, coil_color):
    (x1, y1) = start_pos
    (x2, y2) = end_pos
    full_line_lenght = math.sqrt(
        (y2-y1)**2+(x2-x1)**2)-2*lenght_of_first_line-2*link_radius

    space_between_link = full_line_lenght/(number_of_links-1)

    if space_between_link > 0:
        for space_id in range(0, number_of_links):
            circle = circle_line(
                start_pos, end_pos, lenght_of_first_line+link_radius+space_between_link*space_id)
            pygame.draw.circle(screen, coil_color, circle,
                               link_radius, link_width)
        x2_solved, y2_solved = circle_line(
            start_pos, end_pos, lenght_of_first_line)
        x3_solved, y3_solved = circle_line(
            end_pos, start_pos, lenght_of_first_line)
        pygame.draw.line(screen, coil_color, (x3_solved,
                         y3_solved), end_pos, line_width)
        pygame.draw.line(screen, coil_color, start_pos,
                         (x2_solved, y2_solved), line_width)
    else:
        circle = circle_line(start_pos, end_pos,
                             lenght_of_first_line+link_radius)
        pygame.draw.circle(screen, coil_color, circle, link_radius, link_width)
        line_pos1 = circle_line(start_pos, end_pos, lenght_of_first_line)
        line_pos2 = circle_line(
            start_pos, end_pos, lenght_of_first_line+2*link_radius)
        line_pos3 = circle_line(start_pos, end_pos, 2 *
                                lenght_of_first_line+2*link_radius)
        pygame.draw.line(screen, coil_color, start_pos, line_pos1, line_width)
        pygame.draw.line(screen, coil_color, line_pos2, line_pos3, line_width)


def draw_straight_line(x_s, y_s, x_m, y_m):
    if abs(y_s - y_m) < abs(x_s - x_m):
        return (x_m, y_s)
    else:
        return (x_s, y_m)


def moving_blocks(list_of_coils, list_of_weights, dict_of_connections, speed_multipler, fps, gravitation):
    # print(list_of_coils)
    list_of_keys = (list(dict_of_connections.keys()))
    new_list_of_coils = list_of_coils
    new_list_of_weights = list_of_weights
    for i in range(0, len(list_of_keys)):
        weight_idx = list_of_keys[i]
        weight_pos_x = list_of_weights[weight_idx][0][0]
        weight_pos_y = list_of_weights[weight_idx][0][1]
        weight_mass = list_of_weights[weight_idx][1]
        weight_velocity_vector = list_of_weights[weight_idx][2]

        list_of_connected_coils = dict_of_connections.get(weight_idx)
        force_vectors = []
        for coil in list_of_connected_coils:

            coil_idx = coil[0]
            coil_start_pos_x = list_of_coils[coil_idx][0][0]
            coil_start_pos_y = list_of_coils[coil_idx][0][1]
            coil_end_pos_x = list_of_coils[coil_idx][1][0]
            coil_end_pos_y = list_of_coils[coil_idx][1][1]
            coil_base_lenght = list_of_coils[coil_idx][2]
            coil_k = list_of_coils[coil_idx][3]
            coil_lenght = ((coil_end_pos_x-coil_start_pos_x) **
                           2 + (coil_end_pos_y-coil_start_pos_y)**2)**0.5
            f = coil_k * (coil_lenght-coil_base_lenght)

            if coil[1] == 0:
                vector_start_pos = (coil_start_pos_x, coil_start_pos_y)
                vector_end_pos = circle_line(
                    (coil_start_pos_x, coil_start_pos_y), (coil_end_pos_x, coil_end_pos_y), f)
            elif coil[1] == 1:
                vector_start_pos = (coil_end_pos_x, coil_end_pos_y)
                vector_end_pos = circle_line(
                    (coil_end_pos_x, coil_end_pos_y), (coil_start_pos_x, coil_start_pos_y), f)
            force_vectors.append([vector_start_pos, vector_end_pos])
        force_vectors.append([(weight_pos_x, weight_pos_y),
                             (weight_pos_x, weight_pos_y+weight_mass*gravitation)])
        # print(force_vectors)
        result_vector = [0, 0]
        for j in force_vectors:
            result_vector[0] += j[1][0]-j[0][0]
            result_vector[1] += j[1][1]-j[0][1]
        vector_value = (result_vector[0]**2+result_vector[1]**2)**0.5
        delta_v = (vector_value/weight_mass)*(1/fps)
        vector_v = circle_line((weight_pos_x, weight_pos_y), (weight_pos_x+int(
            result_vector[0]), weight_pos_y+int(result_vector[1])), delta_v*speed_multipler)

        weight_velocity_vector[0] += vector_v[0]-weight_pos_x
        weight_velocity_vector[1] += vector_v[1]-weight_pos_y
        x_result_pos = weight_velocity_vector[0]/fps
        y_result_pos = weight_velocity_vector[1]/fps

        result_pos = (weight_pos_x+x_result_pos, weight_pos_y+y_result_pos)
        new_list_of_weights[weight_idx][0] = result_pos

        for coil in list_of_connected_coils:
            # print(coil)
            if coil[1] == 1:
                new_list_of_coils[coil[0]][1] = result_pos
            else:
                new_list_of_coils[coil[0]][0] = result_pos
    # print(new_list_of_coils)
    return(new_list_of_coils, new_list_of_weights)


def distance_between_points(x1, y1, x2, y2):
    distance = ((x1-x2)**2 + (y1-y2)**2)**0.5
    return(distance)
