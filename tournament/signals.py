from datetime import timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Tournament, Team, Fixture

#create signal to Send an email notification to registered teams at the time of tournament creation.
@receiver(post_save, sender=Tournament)
def tournament_creation_email(sender, instance, created, **kwargs):
    if created:
        teams = Team.objects.all()
        email_addresses = [team.contact_email for team in teams]
        
        print(f"Email addresses to notify: {email_addresses}")
       
        subject = f'New Tournament Created: {instance.name}'
        message = (
            f'Dear Team,\n\n'
            f'We are excited to announce the creation of a new tournament:\n\n'
            f'Name: {instance.name}\n'
            f'Start Date: {instance.start_date}\n'
            f'End Date: {instance.end_date}\n'
            f'Location: {instance.location}\n\n'
            f'We hope to see your participation in the tournament. '
            f'Please prepare your team and ensure you are ready by the start date.\n\n'
            f'Best regards,\n'
            f'Tournament Management Team'
        )
        send_mail(
            subject=subject,
            message=message,
            from_email='tournaments.management@gmail.com',
            recipient_list=email_addresses,
            fail_silently=False,
        )

