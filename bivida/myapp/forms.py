from django import forms
from models import Signup, Tender, Gov


class SignUpForm(forms.ModelForm):
    class Meta:
        model = Signup
        fields = ['username', 'password', 'confirm_password', 'email', 'phone']


class LoginForm(forms.ModelForm):
    class Meta:
        model = Signup
        fields = ['username','password']


class TenderForm(forms.ModelForm):
    class Meta:
        model = Tender
        fields = ['first_name', 'last_name', 'phone', 'date_of_birth', 'gender', 'email', 'address', 'city', 'state',
                    'company_name', 'company_registration_no', 'status_of_applicant', 'nature_of_organization',
                  'nature_of_business', 'experience', 'pan_no', 'tin_no', 'aadhar_no', 'turnover', 'net_worth',
                  'description']


class GovForm(forms.ModelForm):
    class Meta:
        model = Gov
        fields = ['tender_no', 'tender_type', 'form_of_contact', 'tender_category', 'work_item_title','work_description',
                  'pre_qual_details', 'product_category', 'product_sub_category', 'contract_type', 'bid_valid_day',
                  'completion_period', 'locations', 'pincode', 'publishing_date', 'document_sale_start',
                  'document_sale_end', 'seek_clarification_start', 'seek_clarification_end', 'pre_bid_meeting',
                  'bid_submission_start', 'bid_submission_end', 'bid_opening_date']