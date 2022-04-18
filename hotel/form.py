from dataclasses import fields
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User


class RoomForm(ModelForm):
    class Meta:
        model = room
        fields = '__all__'
        