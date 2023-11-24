
import csv
from django.core.management.base import BaseCommand
from django.db import transaction
from base.models import Match,Delivery


class Command(BaseCommand):
    
    help = 'Import IPL dataset into tables'

    def handle(self, *args, **kwargs):
        Match.objects.all().delete()
        Delivery.objects.all().delete()
        
        with transaction.atomic():
            
            with open('Data/matches.csv') as csvfile:
                dataset = csv.DictReader(csvfile)
                
                for row in dataset:
                    Match.objects.create(**row)
                    
            with open('Data/deliveries.csv') as csvfile:
                  dataset = csv.DictReader(csvfile)
                  
                  for row in dataset:
                    match_id = row.pop('match_id')
                    match = Match.objects.get(id=match_id)
                    Delivery.objects.create(match_id=match, **row)



        
    
    
