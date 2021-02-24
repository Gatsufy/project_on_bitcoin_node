import pandas as pd

from pprint import pprint

dict_from_csv = {}

def to_list(s):

    lista = s.replace('[', '').replace(']', '').split(',')

    return [int(n) for n in lista]


def from_csv_to_dict(filename):

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

    return dict_from_csv


from_csv_to_dict("C://Users//mmmel//Desktop//nodes_disc.csv")
