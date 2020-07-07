from django.shortcuts import render
from .models import Senator, Representative, Issue

# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html', context)

def contact_reps(request):
    context = {}
    return render(request, 'email_rep.html', context)

def senator_page(request):
    context = {}
    return render(request, 'SenatorPage.html', context)

def propose_vote_issues(request):
    context = {}
    return render(request, 'propose_vote_issues.html', context)

def reps_page(request):
    reps = Representative.objects.all()
    context = {'reps': reps}
    return render(request, 'RepsPage.html', context)
