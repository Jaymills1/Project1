from django import forms

from . models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('title', 'author', 'pdf', 'discription','cover')


class UpdateReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('title', 'author', 'discription','isUpdated')

class UpdateViewForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('viewers',)
