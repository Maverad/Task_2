

class ProfileValidation:
    # Profile errors
    PROFILE_ALREADY_EXISTS = 'User already exists'
    CREATE_PROFILE_MISSING_REQUIRED_FIELDS = 'Email, password and name are required fields'
    LOGIN_WRONG_DATA = 'email or password are incorrect'
    EDIT_PROFILE_NO_AUTHORIZATION = 'You should be authorised'


class OrderValidation:
    # Order errors
    GET_USER_ORDERS_NO_AUTHORIZATION = 'You should be authorised'
    CREATE_ORDER_WRONG_INGREDIENTS_ID = 'One or more ids provided are incorrect'
    CREATE_ORDER_NO_INGREDIENTS = 'Ingredient ids must be provided'