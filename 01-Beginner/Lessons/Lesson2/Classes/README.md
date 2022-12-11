# Classes

Classes in Python are used to create objects. Objects are used to store data and perform actions. 

Classes are somethings we should consider when there are multiple objects of the same type.

Classes are also perfect candidates when we have a set of manipulations to perform on a set of objects.

Let's consider a simple example of a class.

```python
class APIClient:
    def __init__(self, username, api_key):
        self.username = username
        self.api_key = api_key
```

We have a class here called APIClient. It takes the parameters username and api_key.
These are the attributes of the class that we plan on using a few times throughout this lesson.

We want to add a method that will allow us to make requests to the API. 

```python
import requests

class APIClient:
    def __init__(self, username, api_key):
        self.username = username
        self.api_key = api_key

    def _make_post_request(self, endpoint):
        # Make a request to the API
        return requests.post(endpoint, auth=(self.username, self.api_key))
```

All of our post requests to our API will be made using this method. It prevents us from needing to continue to hold add these arguments together.

```python
import requests

class APIClient:
    def __init__(self, username, api_key, endpoint):
        self.username = username
        self.api_key = api_key
        self.endpoint = "https://api.github.com/graphql"

    def _make_post_request(self, api_query):
        # Make a request to the API
        return requests.post(f"{self.endpoint}/{endpoint}", auth=(self.username, self.api_key))

    def get_user_info(self, username):
        # Make a request to the API
        users f"/users/{username}"
        response = self._make_post_request(users))
        # Parse the response
        return response.json()
```

It we not have a method that we can use to make requests to the API, we can use the _make_post_request method to make requests.

What else we notice with APIs is we keep needing a default endpoint that all of the requests will use.

Why not set it so that we can reference it in the _make_post_request method?


