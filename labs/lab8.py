from urllib.request import urlopen
response = urlopen('http://www.depaul.edu')
html_content  = response.read()
decoded_content  = html_content.decode()
count_d =  decoded_content.count("d")
print(f"The letter 'd' appears {count_d} times on the DePaul homepage.")