import pandas as pd
import io
import requests
import time


#from .models import Table_content


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

def data_save_model():
    # saving the current data file
    file_name_today = str(time.time())
    get_data_for_today = requests.get(
        'https://www.nseindia.com/api/equity-stockIndices?csv=true&index=SECURITIES%20IN%20F%26O',
        headers=headers).content[3:]
    df_today = pd.read_csv(io.StringIO(get_data_for_today.decode('utf-8')))
    data_from_web_today = df_today.to_csv(file_name_today+'.csv', index=False, encoding='utf-8')

    # sorting today data
    data_extract_today = pd.read_csv(file_name_today + ".csv",
                                     names=['SYMBOL', 'OPEN', 'HIGH', 'LOW', 'PREV.CLOSE', 'LTP', 'CHNG', '%CHNG',
                                            'VOLUME(shares)', 'VALUE', '52WH', '52WL'])
    data_extract_today = data_extract_today.drop(
        ['PREV.CLOSE', 'CHNG', 'VALUE', '52WH', '52WL'], axis=1)
    data_extract_today = data_extract_today.drop([0], axis=0)
    data_extract_today = data_extract_today.sort_values('SYMBOL', ascending=True)
    print(data_extract_today.head())



data_save_model()























#     #saving the current data file
#     # file_name_today = str(time.time())
#     # # print(file_name_today)
#     # get_data_for_today =requests.get('https://www.nseindia.com/api/equity-stockIndices?csv=true&index=SECURITIES%20IN%20F%26O',headers = headers).content[3:]
#     # df_today = pd.read_csv(io.StringIO(get_data_for_today.decode('utf-8')))
#     # data_from_web_today = df_today.to_csv('media/today/' + file_name_today + '.csv', index=False, encoding='utf-8')
#
#     #sorting today data
#     data_extract_today = pd.read_csv("products.csv",names=['SYMBOL', 'OPEN', 'HIGH', 'LOW', 'PREV.CLOSE', 'LTP', 'CHNG', '%CHNG','VOLUME(shares)', 'VALUE', '52WH', '52WL'])
#     data_extract_today = data_extract_today.drop(['HIGH', 'LOW', 'PREV.CLOSE', 'CHNG', '%CHNG','VOLUME(shares)', 'VALUE', '52WH', '52WL'], axis=1)
#     data_extract_today = data_extract_today.drop([0], axis=0)
#     data_extract_today= data_extract_today.sort_values('SYMBOL', ascending=True)
#
#     #extracting yesterday data
#     table_Symbole_today = data_extract_today["SYMBOL"].values
#     table_Price_today = data_extract_today['LTP'].values
#     table_today_open = data_extract_today['OPEN'].values
#
#
#     print(table_Price_today,table_Symbole_today,table_today_open)
#
#     #saving the yesterday data file
#     # file_name_yesterday = str(date.today())
#     # # print(file_name_yesterday)
#     # get_data_for_yesterday = requests.get('https://www.nseindia.com/api/equity-stockIndices?csv=true&index=SECURITIES%20IN%20F%26O',headers = headers).content[3:]
#     # df = pd.read_csv(io.StringIO(get_data_for_yesterday.decode('utf-8')))
#     # data_from_web_yesterday = df.to_csv('media/yesterday/'+file_name_yesterday+'.csv', index=False, encoding='utf-8')
#
#     #sorting yesterday data
#     data_extract_yesterday = pd.read_csv("products.csv", names = ['SYMBOL','OPEN','HIGH','LOW','PREV.CLOSE','CLOSE','CHNG','%CHNG','VOLUME(shares)','VALUE','52WH','52WL'])
#     data_extract_yesterday = data_extract_yesterday.drop(['HIGH','LOW','PREV.CLOSE','CHNG','OPEN','VOLUME(shares)','VALUE','52WH','52WL'] ,axis=1)
#     data_extract_yesterday = data_extract_yesterday.drop([0], axis=0)
#     data_extract_yesterday = data_extract_yesterday.sort_values('SYMBOL',ascending=True)
#
#     #extracting yesterday data
#     table_Symbole_yesterday = data_extract_yesterday["SYMBOL"].values
#     table_close_yesterday = data_extract_yesterday['CLOSE'].values
#     table_change_yesterday = data_extract_yesterday['%CHNG'].values
#
#     print(table_Symbole_yesterday,table_change_yesterday,table_close_yesterday)
#     #deleting the past data
#     # delete_symbole = table_Symbole_yesterday
#     # for data in delete_symbole:
#     #     Table_content.objects.filter(table_Symbole=data).delete()
#
#     #saving the new data
#     # for data in range(len(table_Symbole_yesterday)):
#     #
#     #     table_symbole2 = Table_content()
#     #     table_symbole2.table_Symbole= table_Symbole_yesterday[data]
#     #     print("table:",table_Symbole_yesterday)
#     #     price = table_Price_today[data]
#     #     price(price)
#     #     table_symbole2.table_Price = float(table_Price_today[data].replace(',', ''))
#     #     table_symbole2.table_Yesterday_close = float(table_close_yesterday[data].replace(',', ''))
#     #     table_symbole2.table_Yesterday_ralley_percentage = float(table_change_yesterday[data].replace(',', ''))
#     #     table_symbole2.table_today_open= float(table_today_open[data].replace(',', ''))
#     #     table_symbole2.table_extra = table_Symbole_today[data]
#     #     table_symbole2.save()
#
#     # print(print(table_close_yesterday,table_Symbole_yesterday,table_change_yesterday))
#
# data_save_model()
#






















# def data_save():

    # table_content = Table_content()
    # table_Symbole = s["SYMBOL"].values
    # table_Price = s["CLOSE"].values
    # table_Yesterday_close = s["CLOSE_YESTERDAY"].values
    # table_Yesterday_ralley_percentage = s["%CHNG"].values
    # table_today_open = s["CLOSE"].values
    # table_extra = "buy/sell"
    # b = s["SYMBOL"].iloc[0]
    # print(b)
    # a = -1
    # z = a
    # for data in table_Symbole:
    #     if data == "ZEEL":
    #         break
    #     a = a+1
    #     table_content= table_Symbole[a]
    #     print(table_content)
        # table_content.table_Price = s["CLOSE"].iloc[a]
        # table_content.table_Yesterday_close = s["CLOSE_YESTERDAY"].iloc[a]
        # table_content.table_Yesterday_ralley_percentage = s["%CHNG"].iloc[a]
        # table_content.table_today_open = s["CLOSE"].iloc[a]
        # table_content.table_extra = "buy/sell"
        # table_content.save()

    # return

    # print(table_Price,table_Yesterday_close,table_Yesterday_ralley_percentage,table_today_open,table_extra,table_Symbole)



# data_save_model()











    # return data1

# data_save_model()

# s = pd.read_csv("products.csv",
#                 names=['number', 'SYMBOL', 'CLOSE', 'IEPPRICE', 'CHNG', '%CHNG', 'CLOSE_YESTERDAY', 'FINALQUANTITY',
#                        'VALUE', 'FFM CAP', 'NM 52W H', 'NM 52W L'])
# s = s.head()
# s = s.drop('FINALQUANTITY', axis=1)
# s = s.drop('number', axis=1)
# s = s.drop('IEPPRICE', axis=1)
# s = s.drop('CHNG', axis=1)
# s = s.drop('VALUE', axis=1)
# s = s.drop('FFM CAP', axis=1)
# s = s.drop('NM 52W H', axis=1)
# s = s.drop('NM 52W L', axis=1)
# s = s.head()
# print(s)






# def data_save_model():
#     get_data_from_pre_open_fo = requests.get('https://www.nseindia.com/api/market-data-pre-open?key=FO&csv=true',headers = headers).content[3:]
#     df = pd.read_csv(io.StringIO(get_data_from_pre_open_fo.decode('utf-8')))
#     data_from_web = df.to_csv('products.csv', index=False, encoding='utf-8')
#     s = pd.read_csv("products.csv",
#                     names=['SYMBOL', 'CLOSE', 'IEPPRICE', 'CHNG', '%CHNG', 'CLOSE_YESTERDAY', 'FINALQUANTITY',
#                            'VALUE', 'FFM CAP', 'NM 52W H', 'NM 52W L'])
#     s = s.drop(['FINALQUANTITY', 'IEPPRICE', 'CHNG', 'VALUE', 'FFM CAP', 'NM 52W H', 'NM 52W L'], axis=1)
#     s = s.drop([0], axis=0)
#     s = s.sort_values('SYMBOL', ascending=True)
#
#     table_Symbole = s["SYMBOL"].values
#     table_Symbole123 = table_Symbole
#     for data in table_Symbole:
#         Table_content.objects.filter(table_Symbole=data).delete()
#
#     table_Price = s["CLOSE"].values
#     table_Yesterday_close =s["CLOSE_YESTERDAY"].values
#     table_Yesterday_ralley_percentage =s["%CHNG"].values
#     table_today_open =s["CLOSE"].values
#
#
#     #a = 0
#     for data in range(len(table_Symbole123)):
#         # if data == 143:
#         #     break
#         table_symbole2 = Table_content()
#         table_symbole2.table_Symbole= table_Symbole[data]
#         table_symbole2.table_Price = table_Price[data]
#         table_symbole2.table_Yesterday_close = table_Yesterday_close[data]
#         table_symbole2.table_Yesterday_ralley_percentage = table_Yesterday_ralley_percentage[data]
#         table_symbole2.table_today_open= table_today_open[data]
#         table_symbole2.table_extra = data
#         table_symbole2.save()
