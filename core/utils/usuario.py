from core.models import MyUser
from django.http import HttpResponse
from datetime import date, datetime, timedelta
import json


def GetUsuario(id):
    usuario = MyUser.objects.filter(pk=id)
    if usuario:
        return usuario
    else:
        return False