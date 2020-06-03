from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View

from .models import Category


def home(request):
    return HttpResponse("hi")


class HomeView(View):
    def get(self, request):
        category_list = Category.objects.all()
        context = {"categories": category_list}
        return render(request, "blog/home.html", context)

    def post(self, request):
        pass


class CategoryView(View):
    """Вывод статей категории"""

    def get(self, request, category_name):
        category = Category.objects.get(slug=category_name)
        return render(request, "blog/post_list.html", {"category": category})
