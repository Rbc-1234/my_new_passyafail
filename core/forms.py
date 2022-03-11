from django.contrib import admin
from .models import users,contest_category,contests,contest_sponsor,contest_price_list,blog,reachus
from django import forms


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Contestcategory_Form(forms.ModelForm):
    class Meta:
        model = contest_category
        fields = ('parent_id','name','slug','color','description','masterstatus')

class Create_Contest_Form(forms.ModelForm):
    class Meta:
        model = contests
        fields = ('category','contest_title','question','contest_venue','contest_schedule_date','contest_schedule_time','uploadContest','contest_image','contest_thumbnail','video_ad_url','prize_description','description','contest_term_conditions','no_winner','type_price','type_price_nd','contest_image_thumb','total_amount','position_amount','contestWinTitle','contestWinAmountTitle','contest_start_date','contest_start_time','contest_end_date','contest_end_time','total_amount_nd','feature_image','mobile_feature_img','sponsor_id','video_ad_type','video_ad_company','video_ad_time','video_ad_skip_time','google_ad_after_header','ad_after_header_image','ad_after_header_url','google_ad_1_sidebar','ad_1_side_image','ad_1_side_url','google_ad_2_sidebar','ad_2_side_image','ad_2_side_url','status','vac','dgc','ptg','gpk','eqamount','reamt','amount_change')


class Sponcers_Form(forms.ModelForm):
    class Meta:
        model = contest_sponsor
        fields = ('online_presense','offline_presense','brand_name','company_name','web_url','address','state','country','company_phone','company_gst','company_logo','person_name','person_designation','person_mobile','person_mail','status')

class Contest_Prize_Form(forms.ModelForm):
    class Meta:
        model = contest_price_list
        fields = ('price_name','status')

class PYF_Form(forms.ModelForm):
    class Meta:
        model = users
        fields = '__all__'

class Blog_Form(forms.ModelForm):
    class Meta:
        model = blog
        fields = '__all__'

class Reach_Form(forms.ModelForm):
    class Meta:
        model = reachus
        fields = '__all__'

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea)
        

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )