from from_csv_to_dict import from_csv_to_dict

import numpy as np

import matplotlib.pyplot as plt

import matplotlib.patches as mpatches

import datetime

from pprint import pprint

print(" i mesi gennaio, marzo, maggio, luglio, agosto,ottobre e dicembre hanno 31 giorni, gli altri 30. Febbraio 28")

date_1 = input("Inserisci la prima data nel formato YYYY-MM-DD")

date_2 = input(" Inserisci la seconda data nel formato YYYY-MM-DD")


dict_to_plot = {}


def gantt_chart_between_date(filename,data_1, data_2):

    dict_from_dates = from_csv_to_dict(filename)

    date_time_obj_1 = datetime.datetime.strptime(data_1, '%Y-%m-%d')

    date_time_obj_2 = datetime.datetime.strptime(data_2, '%Y-%m-%d')

    

    for key, value in dict_from_dates.items():

        for i in range(len(value)):

            if value[i][0] >= date_time_obj_1 and value[i][1] <= date_time_obj_2:

                if key not in dict_to_plot:

                    dict_to_plot[key] = [[value[i][0], value[i][1], value[i][2], value[i][3]]]

                else:

                    dict_to_plot[key].append(

                        [value[i][0], value[i][1], value[i][2], value[i][3]]

                    )

    plt.figure(num=1, figsize=[20, 40], dpi=100)

    plt.xlabel("Date", weight="bold")

    plt.ylabel("IP", weight="bold")

    plt.ylim(0, len(dict_to_plot.keys()))

    # number of keys in the dict
    nrow = len(dict_to_plot.keys())

    y_pos = np.arange(nrow)

    width = 0.6

    plt.tick_params(axis='y', labelsize=8)

    plt.yticks(y_pos, reversed(dict_to_plot.keys()))

    red_patch = mpatches.Patch(color='red', label='outbound')

    blue_patch = mpatches.Patch(color='blue', label='inbound')

    plt.legend(handles=[red_patch, blue_patch])

    # plot the gantt chart from the dict of elements

    for key, value in dict_to_plot.items():

        nrow = nrow - 1

        for i in range(len(value)):

            # inbound

            if value[i][3] is True:

                plt.broken_barh([(value[i][0], value[i][2])], (nrow, width))

            else:

                plt.broken_barh([(value[i][0], value[i][2])], (nrow, width))

    plt.show()


gantt_chart_between_date("C://Users//mmmel//Desktop//nodes_disc.csv",date_1, date_2)
