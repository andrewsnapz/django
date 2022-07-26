from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
# from django.template.loader import render_to_string

monthly_challenges = {
    "january": "Don't eat meat for the entire month",
    "february": "Walk for twenty minutes every day",
    "march": "Learn Django for 20 minutes everyday",
    "april": "Don't eat meat for the entire month",
    "may": "Walk for twenty minutes every day",
    "june": "June Goal",
    "july": "Don't eat meat for the entire month",
    "august":  "Walk for twenty minutes every day",
    "september": "Walk for twenty minutes every day",
    "october": "Don't eat meat for the entire month",
    "november": "Walk for twenty minutes every day",
    "december": None,
}

# Create your views here.


def index(request):
    # list_items = ""
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })

    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])

    #     list_items += f"<li><a href='{month_path}'>{capitalized_month}</a></li>"

    # return HttpResponse(list_items)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])

    # return HttpResponseRedirect("/challenges/" + redirect_month)
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        # only for successful renders:
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month
        })
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except:
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)
        raise Http404()
