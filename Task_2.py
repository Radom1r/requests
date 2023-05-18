import requests
from pprint import *
import json
class YaUploader:
    def __init__(self, token: str):
        self.token = token
    
    def get_headers(self):
        return {'Content-Type': 'application/json', 'Authorization' : f'{self.token}'}
    
    def get_link(self, filename):
        url_for_files = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {'path':path_to_file, 'overwrite':'true'}
        response = requests.get(url=url_for_files, headers=headers, params=params)
        link = response.json()
        return link['href']

    # def get_link(self, disk_path):
    #     pass

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        url = 'https://cloud-api.yandex.net/v1/disk/resourses/publish'
        href = self.get_link(file_path)
        response = requests.put(href, open(file_path, 'rb'))
        print(response)

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    file_list = ['new_file.txt', 'smart.txt']
    token = ''
    uploader = YaUploader(token)
    # uploader.get_link()
    for path_to_file in file_list:
        result = uploader.upload(path_to_file)