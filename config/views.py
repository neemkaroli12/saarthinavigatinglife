from django.shortcuts import render
from services.models import Feedback


def home(request):

    reviews = Feedback.objects.filter(
        publish_permission=True
    ).exclude(
        review=""
    ).order_by("-created_at")

    return render(request, "home.html", {
        "reviews": reviews
    })