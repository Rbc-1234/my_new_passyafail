from core import views
from django.urls import path


from .views import logout_request,Home,Contest_data,Contestcategory_edit,Create_Contest,Createcontestcategory_edit,Sponcer_Home,Sponsor_edit,Contest_Prize,Contest_Prize_Edit,PYF_Users_Home,PYF_Users_Edit,form,Blog_home,Blog_Edit,Reachus_home,Reachus_home_form
from . import views as core_views
from .decoraters import admin_required

urlpatterns = [
   
    path('',admin_required(Home.as_view()),name="index"),
    path('view-category', admin_required(Contest_data.as_view()), name='view-category'),
    path('create-contest-category/<int:id>/',admin_required(Contestcategory_edit.as_view()),name="create-contest-category"),
    path('view-contest', admin_required(Create_Contest.as_view()), name='view-contest'),
    path('create-contest/<int:id>/',admin_required(Createcontestcategory_edit.as_view()),name="create-contest"),
    path('view-sponcer', admin_required(Sponcer_Home.as_view()), name='view-sponcer'),
    path('create-contest-sponsor/<int:id>/',admin_required(Sponsor_edit.as_view()),name="create-contest-sponsor"),
    path('view-contest-prize', admin_required(Contest_Prize.as_view()), name='view-contest-prize'),
    path('create-contest-prize/<int:id>/',admin_required(Contest_Prize_Edit.as_view()),name="create-contest-prize"),
    path('users', admin_required(PYF_Users_Home.as_view()), name='users'),
    path('pyfuser_edit/<int:id>/', admin_required(PYF_Users_Edit.as_view()), name='pyfuser_edit'),
    path('logout/', logout_request, name='logout'),
    path('home2', views.form, name='home2'),
    path('statusChangeUser', views.statusChangeUser, name='statusChangeUser'),
    path('statusOfUser', views.statusOfUser, name='statusOfUser'),
    path('view-blog', admin_required(Blog_home.as_view()), name='view-blog'),
    path('add-edit-blog/<int:id>/', admin_required(Blog_Edit.as_view()), name='add-edit-blog'),
    path('view-reach-Enquiries', admin_required(Reachus_home.as_view()), name='view-reach-Enquiries'),
    path('reachusform/<int:id>/', admin_required(Reachus_home_form.as_view()), name='reachusform'),
    path('register',core_views.signup, name='register'),
    path('login', views.login_request, name='login'),
    path("password_reset", views.password_reset_request, name="password_reset")
    
 
]