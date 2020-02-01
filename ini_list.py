# -*- coding: utf-8 -*-
"""
@author : yKRSW
@purpose: Sample of ini list
"""

import configparser

config = configparser.ConfigParser()
config.read("sample.ini")

"""
[settings]
SETTINGS_01=settings content 01
SETTINGS_02=settings content 02
"""

settings_01 = config.get("settings", "SETTINGS_01")
settings_02 = config.get("settings", "SETTINGS_02")
print("settings_01: {}".format(settings_01))
print("settings_02: {}".format(settings_02))

# settings_01: settings content 01
# settings_02: settings content 02

print()

"""
[settings_list]
SETTINGS_03=["content03-1","content03-2","content03-3"]
"""

settings_03 = config.get("settings_list", "SETTINGS_03")
print(settings_03)
print(type(settings_03))

# ["content03-1","content03-2","content03-3"]
# <class 'str'>

print()

settings_03_1 = eval(config.get("settings_list", "SETTINGS_03"))
print(settings_03_1)
print(type(settings_03_1))

# ['content03-1', 'content03-2', 'content03-3']
# <class 'list'>

print()

import pandas as pd

settings_03_csv = config.get("settings_list", "SETTINGS_03_CSV")
print(settings_03_csv)

df_settings_03 = pd.read_csv(settings_03_csv)
print(df_settings_03["CONTENT"].to_list())
print(type(df_settings_03["CONTENT"].to_list()))

# ['content03-1', 'content03-2', 'content03-3']
# <class 'list'>

print()

import json

settings_03_1 = json.loads(config.get("settings_list", "SETTINGS_03"))
print(settings_03_1)
print(type(settings_03_1))

# ['content03-1', 'content03-2', 'content03-3']
# <class 'list'>