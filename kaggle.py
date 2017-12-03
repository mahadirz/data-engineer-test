
# coding: utf-8


from mechanicalsoup import Browser
from pathlib import Path
import re
import os
from pathlib import Path

#define reusable kaggle downloader
class Kaggle:
    
    def __init__(self):
        self.browser = Browser()

    def login(self,username,password):
        login_url = 'https://www.kaggle.com/account/login'
        login_page = self.browser.get(login_url)

        token = re.search(
            'antiForgeryToken: \'(?P<token>.+)\'',
            str(login_page.soup)
        ).group(1)

        login_result_page = self.browser.post(
            login_url,
            data={
                'username': username,
                'password': password,
                '__RequestVerificationToken': token
            }
        )
        error_match = re.search(
            '"errors":\["(?P<error>.+)"\]',
            str(login_result_page.soup)
        )
        if error_match:
            print(error_match.group(1))
            return
        return self.browser

    def download_dataset(self,url,local_file):
        headers=self.browser.request('head', url).headers
        content_length = int(headers['Content-Length'])
        chunk = 1
        if content_length > 0:
            my_file = Path(local_file)
            if my_file.is_file():
                #delete
                os.remove(local_file)
        if content_length > 1024:
            chunk = 1024
        stream = self.browser.get(url, stream=True)
        with open(local_file, 'ab') as f:
            for chunk in stream.iter_content(chunk_size=chunk):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)