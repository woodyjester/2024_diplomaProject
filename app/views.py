from django.shortcuts import render
from django.http import FileResponse, HttpResponseNotFound
import os
from django.conf import settings


def list_templates(request):
    templates_dir = os.path.join(settings.BASE_DIR, 'app', 'docx')
    templates = list(filter(lambda template_name: template_name.endswith('docx'), os.listdir(templates_dir)))
    return render(request, 'protocolAutomation/template_list.html', {'templates': templates})


def download_template(request, template_name):
    file_path = os.path.join(settings.BASE_DIR, 'app', 'docx', template_name)
    if os.path.exists(file_path):
        response = FileResponse(open(file_path, 'rb'))
        return response
    else:
        return HttpResponseNotFound('The requested docx was not found.')
