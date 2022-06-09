from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import(
    AllowAny, 
    IsAuthenticated,
) 
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    ListAPIView
)
from .permissions import (
    AuthenticatedAndReadOnly,
    SuperUserOnly,
    SelfUserOnly
)
from .serializers import (
    UserSerializer, 
    CustomTokenObtainPairSerializer
)
from .models import User


class CustomObtainTokenPairView(TokenObtainPairView):
    """
    Where users submit their credentials (email & password). Serves as the login
    endpoint.
    - TokenObtainPairView is extended to add flexibility (additional info on 
    token payload e.g. role, username etc.), by using a custom serializer.
    """
    permission_classes = (AllowAny,)
    serializer_class = CustomTokenObtainPairSerializer


class UserCreateView(APIView):
    """
    Creates a user 
        - UserSerializer -> email & password
    change permission here: either admin or superadmin
    """

    permission_classes = [IsAuthenticated, SuperUserOnly] # IsAuthenticated  -> if 2 versions aren't implemented
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


class UserListView(ListAPIView):
    """
    Authenticated users can view basic user list. 
    """
    permission_classes = [IsAuthenticated] 
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
    SuperUsers and Owners can edit and delete user information. 
    Authenticated Users would only be permitted to view user information. 
    """
    permission_classes = [SuperUserOnly | SelfUserOnly
                         | AuthenticatedAndReadOnly] 
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BlacklistTokenUpdateView(APIView):
    """
    use cases: blacklist token after user logs out
    # user presses logout; fires api to this view, process the refresh token and
    put it in the blacklist db table 
    """
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