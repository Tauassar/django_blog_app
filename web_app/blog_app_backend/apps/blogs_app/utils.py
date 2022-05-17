from django.contrib.auth import get_user_model

from apps.blogs_app.models import ReadBlogs, BlogEntity


def get_read_blogs(user):
    """
    Retrieve user's read blogs list
    :param user: Object
    User, who's read blogs is going to be retrieved
    :return: read_blogs: QuerySet
    List of read blogs for particular user
    """
    return ReadBlogs.objects.filter(user=user).values('blog_id')


def get_following_users_list(user):
    """
    Retrieving user's following list
    :param user: Object
    User, who's following list is going to be retrieved
    :return: following_list: QuerySet
    List of users who is being followed by particular user
    """
    return user.following.all().values('id')


def get_feed_queryset(user_id):
    """
    Filtering data for reading blog feed
    :param user_id: int
        ID of user, for whom to retrieve blog feed
    :return: queryset: QuerySet
        Blog feed queryset
    """
    user = get_user_model().objects.get(id=user_id)
    following_users_list = get_following_users_list(user)
    to_exclude = get_read_blogs(user)

    return BlogEntity.objects.filter(
        creator_id__in=following_users_list
    ).exclude(id__in=to_exclude).order_by('-created_at')
