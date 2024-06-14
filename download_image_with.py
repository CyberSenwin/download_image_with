import random
import urllib.request

def download_image(url):
# in serting the range of the image file 
    img_name = random.randrange(50,100)
# I am converting the image range number to a string. i mean from int to str
    full_name =str(img_name)+'jpg'
    #the img file can be png 
    urllib.request.urlretrieve(url,full_name)

download_image('https://udsen.pythonanywhere.com/')