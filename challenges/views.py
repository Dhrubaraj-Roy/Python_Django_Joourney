from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string



monthly_challenge_name = {
    "january": "This is January Challenge",
    "february": "This is February Challenge",
    "march": "This is March Challenge",
    "april": "This is April Challenge",
    "may": "This is May Challenge",
    "june": "This is June Challenge",
    "july": "This is July Challenge",
    "august": "This is August Challenge",
    "september": "This is September Challenge",
    "october": "This is October Challenge",
    "november": "This is November Challenge",
    "december": "This is December Challenge"
}
# Create your views here.

def index(request):
    months = list(monthly_challenge_name.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })

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
        return render(request, "challenges/challenges.html", {
            "text": challenges_name,
            "month_name": month
        })
    except:
        return HttpResponseNotFound("Invalid month")
