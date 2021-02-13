from dict_from_csv_file import to_list

import pandas as pd

import datetime

from pprint import pprint

def avg_numb_day_conn(filename):

    data_frame_csv = pd.read_csv(filename)

    total_day_inbound = 0

    total_day_outbound = 0

    number_key_inbound = len(data_frame_csv[data_frame_csv['inbound'] == True])

    number_key_outbound = len(data_frame_csv[data_frame_csv['inbound'] == False])

    for idx, row in data_frame_csv.iterrows():

        if row['inbound'] is True:

            row['day_in_day_out'] = to_list(row['day_in_day_out'])

            total_day_inbound = total_day_inbound + (row['day_in_day_out'][1] - row['day_in_day_out'][0])

        else:

            row['day_in_day_out'] = to_list(row['day_in_day_out'])

            total_day_outbound = total_day_outbound + (row['day_in_day_out'][1] - row['day_in_day_out'][0])

    pprint("tempo totale inbound")

    pprint(str(datetime.timedelta(seconds=total_day_inbound)))

    pprint("tempo totale outbound")

    pprint(str(datetime.timedelta(seconds=total_day_outbound)))

    avg_total_day_inbound = total_day_inbound / number_key_inbound

    avg_total_day_outbound = total_day_outbound / number_key_outbound

    pprint("media tempo connessione nodi inbound")

    pprint(str(datetime.timedelta(seconds=avg_total_day_inbound)))

    pprint("media tempo connessione nodi outbound")

    pprint(str(datetime.timedelta(seconds=avg_total_day_outbound)))


avg_numb_day_conn("C://Users//mmmel//Desktop//nodes_disc.csv")