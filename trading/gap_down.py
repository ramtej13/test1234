import pandas as pd
import io
import requests
from datetime import date,datetime,timedelta
import time


from .models import Gap_down


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'X-Requested-With': 'XMLHttpRequest',
    'X-MicrosoftAjax': 'Delta=true',
    'Cache-Control': 'no-cache',
    'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
    'Connection': 'keep-alive',
}

def data_save_model_gap_down():
    # saving the current data file
    try:
        x
        file_name_today = str(time.time())
        get_data_for_today =requests.get('https://www.nseindia.com/api/equity-stockIndices?csv=true&index=SECURITIES%20IN%20F%26O',headers = headers).content[3:]
        df_today = pd.read_csv(io.StringIO(get_data_for_today.decode('utf-8')))
        data_from_web_today = df_today.to_csv('media/today/' + file_name_today + '.csv', index=False, encoding='utf-8')

        #sorting today data
        data_extract_today = pd.read_csv('media/today/' + file_name_today + '.csv')#,names=['SYMBOL', 'OPEN', 'HIGH', 'LOW', 'PREV.CLOSE', 'LTP', 'CHNG', '%CHNG','VOLUME(shares)', 'VALUE', '52WH', '52WL'])
        # ['SYMBOL \n', 'OPEN \n', 'HIGH \n', 'LOW \n', 'PREV. CLOSE \n', 'LTP \n',
         # 'CHNG \n', '%CHNG \n', 'VOLUME \n(shares)', 'VALUE ', '52W H \n',
         # '52W L \n', '365 D % CHNG \n 03-May-2019',
         # '30 D % CHNG \n 03-Apr-2020']

        #data_extract_today = data_extract_today.drop([ 'HIGH \n', 'LOW \n', 'PREV. CLOSE \n',
                                                       #'CHNG \n', '%CHNG \n', 'VOLUME \n(shares)', 'VALUE ', '52W H \n',
                                                       #'52W L \n', '365 D % CHNG \n 03-May-2019',
                                                       #'30 D % CHNG \n 03-Apr-2020'], axis=1)
        #data_extract_today = data_extract_today.drop([0], axis=0)
        data_extract_today= data_extract_today.sort_values('SYMBOL \n', ascending=True)

        # #extracting yesterday data
        table_Symbole_today = data_extract_today['SYMBOL \n'].values
        table_ltp_today = data_extract_today['LTP \n'].values
        table_today_open = data_extract_today['OPEN \n'].values


        # saving the yesterday data file
        file_name_yesterday = str(date.today())
        get_data_for_yesterday = requests.get('https://www.nseindia.com/api/equity-stockIndices?csv=true&index=SECURITIES%20IN%20F%26O',headers = headers).content[3:]
        df = pd.read_csv(io.StringIO(get_data_for_yesterday.decode('utf-8')))
        data_from_web_yesterday = df.to_csv('media/yesterday/'+file_name_yesterday+'.csv', index=False, encoding='utf-8')

        today = datetime.utcnow().date()
        yesterday = str(today - timedelta(days=1))

        #sorting yesterday data
        data_extract_yesterday = pd.read_csv("media/yesterday/"+yesterday+".csv")#, names = ['SYMBOL','OPEN','HIGH','LOW','PREV.CLOSE','CLOSE','CHNG','%CHNG','VOLUME(shares)','VALUE','52WH','52WL'])
        # data_extract_yesterday = data_extract_yesterday.drop([ 'OPEN \n', 'HIGH \n', 'PREV. CLOSE \n',
        #                                                       'CHNG \n', '%CHNG \n', 'VOLUME \n(shares)', 'VALUE ', '52W H \n',
        #                                                       '52W L \n', '365 D % CHNG \n 03-May-2019',
        #                                                       '30 D % CHNG \n 03-Apr-2020'] ,axis=1)
        #data_extract_yesterday = data_extract_yesterday.drop([0], axis=0)
        data_extract_yesterday = data_extract_yesterday.sort_values('SYMBOL \n',ascending=True)



        # extracting yesterday data
        table_Symbole_yesterday = data_extract_yesterday['SYMBOL \n'].values
        table_close_yesterday = data_extract_yesterday['LTP \n'].values
        table_low_yesterday = data_extract_yesterday['LOW \n'].values

        #extracting chartdata
        data_extract_chart = pd.read_csv("media/chart/chart_data.csv",
                                             names=['SYMBOL', 'zerodha','marketmojo','etnow'])
        data_extract_chat = data_extract_chart.drop([0], axis=0)
        table_chart_link = data_extract_chat.sort_values('SYMBOL', ascending=True)
        table_chart_zerodha = table_chart_link['zerodha'].values
        table_chart_marketmojo = table_chart_link['marketmojo'].values
        table_chart_etnow = table_chart_link['etnow'].values

        saved_data = []
        difference = table_Symbole_yesterday
        for data in range(len(difference)):
            low = float(table_low_yesterday[data].replace(',', ''))
            open = float(table_today_open[data].replace(',', ''))
            diff = ((low-open)/low) * 100
            saved_data.append(diff)



        # deleting the past data
        # delete_symbole = table_Symbole_yesterday
        # for data in delete_symbole:
        #     Gap_down.objects.filter(gap_down_yesterday_symbol=data).delete()

        #newmethod
        datatadelet = Gap_down.objects.all().delete()

        for data in range(len(table_Symbole_yesterday)):

            table_symbole_gap_down = Gap_down()
            table_symbole_gap_down.gap_down_current_price= float(table_ltp_today[data].replace(',', ''))
            table_symbole_gap_down.gap_down_open = float(table_today_open[data].replace(',', ''))
            table_symbole_gap_down.gap_down_percentage = int(saved_data[data])
            table_symbole_gap_down.gap_down_yesterday_low = float(table_low_yesterday[data].replace(',', ''))
            table_symbole_gap_down.gap_down_yesterday_symbol = table_Symbole_yesterday[data]
            table_symbole_gap_down.gap_down_today_symbol = table_Symbole_today[data]
            table_symbole_gap_down.gap_down_chat1_zerodha = table_chart_zerodha[data]
            table_symbole_gap_down.gap_down_chat_marketmojo = table_chart_marketmojo[data]
            table_symbole_gap_down.gap_down_chat_economictimes = table_chart_etnow[data]
            table_symbole_gap_down.save()
        return True
    except:
        return False


data_save_model_gap_down()
