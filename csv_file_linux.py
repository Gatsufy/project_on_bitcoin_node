import pandas as pd
import time
from datetime import datetime

dateTimeObj = datetime.now()

timestampStr = dateTimeObj.strftime("%d-%b-%Y-%H-%M")


def from_json_to_csv():
    data_frame = pd.read_json("//home//btc-user//bitcoin_peer.json")

    data_frame.to_json("//home//btc-user//marco_mel//json//" + timestampStr + ".json")

    new_dataframe = pd.DataFrame(data_frame, columns=['id', 'inbound', 'addr', 'conntime'])

    new_dataframe.insert(loc=4, column='today', value=int(time.time()))

    new_dataframe.to_csv("//home//btc-user//marco_mel//file_csv//" + timestampStr + ".csv")


from_json_to_csv()
