from avg_numb_day_conn_inbound_outbound import avg_numb_day_conn

from dict_from_csv_file import to_list

import pandas as pd

import datetime

import math

lista=[]

deviation_outbound=0

def standard_deviation(filename):

    lista=avg_numb_day_conn(filename)

    dataframe=pd.read_csv(filename)

    number_inbound = len(dataframe[dataframe['inbound'] == True])

    number_outbound = len(dataframe[dataframe['inbound'] == False])
    
    deviation_inbound=0

    deviation_outbound=0

    for idx, rows in dataframe.iterrows():

        if rows['inbound'] is True: 
            
            rows['day_in_day_out'] = to_list(rows['day_in_day_out'])
            
            deviation_inbound +=  pow((rows['day_in_day_out'][1] -rows['day_in_day_out'][0]) - lista[0], 2)
        
        else:

            rows['day_in_day_out'] = to_list(rows['day_in_day_out'])

            deviation_outbound += pow((rows['day_in_day_out'][1]-rows['day_in_day_out'][0]) - lista[1],2)

    varianza_inbound = deviation_inbound/number_inbound

    varianza_outbound = deviation_outbound/number_outbound

    deviation_inbound = int(math.sqrt(varianza_inbound))

    deviation_outbound = int(math.sqrt(varianza_outbound))

    deviation_inbound = str(datetime.timedelta(seconds=deviation_inbound))

    deviation_outbound = str(datetime.timedelta(seconds=deviation_outbound))

    print("deviazione inbound")

    print(deviation_inbound)

    print("deviazione outbound")

    print(deviation_outbound)


standard_deviation("C://Users//mmmel//Desktop//nodes_disc.csv")