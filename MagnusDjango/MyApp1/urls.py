from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('help/',views.help,name='help'),
    path('contact/',views.contact,name='contact'),
    path('emp/',views.emp,name="emp"),
    path('dept/',views.dept,name="dept"),
    path('user/',views.form_page,name='UserForm'),
    path('empform/',views.emp_formpage,name="empform"),



]
