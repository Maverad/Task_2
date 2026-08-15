from api_controller.base_controller import BaseController
import allure

class OrderController(BaseController):
    API_GET_INGRIDIENTS = "api/ingredients"
    API_ORDER = "api/orders"   # allowed methods POST (create an order), GET (get user order)
    API_GET_ALL_ORDERS = "api/orders/all"
       
    @allure.step('Get ingredients')
    def get_ingredients(self):
        response = self.get(self.API_GET_INGRIDIENTS)
        return response

    @allure.step('Get user order')
    def get_user_orders(self, token):
        headers = {
            "Authorization": token
        }
        response = self.get(self.API_ORDER, headers=headers)
        return response

    @allure.step('Get all orders')
    def get_all_orders(self):
        response = self.get(self.API_GET_ALL_ORDERS)
        return response

    @allure.step('Create an order with authorization and two ingredients')
    def create_order_positive(self, token):
        headers = {
            "Authorization": token
        }
        data = {
            "ingredients": ['691577430cc94f001a65b863', '691577430cc94f001a65b859']
        }
        response = self.post(self.API_ORDER, data=data, headers=headers)
        return response

    @allure.step('Create an order with no ingredients')
    def create_order_no_ingredients(self, token):
        headers = {
            "Authorization": token
        }
        data = {
            "ingredients": []
        }
        response = self.post(self.API_ORDER, data=data, headers=headers)
        return response

    @allure.step('Create an order with wrong ingredients id')
    def create_order_wrong_ingredients_id(self, token):
        headers = {
            "Authorization": token
        }
        data = {
            "ingredients": ['test']
        }
        response = self.post(self.API_ORDER, data=data, headers=headers)
        return response

    @allure.step('Create an order with no authorization')
    def create_order_no_authorization(self):
        headers = {
            "Authorization": None
        }
        data = {
            "ingredients": ['691577430cc94f001a65b863', '691577430cc94f001a65b859']
        }
        response = self.post(self.API_ORDER, data=data, headers=headers)
        return response