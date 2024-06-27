from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import (
    MyForm,
    LoginForm,
    FertilizerRecommenderForm,
    CropRecommenderForm,
    CropYieldPredictionForm,
)
from django.contrib.auth import login


def home(request):
    return render(request, "mysite/home.html")


def about(request):
    return render(request, "mysite/about.html")


def yieldpred(request):
    if request.method == "POST":
        form = CropYieldPredictionForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            # Here you would typically call your prediction model
            # For now, we'll just redirect to a success page
            return render(request, "mysite/yieldpred.html", {"form": form})
    else:
        form = CropYieldPredictionForm()

    return render(request, "mysite/yieldpred.html", {"form": form})


def fertpred(request):
    if request.method == "POST":
        form = FertilizerRecommenderForm(request.POST)
        if form.is_valid():

            return render(request, "mysite/fertpred.html", {"form": form})
    else:
        form = FertilizerRecommenderForm()

    return render(request, "mysite/fertpred.html", {"form": form})


def cropreco(request):
    if request.method == "POST":
        form = CropRecommenderForm(request.POST)
        if form.is_valid():
            # Process the form data here
            # You can access form data using form.cleaned_data
            # Perform your crop recommendation logic
            # For now, we'll just render the same page
            return render(request, "mysite/cropreco.html", {"form": form})
    else:
        form = CropRecommenderForm()

    return render(request, "mysite/cropreco.html", {"form": form})


def test(request):
    form = MyForm()
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            pass
    return render(request, "mysite/test.html", context={"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")  # Redirect to home page after login
    else:
        form = LoginForm()
    return render(request, "mysite/login.html", {"form": form})
