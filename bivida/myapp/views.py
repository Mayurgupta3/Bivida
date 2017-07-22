# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from forms import SignUpForm, LoginForm, TenderForm , GovForm
from models import Signup,SessionToken,Tender,Gov
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.


def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            print "yes"
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            user = Signup(username=username, password=make_password(password),
                          confirm_password=make_password(confirm_password),
                          email=email, phone=phone)
            user.save()
            return render(request, 'tender.html')
        else:
            print 'Invalid'
    elif request.method == 'GET':
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})


def login_view(request):
    response_data = {}
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = Signup.objects.filter(username=username).first()

            if user:
                if check_password(password, user.password):
                    token = SessionToken(user=user)
                    token.create_token()
                    token.save()
                    response = redirect('feed/')
                    response.set_cookie(key='session_token', value=token.session_token)
                    return response
                else:
                    response_data['message'] = 'Incorrect Password! Please try again!'

    elif request.method == 'GET':
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def feed_view(request):
    return render(request, 'feed.html')


# For validating the session
def check_validation(request):
    if request.COOKIES.get('session_token'):
        session = SessionToken.objects.filter(session_token=request.COOKIES.get('session_token')).first()
        if session:
            return session.user
    else:
        return None


def tenderform_view(request):
    if request.method == "POST":
        form = TenderForm(request.POST)
        if form.is_valid():
            print "yes"
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone = form.cleaned_data['phone']
            date_of_birth = form.cleaned_data['date_of_birth']
            gender = form.cleaned_data['gender']
            email = form.cleaned_data['email']
            address = form.cleaned_data['address']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            company_name = form.cleaned_data['company_name']
            company_registration_no = form.cleaned_data['company_registration_no']
            status_of_applicant = form.cleaned_data['status_of_applicant']
            nature_of_organization = form.cleaned_data['nature_of_organization']
            nature_of_business = form.cleaned_data['nature_of_business']
            experience = form.cleaned_data['experience']
            pan_no = form.cleaned_data['pan_no']
            tin_no = form.cleaned_data['tin_no']
            aadhar_no = form.cleaned_data['aadhar_no']
            turnover = form.cleaned_data['turnover']
            net_worth = form.cleaned_data['net_worth']
            description = form.cleaned_data['description']
            user = Tender(first_name=first_name, last_name=last_name, phone=phone, date_of_birth=date_of_birth,
                          gender=gender, email=email, address=address, city=city, state=state, company_name=company_name,
                          company_registration_no=company_registration_no, status_of_applicant=status_of_applicant,
                          nature_of_organization=nature_of_organization, nature_of_business=nature_of_business,
                          experience=experience, pan_no=pan_no, tin_no=tin_no, aadhar_no=aadhar_no, turnover=turnover,
                          net_worth=net_worth, description=description)
            user.save()
            return render(request, 'index.html')
        else:
            print 'Invalid'
    elif request.method == 'GET':
        form = SignUpForm()

    return render(request, 'tenderform.html', {'form': form})


def govform_view(request):
    if request.method == "POST":
        form = GovForm(request.POST)
        if form.is_valid():
            print "yes"
            tender_no = form.cleaned_data['tender_no']
            tender_type = form.cleaned_data['tender_type']
            form_of_contact = form.cleaned_data['form_of_contact']
            tender_category = form.cleaned_data['tender_category']
            work_item_title = form.cleaned_data['work_item_title']
            work_description = form.cleaned_data['work_description']
            pre_qual_details = form.cleaned_data['pre_qual_details']
            product_category = form.cleaned_data['product_category']
            product_sub_category = form.cleaned_data['product_sub_category']
            contract_type = form.cleaned_data['contract_type']
            bid_valid_day = form.cleaned_data['bid_valid_day']
            completion_period = form.cleaned_data['completion_period']
            location = form.cleaned_data['location']
            pincode = form.cleaned_data['pincode']
            publishing_date = form.cleaned_data['publishing_date']
            document_sale_start = form.cleaned_data['document_sale_start']
            document_sale_end = form.cleaned_data['document_sale_end']
            seek_clarification_start = form.cleaned_data['seek_clarification_start']
            seek_clarification_end = form.cleaned_data['seek_clarification_end']
            pre_bid_meeting = form.cleaned_data['pre_bid_meeting']
            bid_submission_start = form.cleaned_data['bid_submission_start']
            bid_submission_end = form.cleaned_data['bid_submission_end']
            bid_opening_date = form.cleaned_data['bid_opening_date']
            user = Gov(tender_no=tender_no, tender_type=tender_type, form_of_contact=form_of_contact,
                          tender_category=tender_category, work_item_title=work_item_title, work_description=work_description,
                          pre_qual_details=pre_qual_details, product_category=product_category, product_sub_category=product_sub_category,
                          contract_type=contract_type, bid_valid_day=bid_valid_day, completion_period=completion_period,
                          location=location, pincode=pincode, publishing_date=publishing_date, document_sale_start=document_sale_start,
                          document_sale_end=document_sale_end, seek_clarification_start=seek_clarification_start,
                          seek_clarification_end=seek_clarification_end, pre_bid_meeting=pre_bid_meeting, bid_submission_start=bid_submission_start,
                          bid_submission_end=bid_submission_end, bid_opening_date=bid_opening_date)
            user.save()
            return render(request, 'index.html')
        else:
            print 'Invalid'
    elif request.method == 'GET':
        form = SignUpForm()

    return render(request, 'tenderform.html', {'form': form})