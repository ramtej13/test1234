import pandas as pd
import io
import requests
import time
from datetime import date,datetime,timedelta


from .models import Historic_data

def data_save_model_Historic_data(file_name_id):
    if file_name_id > "2020-05-01":
        print("first")
        try:
            print(file_name_id)
            data_extract_today = pd.read_csv('media/yesterday/' + file_name_id + '.csv')
            print("hello")
            data_extract_today = data_extract_today.sort_values('SYMBOL \n', ascending=True)
            symbole = data_extract_today['SYMBOL \n'].values
            open = data_extract_today['OPEN \n'].values
            high = data_extract_today['HIGH \n'].values
            low = data_extract_today['LOW \n'].values
            ltp = data_extract_today['LTP \n'].values
            change = data_extract_today['%CHNG \n'].values
            volume = data_extract_today['VOLUME \n(shares)'].values

            # delete_symbole = symbole
            # for data in delete_symbole:
            #     Historic_data.objects.filter(Historic_data_symbole=data).delete()


            data1 = Historic_data.objects.all().delete()


            # newpercentage = []
            # difference = symbole
            # for data in range(len(difference)):
            #     newpercentage1 = change[data] + "0"
            #     newpercentage.append(newpercentage1)


            for data in range(len(symbole)):
                table_symbole2 = Historic_data()
                table_symbole2.Historic_data_open = float(open[data].replace(',', ''))
                table_symbole2.Historic_data_percentage_change =change[data]
                table_symbole2.Historic_data_high = float(high[data].replace(',', ''))
                table_symbole2.Historic_data_low = float(low[data].replace(',', ''))
                table_symbole2.Historic_data_volume = float(volume[data])#.replace(',', ''))
                table_symbole2.Historic_data_symbole = symbole[data]
                table_symbole2.Historic_data_ltp = float(ltp[data].replace(',', ''))
                table_symbole2.save()
            return True
        except Exception as e:
            print(e)
            return False
    else:
        try:
            data_extract_today = pd.read_csv('media/yesterday/' + file_name_id + '.csv',
                                             names=['SYMBOL', 'OPEN', 'HIGH', 'LOW', 'PREV.CLOSE', 'LTP', 'CHNG', '%CHNG',
                                                    'VOLUME(shares)', 'VALUE', '52WH', '52WL'])
            data_extract_today = data_extract_today.drop([0], axis=0)
            data_extract_today = data_extract_today.sort_values('SYMBOL', ascending=True)
            symbole = data_extract_today['SYMBOL'].values
            open = data_extract_today['OPEN'].values
            high = data_extract_today['HIGH'].values
            low = data_extract_today['LOW'].values
            ltp = data_extract_today['LTP'].values
            change = data_extract_today['%CHNG'].values
            volume = data_extract_today['VOLUME(shares)'].values

            # delete_symbole = symbole
            # for data in delete_symbole:
            #     Historic_data.objects.filter(Historic_data_symbole=data).delete()

            data1 = Historic_data.objects.all().delete()

            newpercentage = []
            difference = symbole
            for data in range(len(difference)):
                newpercentage1 = change[data] + "0"
                newpercentage.append(newpercentage1)



            for data in range(len(symbole)):
                table_symbole2 = Historic_data()
                table_symbole2.Historic_data_open = float(open[data].replace(',', ''))
                table_symbole2.Historic_data_percentage_change = newpercentage[data]
                table_symbole2.Historic_data_high = float(high[data].replace(',', ''))
                table_symbole2.Historic_data_low = float(low[data].replace(',', ''))
                table_symbole2.Historic_data_volume = float(volume[data])  # .replace(',', ''))
                table_symbole2.Historic_data_symbole = symbole[data]
                table_symbole2.Historic_data_ltp = float(ltp[data].replace(',', ''))
                table_symbole2.save()
            return True

        except Exception as e:
            print(e)
            return False





