from django.shortcuts import render, redirect
from django.views.generic import View
# from .forms import AddDateForm, SearchDateForm
# from .models import UserProfile, Dates 

# Create your views here.
class Index(View):
    def get(self, request):
        # # this gets them all, eventually want to add hits and show the ones with the most hits
        # dates = Dates.objects.all().order_by('-created_at')
        # context = {
        #     'dates': dates, }
        return render(request, "index.html")
