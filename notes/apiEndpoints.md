# GlobalVibes Blog API Endpoints

## Base URL: `https://your-api-base-url.com`

## Authentication Endpoints

- **Register User:** `POST /accounts/register/`
- **Login User:** `POST /accounts/login/`
- **Logout User:** `POST /accounts/logout/`
- **Change Password:** `POST /accounts/password/change/`
- **Reset Password Confirm:** `POST /accounts/password/reset/confirm/`
- **Social Login (Google):** `POST /accounts/social/login/google/`
- **Social Login (Facebook):** `POST /accounts/social/login/facebook/`
- **Social Login (GitHub):** `POST /accounts/social/login/github/`
- **User Details:** `GET /accounts/userdetails/`
- **User Details Registration:** `POST /userdetails/register/`

## Blog Endpoints

### Categories

- **List/Create Categories:** `GET/POST /api/blog/categories/`

### Blog Posts

- **List/Create Blog Posts:** `GET/POST /api/blog/blogposts/`
- **Retrieve/Update/Delete Blog Post:** `GET/PUT/DELETE /api/blog/blogposts/{post_id}/`

### Comments

- **List/Create Comments:** `GET/POST /api/blog/comments/`

### Likes and Favorites

- **Create Like for a Post:** `POST /api/blog/likes/`
- **Create Favorite for a Post:** `POST /api/blog/favorites/`

## Chat Endpoints

### Communities

- **List All Communities:** `GET /api/chat/communities/`
- **Join a Community:** `POST /api/chat/communities/join/`
- **List Community Members:** `GET /api/chat/communities/members/`
- **View Community Member Details:** `GET /api/chat/communities/members/{member_id}/`
- **Leave a Community:** `DELETE /api/chat/communities/leave/{community_id}/`
- **Send Message in a Community:** `POST /api/chat/communities/{community_id}/send/`
- **List User Chats in a Community:** `GET /api/chat/communities/{community_id}/chats/`
- **List Notifications:** `GET /api/chat/notifications/`
- **Mute/Unmute Community:** `UPDATE /api/chat/communities/{community_id}/mute/`
- **List User Communities:** `GET /api/chat/communities/user/`

## Consultation Endpoints

- **List/Create Consultations:** `GET/POST /api/consultation/consultations/`
- **Retrieve Consultation:** `GET /api/consultation/consultations/{consultation_id}/`
- **Consultation Notifications:** `GET /api/consultation/consultation-notifications/`

## Moderators Endpoints

- **List Moderators:** `GET /api/moderators/list/`
- **Promote User to Moderator:** `POST /api/moderators/promote/{user_id}/`
- **Demote User from Moderator:** `DELETE /api/moderators/demote/{user_id}/`

## Swagger Documentation

- **Swagger UI:** `GET /swagger/`
- **Redoc UI:** `GET /redoc/`
