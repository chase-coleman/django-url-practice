from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
  return HttpResponse("<h1>Hello Home</h1>")

def rectangle_area(request, width, length):
  return HttpResponse(width * length)

def rectangle_perimeter(request, width, length):
  return HttpResponse((width * 2) + (length * 2))

def circle_area(request, radius):
  return HttpResponse(3.14 * (radius ** 2))

def circle_perimeter(request, radius):
  return HttpResponse(2 * (3.14 * radius))

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('rectangle/area/<int:width>/<int:length>', rectangle_area),
    path('rectangle/perimeter/<int:width>/<int:length>', rectangle_perimeter),
    path('circle/area/<int:radius>', circle_area),
    path('circle/perimeter/<int:radius>', circle_perimeter),
]