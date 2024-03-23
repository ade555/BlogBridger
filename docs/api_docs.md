# API Overview

## Base URL: `api/posts/`
---
## **Posts**

The endpoints under the posts API allow users to Create, Update, Delete, and Retrieve posts.


### **Parameters (Posts)**
The following defines parameters that are general to all or most of the endpoints under the Post API

**Path Parameters**

| Parameter |Data Type| Description| Required |
|-----------|---------|------------|----------|
| post_id| integer | The unique ID associated with each post. | Yes|

---

### **General Response Schema (Posts)**
The following table explains the most common response fields you will come across under the post API. Unique response fields may be documented alongside the specific endpoint(s) they apply to.

| Response field | Data Type | Description |
|----------------|---------|---------------|
|message | string | Indicates the status of the request made. It can either be successful or failed |
| data | object | Contains the resource requested |
| data/**id** | integer | Indicates the ID of the post requested or created |
| data/**post_title** | char | Indicates the title of the post requested or created. Maximum length is 50 characters |
| data/**post_body** | varchar | Indicates the body/content of the post requested or created |
| data/**created_at** | date field | Indicates the date the post was created. For example: **"2024-02-14"** |
| data/**author** | object | Indicates the author associated with the post. The fields returned under this object generally depends on your user model |
| data/author/**id** | integer | The unique ID associated with the author of a post |
| data/author/**first_name** | char | Author's first name. The maximum length is 150 characters, unless specified otherwise in your user model |
| data/author/**last_name** | char | Author's last name. The maximum length is 150 characters, unless specified otherwise in your user model|
| data/author/**username** | char | Author's unique username. The maximum length is 150 characters, unless specified otherwise in your user model|
| data/author/**email** | varchar | Author's unique email |
| info | object or string | Usually an object, but can sometimes be a string. It returns information about failed requests |

### **Endpoints (Posts)**:
The following endpoints are related to performing CRUD operations on post objects.

#### **1. Create Post**

- **Endpoint**: `create/`
- **HTTP Method**: `POST`
- **Description**: Creates a new post for the user.
- **Permission Level**: Only authenticated users can call this endpoint.


**Headers**

| Key | Data Type | Value  |
|-----|-----------|--------|
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
|-----------|-----------|----------------------------------|----------|
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
- `401 Unauthorized`: You're unauthorized to perform the action. Ensure you include the authentication token in your request header.
- `5XX Internal Server Error`: Unexpected server error. This shouldn't happen, so please raise an issue or make a PR if you can fix it.

---

#### **2. Get All Posts**
- **Endpoint**: `list/`
- **HTTP Method**: `GET`
- **Description**: Returns a list of available posts
- **Permission Level**: Anyone can call this endpoint

**Query String Parameters**

| Parameter | Data Type | Description | Required |
|-----------|-----------|-------------|----------|
| author | string | Username of a specific author. Including this parameter will return all posts made by the user specified. | No |
| title | string | The title of a specific post. Including this parameter will return posts that contain the exact string or something simiar | No |


**Example Request**

```bash
http://127.0.0.1:8000/api/posts/list/?author=johnny
```

**Example Response**

```json
{
    "message": "successful",
    "data": [
        {
            "id": 9,
            "author": {
                "id": 8,
                "first_name": "ade",
                "last_name": "Tom",
                "username": "johnny",
                "email": "tommm@ade.com"
            },
            "post_title": "New post again",
            "post_body": "test body",
            "created_at": "2024-02-15"
        }
    ]
}
```

- `200 OK`: Indicates that the operation was successful. Here is the typical response body you should expect:
You can get the response definition from the [general response schema](#general-response-schema-posts) section.

- `5XX Internal Server Error`: Unexpected server error. This shouldn't happen, so please raise an issue or make a PR if you can fix it.

---

#### **3. Update Post**

- **Endpoint**: `{post_id}/`
- **HTTP Method**: `PATCH`
- **Description**: Updates the post with the specified `{post_id}`.
- **Permission Level**: Only the post's author can call this endpoint, provided they are logged in.

**Headers**

| Key          | Data Type | Value   |
|--------------|-----------|---------|
| Authorization | String    | Set the value of this to the user's access/authentication token|


**Parameters**

| Parameter | Data Type | Description                 | Required |
|-----------|-----------|-----------------------------|----------|
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
- `401 Unauthorized`: You're unauthorized to perform this action. Ensure you have the right authentication token. Only the author of a post can update it.
- `404 Not Found`: This means the post you're trying to update doesn't exist. Check the `{post_id}` parameter.
- `5xx Internal Server Error`: Unexpected server error. This shouldn't happen, so please raise an issue or make a PR if you can fix it.
---

#### **4. Retrieve Post**
- **Endpoint**: `{post_id}/`
- **HTTP Method**: `GET`
- **Description**: Returns the details of the post with the specified `{post_id}`, including the author and comments under the post.
- **Permission Level**: Anyone can call this endpoint.

**Request Body**
This endpoint does not require a request body.

**Responses**

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
- `5xx Internal server error`: Unexpected server error. This shouldn't happen, so please raise an issue or make a PR if you can fix it.

**Response Definition**
The post response is defined in the [general response schema](#general-response-schema). However, this endpoint sees the addition of a new response field, `post_comments`. The schema for this is explained below:

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

#### **5. Delete Post**
- **Endpoint**: `{post_id}/`
- **HTTP Method**: `DELETE`
- **Description**: Deletes the post with the specified `{post_id}`.
- **Permission Level**: Only the post's author can delete the specified post if they are logged in.

**Headers**

| Key          | Data Type | Value                                                          |
|--------------|-----------|----------------------------------------------------------------|
| Authorization | String    | Set the value of this to the user's access/authentication token|


**Request Body**
This endpoint does not require a request body.

**Responses**

- `204 No Content`: This indicates that the post has been deleted.
- `404 Not Found`: This means there is no post with the specified `{post_id}`. Check the `{post_id}` path parameter.
- `5xx Internal server error`: Unexpected server error. This shouldn't happen, so please raise an issue or make a PR if you can fix it.
---

## **Comments**
The comments endpoints provide information about comments available under a post. It allows you to create comments for a specific post and retrieve all the comments available under a specific post.

### **Parameters (Comments)**
The following defines parameters that are general to all or most of the endpoints under the Post API

**Path Parameters**

| Parameter | Data Type   | Description                              | Required |
|-----------|-------------|------------------------------------------|----------|
| post_id        | integer | The unique ID associated with each post. | Yes      |


### **General Response Schema (Comments)**
The following table explains the most common response fields you will come across under the Post API. Unique response fields may be documented alongside the specific endpoint(s) they apply to.

| Response field | Data Type | Description |
|----------------|-----------|-------------|
|message | string | Indicates the status of the request made. It can either be successful or failed |
| data | object | Contains the resource requested |
| data/**id** | integer | The unique ID of a comment |
| data/**comment_author** | object | Contains details such as names, and email about the author of the comment. |
| data/**comment** | string | The comment text. | 
| data/**created_at** | date field | Indicates when the comment was made |

### **Endpoints (Comments)**:
The following endpoints will help you interact with the comment API.

**Path Parameters**

| Parameter | Data Type | Description                              | Required |
|-----------|-----------|------------------------------------------|----------|
| post_id        | integer | The unique ID associated with each post. | Yes      |

#### **1. Create Comment**

- **Endpoint**: `{post_id}/comment`
- **HTTP Method**: `POST`
- **Description**: Creates a new comment under the post with the given `{post_id}`
- **Permission Level: Only logged-in users can create comments

**Headers**

| Key          | Data Type | Value                                                          |
|--------------|-----------|----------------------------------------------------------------|
| Authorization | String    | Set the value of this to the user's access/authentication token|

**Request Body**:

```json
{
    "comment":"This is very good!"
}
```
**Request Body Definition**

| Parameter | Data Type | Description                      | Required |
|-----------|-----------|----------------------------------|----------|
| comment | varchar | The user's comment text | Yes |


**Responses**

- `201 Created`: Indicates that you have created a response. Here is an example response:
    ```json
    {
        "message": "successful",
        "data": {
            "id": 4,
            "comment_author": {
                "id": 2,
                "first_name": "ade",
                "last_name": "Tom",
                "username": "johnny",
                "email": "tommm@ade.com"
            },
            "comment": "This is very good!",
            "created_at": "2024-02-19"
        }
    }
    ```

- `400 Bad Request`: Invalid input or malformed request. Check your request body and ensure you're not skipping any fields or violating any rules.
- `401 Unauthorized`: You're unauthorized to perform the action. Ensure you include the authentication token in your request header.
- `5XX Internal Server Error`: Unexpected server error. This shouldn't happen, so please raise an issue or make a PR if you can fix it.

---

#### **2. Get comments under a specific post**

- **Endpoint**: `{post_id}/comment`
- **HTTP Method**: `GET`
- **Description**: Retrieves all the comments under a post with the specific `{post_id}`
- **Permission Level**: Anyone can view comments

**Request Body**: This request has no body.

**Responses**

- `200 OK`: Indicates that you have created a response. Here is an example response:
    ```json
    {
        "message": "successful",
        "data": [
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
            },
            {
                "id": 2,
                "comment_author": {
                    "id": 1,
                    "first_name": "ade",
                    "last_name": "Tom",
                    "username": "superr",
                    "email": "tomm@ade.com"
                },
                "comment": "great post!",
                "created_at": "2024-02-15"
            }
        ]
    }
    ```
- `5XX Internal Server Error`: Unexpected server error. This shouldn't happen, so please raise an issue or make a PR if you can fix it.