
import pandas as pd
import numpy as np
from faker import Faker
import requests
import json

###----DB-------





def return_request():
    with open(r'requirements.txt', 'r') as r:
        all_lines = r.readlines()
    return str(all_lines)


def mean():
    df1 = pd.read_csv(r'./hw (2) (1).csv')
    df1['Height(Centimeters)'] = df1.iloc[:, 1] / 2.54
    df1['Weight(Kilograms)'] = df1.iloc[:, 2] / 2.205
    avg_cm = pd.Series(df1.iloc[:, 3]).mean()
    avg_kg = pd.Series(df1.iloc[:, 4]).mean()
    result = f'{avg_cm} cm,  {avg_kg} kg '
    return result




def generate_users(n):
    fake = Faker()
    names=[fake.name() for i in range(n)]
    emails = [fake.email() for i in range(n)]
    result = zip(names, emails)
    return dict(result)



def count_astronauts():
    r = requests.get('http://api.open-notify.org/astros.json')
    temp_j = r.json()
    len_dict = len(temp_j['people'])
    return str(len_dict)


