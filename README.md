# Nearby API Documentation

### Creating users
Endpoint: `/signup/`

Request type: `POST`

Parameters:
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

Request type: `POST`

Parameters:
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
HTTP 200 Ok
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImxibDUxMDhAcHN1LmVkdSIsImV4cCI6MTUyNDE3OTk0NSwiZW1haWwiOiIifQ.m6gEl4Bvx6lT2BAcTxgXb_W4lKsuajggDet4QtKXvmI"
}
```

### Accessing protected URLs
To access protected URLs, first obtain an authorization token (see "Logging in"). Include the token in the header of any requests made to protected urls:
```
Authorization: JWT <token>
```

### Upvoting events
Endpoint: `/upvote/`

Request type: `POST`

Parameters:
* Email address
* Event id

Request body:
```
{
    "user_email": "example@gmail.com"
    "event_id": "1270"
}
```

Expected response:
```
HTTP 204 No Content
```

If a user attempts to upvote a post more than once, `HTTP 403 Forbidden` will be returned