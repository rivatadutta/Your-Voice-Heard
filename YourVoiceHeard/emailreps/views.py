from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.db.models import Avg, Count, Min, Sum
from django.db.models.functions import Coalesce
from .models import Senator, Representative, Issue, Vote
from .forms import IssueForm

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

# Create your views here.

def index(request):
    context = {}
    return render(request, 'index.html', context)

def blm(request):
    context = {}
    return render(request, 'blm.html', context)

def ice(request):
    context = {}
    return render(request, 'ice.html', context)

def yemen(request):
    context = {}
    return render(request, 'yemen.html', context)

def climatechange(request):
    context = {}
    return render(request, 'climatechange.html', context)

def proposeissues(request):
    issue_form = IssueForm()
    context = {'issue_form': issue_form}
    return render(request, 'proposeissues.html', context)

def caofficals(request):
    context = {}
    return render(request, 'caofficals.html', context)

def elections2020(request):
    context = {}
    return render(request, '2020elections.html', context)

def vote(request):
    context = {}
    return redirect('emailreps:results')

def upvote(request, id):
    ip = get_client_ip(request)
    issue = Issue.objects.get(id=id)
    if Vote.objects.filter(ip_address=ip, issue=issue).exists():
        vote_check = Vote.objects.get(ip_address=ip, issue=issue)
        if vote_check.vote_type == 1:
            vote_check.vote_type = 0
        elif vote_check.vote_type == 0:
            vote_check.vote_type = 1
        else:
            vote_check.vote_type = 1
        vote_check.save()
        return redirect('emailreps:results')
    else:
        vote = Vote(vote_type=1, ip_address=get_client_ip(request), issue=issue)
        vote.save()
        return redirect('emailreps:results')

def downvote(request, id):
    ip = get_client_ip(request)
    issue = Issue.objects.get(id=id)
    if Vote.objects.filter(ip_address=ip, issue=issue).exists():
        vote_check = Vote.objects.get(ip_address=ip, issue=issue)
        if vote_check.vote_type == -1:
            vote_check.vote_type = 0
        elif vote_check.vote_type == 0:
            vote_check.vote_type = -1
        else:
            vote_check.vote_type = -1
        vote_check.save()
        return redirect('emailreps:results')
    else:
        vote = Vote(vote_type=-1, ip_address=get_client_ip(request), issue=issue)
        vote.save()
        return redirect('emailreps:results')

def results(request):
    # need to count the number of vote objects for a given issue
    curr_issues = Issue.objects.annotate(true_vote=Coalesce(Sum('vote__vote_type'), 0)).order_by('-true_vote')
    context = {'issues': curr_issues}
    return render(request, 'results.html', context)

def reps_page(request):
    reps = Representative.objects.all()
    context = {'reps': reps}
    return render(request, 'RepsPage.html', context)


def make_issue(request):
    Issue.objects.all().delete()
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
    return redirect('emailreps:results')
