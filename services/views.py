from django.shortcuts import render, redirect
from urllib.parse import quote

def handle(request):
    return render(request, 'handle.html')

def play(request):
    return render(request, 'play.html')

def music(request):
    return render(request, 'music.html')

def social(request):
    return render(request, 'Social.html')

def online(request):
    return render(request, 'online.html')

def art(request):
    return render(request, 'art.html')

def emdr(request):
    return render(request, 'emdr.html')

def cbt(request):
    return render(request,'cbt.html')

def contact(request):
    return render(request,'contact.html')

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

