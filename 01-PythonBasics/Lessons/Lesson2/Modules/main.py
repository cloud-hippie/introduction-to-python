
from request_api import APIClient, Person

my_client = APIClient("username", "api_key")
print(my_client)


justin = Person("Justin", 30, "Boston")
print(justin.get_age() )