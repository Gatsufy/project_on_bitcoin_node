import pandas as pd

import time

from datetime import datetime

dateTimeObj = datetime.now()

timestampStr = dateTimeObj.strftime("%d-%b-%Y-%H-%M")

# convert a file json in a csv file
def from_json_to_csv():
    
    data_frame = pd.read_json("C://Users//mmmel//Desktop//bitcoin_peer.json")

    data_frame.to_json("C://Users//mmmel//Desktop//" + timestampStr + ".json",indent=4)

    new_dataframe = pd.DataFrame(data_frame, columns=['id', 'inbound', 'addr', 'conntime'])

    new_dataframe.insert(loc=4, column='today', value=int(time.time()))

    new_dataframe.to_csv("C://Users//mmmel//Desktop//"+timestampStr+".csv")


from_json_to_csv()
