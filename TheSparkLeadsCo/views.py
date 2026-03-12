from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from contact.models import ContactMessage, Subscriber

def home_view(request):
    """
    Renders the ThinkTank landing page.
    """
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        member_id = request.POST.get('member-login-number')
        password = request.POST.get('member-login-password')
        remember_me = request.POST.get('remember_me') # Get the checkbox value

        user = authenticate(request, username=member_id, password=password)

        if user is not None:
            login(request, user)
            
            # If "Remember me" is not checked, session expires on browser close
            if not remember_me:
                request.session.set_expiry(0)
            
            messages.success(request, "Access Granted. Welcome back.")
            
            # Logic to separate Admin from Member
            if user.is_staff:
                return redirect('admin_dashboard')
            return redirect('home')
        else:
            messages.error(request, "Authentication Failed. Please check your ID and Password.")
            
    return redirect('home')


@staff_member_required
def admin_dashboard(request):
    # Fetching all data
    messages = ContactMessage.objects.all().order_by('-created_at')
    subscribers = Subscriber.objects.all().order_by('-subscribed_at')
    
    return render(request, 'admin_dashboard.html', {
        'contact_messages': messages,
        'subscribers': subscribers
    })

@staff_member_required
def delete_message(request, id):
    get_object_or_404(ContactMessage, id=id).delete()
    return redirect('admin_dashboard')

@staff_member_required
def delete_subscriber(request, id):
    get_object_or_404(Subscriber, id=id).delete()
    return redirect('admin_dashboard')

from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    messages.info(request, "You have been successfully logged out.")
    return redirect('login') # Redirects back to your login page