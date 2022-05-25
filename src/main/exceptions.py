from rest_framework.exceptions import APIException


class IncorrectMethod(APIException):
    status_code = 405
    default_detail = 'Incorrect using of method'
    default_code = 'method_not_allowed'


class BadOperation(APIException):
    status_code = 400
    default_detail = 'Incorrect operation'
    default_code = 'bad_request'
