from django.urls import re_path, path

from . import views

urlpatterns = [
    path("",views.index ,name="index"),
    path("incomeadd",views.income_form_view, name="form"),
    path("expenseadd",views.expense_form_view , name="form"),
    path("transferamount",views.transfer_amount_form_view , name="form"),
    path("budgetadd",views.budget_form_view , name="form"),
    path("goaladd",views.goal_form_view , name="form"),
    path("dailyadd",views.daily_add_form_view, name ="form"),
    path("about",views.about ,name='about'),
    path('contact',views.contact,name='contact'),
    path('services',views.services,name='services'),
    path('team',views.team,name='team'),
    path('succes',views.succes, name='succes'),
    path('calculator', views.calculator, name='calculator'),
]