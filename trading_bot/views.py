from django.shortcuts import render,redirect
# Create your views here.
from django.contrib.auth.decorators import login_required
from .forms import Resume
# from .profile import profile_details
from .zerodha_login import get_login

# from .models import Apikeys

def index(request):
    return render(request, 'trading_bot/index.html')

@login_required(login_url='login')
def about(request):
    return render(request, 'trading_bot/about.html')

def resumadownload(request):
    if request.method == 'POST':
        form = Resume(request.POST)
        if form.is_valid():
            form.save()
        return redirect('thankyou')
    else:
        form = Resume()

    return render(request, 'trading_bot/resumadownload.html', {
        'form': form
    })

def thankyou(request,):
    return render(request, 'trading_bot/thankyou.html',)

@login_required(login_url='login')
def profile(request):
    # profile_de = profile_details()
    profile_data = {"username":"srilatha"}
    print(profile_data)
    return render(request, 'trading_bot/profile.html',{'profile_data':profile_data})

def stock_data(request):
    data={0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 11, 12: 12, 13: 13, 14: 14, 15: 15, 16: 16, 17: 17, 18: 18, 19: 19, 20: 20, 21: 21, 22: 22, 23: 23, 24: 24, 25: 25, 26: 26, 27: 27, 28: 28, 29: 29, 30: 30, 31: 31, 32: 32, 33: 33, 34: 34, 35: 35, 36: 36, 37: 37, 38: 38, 39: 39, 40: 40, 41: 41, 42: 42, 43: 43, 44: 44, 45: 45, 46: 46, 47: 47, 48: 48, 49: 49, 50: 50, 51: 51, 52: 52, 53: 53, 54: 54, 55: 55, 56: 56, 57: 57, 58: 58, 59: 59, 60: 60, 61: 61, 62: 62, 63: 63, 64: 64, 65: 65, 66: 66, 67: 67, 68: 68, 69: 69, 70: 70, 71: 71, 72: 72, 73: 73, 74: 74, 75: 75, 76: 76, 77: 77, 78: 78, 79: 79, 80: 80, 81: 81, 82: 82, 83: 83, 84: 84, 85: 85, 86: 86, 87: 87, 88: 88, 89: 89, 90: 90, 91: 91, 92: 92, 93: 93, 94: 94, 95: 95, 96: 96, 97: 97, 98: 98, 99: 99, 100: 100, 101: 101, 102: 102, 103: 103, 104: 104, 105: 105, 106: 106, 107: 107, 108: 108, 109: 109, 110: 110, 111: 111, 112: 112, 113: 113, 114: 114, 115: 115, 116: 116, 117: 117, 118: 118, 119: 119, 120: 120, 121: 121, 122: 122, 123: 123, 124: 124, 125: 125, 126: 126, 127: 127, 128: 128, 129: 129, 130: 130, 131: 131, 132: 132, 133: 133, 134: 134, 135: 135, 136: 136, 137: 137, 138: 138, 139: 139, 140: 140, 141: 141, 142: 142, 143: 143, 144: 144, 145: 145, 146: 146, 147: 147, 148: 148, 149: 149, 150: 150, 151: 151, 152: 152, 153: 153, 154: 154, 155: 155, 156: 156, 157: 157, 158: 158, 159: 159, 160: 160, 161: 161}
    # data =  {0,1,2,3,4,5,6,7,8,9}

    return render(request, 'trading_bot/stock_data.html',{'data123':data})

def chart(request):
    return render(request, 'trading_bot/chart.html')

def accesstokenbot(request):
    return render(request, 'trading_bot/accesstokenbot.html')
    # if request.method == 'POST':
    #     contact_form_name = request.POST.get('contact_form_name')
    #     contact_form_email = request.POST.get('contact_form_email')









# def api_updater(request):
#     if request.method == 'POST':
#         form = Resume(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect('thankyou')
#     else:
#         form = Resume()
#
#     return render(request, 'trading_bot/resumadownload.html', {
#         'form': form
#     })
