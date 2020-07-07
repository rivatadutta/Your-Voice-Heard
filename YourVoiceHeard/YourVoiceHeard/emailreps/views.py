from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html', context)

def contact_reps(request):
    context = {}
    return render(request, 'emailreps/email_rep.html', context)

def senator_page(request):
    context = {}
    return render(request, 'emailreps/SenatorPage.html', context)

def propose_vote_issues(request):
    context = {}
    return render(request, 'emailreps/propose_vote_issues.html', context)