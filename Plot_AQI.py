# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 19:16:19 2022

@author: Sudharsan
"""

import pandas as pd
import matplotlib.pyplot as plt

def avg_data(year):
    temp_i = 0
    average = []
    for rows in pd.read_csv('Data/AQI/aqi{}.csv'.format(year),chunksize=24):
        add_var = 0
        avg = 0.0
        data = []
        df = pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var += i
            elif type(i) is str:
                if i != 'NoData' and i != 'PwrFail' and i!= '---' and i != 'InVld':
                    temp = float(i)
                    add_var += temp
        avg = add_var/24
        temp_i += 1

        average.append(avg)
    return average

if __name__ == "__main__":
    for year in range(2013,2019):
        globals()[f"lst{year}"] = avg_data(year)

    plt.plot(range(0,365),lst2013,label="2013 data")
    plt.plot(range(0,364),lst2014,label="2014 data")
    plt.plot(range(0,365),lst2015,label="2015 data")
    plt.show()