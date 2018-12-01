import urllib.request
import zipfile
import os

def py_downloader(url,file_name = ''):
    if file_name == '':
        file_name = url.rsplit('/',1)[1]        
    urllib.request.urlretrieve(url,file_name)
    if file_name.rsplit('.',1)[1] == 'zip':
        with zipfile.ZipFile(file_name,'r') as zip_handler:
            zip_handler.extractall(f"{os.system('$PWD')}")
        os.system(f"rm {filename}")

url = input("File URL: ")
file_name = input("(Optional, Press enter to skip) File name:")
py_downloader(url,file_name)
