from django import forms
from app.models import Template, DataSource, RenderedFile


class TemplateForm(forms.ModelForm):
    name = forms.CharField(label='Template Name')
    file = forms.FileField(label='Upload Template File')

    class Meta:
        model = Template
        fields = ['name', 'file']


class DataSourceForm(forms.ModelForm):
    name = forms.CharField(label='Data Source Name')
    file = forms.FileField(label='Upload Data Source File')

    class Meta:
        model = DataSource
        fields = ['name', 'file']


class RenderedFileForm(forms.ModelForm):
    datasource = forms.ModelChoiceField(queryset=DataSource.objects.all(), label='Select Data Source')
    template = forms.ModelChoiceField(queryset=Template.objects.all(), label='Select Template')
    sheet = forms.CharField(label='Sheet Name', required=False)

    class Meta:
        model = RenderedFile
        fields = ['datasource', 'template', 'sheet']
