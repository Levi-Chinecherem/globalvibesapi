
# GlobalVibes Blog API Endpoints

Below are detailed explanations for each of the provided API endpoints, intended to guide frontend developers in utilizing the GlobalVibes Blog API:

### Base URL: `https://your-api-base-url.com`

This is the base URL for all API requests. will be updated when hosted.

---

### Authentication Endpoints

#### Register User: `POST /accounts/register/`

- **Description:** Allows users to register a new account.
- **Request:** Send a POST request with user details (email, password, etc.).
- **Response:** Returns user details on successful registration.

#### Login User: `POST /accounts/login/`

- **Description:** Enables users to log in.
- **Request:** Requires a POST request with user credentials.
- **Response:** Provides an authentication token on successful login.

#### Logout User: `POST /accounts/logout/`

- **Description:** Logs out the authenticated user.
- **Request:** Requires a POST request with a valid authentication token.
- **Response:** Indicates successful logout.

#### Change Password: `POST /accounts/password/change/`

- **Description:** Allows users to change their account password.
- **Request:** Requires a POST request with the old and new passwords.
- **Response:** Confirms successful password change.

#### Reset Password Confirm: `POST /accounts/password/reset/confirm/`

- **Description:** Confirms the reset of a user's password.
- **Request:** POST request with a reset token and new password.
- **Response:** Indicates successful password reset confirmation.

#### Social Login (Google): `POST /accounts/social/login/google/`

- **Description:** Enables users to log in using their Google accounts.
- **Request:** Requires a POST request with Google authentication details.
- **Response:** Returns user details and authentication token on successful login.

#### Social Login (Facebook): `POST /accounts/social/login/facebook/`

- **Description:** Allows users to log in using their Facebook accounts.
- **Request:** Requires a POST request with Facebook authentication details.
- **Response:** Returns user details and authentication token on successful login.

#### Social Login (GitHub): `POST /accounts/social/login/github/`

- **Description:** Enables users to log in using their GitHub accounts.
- **Request:** Requires a POST request with GitHub authentication details.
- **Response:** Returns user details and authentication token on successful login.

#### User Details: `GET /accounts/userdetails/`

- **Description:** Retrieves details of the authenticated user.
- **Request:** Requires a GET request with a valid authentication token.
- **Response:** Returns user details.

#### User Details Registration: `POST /userdetails/register/`

- **Description:** Allows users to provide additional details after registration.
- **Request:** Requires a POST request with additional user details.
- **Response:** Confirms successful registration of user details.

---

### Blog Endpoints

#### Categories

##### List/Create Categories: `GET/POST /api/blog/categories/`

- **Description:** Fetches existing blog categories or creates a new one.
- **Request:** GET for listing, POST for creating, with appropriate data.
- **Response:** Returns a list of categories or confirms category creation.

#### Blog Posts

##### List/Create Blog Posts: `GET/POST /api/blog/blogposts/`

- **Description:** Retrieves existing blog posts or creates a new one.
- **Request:** GET for listing, POST for creating, with appropriate data.
- **Response:** Returns a list of blog posts or confirms post creation.

##### Retrieve/Update/Delete Blog Post: `GET/PUT/DELETE /api/blog/blogposts/{post_id}/`

- **Description:** Fetches, updates, or deletes a specific blog post.
- **Request:** GET for fetching, PUT for updating, DELETE for deletion.
- **Response:** Returns post details, confirms update, or indicates successful deletion.

#### Comments

##### List/Create Comments: `GET/POST /api/blog/comments/`

- **Description:** Retrieves existing comments or adds a new one.
- **Request:** GET for listing, POST for creating, with appropriate data.
- **Response:** Returns a list of comments or confirms comment creation.

#### Likes and Favorites

##### Create Like for a Post: `POST /api/blog/likes/`

- **Description:** Registers a like for a specific blog post.
- **Request:** Requires a POST request with post ID.
- **Response:** Confirms successful creation of a like.

##### Create Favorite for a Post: `POST /api/blog/favorites/`

- **Description:** Marks a blog post as a favorite for the user.
- **Request:** Requires a POST request with post ID.
- **Response:** Confirms successful creation of a favorite.

---

### Chat Endpoints

#### Communities

##### List All Communities: `GET /api/chat/communities/`

- **Description:** Fetches a list of all available chat communities.
- **Request:** Requires a GET request.
- **Response:** Returns a list of chat communities.

##### Join a Community: `POST /api/chat/communities/join/`

- **Description:** Allows a user to join a specific chat community.
- **Request:** Requires a POST request with community details.
- **Response:** Confirms successful community join.

##### List Community Members: `GET /api/chat/communities

/members/`

- **Description:** Fetches a list of members in the community.
- **Request:** Requires a GET request.
- **Response:** Returns a list of community members.

##### View Community Member Details: `GET /api/chat/communities/members/{member_id}/`

- **Description:** Retrieves details of a specific community member.
- **Request:** Requires a GET request with member ID.
- **Response:** Returns details of the community member.

##### Leave a Community: `DELETE /api/chat/communities/leave/{community_id}/`

- **Description:** Allows a user to leave a specific chat community.
- **Request:** Requires a DELETE request with community ID.
- **Response:** Confirms successful community departure.

##### Send Message in a Community: `POST /api/chat/communities/{community_id}/send/`

- **Description:** Sends a message in a specific chat community.
- **Request:** Requires a POST request with message details.
- **Response:** Confirms successful message sending.

##### List User Chats in a Community: `GET /api/chat/communities/{community_id}/chats/`

- **Description:** Retrieves a list of user chats within a community.
- **Request:** Requires a GET request with community ID.
- **Response:** Returns a list of user chats.

##### List Notifications: `GET /api/chat/notifications/`

- **Description:** Retrieves a list of notifications for the user.
- **Request:** Requires a GET request.
- **Response:** Returns a list of notifications.

##### Mute/Unmute Community: `UPDATE /api/chat/communities/{community_id}/mute/`

- **Description:** Allows the user to mute or unmute a specific community.
- **Request:** Requires an UPDATE request with mute status.
- **Response:** Confirms successful mute/unmute operation.

##### List User Communities: `GET /api/chat/communities/user/`

- **Description:** Fetches a list of communities associated with the user.
- **Request:** Requires a GET request.
- **Response:** Returns a list of user communities.

---

### Consultation Endpoints

#### List/Create Consultations: `GET/POST /api/consultation/consultations/`

- **Description:** Fetches existing consultations or creates a new one.
- **Request:** GET for listing, POST for creating, with appropriate data.
- **Response:** Returns a list of consultations or confirms consultation creation.

#### Retrieve Consultation: `GET /api/consultation/consultations/{consultation_id}/`

- **Description:** Retrieves details of a specific consultation.
- **Request:** Requires a GET request with consultation ID.
- **Response:** Returns details of the consultation.

#### Consultation Notifications: `GET /api/consultation/consultation-notifications/`

- **Description:** Retrieves a list of notifications for consultations.
- **Request:** Requires a GET request.
- **Response:** Returns a list of consultation notifications.

---

### Moderators Endpoints

#### List Moderators: `GET /api/moderators/list/`

- **Description:** Fetches a list of all moderators.
- **Request:** Requires a GET request.
- **Response:** Returns a list of moderators.

#### Promote User to Moderator: `POST /api/moderators/promote/{user_id}/`

- **Description:** Promotes a user to the role of a moderator.
- **Request:** Requires a POST request with user ID.
- **Response:** Confirms successful promotion.

#### Demote User from Moderator: `DELETE /api/moderators/demote/{user_id}/`

- **Description:** Demotes a user from the role of a moderator.
- **Request:** Requires a DELETE request with user ID.
- **Response:** Confirms successful demotion.

---

### Swagger Documentation

#### Swagger UI: `GET /swagger/`

- **Description:** Accesses Swagger UI for interactive API documentation.
- **Request:** Requires a GET request.
- **Response:** Opens the Swagger UI for exploring the API.

#### Redoc UI: `GET /redoc/`

- **Description:** Accesses ReDoc UI for user-friendly API documentation.
- **Request:** Requires a GET request.
- **Response:** Opens the ReDoc UI for simplified API exploration.

---

These detailed explanations are designed to assist frontend developers in understanding and utilizing the various functionalities provided by the GlobalVibes Blog API. Ensure to follow the specified request formats and handle responses appropriately for seamless integration.
