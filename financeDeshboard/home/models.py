from django.db import models

# Create your models here.
class Income_add_model(models.Model):
    amount  = models.FloatField(max_length=100)
    account = models.CharField(max_length=100)
    catagory= models.CharField(max_length=100)

class Expanse_add_model(models.Model):
    amount  = models.FloatField(max_length=100)
    account = models.CharField(max_length=100)
    catagory= models.CharField(max_length=100)

class Transfer_amount_model(models.Model):
    amount  = models.FloatField(max_length=100)
    from_ac = models.CharField(max_length=100)
    to_ac   = models.CharField(max_length=100)


# class Transfer_amount_model(models.Model):
#     amount  = models.FloatField(max_length=100)
#     from_ac = models.CharField(max_length=100)
#     to_ac   = models.CharField(max_length=100)

class Budget_create_model(models.Model):
    budget_name = models.CharField(max_length=100)
    period      = models.CharField(max_length=100)
    amount      = models.FloatField(max_length=100)
    catagery    = models.CharField(max_length=100)
    account     = models.CharField(max_length=100)
    label       = models.CharField(max_length=100)


class Goal_create_model(models.Model):
    goal_name     = models.CharField(max_length=100)
    target_amount = models.FloatField(max_length=100)
    saved_already = models.FloatField(max_length=100)
    desired_date  = models.DateField()
    notes         = models.TextField()

from django.utils import timezone
TYPE_CHOICES =(
    ("income",'INCOME'),
    ("expense", 'EXPENSE'),
)
class Daily_add_model(models.Model):
    type_choose   = models.CharField(max_length=20 ,choices=TYPE_CHOICES,default='cash')
    component     = models.CharField(max_length=100)
    amount        = models.FloatField(max_length=100)
    date          = models.DateField(default=timezone.now)



class Daily_add_model_demo(models.Model):
    type_choose   = models.CharField(max_length=20 ,choices=TYPE_CHOICES,default='cash')
    component     = models.CharField(max_length=100)
    amount        = models.FloatField(max_length=100)
    date          = models.DateField(default=timezone.now)