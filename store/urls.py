from django.contrib import admin
from django.urls import path
from .views.home import Index , store
from .views.signup import Signup
from .views.login import Login , logouts
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .middlewares.auth import  auth_middleware
from .views.basiclink import *
from .views.payment import Payment

urlpatterns = [
    path('home', home_page, name='home_page'),    
    path('', Index.as_view(), name='homepage'),
    path('store', store , name='store'),

#basic link  
    path('lock', lockbefore_page , name='loked_page'),
    path('cources', courses_page, name='coursespage'),
    path('contact', contact_page, name='contactpage'),
    path('services',service_page,name="services_page"),
    path('about',aboutus_page,name="aboutus_page"),
    path('career',career_page,name="career_page"),
    path('jobs/list',job_list_page,name="joblist_page"),
    path('payments',auth_middleware(payments_page),name="payments_page"),
    path("mail/submitted",contact_email,name="contact_email_send"),
    path('adhd/quiz',auth_middleware(adhd_quiz), name='adhd_quiz'),
#end basic link  
    path('signup', Signup.as_view(), name='signup'),
    path('payment', Payment.as_view(), name='payment_page'), #/////////////////////////
    path('login', Login.as_view(), name='login'),
    path('logout', logouts , name='logout'),
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
#  Quizes and job details 
    path('adhd_quiz',auth_middleware(adhd_quiz), name='adhd_quiz'),
    path('anxiety_quiz',auth_middleware(anxiety_quiz), name='anxiety_quiz'),
    path('bipolar_quiz',auth_middleware(bipolar_quiz), name='bipolar_quiz'),
    path('eatingdisorder_quiz',auth_middleware(eatingdisorder_quiz), name='eatingdisorder_quiz'),
    path('ocd_quiz',auth_middleware( ocd_quiz), name='ocd_quiz'),
    path('panicdisorder_quiz',auth_middleware(panicdisorder_quiz), name='panicdisorder_quiz'),
    path('schizoprenia_quiz',auth_middleware( schizoprenia_quiz), name='schizoprenia_quiz'),
    path('blog', blog, name='blog'),
    path('Creative_Part',auth_middleware(Creative_Part), name='Creative_Part'),
    path('forms_py',auth_middleware(forms_py), name='forms_py'),
    path('forgot', forgot, name='forgot'),
    path('job_content_writer',auth_middleware(job_content_writer), name='job_content_writer'),
    path('job_creative',auth_middleware(job_creative), name='job_creative'),
    path('job_customer_service',auth_middleware(job_customer_service), name='job_customer_service'),
    path('job_detail',auth_middleware(job_detail), name='job_detail'),
    path('job_detail_part',auth_middleware(job_detail_part), name='job_detail_part'),
    path('job_financial_Analyst',auth_middleware(job_financial_Analyst), name='job_financial_Analyst'),
    path('job_human_resources',auth_middleware(job_human_resources), name='job_human_resources'),
    path('job_product_designer',auth_middleware(job_product_designer), name='job_product_designer'),
    path('job_software',auth_middleware(job_software), name='job_software' ),
    path('job_software_part',auth_middleware(job_software_part), name='job_software_part'),
    path('job_wordpress',auth_middleware(job_wordpress), name='job_wordpress'),
    path('product_designer_part',auth_middleware(product_designer_part), name='product_designer_part'),
    path('registration', registration, name='registration'),
    path('sales',auth_middleware(sales), name='sales'),
    path('wordpress_part',auth_middleware(wordpress_part), name='wordpress_part'),
    path('success', success, name='success'),
#  Quizes and job details 
]


