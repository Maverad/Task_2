from helpers import GenerateTestData as GD
from validation_data import ProfileValidation as PV
import allure

class TestProfile:

    @allure.title('Создание нового пользователя')
    def test_create_new_user_positive(self, new_user_random_data):
        response, user, _ = new_user_random_data
        data = response.json()

        assert response.status_code == 200
        assert data.get('success') is True
        assert data.get('user')['email'] == user['email']
        assert data.get('user')['name'] == user['name']

    @allure.title('Создание уже созданного пользователя')
    def test_create_new_user_already_exists(self, new_user_test_data, p_controller):
        _, user, _ = new_user_test_data
        response = p_controller.create_new_user(email=user.get('email'), password=user.get('password'), name=user.get('name'))
        data = response.json()

        assert response.status_code == 403
        assert data.get('message') == PV.PROFILE_ALREADY_EXISTS
        assert data.get('success') is False
        
    @allure.title('Создание пользователя без обязательных атрибутов')
    def test_create_new_user_no_required_attributes(self, p_controller):
        generate = GD()
        response = p_controller.create_new_user_no_password(email=generate.generate_random_email(), name=generate.generate_random_name())
        data = response.json()

        assert response.status_code == 403
        assert data.get('message') == PV.CREATE_PROFILE_MISSING_REQUIRED_FIELDS
        assert data.get('success') is False

    @allure.title('Логин')
    def test_login_user_positive(self, new_user_test_data, p_controller):
        _, user, _ = new_user_test_data
        response = p_controller.login_user(email=user.get('email'), password=user.get('password'))
        data = response.json()

        assert response.status_code == 200
        assert data.get('success') is True
        assert data.get('user')['email'] == user['email']
        assert data.get('user')['name'] == user['name']

    @allure.title('Логин с несуществующими данными')
    def test_login_user_wrong_data(self, p_controller):
        generate = GD()
        response = p_controller.login_user(email=generate.generate_random_email(), password=generate.generate_random_password())
        data = response.json()

        assert response.status_code == 401
        assert data.get('success') is False
        assert data.get('message') == PV.LOGIN_WRONG_DATA

    @allure.title('Изменение данных пользователя')
    def test_edit_user_data_positive(self, new_user_random_data, p_controller):
        generate = GD()
        _, _, token = new_user_random_data
        new_email, new_name = generate.generate_random_email().lower(), generate.generate_random_name().lower()
        response = p_controller.edit_user_info(token=token, email=new_email, name=new_name)
        data = response.json()

        assert response.status_code == 200
        assert data.get('success') is True
        assert data.get('user')['name'] == new_name
        assert data.get('user')['email'] == new_email

    @allure.title('Изменение данных пользователя без регистрации')
    def test_edit_user_data_no_registration(self, p_controller):
        generate = GD()
        new_email, new_name = generate.generate_random_email(), generate.generate_random_name()
        response = p_controller.edit_user_info(token=None, email=new_email, name=new_name)
        data = response.json()

        assert response.status_code == 401
        assert data.get('success') is False
        assert data.get('message') == PV.EDIT_PROFILE_NO_AUTHORIZATION
    
    
    

    