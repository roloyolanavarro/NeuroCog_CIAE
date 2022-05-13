import csv
import re


def erase_between_lines(csv_file):
    csv_file_no_between_lines ='trials_without_between_lines.csv'

    lines_from_csv = []
    count_numbers = {'10': 0, '20s': 0, '40s': 0, 'other': 0}
    with open(csv_file) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=';')
        for i, row in enumerate(readCSV):
            row_separated = row[0].split(',')
            if i != 0:
                only_numbers = re.sub("\D", "", row_separated[1])
                if only_numbers.isdigit():
                    new_signal = int(only_numbers)
                else:
                    new_signal = only_numbers

                if new_signal == 10:
                    count_numbers['10'] += 1
                elif new_signal in [21, 22, 23, 24, 25]:
                    count_numbers['20s'] += 1
                elif new_signal in [41, 42, 43]:
                    count_numbers['40s'] += 1
                else:
                    print(new_signal)
                    count_numbers['other'] += 1

            lines_from_csv.append(row_separated)

    # Create new csv
    with open(csv_file_no_between_lines,  'w', newline='') as csvfile2:
        fieldnames = ['trial', 'senal1']
        writer = csv.DictWriter(csvfile2, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()

        i_change = False
        for i in range(451):
            if i != 0:
                writer.writerow({'trial': lines_from_csv[i][0],
                                 'senal1': lines_from_csv[2*(i-1)+i][1]})


if __name__ == '__main__':
    erase_between_lines(csv_file='trials_editado.csv')