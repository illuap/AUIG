import configparser
import json

# config = configparser.ConfigParser()
# config.read('config.json')

ENVIRONMENT = "TEST"

if('config' not in vars()): 
    with open('config.json', 'r') as f:
        cfg_all = json.load(f)
        print(cfg_all[ENVIRONMENT])
        config = cfg_all[ENVIRONMENT]

