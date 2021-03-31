from django.db import models
from django.contrib import messages
import re
import bcrypt

class UserManager(models.Manager):
    def emailValidator(self, postData):
        errors = {}
        if len(postData['first_name'])<2:
            errors['first_name'] = "First name must be more than 2 characters"
        if len(postData['last_name'])<2:
            errors['last_name'] = "Last name must be more than 2 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Invalid email address!'
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least eight characters."
        if postData['password'] != postData['confirm_password']:
            errors['confirm_password'] = "Passwords don't match."
        else:
            user_list = User.objects.filter(email = postData['email'])
            if len(user_list)>0:
                errors['email'] = 'Email already in use'
        return errors

    def loginValidator(self, postData):
        errors = {}
        user = User.objects.filter(email=postData['email'])
        if len(user) > 0:
            logged_user = user[0]
            if not bcrypt.checkpw(postData['password'].encode(), logged_user.password.encode()):
                erros['password'] = 'Username or password you entered is incorrect.'
        else:
            errors['email'] = 'Username or password you entered is incorrect.'
        return errors

class Race(models.Model):
    name = models.CharField(max_length=50)
    strength = models.IntegerField()
    hitpoints = models.IntegerField()
    agility = models.IntegerField()
    endurance = models.IntegerField()
    intelligence = models.IntegerField()
    defense = models.IntegerField()
    credit = models.IntegerField()
    descrip = models.TextField()

class Planets(models.Model):
    planet_name =  models.CharField(max_length=255)
    planet_type = models.CharField(max_length=255)
    planet_desc = models.TextField()
    planet_region = models.CharField(max_length=255)

class Skill(models.Model):
    skill_title = models.CharField(max_length=25)
    skill_level = models.IntegerField()
    start_time = models.DateTimeField()
    time_to_complete = models.IntegerField()

class Skill_Que(models.Model):
    skills_in_que = models.CharField(max_length=25)
    skills = models.ForeignKey(Skill, related_name="skills", on_delete = models.CASCADE, default='null')

class Profession(models.Model):
    pass

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Item(models.Model):
    equip = models.BooleanField(default=False)
    damage = models.IntegerField()
    armor = models.IntegerField() 
    descript = models.TextField()
    tier = models.IntegerField()
    level = models.IntegerField()

class Ship(models.Model):
    ship_name = models.CharField(max_length=55)
    ship_class =models.CharField(max_length=55)
    ship_speed_modifier = models.IntegerField()
    ship_desc = models.CharField(max_length=55, default='null')

class Npc(models.Model):
    npc_name = models.CharField(max_length=55)
    npc_level = models.CharField(max_length=55)
    npc_strength = models.IntegerField()
    npc_hitpoints = models.IntegerField()
    npc_agility = models.IntegerField()
    npc_endurance = models.IntegerField()
    npc_intelligence = models.IntegerField()
    npc_defense = models.IntegerField()
    npc_descrip = models.TextField()
    npc_tameable = models.BooleanField(default=False)

class Cities(models.Model):
    City_name = models.CharField(max_length = 50)

class Characters(models.Model):
    Char_First_Name= models.CharField(max_length=25)
    Char_Last_Name= models.CharField(max_length=25)
    Char_Race = models.ForeignKey(Race, related_name="characters", on_delete = models.CASCADE)
    Char_Level = models.IntegerField()
    Char_Skill = models.ForeignKey(Skill, related_name='Characters', on_delete = models.CASCADE)
    Char_Profession = models.ForeignKey(Profession, related_name='Character', on_delete= models.CASCADE)
    Char_User = models.ForeignKey(User, related_name='User', on_delete= models.CASCADE)