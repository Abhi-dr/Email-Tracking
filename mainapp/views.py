import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Email
import uuid

@csrf_exempt
def send_email(request):
    if request.method == 'POST':
        recipient = request.POST.get('recipient')
        subject = request.POST.get('subject')
        body = request.POST.get('body')

        try:
            # Create the email message
            message = MIMEMultipart()
            message['Subject'] = subject
            message['From'] = 'anyone@gmail.com'
            message['To'] = recipient

            # Generate a unique tracking URL for the recipient
            tracking_url = f"http://whatever_your_domian.com/track_mail/{uuid.uuid4().hex}/{recipient}"

            # Create the HTML content with the tracking URL
            html_content = f"""
            <html>
            <body>
                <h1>{subject}</h1>
                <p>{body}</p>
                <img src="{tracking_url}" alt="{tracking_url}" width="1" height="1">
            </body>
            </html>
            """

            # Attach the HTML content to the email
            message.attach(MIMEText(html_content, 'html'))

            # Send the email
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login('anyone@gmail.com', 'have-to-create-app-password')
            server.sendmail('anyone@gmail.com', [recipient], message.as_string())
            server.quit()

            # Create an instance of the Email model
            email = Email(recipient=recipient, subject=subject, body=body, tracking_url=tracking_url)
            email.save()

            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return render(request, 'index.html')

@csrf_exempt
def track_mail(request, uuid, recipient):
    if request.method == 'GET':
        try:
            email = Email.objects.get(tracking_url=f"http://whatever_your_domian.com/track_mail/{uuid}/{recipient}", opened=False)
            email.opened = True
            email.save()
        except Email.DoesNotExist:
            # Handle the case where the email doesn't exist, URL doesn't match, or other error occurred
            pass

        # Return a transparent image response
        pixel = bytes.fromhex('47494638396101000100800000ffffff00ffffff21f90401000000002c00000000010001000002024401003b')
        return HttpResponse(pixel, content_type='image/gif')

    return HttpResponse('Invalid request method', status=405)