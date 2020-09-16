from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import json
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'chart/index.html', {})

# @login_required
def room(request, room_name):
    return render(request, 'chart/room.html', {
        'room_name': room_name,
        # 'room_name_json': mark_safe(json.dumps(room_name)),
        # 'username': mark_safe(json.dumps(request.user.username)),
    })

