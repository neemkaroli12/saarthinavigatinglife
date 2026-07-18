from django.shortcuts import render, redirect
from urllib.parse import quote
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from .models import Feedback

def handle(request):
    return render(request, 'handle.html')

def play(request):
    return render(request, 'play.html')

def music(request):
    return render(request, 'music.html')

def social(request):

    if request.method == "POST":

        services = request.POST.getlist("services")
        liked = request.POST.getlist("liked")

        Feedback.objects.create(
            full_name=request.POST.get("full_name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),

            services=", ".join(services),
            other_service=request.POST.get("other_service", ""),

            satisfaction=request.POST.get("satisfaction", ""),

            liked=", ".join(liked),
            other_liked=request.POST.get("other_liked", ""),

            heard=request.POST.get("heard", ""),
            wellbeing=request.POST.get("wellbeing", ""),
            recommend=request.POST.get("recommend", ""),

            review=request.POST.get("review"),
            suggestions=request.POST.get("suggestions", ""),

            publish_permission=(
                request.POST.get("publish_permission") == "yes"
            ),

            anonymous=(
                request.POST.get("anonymous") == "yes"
            ),
        )

        return redirect("home")

    return render(request, "feedback.html")
def online(request):
    return render(request, 'online.html')

def art(request):
    return render(request, 'art.html')

def emdr(request):
    return render(request, 'emdr.html')

def cbt(request):
    return render(request,'cbt.html')

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            area = form.cleaned_data['area']
            message = form.cleaned_data['message']

            email_message = f"""
Name: {name}

Phone: {phone}

Email: {email}

Area: {area}

Message:
{message}
"""

            send_mail(
                subject=f"New Contact Form Submission - {name}",
                message=email_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['info@saarthinavigatinglife.com'],
                fail_silently=False,
            )

            return redirect('contact')

    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def about(request):
    return render(request,'about.html')


def explore(request):
    return render(request, 'explore.html')



def form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        date = request.POST.get("date")
        time = request.POST.get("time")
        session_type = request.POST.get("session_type")
        message = request.POST.get("message")

        whatsapp_message = f"""
 New Demo Session Booking

 Name: {name}
 Email: {email}
 Phone: {phone}

 Preferred Date: {date}
 Preferred Time: {time}

 Session Type: {session_type}

 Message:
{message}
"""

        whatsapp_number = "919116914358" 

        whatsapp_url = (
            f"https://wa.me/{whatsapp_number}?text={quote(whatsapp_message)}"
        )

        return redirect(whatsapp_url)

    return render(request, "form.html")

