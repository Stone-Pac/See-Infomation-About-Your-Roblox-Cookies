import http.cookiejar
import urllib.request

cookie = input("Please enter the RBXIDCHECK cookie: ")

cj = http.cookiejar.CookieJar()

cj.set_cookie(http.cookiejar.Cookie(version=0, name='RBXIDCHECK', value=cookie, port=None, port_specified=False, domain='', domain_specified=False, domain_initial_dot=False, path='/', path_specified=True, secure=False, expires=None, discard=True, comment=None, comment_url=None, rest={'HttpOnly': None}, rfc2109=False))

opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

response = opener.open("https://www.roblox.com/")

print(response.read())

input("Press enter to exit")
