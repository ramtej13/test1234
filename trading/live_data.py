import pandas as pd
import io
import requests
import time


from .models import Live_data


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

def data_save_model_live_data():
    try:
        x
        # saving the current data file
        file_name_today = str(time.time())
        get_data_for_today = requests.get('https://www.nseindia.com/api/equity-stockIndices?csv=true&index=SECURITIES%20IN%20F%26O',
            headers=headers).content[3:]
        df_today = pd.read_csv(io.StringIO(get_data_for_today.decode('utf-8')))
        data_from_web_today = df_today.to_csv("media/today/"+file_name_today+'.csv', index=False, encoding='utf-8')

        # sorting today data
        data_extract_today = pd.read_csv('media/today/' + file_name_today + '.csv')

        # colloum names ['SYMBOL \n', 'OPEN \n', 'HIGH \n', 'LOW \n', 'PREV. CLOSE \n', 'LTP \n',
        #        'CHNG \n', '%CHNG \n', 'VOLUME \n(shares)', 'VALUE ', '52W H \n',
        #        '52W L \n', '365 D % CHNG \n 03-May-2019',
        #        '30 D % CHNG \n 03-Apr-2020']
        # data_extract_today = data_extract_today.drop(
        #     ['PREV. CLOSE \n',
        #        'CHNG \n', 'VALUE ', '52W H \n',
        #        '52W L \n', '365 D % CHNG \n 03-May-2019',
        #        '30 D % CHNG \n 03-Apr-2020'], axis=1)

        # data_extract_today = data_extract_today.drop([0], axis=0)
        data_extract_today = data_extract_today.sort_values('SYMBOL \n', ascending=True)
        symbole = data_extract_today['SYMBOL \n'].values
        open = data_extract_today['OPEN \n'].values
        high = data_extract_today['HIGH \n'].values
        low = data_extract_today['LOW \n'].values
        ltp = data_extract_today['LTP \n'].values
        change = data_extract_today['%CHNG \n'].values
        volume = data_extract_today[ 'VOLUME \n(shares)'].values

        #extracting chartdata
        data_extract_chart = pd.read_csv("media/chart/chart_data.csv",
                                             names=['SYMBOL', 'zerodha','marketmojo','etnow'])
        data_extract_chat = data_extract_chart.drop([0], axis=0)
        table_chart_link = data_extract_chat.sort_values('SYMBOL', ascending=True)
        table_chart_zerodha = table_chart_link['zerodha'].values
        table_chart_marketmojo = table_chart_link['marketmojo'].values
        table_chart_etnow = table_chart_link['etnow'].values



        # delete_symbole = symbole
        # for data in delete_symbole:
        #     Live_data.objects.filter(live_data_symbole=data).delete()

        #new method
        datatadelet = Live_data.objects.all().delete()


        for data in range(len(symbole)):
            table_symbole2 = Live_data()
            table_symbole2.live_data_open = float(open[data].replace(',', ''))
            table_symbole2.live_data_percentage_change =change[data]
            table_symbole2.live_data_high = float(high[data].replace(',', ''))
            table_symbole2.live_data_low = float(low[data].replace(',', ''))
            table_symbole2.live_data_volume = float(volume[data])#.replace(',', ''))
            table_symbole2.live_data_symbole = symbole[data]
            table_symbole2.live_data_ltp = float(ltp[data].replace(',', ''))
            table_symbole2.live_data_chat_zerodha = table_chart_zerodha[data]
            table_symbole2.live_data_chat_marketmojo = table_chart_marketmojo[data]
            table_symbole2.live_data_chat_economictimes =table_chart_etnow[data]
            table_symbole2.save()
        return True

    except Exception as e:
        print(e)
        return False

data_save_model_live_data()


