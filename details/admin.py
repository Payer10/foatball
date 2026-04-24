from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ('player', 'season_year')



@admin.register(Month)
class MonthAdmin(admin.ModelAdmin):
    list_display = ('month_name','season')


@admin.register(PlayerWeekdetails)
class PlayerWeekdetailsAdmin(admin.ModelAdmin):
    list_display = ('month', 'week_name')


@admin.register(PlayerMatch)
class PlayerMatchAdmin(admin.ModelAdmin):
    list_display = ('team_name', 'status')


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('player', 'match')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('headline', 'hot')
