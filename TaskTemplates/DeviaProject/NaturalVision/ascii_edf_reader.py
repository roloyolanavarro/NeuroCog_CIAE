import numpy as np
import re


def ascii_edf_read(file_name):
    ascii_file = open(file_name, "r")
    ascii_lines = ascii_file.readlines()
    #print(type(ascii_file))
    raw_saccade_data = []
    inside_saccade_data = False
    saccades_index = 0
    had_blink = False
    for i, line in enumerate(ascii_lines):
        if "SSACC" in line and not inside_saccade_data:
            raw_saccade_data.append([])
            raw_saccade_data[saccades_index].append(line)
            inside_saccade_data = True
        elif "ESACC" in line and inside_saccade_data:
            raw_saccade_data[saccades_index].append(line)
            if "SSACC" in raw_saccade_data[saccades_index][0] and "SSACC" in raw_saccade_data[saccades_index][1]:
                raw_saccade_data[saccades_index].pop(0)
            if had_blink:
                raw_saccade_data.pop()
            else:
                saccades_index += 1
            had_blink = False
            inside_saccade_data = False

        if inside_saccade_data:
            if "SBLINK" in line or "EBLINK" in line or "BUTTON" in line:
                had_blink = True
            if "EFIX" not in line and "SSACC" not in line and "MSG" not in line and "SFIX" not in line:
                raw_saccade_data[saccades_index].append(line)


    # Raw to structured
    processed_data = process_raw_saccade_data(raw_saccade_data)

    return processed_data


def process_raw_saccade_data(raw_saccade_data):
    processed_data = []
    for i, saccade_list in enumerate(raw_saccade_data):
        processed_data.append({'start_time': 0, 'end_time': 0, 'saccade_samples': []})
        for j, line in enumerate(saccade_list):
            if j == 0:
                processed_data[i]['start_time'] = float(re.sub("\D", "", line.split(' ')[3]))
            elif j == len(saccade_list) - 1:
                processed_data[i]['end_time'] = float(line.split("\t")[1])
            else:
                no_blank_spaces_line = line.replace(' ', '')
                line_splitted = no_blank_spaces_line.split('\t')
                line_splitted = [None if i == "." else float(i) for i in line_splitted[0:5]]
                processed_data[i]['saccade_samples'].append(line_splitted)
    return processed_data


if __name__ == "__main__":
    print("ascii reader")
    processed_data_example = ascii_edf_read(file_name="s1_e1.asc")
    print("a")