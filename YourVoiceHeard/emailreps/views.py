from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Senator, Representative, Issue
from .forms import IssueForm

# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html', context)

def contact_reps(request):
    context = {}
    return render(request, 'email_rep.html', context)

def senator_page(request):
    senators = Senator.objects.all()
    context = {'senators': senators}
    return render(request, 'SenatorPage.html', context)

def propose_vote_issues(request):
    context = {}
    return render(request, 'propose_vote_issues.html', context)

def reps_page(request):
    reps = Representative.objects.all()
    context = {'reps': reps}
    return render(request, 'RepsPage.html', context)
    
def make_issue(request):
    issue_form = IssueForm()
    curr_issues = reversed(Issue.objects.all())
    context = {'issue_form': issue_form, 'issues': curr_issues}
    return render(request, 'make_issue.html', context)

# Post request to add the issue to the DB
@require_POST
def add_issue(request):
    form = IssueForm(request.POST)
    if form.is_valid():
        #new_issue = Issue(issue_name = form.cleaned_data['issue_name'], issue_text = form.cleaned_data['issue_text'])
        #new_issue.save()
        new_issue = form.save()
    return redirect('emailreps:make_issue')
