from django.shortcuts import render , redirect
from django.views import  View
from django.contrib.auth.decorators import login_required
from store.models.customer import Newletter
from django.core.mail import send_mail


def home_page(request):
    return render(request,"index.html")

def lock_page(request):
    return render(request,"home.html")


def lockbefore_page(request):
    return render(request,"lockhome.html")

def service_page(request):
    return render(request,"services.html")


def courses_page(request):
    return render(request,"course.html")


def contact_page(request):
    return render(request,"contact.html")
  
def aboutus_page(request):
    return render(request,"about.html")

def career_page(request):
     if request.method == "POST":
        recipient_email = request.POST.get('recipient_email')
        career_page = Newletter(recipient_email=recipient_email)
        career_page.save()
        admin_email_subject = 'Subscribe From Inner_uplift Newsletter'
        admin_email_message = (
            f'New subscribtion from newsletter: {recipient_email}\n'

        )
        send_mail(
            admin_email_subject,
            admin_email_message,
            'bhupeshther5@gmail.com',
            ['bhupeshther5@gmail.com'],  # Replace with the admin's email address
            fail_silently=False,
        )

        # Send a confirmation email to the user
        user_email_subject = 'Subscribe Inner_uplift Newsletter'
        user_email_message = (
            f'You have successfully subscribed to the Inner_uplift Newsletter with the email address: {recipient_email}\n'
            f'Thank you for subscribing to Inner_uplift Newsletter.\n'
            f'For more information, connect with us at bhupeshther5@gmail.com'
        )
        send_mail(
            user_email_subject,
            user_email_message,
            'bhupeshther5@gmail.com',  # Replace with your sender email address
            [recipient_email],
            fail_silently=False,
        )

     return render(request, "career.html")
  
def job_list_page(request):
    return render(request,"job_list.html")

def payments_page(request):
    return render(request,"payments.html")

def adhd_quiz(request):
    return render(request,"adhd_quiz.html")


def store_books_poadcast(request):
    return render(request,"bookspoadcast.html")
  
from django.core.mail import send_mail

def contact_email(request):
    # Assuming your form fields are named 'name', 'email', 'subject', and 'message'
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    message = request.POST.get('user_msg')

    # Send email
    send_mail(
        f'Message from {name} ',
        f"Subject: {subject}\nUser message: {message}\nUser email: {email}",
            email,
        {'bhupeshther5@gmail.com'} # This should be a list or tuple   # Replace with the recipient's email
    )

    return redirect("contactpage")#    else:
#     return render(request, 'contact.html')


@login_required(login_url='/adhd/login/')
def adhd_quiz(request):
    return render(request,"adhd_quiz.html")

def anxiety_quiz(request):
    return render(request, "anxiety_quiz.html")

def bipolar_quiz(request):
    return render(request,"bipolar_quiz.html")

def eatingdisorder_quiz(request):
    return render(request,"eatingdisorder_quiz.html")


def ocd_quiz(request):
    return render(request,"ocd_quiz.html")

def panicdisorder_quiz(request):
    return render(request,"panicdisorder_quiz.html")

def schizoprenia_quiz(request):
    return render(request,"schizoprenia_quiz.html")

def blog(request):
    return render(request,"blog.html")

def Creative_Part(request):
    return render(request, "Creative-Part.html")

def forms_py(request):
    return render(request, "forms.py.html")

def forgot(request):
    return render(request, "forgot.html")

def job_content_writer(request):
    return render(request, "job-Content-Writer.html")

def job_creative(request):
    return render(request, "job-Creative.html")

def job_customer_service(request):
    return render(request,"job-Customer-Service.html")

def job_detail(request):
    return render(request, "job-detail.html")

def job_detail_part(request):
    return render(request,"job-detail-part.html")

def job_financial_Analyst(request):
    return render(request,"job-Financial_Analyst.html")

def job_human_resources(request):
    return render(request,"job-Human_Resources.html")

def job_product_designer(request):
    return render(request,"job-Product-Designer.html")

def job_software(request):
    return render(request,"job-software.html")

def job_software_part(request):
    return render(request,"job-software-part.html")

def job_wordpress(request):
    return render(request, "job-wordpress.html")

def product_designer_part(request):
    return render(request, "Product-Designer-part.html")

def registration(request):
    return render(request, "registration.html")

def sales(request):
    return render(request, "sales.html")

def wordpress_part(request):
    return render(request, "wordpress-part.html")

def success(request):
    return render(request, "success.html")






from django.http import HttpResponse

def css_view(request):
    content = "./css/css" 
    response = HttpResponse(content, content_type='text/css')
    return response