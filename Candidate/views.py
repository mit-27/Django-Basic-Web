from django.shortcuts import render
from .forms import CandidateForm
from django.contrib import messages
# Create your views here.


def candidate_view(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST)
        if form.is_valid():
            print(request.user.id)
            # print(form.candidate_recruiter)
            print(request.user.is_authenticated)
            # candidate = form(commit=False)
            # candidate.candidate_recruiter = request.user
            # print(form.candidate_name)
            # print(form)
            can = form.instance
            can.candidate_recruiter = request.user
            print(can.candidate_recruiter)
            can.save()
            # print(can)
            # form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Candidate is added')
            form = CandidateForm()
    else:
        form = CandidateForm()

    context = {
        'form': form
    }
    return render(request, 'Candidate/add_candidate.html', context)
