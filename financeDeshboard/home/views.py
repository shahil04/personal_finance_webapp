from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse ,reverse_lazy


# Create your views here.
def index(request):
    return render(request ,"index.html")

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def  services(request):
    return render(request, 'services.html')

def team(request):
    return render(request,'team.html')

def succes(request):
    return render(request , 'succes.html')

def calculator(request):
    return render(request , 'calculation.html')

from .models import Income_add_model
from .forms import *

def income_form_view(request):
    if request.method == "POST":
        form = Income_add_form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Income_add_form()

    return render(request, 'income_add.html',{'form':form})

def expense_form_view(request):
    if request.method == "POST":
        form = Expense_add_form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Expense_add_form()

    return render(request, 'expnse_add.html',{'form':form})

def transfer_amount_form_view(request):
    if request.method == "POST":
        form = Transfer_amount_form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Transfer_amount_form()

    return render(request, 'transfer_amount_add.html',{'form':form})

def budget_form_view(request):
    if request.method == "POST":
        form = Budget_create_form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Budget_create_form()

    return render(request, 'budget_add.html',{'form':form})

def goal_form_view(request):
    if request.method == "POST":
        form = Goal_create_form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Goal_create_form()

    return render(request, 'goal_add.html',{'form':form})

@login_required(login_url="/login/")
def daily_add_form_view(request):
    if request.method == "POST":
        form = Daily_add_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('succes')
    else:
        form = Daily_add_form()

    return render(request, 'daily_add.html',{'form':form})