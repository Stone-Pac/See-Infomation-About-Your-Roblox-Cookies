import http.cookiejar
import urllib.request

# Prompt the user to input the __utma cookie
cookie = input("Please enter the __utma cookie: ")

# Create a cookie jar to store the __utma cookie
cj = http.cookiejar.CookieJar()

# Add the cookie to the cookie jar
cj.set_cookie(http.cookiejar.Cookie(version=0, name='__utma', value=cookie, port=None, port_specified=False, domain='', domain_specified=False, domain_initial_dot=False, path='/', path_specified=True, secure=False, expires=None, discard=True, comment=None, comment_url=None, rest={'HttpOnly': None}, rfc2109=False))

# Create an opener to use the cookie jar
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

# Get the information stored in the cookie
response = opener.open("https://www.roblox.com/")

# Print the information stored in the cookie
print(response.read())

input("Press enter to exit")