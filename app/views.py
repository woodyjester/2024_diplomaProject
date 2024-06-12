import pandas as pd
from django.shortcuts import render, redirect
from app.forms import TemplateForm, DataSourceForm, RenderedFileForm
from app.models import Template, DataSource, RenderedFile
from docx import Document
from django.http import FileResponse


def index(request):
    return render(request, 'index.html')


def download(request, type, id):
    try:
        if type == 'template':
            template_object = Template.objects.get(id=id)
            file_path = template_object.file.path
        elif type == 'datasource':
            datasource_object = DataSource.objects.get(id=id)
            file_path = datasource_object.file.path
        elif type == 'render':
            render_object = RenderedFile.objects.get(id=id)
            file_path = render_object.file.path
        else:
            return redirect('app:index')
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=file_path.split('/')[-1])
    except Exception as e:
        print(e)
        return redirect('app:index')


def templates(request):
    if request.method == 'POST':
        form = TemplateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app:templates')
    template_objects = Template.objects.all()
    return render(request, 'templates.html', {
        'templates': template_objects,
        'form': TemplateForm(),
    })


def datasources(request):
    if request.method == 'POST':
        form = DataSourceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app:datasources')
    else:
        form = DataSourceForm()
    datasource_objects = DataSource.objects.all()
    return render(request, 'datasources.html', {
        'datasources': datasource_objects,
        'form': form,
    })


def rendering(request):
    if request.method == 'POST':
        form = RenderedFileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:rendering')
    else:
        form = RenderedFileForm()
    render_objects = RenderedFile.objects.all()
    return render(request, 'renders.html', {
        'renders': render_objects,
        'form': form,
    })
