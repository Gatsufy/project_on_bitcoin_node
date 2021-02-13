from from_csv_gant_chartt import to_list

from pprint import pprint

import pandas as pd

dict_out={}


def dict_from_csv_out(filename):

    data_frame_csv = pd.read_csv(filename)

    data_frame_csv[['Ip', 'Port']] = data_frame_csv.addr.str.split(":", expand=True)

    del data_frame_csv["Port"]

    del data_frame_csv["addr"]

    for idx, row in data_frame_csv.iterrows():

        row['day_in_day_out'] = to_list(row['day_in_day_out'])

        if int(row['day_in_day_out'][1]-row['day_in_day_out'][0]) < 60:

            data_frame_csv = data_frame_csv.drop(index=idx, axis=0)

    data_frame_csv = data_frame_csv.reset_index(drop=True)

    # insert element from a dataframe in a dict
    for idx, row in data_frame_csv.iterrows():

        # create a key for a dict for all the Ip with inbound true that is not in dict_from_csv_in.keys()
        if row['Ip'] not in dict_out:

            if row['inbound'] is False:

                # convert a start time in unix epoch in a date

                start = pd.Timestamp(to_list(row['day_in_day_out'])[0], unit='s')

                # convert a finish time in unix epoch in a date

                finish = pd.Timestamp(to_list(row['day_in_day_out'])[1], unit='s')

                # insert element as first element of a specific key

                dict_out[row['Ip']] = [

                [start, finish, finish - start, row['inbound']]

                ]

        else:

            if row['inbound'] is False:

                # repeat the same operation for all other values as values of the keys

                start = pd.Timestamp(to_list(row['day_in_day_out'])[0], unit='s')

                finish = pd.Timestamp(to_list(row['day_in_day_out'])[1], unit='s')

                dict_out[row['Ip']].append(

                [start, finish, finish - start, row['inbound']])

    print(len(dict_out.keys()))


    return dict_out


dict_from_csv_out("C://Users//mmmel//Desktop//nodes_disc.csv")