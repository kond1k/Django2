from django.urls import path
from . import views


urlpatterns = [
    path("", views.HomeView.as_view()),
    path("<slug:post_name>/", views.PostView.as_view(), name="post"),
    path("<slug:category_name>/", views.CategoryView.as_view(), name="category")
]
