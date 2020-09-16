from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import time

#gapup
from .gap_up import data_save_model_gap_up
from .models import Gap_up

#redreeen
from.models import Red_green_red
from .red_green_red_str import data_save_model_red_green_red

#gapdown
from .models import Gap_down
from .gap_down import data_save_model_gap_down

#livedata
from .models import Live_data
from .live_data import data_save_model_live_data

#portfolio
from .models import Portfolio

#mainpage
from .models import Main_trading_base

#blogpost
from .models import Blog_post
#from .models import Blog_Post_steps
from .Historic_date import data_save_model_Historic_data
from .models import Historic_data


def trdaing_base(request):
    main_trading_base = Main_trading_base.objects.all()
    return render(request, 'trading/trading_base.html',{'data':main_trading_base,})


def portfolio(request):
    data_portfolio = Portfolio.objects.all()
    return render(request, 'trading/portfolio.html',{'data':data_portfolio})

from .gap_up import data_save_model_gap_up

@login_required(login_url='login')
def gap_up(request):
    def running():
        data_up = data_save_model_gap_up()
        if data_up == True:
            return "running"
        else:
            return "stopped"

    running_fun = running()
    data_gap_up = Gap_up.objects.all()
    return render(request,'trading/gap_up.html',{'data':data_gap_up, 'run_data':running_fun})

@login_required(login_url='login')
def gap_down(request):
    def running():
        data_down = data_save_model_gap_down()
        if data_down == True:
            return "running"
        else:
            return "stopped"

    running_fun = running()
    data_gap_down = Gap_down.objects.all()
    return render(request,'trading/gap_down.html',{'data':data_gap_down, 'run_data':running_fun})


@login_required(login_url='login')
def red_green_red(request):
    def running():
        data_rgr = data_save_model_red_green_red()
        if data_rgr == True:
            return "running"
        else:
            return "stopped"

    running_fun = running()
    data_r_g_r = Red_green_red.objects.all()
    return render(request,'trading/red_green_red.html',{'data':data_r_g_r,'run_data':running_fun})

def live_data(request):
    def running():
        data_live_data = data_save_model_live_data()
        if data_live_data == True:
            return "running"
        else:
            return "stopped"

    running_fun = running()
    print(running_fun)
    data_l_d = Live_data.objects.all()
    return render(request,'trading/live_data.html' , {'data':data_l_d, 'run_data':running_fun})


def register(request):
    if request.method == 'POST':
        register_user_name = request.POST['register_user_name']
        register_password = request.POST['register_password']
        register_confirm_password = request.POST['register_confirm_password']
        register_email = request.POST['register_email']

        if register_password == register_confirm_password:
            if User.objects.filter(username=register_user_name).exists():
                messages.info(request,'Username taken')
                return redirect('register')
            elif User.objects.filter(email=register_email).exists():
                messages.info(request,'email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=register_user_name, password=register_password, email=register_email)
                user.save()
                print("user created",user)
                return redirect('login')
        else:
            messages.info(request,'Password does not match')
            return redirect('register')
    else:
        return render(request,'trading/register.html')



def login(request):
    if request.method == 'POST':
        login_user_name = request.POST['login_user_name']
        login_passwordz = request.POST['login_password']

        user = auth.authenticate(username=login_user_name,password=login_passwordz)

        if user is not None:
            auth.login(request,user)
            print(user)
            return redirect("trading_base")

        else:
            messages.info(request, "invalid Credentials ")
            return redirect('login')

    else:
        return render(request,'trading/login.html')


def logout(request):
    auth.logout(request)
    return redirect("trading_base")


def blog(request):
    post_blog = Blog_post.objects.all()#[:10]
    return render(request,'trading/blog.html',{'content':post_blog})


def blog_post(request,id):
    post_blog_post = Blog_post.objects.get(id=id)
    context = {
        'post':post_blog_post,
    }
    return render(request, 'trading/blog_post.html', context)



histdata_value = []
def historic_data(request):
    if request.method == 'POST':
        date_from_user = str(request.POST['hist_login_user_name'])
        import os
        file_location = os.listdir("/Users/apple/Desktop/coding/python/web_downloaded_temp/media/yesterday")
        def date_finder(file_location):
            for i in file_location:
                c = i.replace(".csv","")
                a = c.find(date_from_user)
                if date_from_user == c:
                    return a
        c = date_finder(file_location=file_location)
        if c == 0:
            data_live_data = data_save_model_Historic_data(file_name_id=date_from_user)
            histdata_value.clear()
            histdata_value.append(data_live_data)
            return redirect('historic_data_view')
        else:
            messages.info(request, "Date not found please check the criteria")
            return redirect('historic_data')
    else:
        return render(request, 'trading/historic_data.html',)



def historic_data_view(request):
    def running():
        if histdata_value == [True]:
            return "running"
        else:
            return "stopped"

    running_fun = running()
    hist_data = Historic_data.objects.all()
    return render(request, 'trading/hist_data.html', {'run_data':running_fun,'hist_data':hist_data})

































######extra code#########
# def historic_data_view(request):
    # start_time = time.time()
    # seconds = 4
    #
    # while True:
    #     current_time = time.time()
    #     elapsed_time = current_time - start_time
    #
    #     if elapsed_time > seconds:
    #         print("Finished iterating in: " + str(int(elapsed_time)) + " seconds")
    #         break
    # def running():
    #     # print("file:",file_name_id)
    #     datavalue = "2020-05-03"
    #     # print(datavalue)
    #     data_live_data = data_save_model_Historic_data(file_name_id=datavalue)
    #     if data_live_data == True:
    #         return "running"
    #     else:
    #         return "stopped"
    # running_fun = running()