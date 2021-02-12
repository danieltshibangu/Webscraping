# this will allow me to scrape website to download my favorite manga
'''
create a file 
Dowload the website 
Read the info on the page 
Get the single multi image display
Dowload it the image to a file
'''

HEADERS = { 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:78.0) Gecko/20100101 Firefox/78.0' }

import bs4, os, requests

# The url that holds the manga 
landing_page_URL = 'https://w3.sololeveling.net/'

# create a directory(file) that will hold the images 
os.makedirs('Latest Solo Leveling')

# Send prompt for downloading 
print( "Downloading your manga...")

# download main page of manga site 
downloadManga = requests.get(landing_page_URL, headers=HEADERS)
downloadManga.raise_for_status() 

# now lets read the actual contents of the downloaded page 
soup = bs4.BeautifulSoup(downloadManga.text, 'lxml')

# select the list of html  
multi_image_manga_page = soup.select('tr a')

# change the url to the latest manga page 
latest_chap_URL = multi_image_manga_page[0].get('href')

# Now download the page of our new opened link into the chapter 
downloadManga = requests.get(latest_chap_URL, headers=HEADERS)
downloadManga.raise_for_status() 

# now lets read the actual contents of the NEW CHAPTER PAGE 
soup = bs4.BeautifulSoup(downloadManga.text, 'lxml') 

# this variable will search our NEW CHAPTER PAGE img tags  
actual_image_page = soup.select( 'img')


for each_image in range(len(actual_image_page)):

    # we store the direct file of that image from the src tag
    manga_img_url = actual_image_page[each_image].get('src')
    #print(manga_img_url)

    #download the actual chapter image
    downloadManga = requests.get(manga_img_url, headers=HEADERS)
    downloadManga.raise_for_status() 

    # TODO: Save it to the folder we made 
    imageFile = open(os.path.join( 'Latest Solo Leveling', os.path.basename(manga_img_url)), 'wb')

    # keep looping over the return value of inter_content() 
    # the code in the for loop writes out chunks of image data to the file
    # and then the file is closed
    # all this only when using Requests
    for each_chunk in downloadManga.iter_content(100000):
        imageFile.write(each_chunk)
    imageFile.close()

print( 'Completed' )
