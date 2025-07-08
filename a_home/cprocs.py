from django.conf import settings

def project_title(request):
    return {
        'PROJECT_TITLE': settings.PROJECT_TITLE
    }