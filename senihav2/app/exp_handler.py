from rest_framework.views import exception_handler

def bti_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        response.data['status'] = False
        if "detail" in response.data:
            response.data['description'] = response.data.pop("detail")
    return response
