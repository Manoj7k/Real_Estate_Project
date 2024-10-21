from django.shortcuts import render, redirect
from .forms import AgentRegistrationForm, InquiryForm
from django.core.mail import send_mail
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

def home(request):
    return render(request, 'bulklands/home.html')

def agent_registration(request):
    if request.method == 'POST':
        form = AgentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail(
                'New Agent Registration',
                f"Agent {form.cleaned_data['name']} has registered.",
                settings.EMAIL_HOST_USER,
                ['tulasirao@gmail.com'],
            )
            return redirect('home')
    else:
        form = AgentRegistrationForm()
    return render(request, 'bulklands/registration.html', {'form': form})


def inquiry(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            
            # Prepare email content
            subject = 'New Inquiry Submission'
            message = f"""
                You have received a new inquiry:
                Name: {form.cleaned_data['name']}
                Mobile Number: {form.cleaned_data['mobile_number']}
                WhatsApp Number: {form.cleaned_data['whatsapp_number']}
                Email: {form.cleaned_data['email']}
                I Want to: {form.cleaned_data['property_type']}
                Property: {form.cleaned_data['property_category']}
                Location: {form.cleaned_data['location']}
                Square Yards/Acres: {form.cleaned_data['square_yards']}
                Budget Range: {form.cleaned_data['budget_range']}
            """
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [form.cleaned_data['email']]  # Sending to the email provided in the form
            
            # Send the email
            try:
                send_mail(subject, message, from_email, recipient_list)
                return JsonResponse({'message': 'Inquiry submitted and email sent successfully!'}, status=200)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)  # Return error if sending fails

        else:
            return JsonResponse({'errors': form.errors}, status=400)

    form = InquiryForm()
    return render(request, 'bulklands/inquiry.html', {'form': form})