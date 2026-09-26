import pytest
from api_controller.profile_controller import ProfileController as PC
from api_controller.order_controller import OrderController as OC
from helpers import GenerateTestData as GD
from data import TestDataAuthorization as DA

@pytest.fixture
def new_user_random_data():
    controller = PC()
    generate = GD()
    user = {
        'email': generate.generate_random_email(7).lower(),
        'password': generate.generate_random_password(10),
        'name': generate.generate_random_name(6).lower()
        }
    response = controller.create_new_user(email=user['email'], password=user['password'], name=user['name'])
    data = response.json()
    token = data.get('accessToken')
    yield (response, user, token)
    controller.delete_user(token)

@pytest.fixture
def new_user_test_data():
    controller = PC()
    user = {
        'email': DA.test_profile.get('email'),
        'password': DA.test_profile.get('password'),
        'name': DA.test_profile.get('name')
        }
    response = controller.create_new_user(email=user['email'], password=user['password'], name=user['name'])
    data = response.json()
    token = data.get('accessToken')
    yield (response, user, token)
    controller.delete_user(token)

@pytest.fixture
def p_controller():
    controller = PC()
    return controller

@pytest.fixture
def o_controller():
    controller = OC()
    return controller