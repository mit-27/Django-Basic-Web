from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from Candidate.models import Candidate
from django.shortcuts import render, get_object_or_404, redirect
from Candidate.forms import CandidateForm
from django.contrib.auth.decorators import login_required


@login_required
def dashboard_view(request):
    candidates = Candidate.objects.filter(candidate_recruiter=request.user)
    no_can = False
    if request.method == "GET":
        can_name = request.GET.get("can-name")
        # print("Can Name:"+can_name)
        if can_name == "":
            
            candidates = Candidate.objects.filter(
                candidate_recruiter=request.user)
            
        else:
            
            candidates = Candidate.objects.filter(
                candidate_recruiter=request.user, candidate_name=can_name)
    candidates = Candidate.objects.filter(candidate_recruiter=request.user)

    print(candidates)
    if candidates.exists():
        no_can = False
    else:
        no_can=True

    context = {
        'candidates': candidates,
        'can_available':no_can
    }
    return render(request, 'dashboard/dashboard.html', context)


@login_required
def update_view(request, id):
    candidate = get_object_or_404(Candidate, pk=id)
    can_form = CandidateForm(request.POST or None, instance=candidate)
    if can_form.is_valid():
        can_form.save()
    return render(request, 'Candidate/add_candidate.html', {'form': can_form})


@login_required
def delete_view(request, id):
    candidate = get_object_or_404(Candidate, pk=id)
    candidate.delete()
    return redirect('dashboard')
