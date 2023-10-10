from django.shortcuts import render
from myapp.models import Contact
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def contact_us(request):
    context = {}
    if request.method == "POST":
        name = request.POST.get("name")
        em = request.POST.get("email")
        sub = request.POST.get("subject")
        msz = request.POST.get("message")

        newMessage = Contact(
            name=name,
            email=em,
            subject=sub,
            message=msz,
        )
        newMessage.save()
        context['message'] = f"Dear {name}, Thanks for your message!"

    return render(request, 'contact.html', context)


def about(request):
    return render(request, 'about.html')


def team(request):
    return render(request, 'team.html')


def all_dishes(request):
    return render(request, 'contact.html')
