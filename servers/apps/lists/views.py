from django.shortcuts import render
from django.views.generic import View
from django.views.generic import ListView
from lists.models import Member

class NWListView(ListView):

    model = Member

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'lists/index.html')
