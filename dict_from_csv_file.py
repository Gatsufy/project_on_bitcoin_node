import pandas as pd

import datetime

from pprint import pprint

dict_from_csv = {}

def to_list(s):

    lista = s.replace('[', '').replace(']', '').split(',')

    return [int(n) for n in lista]


def from_csv_to_gant_chartt(filename):

    data_frame_csv = pd.read_csv(filename)

    data_frame_csv[['Ip', 'Port']] = data_frame_csv.addr.str.split(":", expand=True)

    del data_frame_csv["Port"]

    del data_frame_csv["addr"]

    # insert element from a dataframe in a dict
    for idx, row in data_frame_csv.iterrows():

        # create a key for a dict for all the Ip with inbound true that is not in dict_from_csv_in.keys()
        if row['Ip'] not in dict_from_csv:

            # convert a start time in unix epoch in a date

            start = pd.Timestamp(to_list(row['day_in_day_out'])[0], unit='s')

            # convert a finish time in unix epoch in a date

            finish = pd.Timestamp(to_list(row['day_in_day_out'])[1], unit='s')

            # insert element as first element of a specific key

            dict_from_csv[row['Ip']] = [

                [start, finish, finish - start, row['inbound']]

                ]

        else:

            # repeat the same operation for all other values as values of the keys

            start = pd.Timestamp(to_list(row['day_in_day_out'])[0], unit='s')

            finish = pd.Timestamp(to_list(row['day_in_day_out'])[1], unit='s')

            dict_from_csv[row['Ip']].append(

                [start, finish, finish - start, row['inbound']])

    totale_giorni_inbound = 0

    number_key_inbound = 0

    totale_giorni_outbound = 0

    number_key_outbound = 0
            
    for idx, row in data_frame_csv.iterrows():
        
        if row['inbound'] is True:

            number_key_inbound = number_key_inbound+1
            
            row['day_in_day_out'] = to_list(row['day_in_day_out'])

            totale_giorni_inbound = totale_giorni_inbound + (row['day_in_day_out'][1]-row['day_in_day_out'][0])

        else:
            number_key_outbound = number_key_outbound+1

            row['day_in_day_out'] = to_list(row['day_in_day_out'])

            totale_giorni_outbound = totale_giorni_outbound + (row['day_in_day_out'][1]-row['day_in_day_out'][0])

    media_totale_giorni_inbound = totale_giorni_inbound/number_key_inbound

    media_totale_giorni_outbound = totale_giorni_outbound/number_key_outbound

    pprint("media tempo connessione nodi inbound")

    pprint(str(datetime.timedelta(seconds=media_totale_giorni_inbound)))

    pprint("media tempo connessione nodi outbound")

    pprint(str(datetime.timedelta(seconds=media_totale_giorni_outbound)))

    return totale_giorni_inbound
    

from_csv_to_gant_chartt("C://Users//mmmel//Desktop//nodes_disc.csv")