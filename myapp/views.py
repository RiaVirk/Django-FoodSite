from django.shortcuts import render
from myapp.models import Contact, Dish, Team, Category, Profile
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User


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


def team_members(request):
    context = {}
    members = Team.objects.all().order_by('name')
    context['team_members'] = members
    return render(request, 'team.html', context)


def all_dishes(request):
    context = {}
    dishes = Dish.objects.all()
    if "q" in request.GET:
        id = request.GET.get("q")
        dishes = Dish.objects.filter(category__id=id)
        context['dish_category'] = Category.objects.get(id=id).name

    context['dishes'] = dishes
    return render(request, 'all_dishes.html', context)


def register(request):
    context = {}
    if request.method == "POST":
        # fetch data from html form
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        contact = request.POST.get('number')
        check = User.objects.filter(username=email)
        if len(check) == 0:
            # Save data to both tables
            usr = User.objects.create_user(email, email, password)
            usr.first_name = name
            usr.save()

            profile = Profile(user=usr, contact_number=contact)
            profile.save()
            context['status'] = f"User {name} Registered Successfully!"
        else:
            context['error'] = f"A User with this email already exists"

    return render(request, 'register.html', context)


def check_user_exists(request):
    email = request.GET.get('usern')
    check = User.objects.filter(username=email)
    if len(check) == 0:
        return JsonResponse({'status': 0, 'message': 'Not Exist'})
    else:
        return JsonResponse({'status': 1, 'message': 'A user with this email already exists!'})


def login(request):
    return render(request, 'login.html')


def logout(request):
    return render(request, 'logout.html')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
