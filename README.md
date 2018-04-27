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

The request for creating and removing upvotes is the exact same. The backend decides what action depending on if the user has already upvoted the event or not.



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
### Listing events
Endpoint: `/event/list/?search=&catagories=`

Protected: no

Request type: `GET`

Request parameters:
 * search
	 * Filters results where title or description contain search
 * catagories
	 * Filters results where event contains all catagories.

Response body:
```
{
	"id":id,
	"title":"Title",
	"description":"Description",
	"event_images":[],
	"event_comment":[],
	"lat":"xx.xxxxxx",
	"lng":"xx.xxxxxx",
	"zipcode":"xxxxx",
	"time_stamp":"YYYY-mm-ddThh:mm:ss.ffffffZ",
	"upvote_count":0,
	"start_time":null,
	"end_time":null,
	"user_email":"email@email.com",
	"categories":[
		{"title":"Title",
		...
		"title":"Title"
		}
	]
}
```

### Single Event List
Endpoint: `event/(?P<pk>\d+)`

Protected: no

Request type: `GET`

Request parameters:

Response body:
```
{
	"id":pk,
	"title":"Title",
	"description":"Description",
	"event_images":[
		 {
			  "id":  image_pk,
			  "file":  "[http://127.0.0.1:8000/media/IMG_NAME.JPG]",
			  "timestamp":  "YYYY-mm-ddThh:mm:ss.ffffffZ",
			  "user_email":  "email@email.com",
			  "event_id":  event_pk
		  }
		  ...
	],
	"event_comment":[
		  {
			  "id":  a,
			  "name":  "Name",
		      "comment":  "Comment",
		      "timestamp":  "YYYY-mm-ddThh:mm:ss.ffffffZ",
		      "event_id":  pk
		  },
		  ...
	],
	"lat":"xx.xxxxxx",
	"lng":"xx.xxxxxx",
	"zipcode":"xxxxx",
	"time_stamp":"YYYY-mm-ddThh:mm:ss.ffffffZ",
	"upvote_count":0,
	"start_time":null,
	"end_time":null,
	"user_email":"email@email.com",
	"categories":[
		{"title":"Title",
		...
		"title":"Title"
		}
	]
}
```

### Creating Images
Endpoint: `/image/create/`

Protected: yes

Request type: `POST`

Request parameters:
 * file
 * user_email
 * event_id

### **INSERT POST REQUEST**

Response body:
```
 {
	  "id":  image_pk,
	  "file":  "[http://127.0.0.1:8000/media/IMG_NAME.JPG]",
	  "timestamp":  "YYYY-mm-ddThh:mm:ss.ffffffZ",
	  "user_email":  "email@email.com",
	  "event_id":  event_pk
  }
```

### Image List
Endpoint: `image/list`

Protected: no

Request type: `GET`

Request parameters:

Response body:
```
[
	 {
		  "id":  image_pk,
		  "file":  "[http://127.0.0.1:8000/media/IMG_NAME.JPG]",
		  "timestamp":  "YYYY-mm-ddThh:mm:ss.ffffffZ",
		  "user_email":  "email@email.com",
		  "event_id":  event_pk
	  }
	  ...
]
```

### Creating Comments
Endpoint: `/comment/create/`

Protected: yes

Request type: `POST`

Request parameters:
 * name
 * comment
 * event_id

Request body:

```
  {
	  "name":  "Name",
      "comment":  "Comment",
      "event_id":  pk
  }
```

Response body:
```
  {
	  "id":  a,
	  "name":  "Name",
      "comment":  "Comment",
      "timestamp":  "YYYY-mm-ddThh:mm:ss.ffffffZ",
      "event_id":  pk
  }
```