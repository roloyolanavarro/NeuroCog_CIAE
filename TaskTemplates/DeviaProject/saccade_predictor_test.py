import glob

import math
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from saccade_predictor import pixels_to_degrees_transformation, fitting_function, end_saccade_position
from ascii_edf_reader import ascii_edf_read
from config_helper import read_config

# TODO: works with python 3 only, i guess just leave it that way for now


def compare_fit_to_data(file_name, cfg):
    distance_from_screen_in_cm = cfg['distance_from_screen_in_cm']
    one_degree_cm_to_screen_equivalence = cfg['one_degree_cm_to_screen_equivalence']
    one_cm_to_pixels = cfg['one_cm_to_pixels']
    saccade_range = cfg['saccade_range']

    processed_data = ascii_edf_read(file_name=file_name)
    predictor_data = []
    for i, saccade_data in enumerate(processed_data):
        start_pos = (saccade_data['saccade_samples'][0][1], saccade_data['saccade_samples'][0][2])
        # Search end position
        start_time = saccade_data['start_time']
        end_time = saccade_data['end_time']
        for saccade_sample in saccade_data['saccade_samples']:
            if saccade_sample[0] == end_time:
                end_pos = (saccade_sample[1], saccade_sample[2])
        predictor_data.append([])
        if start_pos[0] is not None and start_pos[1] is not None and end_pos[0] is not None and end_pos[1] is not None:
            saccade_real_length = math.sqrt((end_pos[0] - start_pos[0])**2 + (end_pos[1] - start_pos[1])**2)
            saccade_real_length_degrees = pixels_to_degrees_transformation(distance_from_screen_in_cm=distance_from_screen_in_cm,
                                             one_degree_cm_to_screen_equivalence=one_degree_cm_to_screen_equivalence,
                                             one_cm_to_pixels=one_cm_to_pixels,
                                             pixels=saccade_real_length)

            for new_sample in saccade_data['saccade_samples']:
                if new_sample[1] is not None and new_sample[2] is not None and new_sample[0] <= end_time:
                    t_k = new_sample[0] - saccade_data['start_time']
                    d_k_in_pixels = math.sqrt((new_sample[1] - start_pos[0]) ** 2 + (new_sample[2] - start_pos[1]) ** 2)
                    d_k = pixels_to_degrees_transformation(distance_from_screen_in_cm=distance_from_screen_in_cm,
                                                           one_degree_cm_to_screen_equivalence=one_degree_cm_to_screen_equivalence,
                                                           one_cm_to_pixels=one_cm_to_pixels,
                                                           pixels=d_k_in_pixels)
                    s_k_length = fitting_function(t_k=t_k, d_k=d_k)

                    end_saccade_prediction = end_saccade_position(s_k=s_k_length, start_pos=start_pos,
                                                                  end_pos=(new_sample[1], new_sample[2]),
                                                                  saccade_range=saccade_range,
                                                                  distance_from_screen=distance_from_screen_in_cm,
                                                                  one_degree_cm_to_screen_equivalence=one_degree_cm_to_screen_equivalence,
                                                                  one_cm_to_pixels=one_cm_to_pixels)
                    if end_saccade_prediction is not None:
                        prediction_error_pixels = math.sqrt((end_saccade_prediction[0] - end_pos[0])**2 + (end_saccade_prediction[1] - end_pos[1])**2)
                        prediction_error_degrees = pixels_to_degrees_transformation(distance_from_screen_in_cm,
                                                                                    one_degree_cm_to_screen_equivalence,
                                                                                    one_cm_to_pixels, prediction_error_pixels)
                        predictor_data[i].append({ "t_to_end": (end_time - start_time) - t_k,
                                                   "t_total": end_time - start_time,
                                                    "t_k": t_k,
                                                 "prediction_error_degrees": prediction_error_degrees,
                                                 "end_pos": end_pos,
                                                 "end_saccade_prediction": end_saccade_prediction,
                                                 "prediction_error_pixels": prediction_error_pixels,
                                                 "saccade_real_length_degrees": saccade_real_length_degrees})

    return predictor_data


def analysis_predictor_data(predictor_data):
    analysis_dictionary_t_to_end = {}
    misc_data = {'saccade_lengths': [], 't_totals': []}

    for saccade_data in predictor_data:
        if saccade_data:
            misc_data['saccade_lengths'].append(saccade_data[0]["saccade_real_length_degrees"])
            misc_data['t_totals'].append(saccade_data[0]["t_total"])

        for sample in saccade_data:
            if str(sample['t_to_end']) in analysis_dictionary_t_to_end:
                analysis_dictionary_t_to_end[str(sample['t_to_end'])].append((sample["prediction_error_degrees"],
                                                                              sample["saccade_real_length_degrees"],
                                                                              sample['t_total'],
                                                                              sample['t_k']))
            else:
                analysis_dictionary_t_to_end[str(sample['t_to_end'])] = []
                analysis_dictionary_t_to_end[str(sample['t_to_end'])].append((sample["prediction_error_degrees"],
                                                                              sample["saccade_real_length_degrees"],
                                                                              sample['t_total'],
                                                                              sample['t_k']))

    data_by_saccade_length = {'0_to_10': [], '10_to_20': [], '20_to_30': [], '30_to_40': []}
    # For by time before end of saccade
    get_by_total_time = 30
    t_k_search = 14
    for i in range(0, 1000, 2):
        key_string = str(i) + ".0"
        if key_string in analysis_dictionary_t_to_end:
            for element in analysis_dictionary_t_to_end[key_string]:
                if element[2] >= get_by_total_time and t_k_search == element[3]:
                    if 0.0 <= element[1] < 10.0:
                        data_by_saccade_length['0_to_10'].append(element[0])
                    elif 10.0 <= element[1] < 20.0:
                        data_by_saccade_length['10_to_20'].append(element[0])
                    elif 20.0 <= element[1] < 30.0:
                        data_by_saccade_length['20_to_30'].append(element[0])
                    elif 30.0 <= element[1] < 40.0:
                        data_by_saccade_length['30_to_40'].append(element[0])

    for key in data_by_saccade_length:
        print('Amount of data in lengths ' + key)
        print(len(data_by_saccade_length[key]))
        print('Mean in ' + key)
        print(np.mean(data_by_saccade_length[key]))
        plt.hist(data_by_saccade_length[key], bins=100)
        plt.xlabel('Prediction error in degrees')
        plt.ylabel('Frequency')
        plt.title("Saccades of length " + key)
        plt.xticks(np.arange(41, step=5))
        plt.show()

    # Misc data
    for key in misc_data:
        plt.hist(misc_data[key], bins=100)
        plt.xlabel(key)
        plt.ylabel('Frequency')
        plt.title(key)
        plt.show()


def predictor_generate_data():
    cfg = read_config(config_file='config.yml')
    predictor_data = compare_fit_to_data(file_name="s612_nat.asc", cfg=cfg)
    return predictor_data


def predict_batch_of_files(cfg):
    saccades_folder = cfg["saccade_examples_folder"]
    files = glob.glob(saccades_folder + "*")
    all_saccade_data = []
    for file in files:
        new_predictor_data = compare_fit_to_data(file_name=file, cfg=cfg)
        all_saccade_data.extend(new_predictor_data)
    return all_saccade_data


if __name__ == '__main__':
    print("test main")
    cfg_example = read_config(config_file='config.yml')
    all_saccade_data_example = predict_batch_of_files(cfg=cfg_example)
    analysis_predictor_data(predictor_data=all_saccade_data_example)
