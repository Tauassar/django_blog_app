import logging

from celery import shared_task
from django.contrib.auth import get_user_model

from apps.blogs_app.utils import get_feed_queryset
from apps.users_app.utils import send_digest_feed_email
from blog_app_backend.celery import app

logger = logging.getLogger(__name__)


@app.task(name='send_digest_feed_to_all_users_via_email')
def send_digest_feed_to_all_users_via_email():
    logger.info("Sending emails task initiated")
    users = get_user_model().objects.all().values('id', 'email')
    for user in users:
        logger.info(f"Sending email to {user['email']}")
        feed_queryset = get_feed_queryset(user['id'])[:5].values('title', 'body')
        send_digest_feed_email(user['email'], feed_queryset)

