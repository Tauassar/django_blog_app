from apps.blogs_app.models import ReadBlogs


def get_read_blogs(user):
    return ReadBlogs.objects.filter(user=user).values('blog_id')


def get_following_users_list(user):
    return user.following.all().values('id')
