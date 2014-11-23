# Create your views here.

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
import json

import time

from api.models import ResumizrUserData
# list of social auth mapping
backends = ['twitter', 'github', 'facebook',
            'google-oauth2', 'linkedin-oauth2']

@login_required
def theme_generator(request):
    try:
        request.user.resumizr_data
    except ObjectDoesNotExist:
        request.user.resumizr_data = ResumizrUserData(user = request.user)
        request.user.resumizr_data.save()

    context = {'user': request.user, 'oauth_providers': 'lol'}
    return render(request, 'theme_generator/theme-generator.html', context)