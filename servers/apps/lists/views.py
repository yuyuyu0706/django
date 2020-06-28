from django.shortcuts import render
from django.views.generic import ListView
from lists.models import Member

class NWListView(ListView):

    model = Member
