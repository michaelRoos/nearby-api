# Nearby API Documentation

### Creating users
Endpoint: /signup/

Request type: POST

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
Endpoint: /api-token-auth/

Request type: POST

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
