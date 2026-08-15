import requests

class BaseController:
    BASE_URL = 'https://qa-stellarburgers.education-services.ru/'

    def get(self, url, headers=None):
        if headers is None:
            response = requests.get(self.BASE_URL + url)
            return response
        else:
            response = requests.get(self.BASE_URL + url, headers=headers)
            return response
    
    def post(self, url, data, headers=None):
        if headers is None:
            response = requests.post(self.BASE_URL + url, json=data)
            return response
        else:
            response = requests.post(self.BASE_URL + url, json=data, headers=headers)
            return response

    def delete(self, url, headers=None):
        if headers is None:
            response = requests.delete(self.BASE_URL + url)
            return response
        else:
            response = requests.delete(self.BASE_URL + url, headers=headers)
            return response

    def patch(self, url, data, headers=None):
            if headers is None:
                response = requests.patch(self.BASE_URL + url, json=data)
                return response
            else:
                response = requests.patch(self.BASE_URL + url, json=data, headers=headers)
                return response
    

