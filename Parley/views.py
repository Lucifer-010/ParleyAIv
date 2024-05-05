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

from itertools import zip_longest

TWILIO_ACCOUNT_SID="AC5655f15cadd5bcd1aa75757289c26c32"
TWILIO_AUTH_TOKEN="fbac6ab971f88272846ac4943c885267"
TWILIO_NUMBER="+12673991196"

def bot(request):
    if request.method == 'POST':
            incoming_msg = request.POST.get('number')
    return HttpResponse("Hello")