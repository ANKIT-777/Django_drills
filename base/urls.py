from django.urls import path
from .views import index_view, matches_played_per_year,matches_won_per_team_per_year,extra_runs_conceded_per_team_in_2016,top_10_economical_bowler_in_2015,matches_played_view,matches_won_per_team_per_year_view

urlpatterns = [
    path('', index_view, name='index'),
    path('matches_played_per_year/', matches_played_per_year , name='matches_played_per_year'),
    path('matches_played_view/', matches_played_view , name='matches_played_view'),
    path('matches_won_per_team_per_year',matches_won_per_team_per_year,name='matches_won_per_team_per_year'),
    path('extra_runs_conceded_per_team_in_2016',extra_runs_conceded_per_team_in_2016,name='extra_runs_conceded_per_team_in_2016'),
    path('top_10_economical_bowler_in_2015',top_10_economical_bowler_in_2015,name='top_10_economical_bowler_in_2015')
]
