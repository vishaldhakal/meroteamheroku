from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name="index"),
    path('matches/',views.matches,name="matches"),
    path('contests/',views.contests,name="contests"),
    path('teams_list/',views.teamslist,name="teams_list"),
    path('team-select/<no>/',views.team_select,name="team_select"),
    path('team-edit/<int:no>/',views.team_edit,name="team_edit"),
    path('team-delete/<int:no>/',views.teams_delete,name="teams_delete"),
    path('team-select-submit/<no>/',views.team_select_submit,name="team_select_submit"),
    path('team-select-update/<int:no>/',views.team_select_update,name="team_select_update"),
]