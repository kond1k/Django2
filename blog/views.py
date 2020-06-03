from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View


def home(request):
    return HttpResponse("hi")


class HomeView(View):
    def get(self, request):
        return HttpResponse("Good")

    def post(self, request):
        pass
