import factory

from django.contrib.auth.hashers import make_password
from django.utils.timezone import get_current_timezone
from factory.django import DjangoModelFactory

from apps.blogs_app.models import BlogEntity
from apps.users_app.models import CustomUser


class UserFactory(DjangoModelFactory):
    class Meta:
        model = CustomUser
        django_get_or_create = ('username',)

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")
    password = make_password("default")
    username = factory.Sequence(lambda n: "Sample_user_%03d" % n)

    @factory.post_generation
    def blogs(self, create, extracted, **kwargs):
        if extracted:
            # A list of groups were passed in, use them
            for blog in extracted:
                blog.creator = self
                blog.save()
        else:
            for _ in range(10):
                BlogFactory(creator=self)

    @factory.post_generation
    def following(self, create, extracted, **kwargs):
        if extracted:
            # A list of groups were passed in, use them
            try:
                for user in extracted:
                    self.following.add(user)
            except TypeError:
                self.following.add(extracted)
        else:
            users = [UserFactory(following=(self)) for _ in range(3)]
            for user in users:
                self.following.add(user)
            return


class BlogFactory(DjangoModelFactory):
    class Meta:
        model = BlogEntity

    title = factory.Faker(
        "sentence",
        nb_words=5,
        variable_nb_words=True
    )
    created_at = factory.Faker("date_time", tzinfo=get_current_timezone())
    body = factory.Faker(
        "sentence",
        nb_words=30,
        variable_nb_words=True
    )
