# Django blog application backend

<!-- ABOUT THE PROJECT -->
## About The Project

The purpose of this project is to build back-end for the blog application with personal blogs feed. Project built with Python Django + DRF.

## Features

* Users can subscribe and unsubscribe to other people's blogs
* Users have personal blogs feed based on subscribed people's blogs
* Users can mark blogs as read
* Read blogs do not appear in personal blogs feed of user
* On blog's creation and deletion blogs feed of subscribed users refreshes

## API

Application have a list of following API to interact:

### User token

**POST**
* api/auth/token - Obtain auth token
* api/auth/token/refresh - Refresh auth token


### Subscriptions entity
**GET**
* api/user/subscription - Get subscriptions list

**POST**
* api/user/subscription - Subscribe to user

**DELETE**
* api/user/subscription/<id> - Unsubscribe from user


### Blogs entity
**GET**
* api/blogs/ - Get list of own blogs
* api/blogs/<id> - Get particular blog
* api/blogs/read - Get list of read blogs
* api/blogs/read/<id> - Get particular read blog
* api/blogs/blogs_feed - Get list of blogs from personal blogs feed

**POST**
* api/blogs/ - to create new blog
* api/blogs/read - to mark blog as read

**DELETE**
* api/blogs/<id> - for deleting blog
* api/blogs/read/<id> - to unmark blog as read


<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

To run this project you need to have docker and docker-compose installed on your computer.

### Installation

1. Clone the repo
   ```sh
   git clone git@github.com:Tauassar/django_blog_app.git
   ```
2. Run docker-compose
   ```sh
   docker-compose up --build
   ```
<br/>

### Adding superuser to django application

To add superuser we need to connect to container with django application, web_app in this case, and run appropriate command.

1. Locate container's ID
   ```sh
   docker ps --filter "name=django_blog_app_web_app"
   ```
2. Run docker-compose
   ```sh
   docker exec -it <container ID> bash
   ```
3. Run django manage.py command to initiate creation of superuser
   ```sh
   python3 blog_app_backend/manage.py createsuperuser
   ```
After you need to fill requested information in interactive terminal window. 

<br/>

### Populate database with test data


1. Locate container's ID
   ```sh
   docker ps --filter "name=django_blog_app_web_app"
   ```
2. Run docker-compose
   ```sh
   docker exec -it <container ID> bash
   ```
3. Run django manage.py command to initiate creation of superuser
   ```sh
   python3 blog_app_backend/manage.py generate_test_data
   ```
This command adds 300 test users with 10 blog posts and 3 subscriptions each.


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

