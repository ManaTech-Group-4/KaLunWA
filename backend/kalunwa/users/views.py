from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import (
    UserSerializer, 
    CustomTokenObtainPairSerializer
)
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import(
    AllowAny, 
    IsAuthenticated,
) 

################
# logging in is done in api/token/
# registration is done in api/users/register/
################

class CustomObtainTokenPairView(TokenObtainPairView):
    """
    added given username addition on payload. 
    """
    permission_classes = (AllowAny,)
    serializer_class = CustomTokenObtainPairSerializer

class UserCreate(APIView):
    """
    Creates a user 
        - UserSerializer -> email & password
    change permission here: either admin or superadmin
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, format='json'):
        """
        create signal to create a profile if user creation is successful 
        (if admin profile needs to be created)
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


################
# logging in is done in api/users/logout/blacklist/
################
class BlacklistTokenUpdateView(APIView):
    """
    use cases: blacklist token after user logs out
    # user presses logout; fires api to this view, process the refresh token and
    put it in the blacklist db table 
    """
   # permission_classes = [IsAuthenticated] #should this be is_authenticated
    authentication_classes = ()

    def post(self, request):
        try:
            # warning message if refresh_token none (this is required etc.)
            refresh = request.data["refresh"]
            token = RefreshToken(refresh)
            token.blacklist()
            # # tell client to reset the view (back to login page)
            return Response(status=status.HTTP_205_RESET_CONTENT) 
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)