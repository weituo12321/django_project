from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("You can you up, no can no bb!")


def encode(request):
    # get long url from request.POST

    # convert to short url

    # create object in database

    return HttpResponse(short_url)


def decode(request, short_url):
    # get long url from db

    # if it does not exist, return error info
    return HttpResponse("error")

    # redirect to long url
    return HttpResponseRedirect(long_url)
