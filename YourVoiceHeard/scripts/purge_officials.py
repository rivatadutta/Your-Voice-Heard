'''
Simple Script to delete all Senators and 
Representatives from the database
'''
from emailreps.models import Representative, Senator
import csv
import os

def run():
    print(Representative.objects.all())
    print(Senator.objects.all())
    Representative.objects.all().delete()
    Senator.objects.all().delete()
    return
    
    
    
    