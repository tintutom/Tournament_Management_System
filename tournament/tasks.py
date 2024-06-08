from celery import shared_task
from django.core.mail import send_mail
from .models import Fixture
import logging

logger = logging.getLogger(__name__)

@shared_task
def matchday_notification(fixture_id):
    try:
        logger.info(f"Starting to process fixture_id: {fixture_id}")
        fixture = Fixture.objects.get(id=fixture_id)
        teams = fixture.teams.all()
        email_addresses = [team.contact_email for team in teams]
        logger.info(f"Email addresses to notify: {email_addresses}")
        
        subject = f'Matchday Notification: {fixture.tournament.name}'
        message = (
            f'Dear Team,\n\n'
            f'This is a reminder for your upcoming match in the tournament "{fixture.tournament.name}".\n\n'
            f'Details of the match are as follows:\n'
            f'Date: {fixture.date}\n'
            f'Time: {fixture.time}\n'
            f'Location: {fixture.location}\n\n'
            f'Please be prepared and arrive on time with the registered team mates.\n\n'
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
        logger.info("Email sent successfully")
    except Exception as e:
        logger.error(f"Failed to send email: {e}")
