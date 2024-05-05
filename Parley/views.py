from django.shortcuts import render

# Create your views here.
from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse , HttpResponseRedirect , HttpRequest 
from django.contrib.auth import authenticate ,login ,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User 
import random,datetime
from django.views.decorators.csrf import csrf_exempt
import smtplib, ssl
from email.mime.text import MIMEText
from django.http import HttpResponseBadRequest, JsonResponse
from email.mime.multipart import MIMEMultipart
# Create your views here.
import datetime,time,requests
from .models import Conversation
from .utils import send_message, logger
import os

import google.generativeai as genai

from itertools import zip_longest


API_KEY = "AIzaSyAkJik7N15J_knNLcpt7yEZbmCXjJN_SY4"
# Initialize the GenerativeAI client
genai.configure(api_key = API_KEY)

# Get the Gemini Pro model
model = model = genai.GenerativeModel('gemini-pro')
genai.types.GenerationConfig(
        # Only one candidate for now.
        candidate_count=1,
        stop_sequences=['x'],
        max_output_tokens=20,
        temperature=1.0)

def bot(request):
    if request.method == 'POST':
            incoming_msg = request.POST.get('number')
    return HttpResponse("Hello")


@csrf_exempt
def reply(request):
      whatsapp_number = request.POST.get('From').split("whatsapp:")[-1]
      body = request.POST.get('Body', '')
      msg = f"{body} \nIn less than 1600 words"
      gemini_get = model.generate_content(msg)
      gemini_response = gemini_get.text
      send_message(whatsapp_number, gemini_response)
      return HttpResponse('')
