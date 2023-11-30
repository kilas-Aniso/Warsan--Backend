from django.core.mail import send_mail



def send_emails(email, subject, message):
    send_mail(subject,message,'noreply@warsan.xyz',[email],fail_silently=False)


        