from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse



monthly_challenge_name = {
    "january": "this is jan C",
    "february": "this is feb C",
    "march": "this is mar C",
    "april": "this is apr C",
    "may": "this is may C",
    "june": "this is jun C",
    "july": "this is jul C",
    "august": "this is aug C",
    "september": "this is sep C",
    "october": "this is oct C",
    "november": "this is nov C",
    "december": "this is dec C"
}
# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challenge_name.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenge_name.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenges_name = monthly_challenge_name[month]
        return HttpResponse(challenges_name)
    except:
        return HttpResponse("Invalid month")
    
