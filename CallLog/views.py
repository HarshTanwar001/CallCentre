from .models import Log
from django.db.models import Q
from django.shortcuts import render

import re


def index(request):
    return render(request, 'index.html')


# view to save the call details in the db when the call has been initiated
def call(request):
    from_no = request.POST['from'].strip()
    to_no = request.POST['to'].strip()

    # checking if the phone numbers length is valid or not
    if len(from_no) < 10 or len(to_no) < 10:
        return render(request, 'index.html', {'msg': "Phone Numbers consist of 10 digits, please check the number/s"})
    
    # checking if the phone numbers consist of invalid characters or not
    x = re.findall("[^0-9]", from_no)
    y = re.findall("[^0-9]", to_no)

    if x or y:
        return render(request, 'index.html', {'msg': "Phone Numbers are numerical in nature, please check the number/s"})
    
    # checking if the user is trying to call himself/ herself
    if x == y:
        return render(request, 'index.html', {'msg': "A person cannot call himself/herself, please check the number/s"})

    data = Log(from_no=from_no, to_no=to_no)
    data.save()

    return render(request, 'index.html')


def report(request):
    return render(request, 'report.html')


# view to get all the data from the db where from_no = phone or to_no = phone
def generate(request):
    phone = request.GET['phone'].strip()

    # checking if the phone number length is valid or not
    if len(phone) < 10:
        return render(request, 'report.html', {'msg': "Phone Numbers consist of 10 digits, please check the number"})
    
    # checking if the phone number consists of invalid characters or not
    x = re.findall("[^0-9]", phone)

    if x:
        return render(request, 'report.html', {'msg': "Phone Numbers are numerical in nature, please check the number"})

    data = Log.objects.filter(Q(from_no=phone) | Q(to_no=phone))

    return render(request, 'generate.html', {'data': data})
