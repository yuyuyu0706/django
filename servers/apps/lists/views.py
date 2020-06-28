from django.shortcuts import render
from django.views.generic import ListView
from .models import Member

class NWListView(ListView):

    model = Member
