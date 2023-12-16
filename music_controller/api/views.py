from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request) -> None:
    return HttpResponse("<h1>Hello<h1>")