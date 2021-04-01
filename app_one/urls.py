from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('registration',views.regis),
    path('login',views.login),
    path('login_page',views.login_page),
    path('register_page',views.register),
    path('galaxyhub',views.galaxyhub),
    path('logout',views.logout),
    path('planet',views.planet),
    path('planet/create',views.planetcreate),
    path('planet/edit/<int:planet_id>',views.planetedit),
    path('edit/<int:planet_id>',views.planetfinaledit),
    path('planet/remove/<int:planet_id>',views.planetremove),
    path('race',views.race),
    path('race/create',views.racecreate),
    path('race/edit/<int:race_id>',views.raceedit),
    path('edit/<int:race_id>',views.racefinaledit),
    path('race/remove/<int:race_id>',views.raceremove),
    path('character_sheet',views.character_sheet),
    path('planet_sheet/<planet_name>',views.planet_sheet),
    # path('planet_sheet',views.planet_sheet),
    path('ship_sheet',views.ship_sheet),
    path('character_selector', views.character_selector),
    path('character_creation',views.character_creation),
    path('Character_final_creation', views.Character_final_creation),
    # path('timer')
]
