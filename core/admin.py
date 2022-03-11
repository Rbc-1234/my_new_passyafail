# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register([become_sponsor,blog,contests,contests_old,contest_category,contest_price_list,contest_prizes,contest_sponsor,failed_jobs,global_ads,global_ads_login,global_ads_profile,jobs,knowledge_center,leaderboard,mailerhtml,migrations,password_resets,previews,reachus,sponsors,subscribes,tbl_cities,tbl_countries,tbl_referal,tbl_states,temp_edit_winner,users,users_questions,user_points,winners])