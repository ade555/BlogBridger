# API Overview

## Index

- [Posts](#posts)
    - [Base URL](#base-url-apiposts)
    - [Parameters](#parameters)
    - [Response Schema](#response-schema)
    - [Endpoints](#endpoints)
        - [Create Post](#1-create-post)
        - [Update Post](#2-update-post)
        - [Retrieve Post](#3-retrieve-post)
        - [Delete Post](#4-delete-post)

# Posts

The endpoints under the posts API allow users to Create, Update, Delete, and Retrieve posts.

## Base URL: `api/posts/`

## Parameters
The following defines parameters that are general to all or most of the endpoints under the post API

**Path Parameters**
| Parameter | Data Type    | Description                              | Required |
|-----------|---------|------------------------------------------|----------|
| id        | integer | The unique ID associated with each post. | Yes      |

---

## Response Schema
The following table explains the most common response fields you will come across under the post api. Unique response fields may be documented alngside the specific endpoint(s) they apply to.

| Response field | Data Type | Description |
|----------------|---------|---------------|
|message | string | Indicates the status of the request made. It can either be successful or failed |
| data | object | Contains the resource requested |
| data/**id** | integer | Indicates the ID of the post requested or created |
| data/**post_title** | char | Indicates the title of the post requested or created. Maximum length is 50 characters |
| data/**post_body** | varchar | Indicates the body/content of the post requested or created |
| data/**created_at** | date field | Indicates the date the post was created |
| data/**author** | object | Indicates the author associated with the post. The fields returned under this object generally depends on your user model |
| data/author/**id** | integer | The unique ID associated with the author of a post |
| data/author/**first_name** | char | Author's first name. The maximum length is 150 characters, unless specified otherwise in your user model |
| data/author/**last_name** | char | Author's last name. The maximum length is 150 characters, unless specified otherwise in your user model|
| data/author/**username** | char | Author's unique username. The maximum length is 150 characters, unless specified otherwise in your user model|
| data/author/**email** | varchar | Author's unique email |

## Endpoints:
The following endpoints are related to performing CRUD operations on post objects.

### 1. Create Post

- **Endpoint**: `create/`
- **HTTP Method**: `POST`
- **Description**: Creates a new post for the user.


**Headers**

| Key          | Data Type  | Value                                                          |
|---------------|-----------|----------------------------------------------------------------|
| Authorization | String    | Set the value of this to the user's access/authentication token|

**Request Body**:

```json
{
    "post_title":"My new post",
    "post_body": "My new post is amazing and educative!"
}
```
**Request Body Definition**

| Parameter | Data Type | Description                      | Required |
|-----------|------|----------------------------------|----------|
| post_title | char | The title of the new post. Maximum value is 50 characters | Yes |
| post_body | varchar | The content of the new post | Yes |


**Responses**:

- `201 Created`: Indicates that you have successfully created a post.

```json
{
    "message": "successful",
    "data": {
        "id": 2,
        "author": {
            "id": 1,
            "first_name": "ade",
            "last_name": "Tom",
            "username": "superr",
            "email": "tomm@ade.com"
        },
        "post_title": "New post again",
        "post_body": "test body",
        "created_at": "2024-02-14"
    }
}
```
- `400 Bad Request`: Invalid input or malformed request. Check your request body and ensure you're not skipping any fields or violating any rules.
- `401 Unauthorized`: You're unauthorized to perfrom the action. Ensure you include the authentication token in your request header.
- `5XX Internal Server Error`: Unexpected server error. This shouldn't happen, so please raise an issue or make a PR if you are able to fix it.

---

### 2. Update Post

- **Endpoint**: `{post_id}/`
- **HTTP Method**: `PATCH`
- **Description**: Updates a specific post

| Parameter | Data Type | Description                      | Required |
|-----------|------|----------------------------------|----------|
| post_title | char | The updated title. Maximum value is 50 characters | No |
| post_body | varchar | The updated content of the post | No |

**NOTE**: Although both parameters are optional, you have to provide at least one of them to use this endpoint.

**Request Body**:

```json
{
    "post_title":"Updated title"
}
```

**Responses**:

- `200 OK`: Indicates a successful update operation.
- `400 Bad Request`: Invalid input or malformed request. Ensure your request body is correct. Here's a simple example:
```json
{
    "message": "failed",
    "info": {
        "non_field_errors": [
            "At least one field (post_title or post_body) must be provided for update"
        ]
    }
}
```
- `401 Unauthorized`: You're unauthorized to perform this action. ENsure you have thr right authrntication token. Only the author of a post can update it. 
- `500 Internal Server Error`: Unexpected server error. This shouldn't happen, so please raise an issue or make a PR if you are able to fix it.
---

### 3. Retrieve Post

### 4. Delete Post