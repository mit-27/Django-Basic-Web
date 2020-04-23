from django import forms
from .models import Candidate
from crispy_forms.helper import FormHelper


class CandidateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    class Meta:
        model = Candidate
        fields = [

            'candidate_name',
            'candidate_email',
            'candidate_phone',
            'candidate_gender',
            'candidate_job_title',
            'candidate_source',
            'candidate_address'

        ]
