# API Overview

## Index

- [Posts](#posts)
    - [Base URL](#base-url-apiposts)
    - [Parameters](#parameters)
    - [General Response Schema](#response-schema)
    - [Endpoints](#endpoints)
        - [Create Post](#1-create-post)
        - [Get All Posts](#2-get-all-posts)
        - [Update Post](#3-update-post)
        - [Retrieve Post](#4-retrieve-post)
        - [Delete Post](#5-delete-post)

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

## General Response Schema
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
| info | object or string | Usually an object, but can sometimes be a string. It returns information about failed requests |

## Endpoints:
The following endpoints are related to performing CRUD operations on post objects.

### 1. Create Post

- **Endpoint**: `create/`
- **HTTP Method**: `POST`
- **Description**: Creates a new post for the user.
- **Permission Level**: Only authenticated users can call this endpoint.


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

- `201 Created`: Indicates that you have successfully created a post. Here's what a typical response to the `create` endpoint should look like:

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
            "post_title": "New post",
            "post_body": "test body",
            "created_at": "2024-02-14"
        }
    }
    ```
- `400 Bad Request`: Invalid input or malformed request. Check your request body and ensure you're not skipping any fields or violating any rules.
- `401 Unauthorized`: You're unauthorized to perfrom the action. Ensure you include the authentication token in your request header.
- `5XX Internal Server Error`: Unexpected server error. This shouldn't happen, so please raise an issue or make a PR if you are able to fix it.

---

### 2. Get All Posts
- **Endpoint**: `list/`
- **HTTP Method**: `GET`
- **Description**: Returns a list of available posts
- **Permission Level**: Anyone can call this endpoint

**Request Body**
This endpoint does not require any request body.

**Response**
- `200 OK`: Indicates that the operation was successful. Here is the typical response body you should expect:
    ```json
    {
        "message": "successful",
        "data": [
            {
                "id": 3,
                "author": {
                    "id": 1,
                    "first_name": "ade",
                    "last_name": "Tom",
                    "username": "superr",
                    "email": "tomm@ade.com"
                },
                "post_title": "New post again",
                "post_body": "test body",
                "created_at": "2024-02-15"
            },
            {
                "id": 2,
                "author": {
                    "id": 1,
                    "first_name": "ade",
                    "last_name": "Tom",
                    "username": "superr",
                    "email": "tomm@ade.com"
                },
                "post_title": "Updated title",
                "post_body": "Updated body",
                "created_at": "2024-02-15"
            }
        ]
    }
    ```
You can get the response definition from the [general response schema](#general-response-schema) section.
- `5XX Internal Server Error`: Unexpected server error. This shouldn't happen, so please raise an issue or make a PR if you are able to fix it.

---

### 3. Update Post

- **Endpoint**: `{post_id}/`
- **HTTP Method**: `PATCH`
- **Description**: Updates the post with the specified `{post_id}`.
- **Permission Level**: Only the post's author can call this endpoint, provided they are logged in.

**Headers**

| Key          | Data Type  | Value                                                          |
|---------------|-----------|----------------------------------------------------------------|
| Authorization | String    | Set the value of this to the user's access/authentication token|


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
- `401 Unauthorized`: You're unauthorized to perform this action. Ensure you have the right authrntication token. Only the author of a post can update it.
- `404 Not Found`: This means the post you're trying to update doesn't exist. Check the `{post_id}` parameter.
- `5xx Internal Server Error`: Unexpected server error. This shouldn't happen, so please raise an issue or make a PR if you are able to fix it.
---

### 4. Retrieve Post
- **Endpoint**: `{post_id}`
- **HTTP Method**: `GET`
- **Description**: Returns the details of the post with the specified `{post_id}`, including the author and comments under the post.
- **Permission Level**: Anyone can call this endpoint.

**Request Body**
This endpoint does not require a request body.

**Example Response**
- `200 OK`: You have successfully retrieved the post.
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
        "post_comments": [
            {
                "id": 1,
                "comment_author": {
                    "id": 1,
                    "first_name": "ade",
                    "last_name": "Tom",
                    "username": "superr",
                    "email": "tomm@ade.com"
                },
                "comment": "good post!",
                "created_at": "2024-02-15"
            }
        ],
        "post_title": "New post",
        "post_body": "test body",
        "created_at": "2024-02-15"
    }
}
```
- `404 Not Found`: This means the post you're trying to update doesn't exist. Check the `{post_id}` path parameter.
- `5xx Internal server error`: Unexpected server error. This shouldn't happen, so please raise an issue or make a PR if you are able to fix it.

**Response Definition**
The post response is defined in the [general response schema](#general-response-schema). However this endpoint sees the addition of a new response field, `post_comments`. The schema for this is explained below:

| Response field | Data Type | Description |
|----------------|---------|---------------|
| data/**post_comments** | array | Returns all the comments available under a post |
| post_comments/**id** | integer | The unique ID of a specific comment |
| post_comments/**comment_author**| object | Returns the details of the user who created the comment. This is different from the post author|
|comment_author/**id**| integer | Unique ID of the user who created the comment |
| comment_author/**first_name** | string | The first name of the comment author |
| comment_author/**last_name** | string | The last name of the comment author |
| comment_author/**username** | string | The unique username of the comment author |
| comment_author/**email** | string | The unique email of the comment author |

---

### 5. Delete Post
- **Endpoint**: `{post_id}`
- **HTTP Method**: `DELETE`
- **Description**: Deletes the post with the specified `{post_id}`.
- **Permission Level**: Only the post's author can delete the specified post if they are logged in.

**Headers**
| Key          | Data Type  | Value                                                          |
|---------------|-----------|----------------------------------------------------------------|
| Authorization | String    | Set the value of this to the user's access/authentication token|


**Request Body**
This endpoint does not require a request body.

**Response**
- `204 No Content`: This indicates that the post has been deleted.
- `404 Not Found`: This means there is not post with the specified `{post_id}`. Check the `{post_id}` path parameter.
- `5xx Internal server error`: Unexpected server error. This shouldn't happen, so please raise an issue or make a PR if you are able to fix it.