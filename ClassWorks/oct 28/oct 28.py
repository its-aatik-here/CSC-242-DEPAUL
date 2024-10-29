from urllib.request import urlopen
response = urlopen('http://www.depaul.edu')
html = response.read().decode()  # Read and decode HTML content
