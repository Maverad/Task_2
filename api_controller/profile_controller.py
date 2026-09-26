from api_controller.base_controller import BaseController
import allure

class ProfileController(BaseController):
    API_POST_NEW_USER = "api/auth/register"
    API_POST_LOGIN = "api/auth/login"
    API_USER = "api/auth/user" # allowed methods GET (get user info), PUT (edit user info), DELETE (delete user)
    API_POST_PASSWORD_RESET = "api/password-reset"

    @allure.step('Create new user')
    def create_new_user(self, email, password, name):
        data = {
            "email": email,
            "password": password,
            "name": name
        }
        response = self.post(self.API_POST_NEW_USER, data)
        return response

    @allure.step('Create new user')
    def create_new_user_no_password(self, email, name):
        data = {
            "email": email,
            "name": name
        }
        response = self.post(self.API_POST_NEW_USER, data)
        return response

    @allure.step('Login user')
    def login_user(self, email, password):
        data = {
            "email": email,
            "password": password
        }
        response = self.post(self.API_POST_LOGIN, data)
        return response

    @allure.step('Get user info')
    def get_user_info(self, token):
        headers = {
            "Authorization": token
        }
        response = self.get('api/auth/user', headers=headers)
        return response

    @allure.step('Edit user info')
    def edit_user_info(self, token, name=None, email=None):
        headers = {
            "Authorization": token
        }
        data = {}
        if name is not None:
            data['name'] = name
        if email is not None:
            data['email'] = email
        response = self.patch('api/auth/user', data=data, headers=headers)
        return response

    @allure.step('Delete user')
    def delete_user(self, token):
        headers = {
            "Authorization": token
        }
        response = self.delete(self.API_USER, headers=headers)
        return response