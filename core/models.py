from django.db import models

# Create your models here.

# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models

from django.db.models.deletion import CASCADE
import os
from django.core.validators import FileExtensionValidator




class become_sponsor(models.Model):
    id=models.AutoField(primary_key=True)
    company_name=models.CharField(max_length=255)
    company_web=models.CharField(max_length=255,null=True)
    tob=models.CharField(max_length=255)
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    message=models.TextField()
    created=models.DateTimeField(auto_now_add=True,null=True)
    class Meta:
        db_table = "become_sponsor"

class blog(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.TextField(default=None)
    titleSlag=models.TextField()
    image=models.FileField(default=None,blank=True,null=True)
    s_description=models.TextField(default=None,blank=True,null=True)
    description=models.TextField()
    meta_title=models.TextField()
    meta_desc=models.TextField()
    status=models.IntegerField()
    created=models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "blog"

class contest_price_list(models.Model):
    id=models.AutoField(primary_key=True)
    price_name=models.CharField(max_length=255 )
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=255,null=True,blank=True )

    class Meta:
         db_table = "contest_price_list"

class contest_category(models.Model):
    id=models.AutoField(primary_key=True)
    parent_id=models.IntegerField(default=None,null=True)
    name=models.CharField(max_length=255)
    slug=models.CharField(max_length=255)
    color=models.CharField(max_length=255, unique=True,null=True,blank=True,error_messages={'unique':"Category color has been already exist!"})
    description=models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    masterstatus=models.CharField(max_length=200,default=None,null=True,blank=True)
    class Meta:
         db_table = "contest_category"

class contest_prizes(models.Model):
    id=models.AutoField(primary_key=True)
    contest_id=models.IntegerField()
    prize_number=models.IntegerField(null=True)
    prize_title=models.CharField(max_length=255)
    prize_image=models.CharField(max_length=255, null=True)
    prize_description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
         db_table = "contest_prizes"

class sponsors(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    tab_name=models.CharField(max_length=256,null=True)
    sponsor_image=models.CharField(max_length=255,null=True)
    sponsor_logo=models.CharField(max_length=255,null=True)
    sponsor_description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    
    class Meta:
         db_table = "sponsors"

class contest_sponsor(models.Model):
    id=models.AutoField(primary_key=True)
    online_presense=models.CharField(max_length=255,null=True,blank=True)
    offline_presense=models.CharField(max_length=255,null=True,blank=True)
    brand_name=models.CharField(max_length=255)
    company_name=models.CharField(max_length=255)
    web_url=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    state=models.CharField(max_length=255)
    country=models.CharField(max_length=255)
    company_phone=models.IntegerField(null=True,blank=True)
    company_gst=models.CharField(max_length=255)
    company_logo=models.FileField(default=None,null=True,blank=True,upload_to='pdfs/',error_messages={'unique':"only jpg format supported!"},validators=[FileExtensionValidator(['jpg'])])
    person_name=models.CharField(max_length=255)
    person_designation=models.CharField(max_length=255)
    person_mobile=models.CharField(max_length=255,default=None,null=True,blank=True)
    person_mail=models.EmailField(max_length=70,blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=255,null=True,blank=True)

    class Meta:
         db_table = "contest_sponsor"

class contests(models.Model):
    id=models.AutoField(primary_key=True)
    category=models.ForeignKey(contest_category,on_delete=models.CASCADE,default=None)
    contest_title=models.CharField(max_length=225, null=True,blank=True)
    question=models.CharField(max_length=255,default=None)
    contest_venue=models.CharField(max_length=225, null=True,blank=True)
    contest_schedule_date=models.DateField(null=True,blank=True)
    contest_schedule_time=models.TimeField(default=None,null=True,blank=True)
    uploadContest=models.CharField(max_length=200,default=None,null=True,blank=True) 
    contest_image=models.FileField(null=True,blank=True,upload_to='userprofile',default=None)
    contest_thumbnail=models.FileField(default=None,blank=True,null=True,upload_to='myprofile')
    video_ad_url=models.CharField(max_length=255, null=True,blank=True)
    prize_description=models.TextField(null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    contest_term_conditions=models.TextField(null=True,blank=True)
    no_winner=models.IntegerField(default=None,null=True,blank=True)
    type_price=models.ForeignKey(contest_price_list, on_delete=models.CASCADE,null=True,blank=True,related_name='+')
    type_price_nd=models.ForeignKey(contest_price_list, on_delete=models.CASCADE,null=True,blank=True)
    contest_image_thumb=models.FileField(default=None,null=True,blank=True)
    total_amount=models.IntegerField(null=True,blank=True)
    eqamount=models.IntegerField(null=True,blank=True)
    amount_change=models.CharField(max_length=200,default=None,null=True,blank=True)
    reamt=models.CharField(max_length=255,null=True,blank=True)
    total_amount_nd=models.IntegerField(null=True,blank=True)
    position_amount=models.CharField(max_length=255, null=True,blank=True)
    contestWinTitle=models.TextField(max_length=250,default=None,null=True,blank=True)
    contestWinAmountTitle=models.TextField(max_length=250,default=None,null=True,blank=True)
    contest_start_date=models.DateField(null=True,blank=True)
    contest_start_time=models.TimeField(max_length=200,default=None,null=True,blank=True)
    contest_end_date=models.DateField(null=True,blank=True)
    contest_end_time=models.TimeField(max_length=200,default=None,null=True,blank=True)
    feature_image=models.FileField(default=None,null=True,blank=True)
    mobile_feature_img=models.FileField(default=None,null=True,blank=True)
    sponsor_id=models.ForeignKey(contest_sponsor,on_delete=models.CASCADE,default=None,null=True,blank=True)
    vac=models.CharField(max_length=200,default=None,null=True,blank=True)
    video_ad_type=models.CharField(max_length=255, null=True,blank=True)
    video_ad_company=models.CharField(max_length=255, null=True,blank=True)
    video_ad_time=models.TimeField(max_length=200,default=None,null=True,blank=True)
    video_ad_skip_time=models.TimeField(max_length=200,default=None,null=True,blank=True)
    dgc=models.CharField(max_length=200,default=None,null=True,blank=True) 
    google_ad_after_header=models.CharField(max_length=255, null=True,blank=True)
    ad_after_header_image=models.FileField(default=None,null=True,blank=True)
    ad_after_header_url=models.CharField(max_length=255, null=True,blank=True)
    ptg=models.CharField(max_length=200,default=None,null=True,blank=True)
    google_ad_1_sidebar=models.CharField(max_length=255, null=True,blank=True)
    ad_1_side_image=models.FileField(default=None,null=True,blank=True)
    ad_1_side_url=models.CharField(max_length=255,null=True,blank=True)
    gpk=models.CharField(max_length=200,default=None,null=True,blank=True)
    google_ad_2_sidebar=models.CharField(max_length=255,null=True,blank=True)
    ad_2_side_image=models.FileField(default=None,null=True,blank=True)
    ad_2_side_url=models.CharField(max_length=255,null=True,blank=True)
    status=models.CharField(max_length=255,default=None,null=True,blank=True)

    class Meta:
         db_table = "contests"


class contests_old(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    description=models.CharField(max_length=255, null=True)
    sponsor_id=models.IntegerField()
    contest_image=models.CharField(max_length=255, null=True)
    contest_end_date=models.DateTimeField(null=True)
    contest_term_conditions=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
         db_table = "contests-old"

class failed_jobs(models.Model):
    id=models.AutoField(primary_key=True)
    connection=models.TextField()
    queue=models.TextField()
    payload=models.TextField()
    exception=models.TextField()
    failed_at=models.DateTimeField(auto_now_add=True)

    class Meta:
         db_table = "failed_jobs"

class global_ads(models.Model):
    id=models.AutoField(primary_key=True)
    video_type=models.CharField(max_length=255)
    video_url=models.CharField(max_length=255)
    video_ad_time=models.CharField(max_length=255,null=True)
    video_ad_skip_time=models.CharField(max_length=100,null=True)
    adv_header_type=models.CharField(max_length=255)
    adv_header_content=models.TextField()
    adv_header_image=models.FileField(default=None,null=True,blank=True)
    adv_sidebar_top_type=models.CharField(max_length=255)
    adv_sidebar_top_image=models.FileField(default=None,null=True,blank=True)
    adv_sidebar_top_cntnt=models.TextField()
    adv_sidebar2_type=models.CharField(max_length=255)
    adv_sidebar2_image=models.FileField(default=None,null=True,blank=True)
    adv_sidebar2_content=models.TextField()
    disable_header_ads=models.CharField(max_length=11,null=True)
    disable_side1_ads=models.CharField(max_length=11,null=True)
    disable_side2_ads=models.CharField(max_length=11,null=True)
    created=models.DateTimeField(auto_now_add=True)
    class Meta:
         db_table = "global_ads"

class global_ads_login(models.Model):
    id=models.AutoField(primary_key=True)
    adv_login_type=models.CharField(max_length=11)
    adv_login_content=models.TextField()
    disable_login_ads=models.CharField(max_length=11,null=True)
    created=models.DateTimeField(auto_now_add=True)
    class Meta:
         db_table = "global_ads_login"


class global_ads_profile(models.Model):
    id=models.AutoField(primary_key=True)
    adv_profile_top_type=models.CharField(max_length=255,null=True)
    adv_profile_top_content=models.TextField()
    adv_profile_side1_type=models.CharField(max_length=255,null=True)
    adv_profile_side1_content=models.TextField()
    adv_profile_side2_type=models.CharField(max_length=255,null=True)
    adv_profile_side2_content=models.TextField()
    disable_profile_top_ads=models.CharField(max_length=11,null=True)
    disable_profile_side1_ads=models.CharField(max_length=11,null=True)
    disable_profile_side2_ads=models.CharField(max_length=11,null=True)
    created=models.DateTimeField(auto_now_add=True)
    class Meta:
         db_table = "global_ads_profile"


class jobs(models.Model):
    id=models.AutoField(primary_key=True)
    queue=models.CharField(max_length=255)
    payload=models.TextField()
    attempts=models.SmallIntegerField()
    reserved_at=models.IntegerField(null=True)
    available_at=models.IntegerField()
    created_at=models.IntegerField()

    class Meta:
         db_table = "jobs"

class knowledge_center(models.Model):
    id=models.AutoField(primary_key=True)
    tags=models.CharField(max_length=255)
    age_group=models.CharField(max_length=255)
    question=models.CharField(max_length=255)
    answers=models.TextField()
    correct_answer=models.CharField(max_length=255)
    created=models.DateTimeField(auto_now_add=True)
    class Meta:
         db_table = "knowledge_center"


class leaderboard(models.Model):
    id=models.AutoField(primary_key=True)
    userid=models.IntegerField()
    uname=models.CharField(max_length=255)
    wincounts=models.CharField(max_length=255)
    winpercantege=models.CharField(max_length=255)
    totalparticipate=models.CharField(max_length=255)

    class Meta:
         db_table = "leaderboard"



class mailerhtml(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    html=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    class Meta:
         db_table = "mailerhtml"


class migrations(models.Model):
    id=models.AutoField(primary_key=True)
    migration=models.CharField(max_length=255)
    batch=models.IntegerField()
    class Meta:
         db_table = "migrations"

class password_resets(models.Model):
    email=models.CharField(max_length=255)
    token=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    class Meta:
         db_table = "password_resets"

class previews(models.Model):
    id=models.AutoField(primary_key=True)
    category_id= models.IntegerField()
    question=models.CharField(max_length=255)
    question_slag=models.CharField(max_length=255,null=True)
    contest_title=models.CharField(max_length=225,null=True)
    contest_venue=models.CharField(max_length=225,null=True)
    contest_schedule_date=models.CharField(max_length=255,null=True)
    contest_schedule_time=models.CharField(max_length=255,null=True)
    prize_description=models.TextField()
    description=models.TextField()
    contest_term_conditions=models.TextField()
    contestWinTitle=models.TextField()
    contestWinAmountTitle=models.TextField()
    sponsor_id=models.IntegerField()
    contestCreativeType=models.CharField(max_length=255,null=True)
    contest_image=models.CharField(max_length=255,null=True)
    contest_image_thumb=models.CharField(max_length=255,null=True)
    no_winner=models.IntegerField(default=None)
    type_price_id=models.IntegerField(null=True)
    total_amount=models.IntegerField()
    amount_distribution=models.CharField(max_length=255,null=True)
    position_amount=models.CharField(max_length=255,null=True)
    equal_amount=models.CharField(max_length=255,null=True)
    contest_start_date=models.DateField(null=True)
    contest_start_time=models.CharField(max_length=255,null=True)
    contest_end_date=models.DateField(null=True)
    contest_end_time=models.CharField(max_length=255,null=True)
    video_ad_type=models.CharField(max_length=255,null=True)
    video_ad_company=models.CharField(max_length=255,null=True)
    video_ad_url=models.CharField(max_length=255,null=True)
    video_ad_time=models.CharField(max_length=255,null=True)
    video_ad_skip_time=models.CharField(max_length=100,null=True)
    ad_after_header_type=models.CharField(max_length=255,null=True)
    google_ad_after_header=models.CharField(max_length=255,null=True)
    ad_after_header_image=models.CharField(max_length=255,null=True)
    ad_after_header_url=models.CharField(max_length=255,null=True)
    ad_sidebar_1_type=models.CharField(max_length=255,null=True)
    ad_1_side_image=models.CharField(max_length=255,null=True)
    google_ad_1_sidebar=models.CharField(max_length=255,null=True)
    ad_1_side_url=models.CharField(max_length=255,null=True)
    ad_sidebar_2_type=models.CharField(max_length=255,null=True)
    ad_2_side_image=models.CharField(max_length=255,null=True)
    google_ad_2_sidebar=models.CharField(max_length=255,null=True)
    ad_2_side_url=models.CharField(max_length=255,null=True)
    feature_image=models.CharField(max_length=225,null=True)
    mobile_feature_img=models.CharField(max_length=255,null=True)
    rest_participants=models.CharField(max_length=225,null=True)
    type_of_prize_rest_id=models.IntegerField(null=True)
    amount_rest=models.IntegerField(null=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
         db_table = "previews"

class reachus(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    country=models.CharField(max_length=255)
    message=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    class Meta:
         db_table = "reachus"




class subscribes(models.Model):
    id=models.AutoField(primary_key=True)
    type=models.CharField(max_length=255)
    ids=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
         db_table = "subscribes"


class tbl_cities(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    state_id=models.IntegerField()
    class Meta:
         db_table = "tbl_cities"

class tbl_countries(models.Model):
    id=models.AutoField(primary_key=True)
    sortname=models.CharField(max_length=3)
    name=models.CharField(max_length=150)
    phonecode=models.IntegerField()
    class Meta:
         db_table = "tbl_countries"

class tbl_referal(models.Model):
    id=models.AutoField(primary_key=True)
    refer_user_id=models.IntegerField()
    referal_user_id=models.IntegerField()
    
    class Meta:
         db_table = "tbl_referal"

class tbl_states(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    country_id=models.IntegerField()
    
    class Meta:
         db_table = "tbl_states"

class temp_edit_winner(models.Model):
    id=models.AutoField(primary_key=True)
    user_id=models.IntegerField()
    contest_id=models.IntegerField()
    user_position=models.IntegerField()
    user_name=models.CharField(max_length=255)
    user_email=models.CharField(max_length=255)
    
    class Meta:
         db_table = "temp_edit_winner"

class users(models.Model):
    id=models.AutoField(primary_key=True)
    facebook_id=models.CharField(max_length=255,null=True,blank=True)
    google_id=models.CharField(max_length=255,null=True,blank=True)
    name=models.CharField(max_length=255,null=True,blank=True)
    full_name=models.CharField(max_length=255,null=True,blank=True)
    password=models.CharField(max_length=255,null=True,blank=True)
    profile_pic=models.FileField(default=None,null=True,blank=True)
    dob=models.DateField(default=None)
    gender=models.CharField(max_length=255,null=True,blank=True)
    house_no=models.CharField(max_length=255,null=True,blank=True)
    country=models.CharField(max_length=255,null=True,blank=True)
    state=models.CharField(max_length=255,null=True,blank=True)
    city=models.CharField(max_length=255,null=True,blank=True)
    remember_token=models.CharField(max_length=255,null=True)
    verified=models.IntegerField(default=None,null=True,blank=True)
    sendVerification=models.IntegerField(default=None,null=True,blank=True)
    token=models.CharField(max_length=255,null=True)
    user_status=models.IntegerField(default=None,null=True,blank=True)
    user_value=models.IntegerField(default=None,null=True,blank=True)
    rank_initial=models.BigIntegerField(default=None,null=True,blank=True)
    rank_final=models.BigIntegerField(default=None,null=True,blank=True)
    userpoints=models.BigIntegerField(default=None,null=True,blank=True)
    sharecount=models.BigIntegerField(default=None,null=True,blank=True)
    referral_count=models.CharField(max_length=255,default=None,null=True,blank=True)
    referral_code=models.CharField(max_length=255,default=None,null=True,blank=True)
    referral_by=models.CharField(max_length=255,default=None,null=True,blank=True)
    mobile_no=models.CharField(max_length=255,default=None,null=True,blank=True)
    mobile_otp=models.CharField(max_length=255,default=None,null=True,blank=True)
    email=models.CharField(max_length=255,default=None,null=True,blank=True)
    email_otp=models.CharField(max_length=255,default=None,null=True,blank=True)
    email_verified_at=models.DateTimeField(auto_now_add=True,null=True)
    user_type=models.IntegerField(default=None,null=True,blank=True)
    is_user_verified=models.BooleanField(default=False,null=True,blank=True)
    masterstatus=models.CharField(max_length=255,default=None,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
         db_table = "users"


class users_questions(models.Model):
    id=models.AutoField(primary_key=True)
    user_id=models.IntegerField()
    question_id=models.IntegerField()
    answer=models.CharField(max_length=255,null=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    class Meta:
         db_table = "users_questions"


class user_points(models.Model):
    id=models.AutoField(primary_key=True)
    winner=models.IntegerField(default=0)
    participate=models.IntegerField(default=0)
    correct_answer=models.IntegerField(default=0)
    wrong_answer=models.IntegerField(default=0)
    sharepoints=models.IntegerField(default=0)
    registration_pts=models.IntegerField(default=0)
    referpts=models.IntegerField(default=0)
    created=models.DateTimeField(auto_now_add=True,null=True)
    class Meta:
         db_table = "user_points"

class winners(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(users,on_delete=models.CASCADE)
    contest_id=models.IntegerField()
    email=models.CharField(max_length=255,null=True)
    prize_type=models.CharField(max_length=255,null=True)
    amount=models.CharField(max_length=255,null=True)
    amount_distribution=models.CharField(max_length=255,null=True)
    position=models.CharField(max_length=255,null=True)
    amount_type=models.CharField(max_length=255,null=True)
    user_name=models.CharField(max_length=225,null=True)
    payment=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
         db_table = "winners"