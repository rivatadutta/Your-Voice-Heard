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

# Index page
def index(request):
    context = {}
    return render(request, 'index.html', context)

# Black Lives Matter Page
def blm(request):
    context = {}
    return render(request, 'blm.html', context)

# Ice Page
def ice(request):
    context = {}
    return render(request, 'ice.html', context)

# Yemen Page
def yemen(request):
    context = {}
    return render(request, 'yemen.html', context)

# Climate Change Page
def climatechange(request):
    context = {}
    return render(request, 'climatechange.html', context)

# Issue proposal page
def proposeissues(request):
    issue_form = IssueForm()
    context = {'issue_form': issue_form}
    return render(request, 'proposeissues.html', context)

# Page that lists the current California Representatives and Senators
def caofficals(request):
    reps = Representative.objects.all()
    senators = Senator.objects.all()
    context = {'reps': reps, 'sens': senators}
    return render(request, 'caofficals.html', context)

# Page with info about the 2020 Elections
def elections2020(request):
    context = {}
    return render(request, '2020elections.html', context)

# Voting redirect
def vote(request):
    context = {}
    return redirect('emailreps:results')

# Processes upvote requests
def upvote(request, id):
    ip = get_client_ip(request)
    issue = Issue.objects.get(id=id)
    if Vote.objects.filter(ip_address=ip, issue=issue).exists():
        vote_check = Vote.objects.get(ip_address=ip, issue=issue)
        
        # If the vote was an upvote, sets it to neutral
        if vote_check.vote_type == 1:
            vote_check.vote_type = 0
        # If the vote was neutral, sets it to an upvote
        elif vote_check.vote_type == 0:
            vote_check.vote_type = 1
        # If the vote was a downvote, sets it to an upvote
        else:
            vote_check.vote_type = 1
        vote_check.save()
        return redirect('emailreps:results')
    # If there was no existing vote, create a vote object tied to the client's IP for this given issue
    else:
        vote = Vote(vote_type=1, ip_address=get_client_ip(request), issue=issue)
        vote.save()
        return redirect('emailreps:results')

# Processes downvote requests
def downvote(request, id):
    ip = get_client_ip(request)
    issue = Issue.objects.get(id=id)
    # Checks if a vote for this IP and Issue exists in the db already
    if Vote.objects.filter(ip_address=ip, issue=issue).exists():
        vote_check = Vote.objects.get(ip_address=ip, issue=issue)

        # If the vote was a downvote, set it to neutral
        if vote_check.vote_type == -1:
            vote_check.vote_type = 0
        # If the vote was neutral, set it to a downvote
        elif vote_check.vote_type == 0:
            vote_check.vote_type = -1
        # If the vote was an upvote, set it to a downvote
        else:
            vote_check.vote_type = -1
        vote_check.save()
        return redirect('emailreps:results')
    # If there was no existing vote, create a vote object tied to the client's IP for this given issue
    else:
        vote = Vote(vote_type=-1, ip_address=get_client_ip(request), issue=issue)
        vote.save()
        return redirect('emailreps:results')

# Results page for issue proposal and voting.
def results(request):
    # Counts the number of vote objects for a given issue, if none exist sets them to 0.
    curr_issues = Issue.objects.annotate(true_vote=Coalesce(Sum('vote__vote_type'), 0)).order_by('-true_vote')
    context = {'issues': curr_issues}
    return render(request, 'results.html', context)

# Pending deletion
def reps_page(request):
    reps = Representative.objects.all()
    context = {'reps': reps}
    return render(request, 'RepsPage.html', context)

# Testing page
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
        new_issue = form.save()
    return redirect('emailreps:results')
