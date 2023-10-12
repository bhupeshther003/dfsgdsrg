from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import View
from django.core.mail import send_mail
from django.contrib.auth import logout


class Login(View):
    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get ('return_url')
        return render (request, 'login.html')

    def post(self, request):
        email = request.POST.get ('email')
        password = request.POST.get ('password')
        customer = Customer.get_customer_by_email (email)
        user_agent = request.META.get('HTTP_USER_AGENT', 'Unknown User Agent')
        user_ip = request.META.get('REMOTE_ADDR', 'Unknown IP Address')
        error_message = None
        if customer:
            flag = check_password (password, customer.password)
            if flag:
                request.session['customer'] = customer.id

                if Login.return_url:
                    return HttpResponseRedirect (Login.return_url)
                else:
                    Login.return_url = None
                    send_mail(
                        subject='Login Successful on InnerUplift',
                        message=f'Hello {customer.first_name} {customer.last_name},\n\n'
                                f'You have successfully logged into your InnerUplift account from the following device:\n\n'
                                f'User Agent (Browser): {user_agent}\n'
                                f'IP Address: {user_ip}\n\n'
                                f'If this login was not initiated by you, please contact our support team immediately.\n\n'
                                f'Thank you for using InnerUplift!\n\n'
                                f'Warm regards,\nInner Uplift \nbhupeshthe5@gmail.com',
                        from_email='bhupeshther5@gmail.com',  # Replace with your email
                        recipient_list=[email],
                        )
                return HttpResponseRedirect('home')
            else:
                error_message = 'Invalid !!'
        else:
            error_message = 'Invalid !!'
        

        print (email, password)
        return render (request, 'login.html', {'error': error_message})


def logouts(request):
    # if request.user.is_authenticated:
    #     # Access the Customer object associated with the authenticated user
    #     customer = request.user.customer

    #     # Get the email and name from the Customer object
    #     email = customer.email
    #     full_name = f"{customer.first_name} {customer.last_name}"

    #     # Send the email
    #     send_mail(
    #         subject='Logout Notification from InnerUplift',
    #         message=f'Hello {full_name},\n\n'
    #                 f'You have successfully logged out from your InnerUplift account. If this logout was not initiated by you, please contact our support team immediately.\n\n'
    #                 f'Thank you for using InnerUplift!\n\n'
    #                 f'Warm regards,\nInner Uplift',
    #         from_email='bhupeshther5@gmail.com',  # Replace with your email
    #         recipient_list=[email],
    #     )
        
    #     # Logout the user
    request.session.clear()

    return redirect('login')