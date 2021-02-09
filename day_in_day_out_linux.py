import pandas as pd

from os import path

from datetime import datetime, timedelta

import os

import time

dateTimeObj = datetime.now()

timestampStr = dateTimeObj.strftime("%d-%b-%Y-%H-%M")

ten_minute = timedelta(minutes=10)

diff_ten_minutes = dateTimeObj - ten_minute

timestampStr1 = diff_ten_minutes.strftime("%d-%b-%Y-%H-%M")

lista_day_in_day_out = []

def check_if_2_dataframe_have_same_element():

    data_frame_10_mins_after = pd.read_csv("//home//btc-user//marco_mel//file_csv//"+timestampStr+".csv")

    if path.exists("//home//btc-user//marco_mel//file_csv//"+timestampStr1+".csv"):

        data_frame_2 = pd.read_csv("//home//btc-user//marco_mel//file_csv//"+timestampStr1+".csv")

        common = data_frame_2.merge(data_frame_10_mins_after, on=["id"])

        nodes_disc = data_frame_2[~data_frame_2.id.isin(common.id)]

    for row, value in nodes_disc.iterrows():

        lista_day_in_day_out.append([value[4], int(time.time())])

        # lista_day_in_day_out.append([value[4], value[5]])

    nodes_disc.insert(loc=6, column='day_in_day_out', value=lista_day_in_day_out)

    del nodes_disc["conntime"]

    del nodes_disc["today"]

    del nodes_disc["Unnamed: 0"]

    hdr = False if os.path.isfile('//home//btc-user//marco_mel//file_csv//nodes_disc.csv') else True

    nodes_disc.to_csv('//home//btc-user//marco_mel//file_csv//nodes_disc.csv', mode='a', header=hdr)


check_if_2_dataframe_have_same_element()

for idx_1, row_1 in data_frame_csv.iterrows():

    if row_1['Ip'] not in dict_inbound:

        if row_1['inbound'] is True:
            start = pd.Timestamp(to_list(row_1['day_in_day_out'])[0], unit='s')

            finish = pd.Timestamp(to_list(row_1['day_in_day_out'])[1], unit='s')

            dict_inbound[row_1['Ip']] = [[start, finish, finish - start, row_1['inbound']]]
    else:

        if row_1['inbound'] is True:
            start = pd.Timestamp(to_list(row_1['day_in_day_out'])[0], unit='s')

            finish = pd.Timestamp(to_list(row_1['day_in_day_out'])[1], unit='s')

            dict_inbound[row_1['Ip']].append([start, finish, finish - start, row_1['inbound']])

