from __future__ import unicode_literals
from django.db.models import Count
from django.contrib import messages
from apps.my_app.models import *


def create_dojo(name, city, state):
    dojos=Dojo.objects.create(name=name, city=city, state=state)
    print dojos
    return dojos
# 
def create_ninja(first_name, last_name, dojo):
    ninjas=Ninjas.objects.create(first_name=first_name, last_name=last_name, dojo=dojo)    
    print ninjas 
    return ninjas
    
def creates_both(name, city, state, first_name, last_name):
    dojos=Dojo.objects.create(name=name, city=city, state=state)
    ninjas=Ninjas.objects.create(first_name=first_name, last_name=last_name, dojo=dojos)
    
def get_dojos(id):
    dojo= Dojo.objects.get(id=id)
    return dojo
# ourdojo= get_dojos(3)
# print ourdojo.id

def get_ninjas(id):
    ninjas=Ninjas.objects.get(id=id)
    return ninjas
# myninjas = get_ninjas(2)
# print myninjas.id

def display_ninjas():
    first_dojo = Dojo.objects.first()
    ninjas = Ninjas.objects.filter(dojo=first_dojo)
    for ninja in ninjas:
        print ninja.first_name, ninja.last_name

def display_dojos():
    print Ninjas.objects.first().dojo.name


def delete_dojo(user_id):
    ourdojo=Dojo.objects.get(id=id)
    ourdojo.delete()

def delete_ninja(user_id):
    ourninja=Ninjas.objects.get(id=id)
    ourninja.delete()


