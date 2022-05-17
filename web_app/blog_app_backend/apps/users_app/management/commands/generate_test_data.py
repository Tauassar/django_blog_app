import logging

from django.core.management.base import BaseCommand
from django.db import transaction

from blog_app_backend.test_data_factories import UserFactory

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    NUM_USERS = 300

    @transaction.atomic()
    def create_users(self):
        people = []
        for _ in range(self.NUM_USERS):
            person = UserFactory()
            people.append(person)
        return people

    def handle(self, **options):
        logger.info("Starting to generate test data")
        self.create_users()
        print("Generation of test data finished")
