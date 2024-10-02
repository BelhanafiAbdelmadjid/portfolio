import requests

# Step 1: Create a session object
session = requests.Session()

# Step 2: Send a request and get cookies
# login_url = 'https://example.com/login'
# login_data = {
#     'username': 'your_username',
#     'password': 'your_password'
# }

# # Perform a POST request to log in and set cookies in the session
# response = session.post(login_url, data=login_data)

# # Check if the login was successful and cookies were set
# if response.status_code == 200:
#     print("Login successful!")
#     # Step 3: Print cookies stored in the session
#     print("Cookies after login:", session.cookies.get_dict())

# Step 4: Use the session with cookies for subsequent requests
protected_url = 'https://www.dice.com/register/new-profile'
response = session.get(protected_url)

# Check if accessing a protected page is successful
if response.status_code == 200:
    session_data = {
        'cookies': session.cookies.get_dict(),  # Session cookies
        'session_headers': dict(session.headers),  # Session headers
        'response_headers': dict(response.headers),  # Response headers
    }
    response_headers = session_data['response_headers']

    # Print response headers
    print("Response Headers:", response_headers)
    # To see the session headers (which will include cookies sent in requests)
    print(session.headers)

    # print(response.text)
else:
    print("Failed to access the protected page!")

# Optionally, add or modify cookies in the session
# session.cookies.set('custom_cookie', 'cookie_value')

# You can use session cookies in any subsequent requests:
# another_url = 'https://example.com/another_page'
# response = session.get(another_url)
# print("Cookies after accessing another page:", session.cookies.get_dict())

# # Step 5: End the session
# session.close()
