from validation_data import OrderValidation as OV
import allure

class TestOrder:

    @allure.title('Создание заказа с авторизацией и двумя ингридиентами')
    def test_create_order_positive(self, new_user_test_data, o_controller):
        _, _, token = new_user_test_data
        response = o_controller.create_order_positive(token)
        data = response.json()

        assert response.status_code == 200
        assert data.get('success') is True

    @allure.title('Создание заказа без авторизации')
    def test_create_order_no_authorization(self, o_controller):
        response = o_controller.create_order_no_authorization()
        data = response.json()
        
        assert response.status_code == 200
        assert data.get('success') is True

    @allure.title('Создание заказа с несуществующими ингридиентами')
    def test_create_order_with_wrong_ingredients_id(self, new_user_test_data, o_controller):
        _, _, token = new_user_test_data
        response = o_controller.create_order_wrong_ingredients_id(token)

        assert response.status_code == 500
        assert 'Internal Server Error' in response.text

    @allure.title('Создание заказа без ингридиентов')
    def test_create_order_no_ingredients(self, new_user_test_data, o_controller):
        _, _, token = new_user_test_data
        response = o_controller.create_order_no_ingredients(token)
        data = response.json()

        assert response.status_code == 400
        assert data.get('success') is False
        assert data.get('message') == OV.CREATE_ORDER_NO_INGREDIENTS

    @allure.title('Получение заказов пользователя')
    def test_get_user_orders(self, new_user_test_data, o_controller):
        _, _, token = new_user_test_data
        response = o_controller.get_user_orders(token)
        data = response.json()

        assert response.status_code == 200
        assert data.get('success') is True
        assert 'orders' in data
        assert 'total' in data
        assert 'totalToday' in data

    @allure.title('Получение заказов пользователя без авторизации')
    def test_get_user_order_no_authorization(self, o_controller):
        response = o_controller.get_user_orders(None)
        data = response.json()

        assert response.status_code == 401
        assert data.get('success') is False
        assert data.get('message') == OV.GET_USER_ORDERS_NO_AUTHORIZATION
