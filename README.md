# GlobalVibes Blog API Documentation

Welcome to the GlobalVibes Blog API! This API powers the GlobalVibes Blog, offering a platform to explore diverse content on various topics. Below is an overview of the available endpoints and functionalities.

## Getting Started

To get started with the GlobalVibes Blog API, follow these steps:

1.**Clone the Repository:**

```bash

   git clone https://github.com/Levi-Chinecherem/globalvibesapi.git


```

2.**Install Dependencies:**

```bash

   pip install -r requirements.txt

```

3.**Run Migrations:**

```bash

   python manage.py makemigrations

   python manage.py migrate

```

4.**Create a Superuser (for Admin Access):**

```bash

   python manage.py createsuperuser

```

5.**Run the Development Server:**

```bash

   python manage.py runserver

```

6.**Explore the API:**

- Open the [Swagger Documentation](http://localhost:8000/swagger/) for a detailed API reference.
- Utilize the [Browsable API](http://localhost:8000/api-auth/login/) for interactive testing.

## CKEditor Features

The GlobalVibes Blog API integrates CKEditor for enhanced content creation. CKEditor provides a rich set of features for Markdown editing, allowing users to create and format content seamlessly. Some notable features include:

-**Rich Text Editing:** CKEditor enables users to create content with a WYSIWYG (What You See Is What You Get) editor, making it easy to format text, add images, and more.

-**Markdown Support:** The API supports Markdown syntax for content creation. Users can leverage Markdown features to structure and style their content efficiently.

-**Image Uploads:** CKEditor facilitates the easy upload and insertion of images into blog posts. Users can enhance their content with visually appealing media.

-**Custom Styling:** CKEditor provides a customizable toolbar, allowing users to apply various styling options to their content. This includes text formatting, alignment, and more.

-**Responsive Design:** The editor ensures a responsive design, providing a consistent and user-friendly experience across devices.

Feel free to explore the CKEditor features while creating and editing blog content via the API.

---

## Table of Contents

1. [Categories](#categories)

   - [List and Create Categories](#list-and-create-categories)
2. [Blog Posts](#blog-posts)

   - [List and Create Blog Posts](#list-and-create-blog-posts)
   - [Retrieve Blog Post Details](#retrieve-blog-post-details)
3. [Comments](#comments)

   - [List and Create Comments](#list-and-create-comments)
4. [Likes and Favorites](#likes-and-favorites)

   - [Like a Post](#like-a-post)
   - [Favorite a Post](#favorite-a-post)
5. [User Authentication](#user-authentication)

   - [Register](#register)
   - [Login](#login)
   - [Logout](#logout)
   - [Change Password](#change-password)
   - [Password Reset Confirmation](#password-reset-confirmation)
   - [Social Logins](#social-logins)
   - [User Details](#user-details)
6. [Chat](#chat)

   - [Community List](#community-list)
   - [Join Community](#join-community)
   - [Send Message](#send-message)
   - [Chat History](#chat-history)
   - [Notifications](#notifications)
   - [Mute Community](#mute-community)
   - [Community Members](#community-members)
7. [Consultation](#consultation)

   - [List Consultations](#list-consultations)
   - [Consultation Details](#consultation-details)
   - [Notification for Consultations](#notification-for-consultations)
8. [Moderators](#moderators)

   - [Promote Users to Moderators](#promote-users-to-moderators)
   - [Moderator Notifications](#moderator-notifications)
   - [Moderator Chat](#moderator-chat)

## Categories

### List and Create Categories

- **Endpoint**: `/categories/`
- **HTTP Methods**: GET, POST
- **Description**: Get a list of existing categories or create a new category.
- **Authentication**: Not required for listing. Required for creation.

## Blog Posts

### List and Create Blog Posts

- **Endpoint**: `/posts/`
- **HTTP Methods**: GET, POST
- **Description**: Get a list of blog posts or create a new blog post.
- **Authentication**: Required for creation.

### Retrieve Blog Post Details

- **Endpoint**: `/posts/<int:pk>/`
- **HTTP Methods**: GET
- **Description**: Retrieve details of a specific blog post.
- **Authentication**: Not required.

## Comments

### List and Create Comments

- **Endpoint**: `/comments/`
- **HTTP Methods**: GET, POST
- **Description**: Get a list of comments or add a new comment to a blog post.
- **Authentication**: Required.

## Likes and Favorites

### Like a Post

- **Endpoint**: `/likes/`
- **HTTP Methods**: POST
- **Description**: Like a blog post.
- **Authentication**: Required.

### Favorite a Post

- **Endpoint**: `/favorites/`
- **HTTP Methods**: POST
- **Description**: Favorite a blog post.
- **Authentication**: Required.

## User Authentication

### Register

- **Endpoint**: `/register/`
- **HTTP Methods**: POST
- **Description**: Register a new user.
- **Authentication**: Not required.

### Login

- **Endpoint**: `/login/`
- **HTTP Methods**: POST
- **Description**: Log in with a registered user.
- **Authentication**: Not required.

### Logout

- **Endpoint**: `/logout/`
- **HTTP Methods**: POST
- **Description**: Log out the current user.
- **Authentication**: Required.

### Change Password

- **Endpoint**: `/password/change/`
- **HTTP Methods**: POST
- **Description**: Change the password of the current user.
- **Authentication**: Required.

### Password Reset Confirmation

- **Endpoint**: `/password/reset/confirm/`
- **HTTP Methods**: POST
- **Description**: Confirm the password reset for the user.
- **Authentication**: Not required.

### Social Logins

- **Google**: `/social/login/google/`
- **Facebook**: `/social/login/facebook/`
- **GitHub**: `/social/login/github/`
- **Description**: Log in using social media accounts.
- **Authentication**: Not required.

### User Details

- **Endpoint**: `/userdetails/`
- **HTTP Methods**: GET
- **Description**: Get details of the current user.
- **Authentication**: Required.

## Chat

### Community List

-**Endpoint**: `/communities/`

-**HTTP Methods**: GET

-**Description**: Get a list of available communities.

-**Authentication**: Not required.

### Join Community

-**Endpoint**: `/join/`

-**HTTP Methods**: POST

-**Description**: Join a community.

-**Authentication**: Required.

### Send Message

-**Endpoint**: `/send-message/<int:community_id>/`

-**HTTP Methods**: POST

-**Description**: Send a message to a community.

-**Authentication**: Required.

### Chat History

- **

Endpoint**: `/chat-history/<int:community_id>/`

-**HTTP Methods**: GET

-**Description**: Get the chat history of a community.

-**Authentication**: Required.

### Notifications

-**Endpoint**: `/notifications/`

-**HTTP Methods**: GET

-**Description**: Get notifications for new messages.

-**Authentication**: Required.

### Mute Community

-**Endpoint**: `/mute-community/<int:community_id>/`

-**HTTP Methods**: POST

-**Description**: Mute or unmute notifications for a community.

-**Authentication**: Required.

### Community Members

-**Endpoint**: `/community-members/`

-**HTTP Methods**: GET

-**Description**: Get a list of members in a community.

-**Authentication**: Required.

## Consultation

### List Consultations

-**Endpoint**: `/consultations/`

-**HTTP Methods**: GET, POST

-**Description**: Get a list of consultations or create a new consultation.

-**Authentication**: Required.

### Consultation Details

-**Endpoint**: `/consultations/<int:pk>/`

-**HTTP Methods**: GET

-**Description**: Retrieve details of a specific consultation.

-**Authentication**: Required.

### Notification for Consultations

-**Endpoint**: `/consultation-notifications/`

-**HTTP Methods**: GET

-**Description**: Get notifications for new consultation messages.

-**Authentication**: Required.

## Moderators

### Promote Users to Moderators

-**Endpoint**: `/promote-moderator/<int:user_id>/`

-**HTTP Methods**: POST

-**Description**: Promote a user to the moderator role.

-**Authentication**: Required.

### Moderator Notifications

-**Endpoint**: `/moderator-notifications/`

-**HTTP Methods**: GET

-**Description**: Get notifications for new moderator actions.

-**Authentication**: Required.

### Moderator Chat

-**Endpoint**: `/moderator-chat/`

-**HTTP Methods**: POST

-**Description**: Chat with the admin as a moderator.

-**Authentication**: Required.
