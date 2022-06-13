from django.db import IntegrityError
from django.db.models import ProtectedError
from rest_framework.views import Response, exception_handler
from rest_framework import status


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first to get the standard error response.
    response = exception_handler(exc, context)

    # if there is an IntegrityError and the error response hasn't already been generated
    if isinstance(exc, ProtectedError):

        protected_objects_in_string= ''
        for protected_obj in exc.protected_objects:
            protected_objects_in_string += f"Protected Record: '{protected_obj}' \
in Table: '{protected_obj.__class__.__name__}'-- "

        response =Response( {
            "detail": f"Cannot delete record due to protected references in \
other tables, namely -> {protected_objects_in_string}"
        },
        status=status.HTTP_400_BAD_REQUEST        
        )

        # {<CabinOfficer: Camp Zero Waste Publicity Cabin, Other: lastname 3>}
        print(type(exc.protected_objects))

    if isinstance(exc, IntegrityError) and not response:
        # print(exc.__annotations__)
        response = Response(
            {
                "detail": str(exc.__cause__),
                "code":"integrity-error"
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    return response