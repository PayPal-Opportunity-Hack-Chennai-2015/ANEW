from django import forms
from .models import StudentBatch, Batch


class ChooseStudentForm(forms.ModelForm):

    class Meta:
        model = StudentBatch
        fields = ('batch', 'student', )

    def __init__(self, user,  *args, **kwargs):
            super(ChooseStudentForm, self).__init__(*args, **kwargs)
            self.fields['batch'].queryset = Batch.objects.filter(
                tutor=user)