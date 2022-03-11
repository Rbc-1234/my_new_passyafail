from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import contest_category,contests,contest_price_list,contest_sponsor,users,blog,reachus
from .forms import Contestcategory_Form,Create_Contest_Form,Sponcers_Form,Contest_Prize_Form,PYF_Form,Blog_Form,Reach_Form,SignUpForm
import os
from django.shortcuts import render,redirect
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.db.models import Q
from django.db.models import Count
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
import sys

from django.views import generic
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin


from django.utils.decorators import method_decorator
from .decoraters import admin_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.contrib.auth.forms import PasswordResetForm

from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail, BadHeaderError


# Create your views here.

class Home(View):
    def get(self,requests):
        return render(requests,'core/index.html')

class Create_Contest(View):
    def get(self,requests):
        data=contests.objects.all().order_by('-id')
        contest_sp_data=contest_sponsor.objects.all()
        contast_categ_data=contest_category.objects.all()
        st=''
        mt=''
        rt=''
        gt=''
        if requests.GET.get('searchname'):
            st=requests.GET.get('searchname')
        if requests.GET.get('searchend'):
            mt=requests.GET.get('searchend')
        if requests.GET.get('username'):
            rt=requests.GET.get('username')
        if requests.GET.get('username'):
            rt=requests.GET.get('username')
            rt=int(rt)
            # print(rt)
        if requests.GET.get('newcategory'):
            gt=requests.GET.get('newcategory')
            gt=int(gt)
        

        if ((st!='')and(mt!='')):
            data=contests.objects.filter(Q(contest_start_date=st)|Q (contest_end_date=mt))
            paginator= Paginator(data,5)
            page_number=requests.GET.get('page')
            pre = paginator.get_page(page_number)
            return render(requests,'core/view-contest.html',{'pre':pre,'csd':contest_sp_data,'ccd':contast_categ_data,'st':st,'mt':mt,'rt':rt,'gt':gt})
        
        elif st!='':
            data=contests.objects.filter(contest_start_date=st)
            paginator= Paginator(data,5)
            page_number=requests.GET.get('page')
            pre = paginator.get_page(page_number)
            return render(requests,'core/view-contest.html',{'pre':pre,'csd':contest_sp_data,'ccd':contast_categ_data,'st':st,'mt':mt,'rt':rt,'gt':gt})

        elif mt!='':
            data=contests.objects.filter(contest_end_date=mt)
            paginator= Paginator(data,5)
            page_number=requests.GET.get('page')
            pre = paginator.get_page(page_number)
            return render(requests,'core/view-contest.html',{'pre':pre,'csd':contest_sp_data,'ccd':contast_categ_data,'st':st,'mt':mt,'rt':rt,'gt':gt})

        elif rt!='':
            data=contests.objects.filter(sponsor_id=rt)
            paginator= Paginator(data,5)
            page_number=requests.GET.get('page')
            pre = paginator.get_page(page_number)
            return render(requests,'core/view-contest.html',{'pre':pre,'csd':contest_sp_data,'ccd':contast_categ_data,'st':st,'mt':mt,'rt':rt,'gt':gt})
        
        elif gt!='':
            data=contests.objects.filter(category=gt)
            paginator= Paginator(data,5)
            page_number=requests.GET.get('page')
            pre = paginator.get_page(page_number)
            return render(requests,'core/view-contest.html',{'pre':pre,'csd':contest_sp_data,'ccd':contast_categ_data,'st':st,'mt':mt,'rt':rt,'gt':gt})

        else:
            data=contests.objects.all()
            paginator= Paginator(data,5)
            page_number=requests.GET.get('page')
            pre = paginator.get_page(page_number)
            return render(requests,'core/view-contest.html',{'pre':pre,'csd':contest_sp_data,'ccd':contast_categ_data,'st':st,'mt':mt,'rt':rt,'gt':gt})


class Createcontestcategory_edit(View):
    def get(self,requests,id):
        if(id==0):
            formm=Create_Contest_Form()
            concat=contest_category.objects.all()
            conpriz=contest_price_list.objects.all()
            spon=contest_sponsor.objects.all()
            return render(requests,'core/create-contest.html',{'formm':formm,'concat':concat,'conpriz':conpriz,'spon':spon})
        else:
            concat=contest_category.objects.all()
            conpriz=contest_price_list.objects.all()
            spon=contest_sponsor.objects.all()
            data=contests.objects.get(id=id)
            formm=Create_Contest_Form(instance=data)
           
            return render(requests,'core/create-contest.html',{'formm':formm,'data':data,'concat':concat,'conpriz':conpriz,'spon':spon})

    def post(self,requests,id):
        if(id==0):
            if requests.method =="POST":
                formm=Create_Contest_Form(requests.POST,requests.FILES)
                
                kr=dict(requests.POST)["reamt"]
                all_positionamount=",".join(kr)
                if formm.is_valid():
                    ct=formm.cleaned_data['category']
                    ctt=formm.cleaned_data['contest_title']
                    qu=formm.cleaned_data['question']
                    cv=formm.cleaned_data['contest_venue']
                    csd=formm.cleaned_data['contest_schedule_date']
                    cst=formm.cleaned_data['contest_schedule_time']
                    uc=formm.cleaned_data['uploadContest']
                    ci=formm.cleaned_data['contest_image']
                    cty=formm.cleaned_data['contest_thumbnail']
                    vau=formm.cleaned_data['video_ad_url']
                    pd=formm.cleaned_data['prize_description']
                    dd=formm.cleaned_data['description']
                    ctc=formm.cleaned_data['contest_term_conditions']
                    nw=formm.cleaned_data['no_winner']
                    cit=formm.cleaned_data['contest_image_thumb']
                    ta=formm.cleaned_data['total_amount']
                    eqam=formm.cleaned_data['eqamount']
                    amtredio=formm.cleaned_data['amount_change']
                    newta=formm.cleaned_data['total_amount_nd']
                    pa=formm.cleaned_data['position_amount']
                    cwt=formm.cleaned_data['contestWinTitle']
                    cwat=formm.cleaned_data['contestWinAmountTitle']
                    csdd=formm.cleaned_data['contest_start_date']
                    cstt=formm.cleaned_data['contest_start_time']
                    cedd=formm.cleaned_data['contest_end_date']
                    cett=formm.cleaned_data['contest_end_time']
                    tp=formm.cleaned_data['type_price']
                    newtp=formm.cleaned_data['type_price_nd']
                    fea=formm.cleaned_data['feature_image']
                    mob=formm.cleaned_data['mobile_feature_img']
                    sid=formm.cleaned_data['sponsor_id']
                    aat=formm.cleaned_data['vac']
                    vat=formm.cleaned_data['video_ad_type']
                    vacc=formm.cleaned_data['video_ad_company']
                    vie=formm.cleaned_data['video_ad_time']
                    vast=formm.cleaned_data['video_ad_skip_time']
                    jj=formm.cleaned_data['dgc']
                    gaah=formm.cleaned_data['google_ad_after_header']
                    aahi=formm.cleaned_data['ad_after_header_image']
                    aahu=formm.cleaned_data['ad_after_header_url']
                    adt=formm.cleaned_data['ptg']
                    gas=formm.cleaned_data['google_ad_1_sidebar']
                    asis=formm.cleaned_data['ad_1_side_image']
                    asiuu=formm.cleaned_data['ad_1_side_url']
                    wdt=formm.cleaned_data['gpk']
                    gasi=formm.cleaned_data['google_ad_2_sidebar']
                    asid=formm.cleaned_data['ad_2_side_image']
                    atp=formm.cleaned_data['ad_2_side_url']
                    stat=formm.cleaned_data['status']
                    
                    
                    
                    kr=dict(requests.POST)["reamt"]
                    all_positionamount=",".join(kr)
                    
                    if amtredio ==  'equalldivide':
                        crvk=contests(eqamount=eqam,category=ct,contest_title=ctt,question=qu,contest_venue=cv,contest_schedule_date=csd,contest_schedule_time=cst,uploadContest=uc,contest_image=ci,contest_thumbnail=cty,video_ad_url=vau,prize_description=pd,description=dd,contest_term_conditions=ctc,no_winner=nw,contest_image_thumb=cit,total_amount=ta,amount_change=amtredio,total_amount_nd=newta,position_amount=pa,contestWinTitle=cwt,contestWinAmountTitle=cwat,contest_start_date=csdd,contest_start_time=cstt,contest_end_date=cedd,contest_end_time=cett,type_price=tp,type_price_nd=newtp,feature_image=fea,mobile_feature_img=mob,sponsor_id=sid,vac=aat,video_ad_type=vat,video_ad_company=vacc,video_ad_time=vie,video_ad_skip_time=vast,dgc=jj,google_ad_after_header=gaah,ad_after_header_image=aahi,ad_after_header_url=aahu,ptg=adt,google_ad_1_sidebar=gas,ad_1_side_image=asis,ad_1_side_url=asiuu,gpk=wdt,google_ad_2_sidebar=gasi,ad_2_side_image=asid,ad_2_side_url=atp,status=stat)
                    else:
                        crvk=contests(reamt=all_positionamount,category=ct,contest_title=ctt,question=qu,contest_venue=cv,contest_schedule_date=csd,contest_schedule_time=cst,uploadContest=uc,contest_image=ci,contest_thumbnail=cty,video_ad_url=vau,prize_description=pd,description=dd,contest_term_conditions=ctc,no_winner=nw,contest_image_thumb=cit,total_amount=ta,amount_change=amtredio,total_amount_nd=newta,position_amount=pa,contestWinTitle=cwt,contestWinAmountTitle=cwat,contest_start_date=csdd,contest_start_time=cstt,contest_end_date=cedd,contest_end_time=cett,type_price=tp,type_price_nd=newtp,feature_image=fea,mobile_feature_img=mob,sponsor_id=sid,vac=aat,video_ad_type=vat,video_ad_company=vacc,video_ad_time=vie,video_ad_skip_time=vast,dgc=jj,google_ad_after_header=gaah,ad_after_header_image=aahi,ad_after_header_url=aahu,ptg=adt,google_ad_1_sidebar=gas,ad_1_side_image=asis,ad_1_side_url=asiuu,gpk=wdt,google_ad_2_sidebar=gasi,ad_2_side_image=asid,ad_2_side_url=atp,status=stat)
                    crvk.save()
                    return redirect('/view-contest')
                else:
                    return render(requests,'core/create-contest.html',{'formm':formm})
        else:
            data=contests.objects.get(id=id)
            formm=Create_Contest_Form(requests.POST,instance=data)
            
            if formm.is_valid():
                if requests.FILES.get('contest_image', False):
                    if requests.FILES.get=="":
                        os.remove(data.contest_image.path)
                    data.contest_image=requests.FILES['contest_image']

                if requests.FILES.get('contest_thumbnail', False):
                    if requests.FILES.get=="":
                        os.remove(data.contest_thumbnail.path)
                    data.contest_thumbnail=requests.FILES['contest_thumbnail']
                
                    
                
                if requests.FILES.get('contest_image_thumb', False):
                    os.remove(data.contest_image_thumb.path)
                    data.contest_image_thumb=requests.FILES['contest_image_thumb']

                if requests.FILES.get('feature_image', False):
                    os.remove(data.feature_image.path)
                    data.feature_image=requests.FILES['feature_image']

                if requests.FILES.get('mobile_feature_img', False):
                    os.remove(data.mobile_feature_img.path)
                    data.mobile_feature_img=requests.FILES['mobile_feature_img']

                if requests.FILES.get('ad_after_header_image', False):
                    os.remove(data.ad_after_header_image.path)
                    data.ad_after_header_image=requests.FILES['ad_after_header_image']

                if requests.FILES.get('ad_1_side_image', False):
                    os.remove(data.ad_1_side_image.path)
                    data.ad_1_side_image=requests.FILES['ad_1_side_image']
                
                if requests.FILES.get('ad_2_side_image', False):
                    os.remove(data.ad_2_side_image.path)
                    data.ad_2_side_image=requests.FILES['ad_2_side_image']

                formm.save()
                return redirect('/view-contest')
            else:
                return render(requests,'core/create-contest.html',{'formm':formm})

class Contest_data(View):
    def get(self,requests):
        data=contest_category.objects.all().order_by('-id')

        rt=''
        
        if requests.GET.get('searchname'):
            rt=requests.GET.get('searchname')
        if rt!='':
            data=contest_category.objects.filter(name__icontains=rt)
            paginator= Paginator(data,5)
            page_number=requests.GET.get('page')
            pre = paginator.get_page(page_number)
            return render(requests,'core/view-category.html',{'pre':pre,'rt':rt})
        else:
            data=contest_category.objects.all()
            paginator= Paginator(data,5)
            page_number=requests.GET.get('page')
            pre = paginator.get_page(page_number)
            return render(requests,'core/view-category.html',{'pre':pre,'rt':rt})


class Contestcategory_edit(View):
    def get(self,requests,id):
        if(id==0):
            
            form=Contestcategory_Form()
            concat=contest_category.objects.all()
            return render(requests,'core/create-contest-category.html',{'form':form,'concats':concat, 'concatall':concat})
        else:
            concat=contest_category.objects.get(id=id)
            concatall=contest_category.objects.all()
            form=Contestcategory_Form(instance=concat)
            return render(requests,'core/create-contest-category.html',{'form':form,'concats':concat, 'concatall':concatall})

    def post(self,requests,id):
        if(id==0):
            concat=contest_category.objects.all()
            form=Contestcategory_Form(requests.POST)
            if requests.method =="POST":
                masterstatus=requests.POST.get('masterstatus')
                searchst=contest_category.objects.filter(masterstatus=masterstatus)
            if form.is_valid():
                form.save()
                return redirect("/view-category")
            else:
                concat=contest_category.objects.all()
                name = requests.POST['name']
                slug = requests.POST['slug']
                color = requests.POST['color']
                parent_id = requests.POST['parent_id']
                description = requests.POST['description']
                obj = contest_category(name=name,slug=slug,color=color,parent_id=parent_id,description=description)
                form=Contestcategory_Form(requests.POST, instance=obj)
                return render(requests,'core/create-contest-category.html',{'error':form,'obj':obj,'concats':concat})
        else:
            concat=contest_category.objects.get(id=id)
            form=Contestcategory_Form(requests.POST,instance=concat)
            if form.is_valid():
                form.save()
                return redirect('/view-category')
            else:
                return render(requests,'core/create-contest-category.html',{'form':form,'concats':concat})


class Sponcer_Home(View):
    
    def get(self,requests):
        data=contests.objects.all()
        datacon = contests.objects.values('sponsor_id').order_by('sponsor_id').annotate(count=Count('sponsor_id'))
        
            
        pre=contest_sponsor.objects.all()
        st=''
        if requests.GET.get('searchname'):
            st=requests.GET.get('searchname')
        
        if st!='':
            pre=contest_sponsor.objects.filter(brand_name=st)
            paginator= Paginator(pre,5)
            page_number=requests.GET.get('page')
            sponsordata = paginator.get_page(page_number)
            
            return render(requests,'core/view-sponcer.html',{'sponsordata':sponsordata,'st':st,'dt':data,'datacon':datacon})
        else:
            pre=contest_sponsor.objects.all()
            paginator= Paginator(pre,5)
            page_number=requests.GET.get('page')
            sponsordata = paginator.get_page(page_number)
            
            return render(requests,'core/view-sponcer.html',{'sponsordata':sponsordata,'st':st,'dt':data,'datacon':datacon})


class Sponsor_edit(View):
    def get (self,requests,id):
        if (id==0):
            sponsorform=Sponcers_Form()
            return render(requests,'core/create-contest-sponsor.html',{'sponsorform':sponsorform})
        else:
            sponsordata=contest_sponsor.objects.get(id=id)
            sponsorform=Sponcers_Form(instance=sponsordata)
            return render(requests,'core/create-contest-sponsor.html',{'sponsorform':sponsorform,'sponsordata':sponsordata})
    def post(self,requests,id):
        if (id==0):
            sponsorform=Sponcers_Form(requests.POST, requests.FILES)
            
            if requests.method == "POST":
                sponsorform=Sponcers_Form(requests.POST, requests.FILES)
                if sponsorform.is_valid():
                    ar=sponsorform.cleaned_data['online_presense']
                    br=sponsorform.cleaned_data['offline_presense']
                    cr=sponsorform.cleaned_data['brand_name']
                    dr=sponsorform.cleaned_data['company_name']
                    er=sponsorform.cleaned_data['web_url']
                    fr=sponsorform.cleaned_data['address']
                    gr=sponsorform.cleaned_data['state']
                    hr=sponsorform.cleaned_data['country']
                    ir=sponsorform.cleaned_data['company_phone']
                    jr=sponsorform.cleaned_data['company_gst']
                    kr=sponsorform.cleaned_data['company_logo']
                    lr=sponsorform.cleaned_data['person_name']
                    mr=sponsorform.cleaned_data['person_designation']
                    nr=sponsorform.cleaned_data['person_mobile']
                    pr=sponsorform.cleaned_data['person_mail']
                    sq=sponsorform.cleaned_data['status']
                    formdata=contest_sponsor(online_presense=ar,offline_presense=br,brand_name=cr,company_name=dr,web_url=er,address=fr,state=gr,country=hr,company_phone=ir,company_gst=jr,company_logo=kr,person_name=lr,person_designation=mr,person_mobile=nr,person_mail=pr,status=sq)
                    formdata.save()
                    return redirect('/view-sponcer')
                else:
                    return render(requests,'core/create-contest-sponsor.html',{'sponsorform':sponsorform})

        else:
            sponsordata=contest_sponsor.objects.get(id=id)
            if len(requests.FILES) !=0:
                if len(sponsordata.company_logo)>0:
                    os.remove(sponsordata.company_logo.path)
                    sponsordata.company_logo=requests.FILES['company_logo']
            sponsorform=Sponcers_Form(requests.POST,instance=sponsordata)
            if sponsorform.is_valid():
                sponsorform.save()
                return redirect('/view-sponcer')
            else:
                return render(requests,'core/create-contest-sponsor.html',{'sponsorform':sponsorform})
           
            
class Contest_Prize(View):
    def get(self,requests):
        pre=contest_price_list.objects.all()
        paginator=Paginator(pre,5)
        page_number=requests.GET.get('page')
        prizedata = paginator.get_page(page_number)
        return render(requests,'core/view-contest-prize.html',{'prizedata':prizedata})

class Contest_Prize_Edit(View):
    def get(self,requests,id):
        if (id==0):
            prize_form=Contest_Prize_Form()
            return render(requests,'core/create-contest-prize.html')
        else:
            pre=contest_price_list.objects.get(id=id)
            prize_form=Contest_Prize_Form(instance=pre)
            return render(requests,'core/create-contest-prize.html',{'pre':pre})
    def post(self,requests,id):
        if(id==0):
            prize_form=Contest_Prize_Form(requests.POST)
            if requests.method =="POST":
                if prize_form.is_valid():
                    kr=prize_form.cleaned_data['price_name']
                    jk=prize_form.cleaned_data['status']
                    ktp=contest_price_list(price_name=kr,status=jk)
                    prize_form.save()
                    return redirect('/view-contest-prize')
                else:
                    return render(requests,'core/create-contest-prize.html')
        else:
            pre=contest_price_list.objects.get(id=id)
            prize_form=Contest_Prize_Form(requests.POST,instance=pre)
            if prize_form.is_valid():
                prize_form.save()
                return redirect('/view-contest-prize')
            else:
                return render(requests,'core/contest_prize_edit.html')



class PYF_Users_Home(TemplateView):
    
    def get(self,requests):
        pre=users.objects.all().order_by('-id')
        # print(pre)
        st=''
        rt=''
        gt=''
        mt=''
        if requests.GET.get('searchname'):
            st=requests.GET.get('searchname')
        if requests.GET.get('username'):
            rt=requests.GET.get('username')
        if requests.GET.get('searchh'):
            gt=requests.GET.get('searchh')  
        
        if requests.GET.get('searchend'):
            mt=requests.GET.get('searchend') 
            # print(mt)


        if ((rt!='')and(st!='')and(mt!='')and(gt!='')):
            pre=users.objects.filter(created_at__icontains=st,created_at__range=(st,mt),name__icontains=rt,is_user_verified=gt)
            paginator= Paginator(pre,5 )
            page_number=requests.GET.get('page')
            pre = paginator.get_page(page_number)
            return render(requests,'core/users.html',{'pre':pre,'st':st,'gt':gt,'rt':rt,'mt':mt})
        elif ((st!='') and (mt!='')):
            pre=users.objects.filter(created_at__range=(st,mt))
            paginator= Paginator(pre,5 )
            page_number=requests.GET.get('page')
            pre = paginator.get_page(page_number)
            return render(requests,'core/users.html',{'pre':pre,'st':st,'gt':gt,'rt':rt,'mt':mt})

        elif st!='':
            pre=users.objects.filter(created_at__icontains=st)
            paginator= Paginator(pre,5 )
            page_number=requests.GET.get('page')
            pre = paginator.get_page(page_number)
            return render(requests,'core/users.html',{'pre':pre,'rt':rt, 'st':st,'gt':gt,'mt':mt})
        elif rt!='':
            pre=users.objects.filter(name__icontains=rt)
            paginator= Paginator(pre,5 )
            page_number=requests.GET.get('page')
            pre = paginator.get_page(page_number)
            return render(requests,'core/users.html',{'pre':pre,'st':st,'rt':rt,'gt':gt,'mt':mt})
        elif gt!='':
            pre=users.objects.filter(is_user_verified=gt)
            paginator= Paginator(pre,5 )
            page_number=requests.GET.get('page')
            pre = paginator.get_page(page_number)
            return render(requests,'core/users.html',{'pre':pre,'st':st,'rt':rt,'gt':gt,'mt':mt})

        else:
            pre=users.objects.all()
            paginator= Paginator(pre,5)
            page_number=requests.GET.get('page')
            pre = paginator.get_page(page_number)
            return render(requests,'core/users.html',{'pre':pre,'st':st,'rt':rt,'gt':gt,'mt':mt})

        


class PYF_Users_Edit(View):
    def get(self,requests,id):
        if (id==0):
            userform=PYF_Form()
            return render(requests,'core/pyfuser_edit.html',{'userform':userform})
        else:
            xpdata=users.objects.get(id=id)
            
            userform=PYF_Form(instance=xpdata)
            return render(requests,'core/pyfuser_edit.html',{'userform':userform,'xpdata':xpdata})
    # def post(self,requests,id):
    #     if (id==0):
    #         userform=PYF_Form(requests.POST)
    #         print(requests.POST)
    #         if requests.method=="POST":
    #             if userform.is_valid():
    #                 ac=userform.cleaned_data['name']
    #                 ad=userform.cleaned_data['full_name']
    #                 ae=userform.cleaned_data['email']
    #                 aj=userform.cleaned_data['mobile_no']
    #                 aah=userform.cleaned_data['user_status']
                    
    #                 usertb=users(name=ac,full_name=ad,email=ae,mobile_no=aj,status=aah)
    #                 usertb.save()
    #                 return redirect('/pyf_user')
    #             else:
    #                 return render(requests,'core/pyfuser_edit.html',{'userform':userform})
class Blog_home(View):
    def get(self,requests):
        pre=blog.objects.all()
        paginator=Paginator(pre,5)
        page_number=requests.GET.get('page')
        blogdata = paginator.get_page(page_number)
        return render(requests,'core/view-blog.html',{'blogdata':blogdata})
class Blog_Edit(View):
    def get(self,requests,id):
        if (id==0):
            blogform=Blog_Form()
            return render(requests,'core/add-edit-blog.html',{'blogform':blogform})
        else:
            blogdata=blog.objects.get(id=id)
            blogform=Blog_Form(instance=blogdata)
            return render(requests,'core/add-edit-blog.html',{'blogdata':blogdata})
    
    def post(self,requests,id):
        if (id==0):
            blogform=Blog_Form(requests.POST,requests.FILES)
            
            if requests.method=="POST":
                if blogform.is_valid():
                    ab=blogform.cleaned_data['title']
                    ac=blogform.cleaned_data['titleSlag']
                    ad=blogform.cleaned_data['image']
                    af=blogform.cleaned_data['description']
                    ag=blogform.cleaned_data['meta_title']
                    ah=blogform.cleaned_data['meta_desc']
                    ai=blogform.cleaned_data['status']
                    krp=blog(title=ab,titleSlag=ac,image=ad,description=af,meta_title=ag,status=ai,meta_desc=ah)
                    krp.save()
                    return redirect('/view-blog')
                else:
                    return render(requests,'core/add-edit-blog.html',{'blogform':blogform})

        else:
            blogdata=blog.objects.get(id=id)
            
            if requests.FILES.get('image', False):
                    if requests.FILES.get=="":
                        os.remove(blogdata.image.path)
                    blogdata.image=requests.FILES['image']
            blogform=Blog_Form(requests.POST,instance=blogdata)
            if blogform.is_valid():
                blogform.save()
                return redirect('/view-blog')
            else:
                return render(requests,'core/add-edit-blog.html',{'blogform':blogform,'blogdata':blogdata})

class Reachus_home(View):
    def get(self,requests):
        pre=reachus.objects.all()
        st=''
        mt=''
        rt=''
        if requests.GET.get('searchname'):
            st=requests.GET.get('searchname')
        if requests.GET.get('searchend'):
            mt=requests.GET.get('searchend')
        if requests.GET.get('username'):
            rt=requests.GET.get('username')

        if ((st!='')and(mt!='')and(rt!='')):
            pre=reachus.objects.filter(created__icontains=st,created__range=(st,mt),name__icontains=rt)
            paginator=Paginator(pre,5)
            page_number=requests.GET.get('page')
            blogdata = paginator.get_page(page_number)
            return render(requests,'core/view-reach-Enquiries.html',{'blogdata':blogdata,'st':st,'mt':mt,'rt':rt})
        
        if ((st!='')and(mt!='')):
            pre=reachus.objects.filter(created__range=(st,mt))
            paginator=Paginator(pre,5)
            page_number=requests.GET.get('page')
            blogdata = paginator.get_page(page_number)
            return render(requests,'core/view-reach-Enquiries.html',{'blogdata':blogdata,'st':st,'mt':mt,'rt':rt})
            
        elif st!='':
            pre=reachus.objects.filter(created__icontains=st)
            paginator=Paginator(pre,5)
            page_number=requests.GET.get('page')
            blogdata = paginator.get_page(page_number)
            return render(requests,'core/view-reach-Enquiries.html',{'blogdata':blogdata,'st':st,'mt':mt,'rt':rt})
        
        elif rt!='':
            pre=reachus.objects.filter(name__icontains=rt)
            paginator=Paginator(pre,5)
            page_number=requests.GET.get('page')
            blogdata = paginator.get_page(page_number)
            return render(requests,'core/view-reach-Enquiries.html',{'blogdata':blogdata,'st':st,'mt':mt,'rt':rt})
        
        else:
            pre=reachus.objects.all()
            paginator=Paginator(pre,5)
            page_number=requests.GET.get('page')
            blogdata = paginator.get_page(page_number)
            return render(requests,'core/view-reach-Enquiries.html',{'blogdata':blogdata,'st':st,'mt':mt,'rt':rt})


class Reachus_home_form(View):
    def get(self,requests,id):
        pre=reachus.objects.get(id=id)
        
        userform=Reach_Form(instance=pre)
        return render(requests,'core/reachusform.html',{'pre':pre,'userform':userform})


def form(request):
    if request.method =="POST":
        list_for_random = range(100000)
        to=request.POST.get('toemail')
        content=request.POST.get('content')
        html_content=render_to_string("core/main.html",{'list_for_random':list_for_random, 'content':content})
        text_content=strip_tags(html_content)
        email=EmailMultiAlternatives("testing",text_content,settings.EMAIL_HOST_USER,[to])
        email.attach_alternative(html_content,"text/html")
        email.send()
        return redirect('/users')
        # return JsonResponse({'message':'mail sent'}, status=200)

               

def statusChangeUser(request):
    from django.forms.models import model_to_dict
    
    try:
        userId = int(request.POST['userId'])
        userObj = users.objects.get(id__exact=userId)
        if userObj.user_status == 0:
            userObj.user_status = 1
            userObj.save()
        else:
            userObj.user_status = 0
            userObj.save()
        return JsonResponse({'message':'success'},status=200)
    except Exception as e:
        return JsonResponse({'message':'failed'}, status=500)

def statusOfUser(request):
    from django.forms.models import model_to_dict
    from django.views.decorators.csrf import csrf_protect
    
    try:
        userId = int(request.POST['userId'])
        userObj = blog.objects.get(id__exact=userId)
        # print(userObj)
        if userObj.status == 0:
            userObj.status = 1
            userObj.save()
            messages.success(request, 'Blog is blocked successfully.')
            
        else:
            userObj.status = 0
            userObj.save()
            messages.success(request, 'Blog is activated successfully.')
        return JsonResponse({'message':'success'},status=200)
    except Exception as e:
        return JsonResponse({'message':'failed'}, status=500)
        


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/login')
        else:
            messages.error(request,"Invalid details.")

    else:
        form = SignUpForm()
    return render(request, 'core/register.html', {'form': form})



def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            if user.is_active:
                return redirect("/")
                messages.info(request, f"You are now logged in as {username}.")
            else:
                return render(request,'core/login.html',{'form':form})
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="core/login.html", context={"login_form":form})



def logout_request(request):
    logout(request)
    return redirect('/login')



def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        print(password_reset_form)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "core/password_reset_email.txt"
                    c = {
                    "email":user.email,
                    'domain':'127.0.0.1:8000',
                    'site_name': 'Website',
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "user": user,
                    'token': default_token_generator.make_token(user),
                    'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'abhishek.rai@nubiz.in' , [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
                    return redirect ("/password_reset")
            else:
                messages.error(request, 'An invalid email has been entered.')
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="core/password_reset.html", context={"password_reset_form":password_reset_form})


