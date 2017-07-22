from django.db import models
import uuid


class Signup(models.Model):

    username = models.CharField(max_length=120, default='')
    password = models.CharField(max_length=40, default='')
    confirm_password = models.CharField(max_length=40, default='')
    email = models.EmailField(default='')
    phone = models.IntegerField(default=0)


class SessionToken(models.Model):

    user = models.ForeignKey(Signup)
    session_token = models.CharField(max_length=255)
    last_request_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    is_valid = models.BooleanField(default=True)

    def create_token(self):
        self.session_token = uuid.uuid4()


class Tender(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.IntegerField(default=0)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    email = models.EmailField(default='')
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    company_registration_no = models.CharField(max_length=30)
    status_of_applicant = models.CharField(max_length=40)
    nature_of_organization = models.CharField(max_length=50)
    nature_of_business = models.CharField(max_length=50)
    experience = models.IntegerField(default=0)
    pan_no = models.IntegerField(default=0)
    tin_no = models.IntegerField(default=0)
    aadhar_no = models.IntegerField(default=0)
    turnover = models.IntegerField(default=0)
    net_worth = models.IntegerField(default=0)
    description = models.CharField(max_length=300)


class Gov(models.Model):

    tender_no = models.CharField(max_length=20)
    tender_type = models.CharField(max_length=30)
    form_of_contact = models.CharField(max_length=30)
    tender_category = models.CharField(max_length=20)
    work_item_title = models.CharField(max_length=50)
    work_description = models.CharField(max_length=200)
    pre_qual_details = models.CharField(max_length=200)
    product_category = models.CharField(max_length=50)
    product_sub_category = models.CharField(max_length=100)
    contract_type = models.CharField(max_length=50)
    bid_valid_day = models.IntegerField(default=0)
    completion_period = models.IntegerField(default=0)
    locations = models.CharField(max_length=40)
    pincode = models.IntegerField(default=0)
    publishing_date = models.DateField()
    document_sale_start = models.DateTimeField()
    document_sale_end = models.DateTimeField()
    seek_clarification_start = models.DateTimeField()
    seek_clarification_end = models.DateTimeField()
    pre_bid_meeting = models.DateTimeField()
    bid_submission_start = models.DateTimeField()
    bid_submission_end = models.DateTimeField()
    bid_opening_date = models.DateTimeField()
