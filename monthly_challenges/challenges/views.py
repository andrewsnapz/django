from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.


def monthly_challenge(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "Don't eat meat for the entire month"
    elif month == "february":
        challenge_text = "Walk for twenty minutes every day"
    elif month == "march":
        challenge_text = "Learn Django for 20 minutes everyday"
    else:
        return HttpResponseNotFound("This month is not supported!")

    return HttpResponse(challenge_text)