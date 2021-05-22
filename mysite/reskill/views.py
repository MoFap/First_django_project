from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def reskill_data(request):
    data = {
        "name" : "Morenike Fapojuwo",

        "Track" : "Backend(Python)",

        "Message" : "Commendable Program"

    }

    return JsonResponse(data)
