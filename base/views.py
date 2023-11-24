# ipl_stats/views.py
import json
from django.forms import IntegerField
from django.http import JsonResponse
from django.db.models import Count,Sum,F,ExpressionWrapper, fields
from django.shortcuts import render
from .models import Match,Delivery
from base import models
from django.shortcuts import render


def index_view(request):
    
    return render(request, 'index.html')



def matches_played_per_year(request):
    result = (
        Match.objects
        .values('season')
        .annotate(matches_played=Count('id'))
        .order_by('season')
    )

    data = {'matches_per_year': list(result)}
    return JsonResponse(data)

def matches_played_view(request):
    
    json_data = matches_played_per_year(request)
    data = json_data.content.decode('utf-8')
    data_dict = json.loads(data)
    
    return render(request, 'matches_played_per_year.html', {'data': json.dumps(data_dict)})



def matches_won_per_team_per_year(request):
    
    result = (
        Match.objects
        .values('season', 'winner')
        .annotate(matches_won=Count('id'))
        .order_by('season', 'winner')
    )

    data = {'matches_won_per_team_per_year': list(result)}
    return JsonResponse(data)

def matches_won_per_team_per_year_view(request):
    json_data = matches_won_per_team_per_year(request)
    data = json_data.content.decode('utf-8')
    data_dict = json.loads(data)
    return render(request, 'matches_won_per_team_per_year.html', {'data': json.dumps(data_dict)})
    
    


def extra_runs_conceded_per_team_in_2016(request):
    year = 2016
    match_ids = Match.objects.filter(season=year).values_list('id', flat=True)

    result = (
        Delivery.objects
        .filter(match_id__in=match_ids)
        .values('bowling_team')
        .annotate(extra_runs_conceded=Sum('extra_runs'))
        .order_by('bowling_team')
    )

    data = {'extra_runs_conceded_per_team': list(result)}
    return JsonResponse(data)



def top_10_economical_bowler_in_2015(request):
    year = 2015
    match_ids = Match.objects.filter(season=year).values_list('id', flat=True)
    
    result = (
        Delivery.objects
        .filter(match_id__in=match_ids)
        .values('bowler')
        .annotate(
            economy_rate=  ((Sum('total_runs') - Sum('legbye_runs') - Sum('bye_runs') - Sum('penalty_runs'))/(((Count('ball'))  / 6) + ((Count('ball')) % 6) * 0.1 ))
           
        )
        .order_by('economy_rate')[:10]
        .values('bowler', 'economy_rate')
    )

    data = {'top_10_economical_bowler_in_2015': list(result)}
    
    return JsonResponse(data)
