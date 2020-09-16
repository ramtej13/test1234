from kiteconnect import KiteConnect
from kiteconnect import KiteTicker
from django.contrib.auth.models import auth, User
from django.contrib.auth import get_user_model
# from .models import Apikeys
from .models import User_stock_keys,UserProfile

def get_login(api_k):
    global kws,kite
    kite = KiteConnect(api_key=api_k)
    return kite.login_url()


def access(user_name):
    api_key ="hdtlbz2j74tym170"
    api_secret = "cdh6zl7tjiokssi1acwt46nft3z6nxx1"
    request_token_here = user_name
    kite = KiteConnect(api_key=api_key)
    data = kite.generate_session(request_token_here, api_secret=api_secret)
    kite.set_access_token(data["access_token"])
    return data["access_token"]


def user(user_name):
    try:
        user_name = str(user_name)
        first = int(user_name.find('>',))

        if str(user_name[first+1:first+7]) == "access":
            a = access(user_name[first+8:])
            return a

        elif str(user_name[first+1:]) == "login":
            user_name_pulling = user_name[8:int(user_name.find('>',))]
            # api_key1 = User_stock_keys.objects.all(user_name=user_name_pulling)
            # print(api_key1)
            api_key = 'hdtlbz2j74tym170'
            a = get_login(api_k=api_key)
            return a

        elif str(user_name[first+1:first+11]) == "saveaccess":
            user_name_pulling = user_name[8:int(user_name.find('>',))]
            # UserProfile.a_key = user_name_pulling
            # UserProfile.save(a)

            # if User.objects.get_by_natural_key(username=user_name_pulling):
            #     print(User_stock_keys.user())
            a = "sorry"
            return a

            # User_stock_keys.save()
        else:
            answerbot = "command not found"
            return answerbot

    except Exception as answerbot:
        return str(answerbot)



def tickkkkk(api_key,access_token):
    kite = KiteConnect(api_key=api_key)
    kite.set_access_token(access_token)
    kws = KiteTicker(api_key,access_token)

    inst_token = [5633]
    def on_ticks(ws, ticks):
        for ticks in ticks:
            price = ticks['last_price']
            return price

    def on_connect(ws, response):
        ws.subscribe(inst_token)
        ws.set_mode(ws.MODE_QUOTE, inst_token)

    kws.on_ticks = on_ticks
    kws.on_connect = on_connect
    kws.connect()



def stockdata_chatbot(user_name):
    try:
        user_name = str(user_name)
        first = int(user_name.find('>',))
        print(int(user_name[first+1:]))
        if int(user_name[first+1:]) == 5633:
            stockprice = tickkkkk(api_key='hdtlbz2j74tym170',access_token='KRJuUytyUL1c9CKo5CyanvIEEl3aWLNi')
            return stockprice
        else:
            return "give a proper sockname"

    except Exception as answerbot:
        return answerbot





