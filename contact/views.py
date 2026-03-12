from django.shortcuts import render,redirect
from .models import ContactMessage, Subscriber
from django.contrib import messages

def contact_view(request):
    if request.method == 'POST':
        # Extracting data using the exact 'name' attributes from your HTML
        full_name = request.POST.get('full-name')
        email = request.POST.get('email')
        message_text = request.POST.get('message')

        # Saving to the database
        ContactMessage.objects.create(
            full_name=full_name,
            email=email,
            message=message_text
        )

        messages.success(request, "Success! Your message has been sent.")
        return redirect('contact_page')  # Redirect back to the form or a success page
    
    return redirect('home')

def subscribe_view(request):
    # If you keep 'get', use request.GET; if you change to 'post', use request.POST
    email = request.GET.get('email')
    
    if email:
        # get_or_create prevents errors if the same person clicks subscribe twice
        obj, created = Subscriber.objects.get_or_create(email=email)
        if created:
            messages.success(request, "Thanks for joining our ThinkTank newsletter!")
        else:
            messages.info(request, "You are already subscribed!")
            
    return redirect('home') # Change 'home' to the name of your index URL