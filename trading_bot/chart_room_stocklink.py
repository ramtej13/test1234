from django.contrib.auth.models import auth, User
from trading_bot import zerodha_login
from chart_room.chatbot_2 import chatbot_response
from chart_room.Youtube.main2 import youtubesearch
from googleapiclient.errors import HttpError

def finding(data):
    try:
        if data['message'][0:7] == 'zerodha':
            user_name_pulling = data['message'][8:int(data['message'].find('>',))]
            # user = User.objects.filter(username=user_name_pulling)
            print(user_name_pulling)
            try:
                if User.objects.filter(username=user_name_pulling).exists():
                    answerbot = zerodha_login.user(data['message'])
                    print(answerbot)
                    return answerbot
                else:
                    answerbot = "usernotfound"
                    return answerbot
            except Exception as answerbot:
                return str(answerbot)

        elif data['message'][0:5] == 'stock':
            stockdata = zerodha_login.stockdata_chatbot(data['message'])#"stockdata"
            return stockdata

        elif data['message'][0:7] == 'youtube':
            try:
                if data['message'][8:16] == 'channels':
                    answerbot = youtubesearch(search=str(data['message'][17:]),searchresult=20)
                    return answerbot
                else:
                    answerbot = youtubesearch(search=str(data['message'][8:]),searchresult=10)
                    return answerbot
            except Exception as answerbot:
                return str(answerbot)

        else:
            print(int(data['message'].find('>',)))
            answerbot = chatbot_response(msg=str(data['message']))
            return answerbot

    except Exception as answerbot:
        return str(answerbot)