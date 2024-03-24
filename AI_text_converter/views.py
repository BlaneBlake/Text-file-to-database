from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def test(reqest):

    return HttpResponse("działam")
