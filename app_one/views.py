from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    return render(request,'home.html')

def regis(request):
    errors = User.objects.emailValidator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('/register_page')
    else:
        pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = pw_hash
        )
        request.session['uuid'] = user.id
    return redirect('/character_selector')

def login(request):
    errors = User.objects.loginValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
            return redirect('/login_page')
    else:
        user = User.objects.filter(email=request.POST['email'])
        request.session['uuid'] = user[0].id
        return redirect('/galaxyhub')

def logout(request):
    del request.session['uuid']
    return redirect('/')

def login_page(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def Skill_timer(request):
    pass

def galaxyhub(request):
    context = {
        'Planets':Planets.objects.filter(planet_region="Core Worlds")
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

def character_sheet(request, Race):
    Race = Character.objects.filter(Char_Race=Char_Race)
    imgurl = f"img/{Race[0].name}.png"
    context = {
        'Race': Race[0],
        'img': imgurl
    }
    return render(request,'Character_sheet.html',context)

def planet_sheet(request,planet_name):
    Planet = Planets.objects.filter(planet_name=planet_name)
    imgurl = f"img/{Planet[0].planet_type}.png"
    context = {
        'Planet': Planet[0],
        'img': imgurl
    }
    return render(request,'planet_sheet.html',context)

def ship_sheet(request, ship_class):
    context = {
        'Ship' : Ship.objects.filter(ship_class=ship_class)
    }
    return render(request,'ship_sheet.html', context)

def character_selector(request):
    user = User.objects.get(id=request.session['uuid'])
    characters = user.User.all()
    context = {
        'Character':characters
    }
    return render(request, 'Choose_character.html', context)








            # 'selector' : len(Character.Char_User.all),
        # 'Character' : Character.objects.Char_User.