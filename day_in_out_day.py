import pandas as pd

from os import path

from datetime import datetime, timedelta

dateTimeObj = datetime.now()

timestampStr = dateTimeObj.strftime("%d-%b-%Y-%H-%M")

ten_minute = timedelta(minutes=10)

diff_ten_minutes = dateTimeObj - ten_minute

timestampStr1 = diff_ten_minutes.strftime("%d-%b-%Y-%H-%M")

dict_day_in_day_out: {}

lista_day_in_day_out = []

def check_if_2_dataframe_have_same_element():

    data_frame_10_mins_after = pd.read_csv("C://Users//mmmel//Desktop//29-Dec-2020-10-20.csv")

    if path.exists("C://Users//mmmel//Desktop//29-Dec-2020-10-10.csv"):

        data_frame_2 = pd.read_csv("C://Users//mmmel//Desktop//29-Dec-2020-10-10.csv")

        common = data_frame_2.merge(data_frame_10_mins_after, on=["id"])

        nodes_disc = data_frame_2[~data_frame_2.id.isin(common.id)]
    for row, value in nodes_disc.iterrows():

        lista_day_in_day_out.append([value[4], value[5]])

    nodes_disc.insert(loc=6, column='day_in_day_out', value=lista_day_in_day_out)

    del nodes_disc["conntime"]

    del nodes_disc["today"]

    del nodes_disc["Unnamed: 0"]

    if path.exists("C://Users//mmmel//Desktop//nodes_disc.csv"):

        nodes_disc.to_csv("C://Users//mmmel//Desktop//nodes_disc.csv", header=False, mode='a')

    else:

        nodes_disc.to_csv("C://Users//mmmel//Desktop//nodes_disc.csv")


check_if_2_dataframe_have_same_element()
