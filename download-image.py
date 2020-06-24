import requests
import logging
import os
from bs4 import BeautifulSoup as bs

def get_image_url(site_url, selector):
    """
    return image url in the website specified by site_url
    """
    soup = bs(requests.get(site_url).content, "html.parser")
    img_list = soup.select(selector)

    # for img in img_list:
    #     print(img.attrs.get("src"))
    #     print(img.attrs.get("srcset"))

    # return img_list[0].attrs.get("src")


    if len(img_list) != 0:
        logging.exception("specified image element cannt be found.")
    else:
        return img_list[0].attrs.get("src")

def download_img(url, pathname, filename):
    """
    Downloads a file given an URL and puts it in the folder `pathname`
    """
    # if path doesn't exists, make that path dir
    if not os.path.isdir(pathname):
        os.makedirs(pathname)
    
    filepath = os.path.join(pathname, filename)
    r = requests.get(url, stream = True)
    if r.status_code == 200:
        with open(filepath, 'wb') as f:
            for chunk in r.iter_content(1024):
                f.write(chunk)
def main(): 
    for id in range(1, 12):
        id = f"{id:02d}"
        print(id)
        url = f"https://google.co.jp/{id}"
        medium_url = "https://medium.com/code-85/a-beginners-guide-to-importing-in-python-bb3adbbacc2b"
        img_url = get_image_url(medium_url, "article figure img")
        download_img(img_url, "./img", f"{id}.jpg")

if __name__ == "__main__":
    main()

