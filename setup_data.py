import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint

filename = "C://Users//mmmel//Desktop//nodes_disc.csv"

def to_list(s):
    l = s.replace('[', '').replace(']', '').split(',')
    return [int(n) for n in l]


if __name__ == "__main__":
    data_frame_csv = pd.read_csv(filename)
    del data_frame_csv["Unnamed: 0"]
    data_frame_csv[['Ip', 'Port']] = data_frame_csv.addr.str.split(":", expand=True)
    del data_frame_csv["Port"]
    del data_frame_csv["addr"]

    righe = []
    for _, row in data_frame_csv.iterrows():
        idip = str(row['id']) + " " + str(row['Ip'])
        # idip = row['id']
        start = pd.Timestamp(to_list(row['day_in_day_out'])[0], unit='s')
        finish = pd.Timestamp(to_list(row['day_in_day_out'])[1], unit='s')
        righe.append({
            'id + Ip': idip,
            'start': start,
            'finish': finish
        })


    data = pd.DataFrame(righe, columns=['id + Ip', 'start', 'finish'])
    print(data)

    data.sort_values(
        "start",
        axis=0,
        ascending=False,
        inplace=True
    )

    data.reset_index(
        drop=True,
        inplace=True
    )

    data["delta"] = data["finish"] - data["start"]

    pprint(data["delta"])

    data["PastTime"] = data["start"] - data["start"][0]

    nrow = len(data)
    plt.figure(num=1, figsize=[8, 5], dpi=100)
    width = 0.6

    for i in range(nrow):
        ii = nrow - i - 1

        plt.broken_barh(
            [(
                data["start"][ii],data["delta"][ii]
            )],

            (i - width / 2, width),
            color="b"
        )

    y_pos = np.arange(nrow)
    plt.yticks(y_pos, labels=reversed(data["id + Ip"]))
    #plt.show()