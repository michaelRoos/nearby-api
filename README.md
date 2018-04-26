# Nearby API Documentation

### Accessing protected URLs
To access protected URLs, first obtain an authorization token (see "Logging in"). Include the token in the header of any requests made to protected urls:
```
Authorization: JWT <token>
```

### Creating users
Endpoint: `/signup/`

Protected: no

Request type: `POST`

Request parameters:
* Email address
* Password

Request body:
```
{
    "email": "example@gmail.com",
    "password": "secure-password"
}
```

Expected response:
```
HTTP 201 Created
```
### Logging in
Endpoint: `/api-token-auth/`

Protected: no

Request type: `POST`

Request parameters:
* Email address
* Password

Request body:
```
{
    "email": "example@gmail.com",
    "password": "secure-password"
}
```

Response parameters:
* Token

Expected response:
```
HTTP 200 Ok
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImxibDUxMDhAcHN1LmVkdSIsImV4cCI6MTUyNDE3OTk0NSwiZW1haWwiOiIifQ.m6gEl4Bvx6lT2BAcTxgXb_W4lKsuajggDet4QtKXvmI"
}
```

### Upvoting events/removing upvotes
Endpoint: `/upvote/`

Protected: yes

Request type: `POST`

Request parameters:
* Email address
* Event id

Request body:
```
{
    "user_email": "example@gmail.com"
    "event_id": "1270"
}
```

Response parameters:
* is_upvote - True if the user's action added a vote, False if the user's action took away a vote
Expected response:
```
HTTP 202 Accepted
{
    "is_upvote": True
}
```



### Creating events
Endpoint: `/event/create/`

Protected: yes

Request type: `POST`

Request parameters:
* Title
* Description
* Latitude
* Longitude
* Zipcode
* Start time (optional)
* End time (optional)
* User email
* Categories
* Planned event
* Images (optional)

Request body:
```
{
    "title": "Pizza Party",
    "description": "Free food!",
    "lat": "78.21545",
    "long": "-35.55487",
    "zipcode": "16802",
    "start_time": "2018-04-25T05:05:50.211181Z",
    "end_time": "2018-04-25T06:05:50.211181Z",
    "user_email": "a@a.com",
    "categories": ["All"],
    "planned_event": true,
    "images": []
}
```