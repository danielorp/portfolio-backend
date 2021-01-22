## Authorization

In order to generate a new authorization token for a given user, send a POST request to the /login/ endpoint in the following format:

- `curl -X POST -d "username=MY_USERNAME&password=MY_PASSWORD" http://localhost:8000/login/`

Using the generated token above, hit the endpoints in the following manner:
- `curl -X GET -H "Authorization: JWT my_cool_long_alphanumeric_token" http://localhost:8000/user/`
