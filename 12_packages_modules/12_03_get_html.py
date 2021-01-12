'''
In 3 lines of code, fetch the HTML text from codingnomads' main page
and print it to your console.

TIP:
- if you wonder what to use, google something like
    "most popular python package"
- if you run into encoding/decoding errors, you're experiencing something
    very common. head over to SO and find a solution!

'''
# from lxml import html
# import requests

# page = requests.get('https://codingnomads.co/')
# # tree = html.fromstring(page.content)
# print(page)

from http.client import HTTPConnection
conn = HTTPConnection("codingnomads.co/")
conn.request("GET", "/")  
result = conn.getresponse()
# retrieves the entire contents.  
contents = result.read() 
print(contents)