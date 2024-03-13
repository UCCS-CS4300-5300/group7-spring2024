from django.contrib import admin
from django.urls import path
from . import views
from .views import update_substance_use

urlpatterns = [
    path('', views.home, name='home'),
    path('journal-entry/', views.journal_entry, name='journal_entry'),
    path('color_calendar/', views.color_calendar, name='color_calendar'),
    path('settings/', views.settings, name='settings'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.user_signup, name='signup'),
    path('analytics/', views.analytics, name='analytics'),
    path('get_journal_entries/',
         views.get_journal_entries,
         name='get_journal_entries'),
    path('substance_abuse_chart/',
         views.substance_abuse_chart,
         name='substance_abuse_chart'),
    path('substance_use/increment/',
         lambda request: update_substance_use(request, 'increment'),
         name='increment_substance_use'),
    path('substance_use/reset/',
         lambda request: update_substance_use(request, 'reset'),
         name='reset_substance_use'),
]
