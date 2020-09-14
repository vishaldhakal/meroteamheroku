from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name="index"),
    path('matches/',views.matches,name="matches"),
    path('team-select/<no>/',views.team_select,name="team_select"),
    path('team-select-submit/<no>/',views.team_select_submit,name="team_select_submit"),
]