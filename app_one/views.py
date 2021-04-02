from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt


def index(request):
    return render(request, 'home.html')


def regis(request):
    errors = User.objects.emailValidator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/register_page')
    else:
        pw_hash = bcrypt.hashpw(
            request.POST['password'].encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=pw_hash
        )
        request.session['uuid'] = user.id
    return redirect('/character_selector')


def login(request):
    errors = User.objects.loginValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/login_page')
    else:
        user = User.objects.filter(email=request.POST['email'])
        request.session['uuid'] = user[0].id
        return redirect('/character_selector')


def logout(request):
    request.session.clear()
    return redirect('/')

def login_page(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def Skill_timer(request):
    pass


def galaxyhub(request):
    context = {
        'Character': Characters.objects.get(id=request.session['Character_ID']),
        'Planets': Planets.objects.filter(planet_region="Core Worlds"),
        'Race': Race.objects.all()
    }
    return render(request, 'galaxyhub.html', context)


def galaxyhub1(request):
    context = {
        'Character': Characters.objects.get(id=request.session['Character_ID']),
        'Planets': Planets.objects.filter(planet_region=request.POST['travel']),
        'Race': Race.objects.all()
    }
    return render(request,'galaxyhub.html',context)


def planet(request):
    context = {
        'Planets':Planets.objects.all()
    }
    return render(request,'temp_planet_create.html',context)

def planetcreate(request):
    Planets.objects.create(
        planet_name= request.POST['planet_name'],
        planet_type= request.POST['planet_type'],
        planet_desc= request.POST['planet_desc'],
        planet_region = request.POST['planet_region'],
    )
    return redirect('/planet')

def planetedit(request,planet_id):
    context = {
        'Planet':Planets.objects.get(id=planet_id)
    }
    return render(request, 'temp_editor.html',context)

def planetfinaledit(request,planet_id):
    planet = Planets.objects.get(id=planet_id)
    planet.planet_name = request.POST['planet_name']
    planet.planet_type = request.POST['planet_type']
    planet.planet_desc = request.POST['planet_desc']
    planet.save()
    return redirect('/planet')

def planetremove(request,planet_id):
    planet = Planets.objects.get(id=planet_id)
    planet.delete()
    return redirect('/planet')

def race(request):
    context = {
        'Races':Race.objects.all()
    }
    return render(request, 'temp_race_create.html',context)

def racecreate(request):
    Race.objects.create(
    name = request.POST['name'],
    strength = request.POST['strength'],
    hitpoints = request.POST['hitpoints'],
    agility = request.POST['agility'],
    endurance = request.POST['endurance'],
    intelligence = request.POST['intelligence'],
    defense = request.POST['defense'],
    credit = request.POST['credit'],
    descrip = request.POST['descrip'],
    )
    return redirect('/race')

def raceedit(request,race_id):
    context = {
        'Races':Race.objects.get(id=race_id)
    }
    return render(request, 'temp_editor.html',context)

def racefinaledit(request,race_id):
    race = Race.objects.get(id=race_id)
    race.name = request.POST['name']
    race.strength = request.POST['strength']
    race.hitpoints = request.POST['hitpoints']
    race.agility = request.POST['agility']
    race.endurance = request.POST['endurance']
    race.intelligence = request.POST['intelligence']
    race.defense = request.POST['defense']
    race.credit = request.POST['credits']
    race.descrip = request.POST['descrip']
    race.save()
    return redirect('/race')

def raceremove(request,race_id):
    race = Race.objects.get(id=race_id)
    race.delete()
    return redirect('/race')

def character_sheet(request):
    context = {
        'Character': Characters.objects.get(id=request.session['Character_ID']),
        'Race' : Race.objects.all()
    }
    return render(request,'Character_sheet.html',context)

def planet_sheet(request,planet_name):
    Planet = Planets.objects.filter(planet_name=planet_name)
    context = {
        'Planet': Planet[0],
        'Character': Characters.objects.get(id=request.session['Character_ID']),
    }
    return render(request,'planet_sheet.html',context)

def ship_sheet(request, ship_class):
    context = {
        'Ship' : Ship.objects.filter(ship_class=ship_class)
    }
    return render(request,'ship_sheet.html', context)

def character_selector(request):
    user = User.objects.get(id=request.session['uuid'])
    context = {
        'Characters': Characters.objects.filter(Char_User=request.session['uuid']),
        'selector' : len(Characters.objects.filter(Char_User=request.session['uuid'])),
        'Race' : Race.objects.all()
    }
    return render(request, 'Choose_character.html', context)

def character_creation(request):
    space_station = Planets.objects.get(id=3)
    Characters.objects.create(
        Char_First_Name= request.POST['first_name'],
        Char_Last_Name= request.POST['last_name'],
        Char_Race = Race.objects.get(id=request.POST['race']),
        Char_User = User.objects.get(id=request.session['uuid']),
        Char_Location = space_station
    )
    return redirect('/character_selector')

def Character_final_creation(request):
    context = {
        'Race':Race.objects.all()
    }
    return render(request, 'character_creation.html',context)

def Character_Selection(request):
    if 'Character_ID' not in request.session:
        request.session['Character_ID'] = request.POST['Character_ID']
    return redirect('/galaxyhub')

def characterremove(request,character_id):
    character = Characters.objects.get(id=character_id)
    character.delete()
    return redirect('/character_selector')

def signout(request):
    if 'Character_ID' in request.session:
        del request.session['Character_ID']
    return redirect('/character_selector')

def changelocation(request,planet_name):
    location = Characters.objects.get(id=request.session['Character_ID'])
    location.Char_Location = Planets.objects.get(planet_name=request.POST['planet_name'])
    location.save()
    return redirect(f'/planet_sheet/{planet_name}')












# To DO 

# ship selection / we can just use a default like the friggin yacht

# skills / levels Databased
# current skill level functionality
# skill training levels functionality




# 'Character' : Character.objects.Char_User.
