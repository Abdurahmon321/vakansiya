from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import UserLoginForm, UserSignupForm, UserProfileForm, VakansiyaForm, CommentForm
from .models import UserProfile, Vakansiya


# Create your views here.


def index(request):
    vakansiya = Vakansiya.objects.all()
    return render(request, "index.html", {"vakansiya": vakansiya})


def user_login(request):
    print("salom")
    if request.method == 'POST':
        print("psot ishladi")
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            print("form is valid ishladi")
            return redirect('index')

    return render(request, 'login.html')


def singup(request):
    if request.method == "POST":
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = UserSignupForm()

    context = {
        'form': form,
        "title": "Sign up"
    }
    return render(request, "singup.html", context)


def user_logout(request):
    logout(request)
    return redirect("login")


def user_profile(request, id):
    vakansiya = Vakansiya.objects.filter(author_id=id)
    try:
        user = User.objects.get(pk=id)
        user_profile = UserProfile.objects.get(user_id=user.id)
        context = {
            "vakansiya": vakansiya,
            "user": user,
            "user_profile": user_profile,
            "title": f"{user.username} profili "
        }
    except UserProfile.DoesNotExist:
        # UserProfile topilmaganida, bo'sh obyekt yaratamiz
        user_profile = UserProfile.objects.create(user=user)
        context = {
            "vakansiya": vakansiya,
            "user": user,
            "user_profile": user_profile,
            "title": f"{user.username} profili "
        }
    return render(request, "user_profile.html", context)


def user_profile_edit(request, id):
    if request.user.id == id:
        if request.user:
            try:
                user_profile = UserProfile.objects.get(user=request.user)
            except UserProfile.DoesNotExist:
                user_profile = None

            if request.method == "POST":
                form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
                if form.is_valid():
                    user_profile = form.save(commit=False)
                    user_profile.user = request.user
                    user_profile.save()
                    return redirect("index")

            else:
                form = UserProfileForm(instance=user_profile)

            return render(request, "user_profile_form.html", {"form": form})
        else:
            return HttpResponse("page not found")
    else:
        return HttpResponse("hato")


def user_profile_create(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = UserProfileForm(request.POST, request.FILES)
            if form.is_valid():
                user_profile = form.save(commit=False)
                user_profile.user = request.user
                user_profile.save()
                return redirect("index")
        else:
            form = UserProfileForm()

        return render(request, "user_profile_form.html", {"form": form})
    else:
        return HttpResponse("hato")

def vakansiya_detail(request, id):
    vakansiya = Vakansiya.objects.get(pk=id)

    return render(request, "vakansiya_detail.html", {"vakansiya": vakansiya})


def create_vakansiya(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = VakansiyaForm(request.POST, request.FILES)

            if form.is_valid():
                vakansiya = form.save(commit=False)
                vakansiya.author = request.user
                vakansiya.save()
                return redirect("vakansiya_list")

        else:
            form = VakansiyaForm()
        return render(request, "vakansiya_form.html", {"form": form})
    else:
        return HttpResponse("hato")


def update_vakansiya(request, id):
    vakansiya = Vakansiya.objects.get(pk=id)
    if request.user.id == vakansiya.author.id:
        if request.method == "POST":
            form = VakansiyaForm(request.POST, request.FILES, instance=vakansiya)
            if form.is_valid():
                form.save()
                return redirect("vakansiya_list")

        else:
            form = VakansiyaForm(instance=vakansiya)
        return render(request, "vakansiya_form.html", {"form": form})
    else:
        return HttpResponse("Hato")


def vakansiya_delete(request, id):
    vakansiya = Vakansiya.objects.get(pk=id)
    if request.user.id == vakansiya.aythor.id:
        if request.method == "POST":
            vakansiya.delete()
            return redirect("vakansiya_list")

        return render(request, "delete_vakansiya.html", {"vakansiya": vakansiya})
    else:
        return HttpResponse("hato")


def vakansiya_list(request):
    vakansiya = Vakansiya.objects.all()
    return render(request, "vakansiya_list.html", {"vakansiya": vakansiya})


