# -*- coding: utf-8 -*-  #
import yaml


def read_config(config_file):
    with open(config_file, 'r') as yml_file:
        #cfg = yaml.load(yml_file)
        cfg =yaml.full_load(yml_file)
    return cfg

if __name__ == '__main__':
    read_config(config_file='config.yml')

