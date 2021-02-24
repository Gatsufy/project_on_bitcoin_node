from dict_from_csv_file import to_list

import pandas as pd

import datetime

from pprint import pprint

def avg_numb_day_conn(filename):

    data_frame_csv = pd.read_csv(filename)

    #numero totale connessione in secondi inbound

    total_second_inbound = 0
   
    #numero totale connessioni in secondi outbound
    
    total_second_outbound = 0

    print(len(data_frame_csv))

    number_inbound = len(data_frame_csv[data_frame_csv['inbound'] == True])

    number_outbound = len(data_frame_csv[data_frame_csv['inbound'] == False])

    for idx, row in data_frame_csv.iterrows():

        if row['inbound'] == True:

            row['day_in_day_out'] = to_list(row['day_in_day_out'])

            total_second_inbound += (row['day_in_day_out'][1] - row['day_in_day_out'][0])

        else:

            row['day_in_day_out'] = to_list(row['day_in_day_out'])

            total_second_outbound += (row['day_in_day_out'][1] - row['day_in_day_out'][0])


    avg_total_second_inbound = int(total_second_inbound / number_inbound)

    avg_total_second_outbound = int(total_second_outbound / number_outbound)

    return avg_total_second_inbound,avg_total_second_outbound


avg_numb_day_conn("C://Users//mmmel//Desktop//nodes_disc.csv")