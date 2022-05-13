import glob
import os


def change_file_names(images_folder):
    files = glob.glob(images_folder + "*.png")
    for i, file_name in enumerate(files):
        os.rename(file_name, images_folder + str(i) + ".png")


if __name__ == "__main__":
    print('change images')
    change_file_names(images_folder='./stimuli/')