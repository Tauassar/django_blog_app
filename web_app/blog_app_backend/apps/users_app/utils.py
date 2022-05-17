import logging

logger = logging.getLogger(__name__)


def compose_email(blog_list):
    """
    Prepare email body text
    :param blog_list:
    :return: email_body: String
        Body text of email message
    """
    if len(blog_list):
        email_body = "Hi, have a look at blogs from your feed:\n"
        for blog in blog_list:
            blog_string = f'\n{blog["title"]}\n{blog["body"]}\n'
            email_body += blog_string
        return email_body
    else:
        raise ValueError('Blog list is empty')


def send_digest_feed_email(email, blog_list):
    """
    Stub for sending email for particular user
    :param email: String
    Receiver's email
    :param blog_list:
    List of blogs to include in email
    :return: None
    """
    try:
        email_content = compose_email(blog_list)
        logger.info(f'\nEmail to user {email}:\n{email_content}')
    except ValueError as e:
        logger.info(f'User {email} have no blogs in feed, {e}')
