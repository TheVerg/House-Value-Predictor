import os
import joblib
import numpy as np
from django.shortcuts import render
from .forms import PricePredictionForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.views.generic import  CreateView, ListView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm
from .models import House

def loginView(request):

    if request.user.is_authenticated:
        return redirect('base/home.html')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
                user = User.objects.get(username = username)
        except:
                messages.error(request, 'User does not exist')

                user = authenticate(request, username = username, password = password)

        else:
            messages.error(request, 'Username or Password does not exist')

            if user is not None:
                login(request, user)
                return redirect('home')
        
            else:
                messages.error(request, 'User does not exist')


    context = {}
    return render(request, 'base/login_registration.html',context)

def LogoutView(request):
    logout(request)
    return redirect('home')

def register_user(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        
        else:
            messages.error(request, 'An error occured during signup')

    return render(request, 'base/userReg.html' ,{'form':form})


def home(request): 
    return render(request, 'base/home.html')

def predict_price(request):
    if request.method == 'POST':
        form = PricePredictionForm(request.POST)
        if form.is_valid():
            # Load the trained linear regression model
            model_path = os.path.join(os.path.dirname(__file__), 'models', 'linear_regression_model.pkl')
            model = joblib.load(model_path)

            # Extract input data from the form
            area_sqm = form.cleaned_data['area_sqm']
            bedrooms = form.cleaned_data['bedrooms']
            location = form.cleaned_data['location']
            malls = form.cleaned_data['malls']
            new_data = np.array([area_sqm, bedrooms, location,malls]).reshape(1, -1)

            # Perform prediction
            predicted_price = model.predict(new_data)[0] *1000

            # Prepare the response
            context = {
                'form': form,
                'predicted_price': round(predicted_price, 2),
            }
            return render(request, 'base/prediction.html', context)
    else:
        form = PricePredictionForm()

    context = {'form': form}
    return render(request, 'base/prediction.html', context)


def houses(request):
    return render(request, 'base/houses.html')

def newsBlogs(request):
    return render(request, 'base/news.html')


class HouseCreateView(CreateView,ListView):
    model = House
    template_name = 'base/house.html'
    fields = ['title', 'date_posted', 'description', 'price']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)