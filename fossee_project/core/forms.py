import os
from django import forms
from .models import EventUpload

class EventUploadForm(forms.ModelForm):
    class Meta:
        model = EventUpload
        fields = ['event_type', 'event_date', 'csv_file']
        widgets = {
            'event_type' : forms.Select(attrs={'class': 'form-control'}),
            'event_date' : forms.DateInput(attrs={'type':'date', 'class':'form-control'}),
            'csv_file' : forms.FileInput(attrs={'class': 'form-control'}),
        }

    def clean_csv_file(self):
        file = self.cleaned_data.get('csv_file')
        if file:
            if os.path.splitext(file.name)[1].lower() != '.csv':
                raise forms.ValidationError("Only CSV files are allowed.")
        return file
        