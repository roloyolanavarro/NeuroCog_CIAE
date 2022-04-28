import math
import pylink
import logging
import random
import queue
from pygaze.libtime import clock
from scipy.optimize import minimize, differential_evolution
from ascii_edf_reader import ascii_edf_read
from config_helper import read_config


def degrees_to_pixels_transformation(distance_from_screen,one_degree_cm_to_screen_equivalence,
                                     one_cm_to_pixels, degrees):
    degree_weigh = distance_from_screen / one_degree_cm_to_screen_equivalence
    in_screen_cms = degree_weigh * degrees
    pixels = in_screen_cms * one_cm_to_pixels
    return pixels


def pixels_to_degrees_transformation(distance_from_screen_in_cm, one_degree_cm_to_screen_equivalence,
                                     one_cm_to_pixels, pixels):
    degree_weight = distance_from_screen_in_cm / one_degree_cm_to_screen_equivalence
    in_screen_cms = pixels / one_cm_to_pixels
    in_screen_degrees = in_screen_cms / degree_weight
    return in_screen_degrees


def function_of_time_n_displacement(t, d, params):
    """According to this analysis, polynomial degrees 5 for t and 2 for d provide the lowest cross-validation
    error for the largest number of participants"""
    function_value = params[0]*t**5 + params[1]*t**4 + params[2]*t**3 + params[3]*t**2 + params[4]*t + params[5] \
                      + params[6]*t**5*d + params[7]*t**4*d + params[8]*t**3*d + params[9]*t**2*d + params[10]*t*d + params[11]*d \
                      + params[12]*t**5*d**2 + params[13]*t**4*d**2 + params[14]*t**3*d**2 + params[15]*t**2*d**2 + params[16]*t*d**2 + params[17]*d**2

    return function_value


def create_personalized_polynomial(params):
    """Saccade groups are as described in the paper, groups with the start of saccades positions, all in between values
    and the end of the saccade, for the optimization we use the last position before the end of the saccade. Uses
    equation 7 and 8 from the paper"""
    global saccade_groups
    total_value = 0
    # Implementation of Eq (8)
    for i, saccade_group in enumerate(saccade_groups):
        if saccade_group:
            s_k_length = abs(saccade_group[-1][1] - saccade_group[0][1])

            for tk_dk_tuple in saccade_group:
                t_k_l = tk_dk_tuple[0]
                d_k_l = tk_dk_tuple[1]
                if t_k_l > 0:
                    total_value += (s_k_length - function_of_time_n_displacement(t=float(t_k_l), d=float(d_k_l), params=params))**2
    #print(str(total_value))
    #print(str(params))
    return total_value


def optimized_saccade_model(saccade_groups, bounds=None):
    results = differential_evolution(create_personalized_polynomial, bounds=bounds) #, maxiter=10000000000000)
    #print(results)


def fitting_function(t_k, d_k):
    # TODO: edit to consider personalized model
    t = (t_k - 47.39)/33.4
    d = (d_k - 14.67)/11.72
    poly_f = lambda t, d: -10.19*t + 19.11*t**2 - 17.15*t**3 + 6.251*t**4 - 0.7552*t**5 - 23*d*t + 26.89*d*t**2 - 14.74*d*t**3 + 3.882*d*t**4 - 0.4005*d*t**5 - 11.84*d**2*t + 9.326*d**2*t**2 - 2.583*d**2*t**3 - 0.01058*d**2*t**4 + 0.06587*d**2*t**5 + 20.18*d + 5.071*d**2 + 18.15
    s_k_length = poly_f(t, d)
    return s_k_length


def calculate_theta(start_pos, end_pos):
    if end_pos[0] == start_pos[0]:
        if end_pos[1] > start_pos[1]:
            theta = - math.pi / 2.0
        else:
            theta = math.pi / 2.0
    elif end_pos[0] > start_pos[0]:
        theta = math.atan(float(end_pos[1] - start_pos[1]) / float(end_pos[0] - start_pos[0]))
    else:
        theta = math.atan(float(end_pos[1] - start_pos[1]) / float(end_pos[0] - start_pos[0])) + math.pi
    return theta


def end_saccade_position(s_k, start_pos, end_pos, saccade_range,
                         distance_from_screen, one_degree_cm_to_screen_equivalence,one_cm_to_pixels):
    if saccade_range[0] <= s_k <= saccade_range[1]:
        theta = calculate_theta(start_pos=start_pos, end_pos=end_pos)
        x_degrees_displacement = s_k * math.cos(theta)
        y_degrees_displacement = s_k * math.sin(theta)
        x_pixels_displacement = degrees_to_pixels_transformation(distance_from_screen=distance_from_screen,
                                                                 one_degree_cm_to_screen_equivalence=one_degree_cm_to_screen_equivalence,
                                                                 one_cm_to_pixels=one_cm_to_pixels,
                                                                 degrees=x_degrees_displacement)
        y_pixels_displacement = degrees_to_pixels_transformation(distance_from_screen=distance_from_screen,
                                                                 one_degree_cm_to_screen_equivalence=one_degree_cm_to_screen_equivalence,
                                                                 one_cm_to_pixels=one_cm_to_pixels,
                                                                 degrees=y_degrees_displacement)
        end_saccade_prediction = (start_pos[0] + x_pixels_displacement, start_pos[1] + y_pixels_displacement)
    else:
        end_saccade_prediction = None
    return end_saccade_prediction


def predict_saccade_occurrence(tracker, end_saccade_detector):
    t1, start_pos = tracker.wait_for_saccade_start()
    end_saccade_detector.start()
    return t1, start_pos





def predict_saccade_position(tracker, distance_from_screen_in_cm,
                             one_degree_cm_to_screen_equivalence, one_cm_to_pixels, sampling_time, saccade_range,
                             end_saccade_detector):
    # Waiting for saccade message
    #t, d = tracker.wait_for_event(pylink.ENDSACC)
    #tracker.log('start_fix_{}_{}_{}'.format(t, d.getTime(), d.getStartGaze()))
    #endtime_, startpos_, endpos_ = tracker.wait_for_saccade_end()
    #tracker.log('ended_saccade_before_used_end_time_{}_startpos_{}_endpos_{}'.format(endtime_, startpos_, endpos_))

    # Wait for an end of a saccade first
    #while True:
       # d = pylink.getEYELINK().getNextData()
       # if d == pylink.ENDSACC: # creo que asi se llama el evento
        #    tracker.log('FOUND END SACCADE')
            #print('pylink works')
         #   break
    #tracker.wait_for_saccade_end()
    #while True:
    #NO USAR, NO CALZA CON LO ENTREGADO EN EL EDF
       # d = pylink.getEYELINK().getNextData()
        #if d == pylink.ENDSACC: # creo que asi se llama el evento
          #  tracker.log('end saccade pylink')
           # break
    # Wait 50 ms after end of a saccade
    #wait_50_ms_start = clock.get_time()
    #tracker.log('Waiting 50 ms')
    #while clock.get_time() - wait_50_ms_start < 50:
     #   a = 1
    #tracker.log('End 50 ms wait')
    t1, start_pos = tracker.wait_for_saccade_start()
    #start_pos = tracker.sample()
    #print('start_pos_{}_end_pos_{}_time_{}'.format(start_pos,endpos, endtime))
    #print('start_pos_{}'.format(start_pos))
    tracker.log('start_pos_{}_sampling_time_{}'.format(start_pos, sampling_time))
    tracker.log('t1_{}'.format(t1))
    #tracker.log('clock_{}'.format(clock.get_time()))
    #end_saccade_detector.start()

    # Code adapted from wait for event from libeyelink.py
    # https://stackoverflow.com/questions/35071433/psychopy-and-pylink-example
    #while True:
      #  d = pylink.getEYELINK().getNextData()
      #  if d == pylink.STARTSACC:
      #      float_data = pylink.getEYELINK().getFloatData()
        #    print('float data {}'.format(float_data))
         #   # corresponding clock_time
         #   tc = float_data.getTime() - tracker._get_eyelink_clock_async()
         #   if tc > t0:
          #      return tc, float_data

    end_sampling_time = t1
    #samples = []
    #count_samples = 0
    while end_sampling_time - t1 < sampling_time:
        new_sample = tracker.sample()
        end_sampling_time = clock.get_time()

    d_k_in_pixels = math.sqrt((new_sample[0] - start_pos[0])**2 + (new_sample[1] - start_pos[1])**2)
    d_k = pixels_to_degrees_transformation(distance_from_screen_in_cm=distance_from_screen_in_cm,
                                           one_degree_cm_to_screen_equivalence=one_degree_cm_to_screen_equivalence,
                                           one_cm_to_pixels=one_cm_to_pixels,
                                           pixels=d_k_in_pixels)
    s_k_length = fitting_function(t_k=end_sampling_time-t1, d_k=d_k)
    end_saccade_prediction = end_saccade_position(s_k=s_k_length, start_pos=start_pos, end_pos=new_sample,
                                                  saccade_range=saccade_range,
                                                  distance_from_screen=distance_from_screen_in_cm,
                                                  one_degree_cm_to_screen_equivalence=one_degree_cm_to_screen_equivalence,
                                                  one_cm_to_pixels=one_cm_to_pixels)

    tracker.log('PREDICTION LENGTH {}'.format(s_k_length))
    return end_saccade_prediction, end_sampling_time, start_pos #, start_pos


def data_process_for_model(file_name, cfg):
    distance_from_screen_in_cm = cfg['distance_from_screen_in_cm']
    one_degree_cm_to_screen_equivalence = cfg['one_degree_cm_to_screen_equivalence']
    one_cm_to_pixels = cfg['one_cm_to_pixels']
    processed_data = ascii_edf_read(file_name=file_name)
    data_for_model = []
    for saccade_data in processed_data:
        start_pos = (saccade_data['saccade_samples'][0][1], saccade_data['saccade_samples'][0][2])
        start_time = saccade_data['start_time']
        end_time = saccade_data['end_time']
        data_for_model.append([])
        if start_pos[0] is not None:
            for new_sample in saccade_data['saccade_samples']:
                if new_sample[1] is not None and new_sample[2] is not None and new_sample[0] <= end_time:
                    t_k = new_sample[0] - start_time
                    d_k_in_pixels = math.sqrt((new_sample[1] - start_pos[0]) ** 2 + (new_sample[2] - start_pos[1]) ** 2)
                    d_k = pixels_to_degrees_transformation(distance_from_screen_in_cm=distance_from_screen_in_cm,
                                                           one_degree_cm_to_screen_equivalence=one_degree_cm_to_screen_equivalence,
                                                           one_cm_to_pixels=one_cm_to_pixels,
                                                           pixels=d_k_in_pixels)
                    data_for_model[-1].append((t_k, d_k))

    return data_for_model


if __name__ == '__main__':
    cfg_example = read_config(config_file='config.yml')
    saccade_groups = data_process_for_model(file_name="s605_nat.asc", cfg=cfg_example)
    bounds_example = [(-50.0, 50.0) for i in range(4)]
    optimized_saccade_model(saccade_groups=saccade_groups, bounds=bounds_example)
