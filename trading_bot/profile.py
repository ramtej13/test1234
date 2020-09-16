from kiteconnect import KiteConnect
from kiteconnect import KiteTicker

# from .models import Apikeys

api_data_data_base = Apikeys.objects.all()

api_key = ([p.api_key for p in api_data_data_base][-1])
api_secret = ([p.api_secret for p in api_data_data_base][-1])
access_token = ([p.access_token for p in api_data_data_base][-1])



kite = KiteConnect(api_key=api_key)
kite.set_access_token(access_token)
kws = KiteTicker(api_key,access_token)

def profile_details():
    profile_det = kite.profile()
    return profile_det


