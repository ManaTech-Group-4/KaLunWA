from django.shortcuts import get_object_or_404
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
    ListAPIView,
    RetrieveUpdateAPIView,
)
from .permissions import (
    AuthenticatedAndReadOnly,
    OwnersOnly,
    SuperUserOnly,
    SelfUserOnly
)
from .serializers import (
    UserSerializer, 
    CustomTokenObtainPairSerializer,
    UserChangePasswordSerializer,
)
from .models import User
from rest_framework.response import Response


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

    permission_classes = [SuperUserOnly] 
    def post(self, request, format='json'):
        """
        create signal to create a profile if user creation is successful 
        (if admin profile needs to be created) -> done
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
    SuperUsers and users account owners themselves can edit and delete user information. 
    Authenticated Users would only be permitted to view user information. 
    """
    permission_classes = [
        SuperUserOnly | # SuperUsers can edit and delete user information.
        SelfUserOnly | # users account owners themselves can edit and delete their own user information.
        AuthenticatedAndReadOnly # authenticated users can only view
        ] 
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BlacklistTokenUpdateView(APIView):
    """
    use cases: blacklist token after user logs out
    # user presses logout; fires api to this view, process the refresh token and
    put it in the blacklist db table 
    """

    def post(self, request):
        try:
            # warning message if refresh_token none (this is required etc.)
            refresh = request.data["refresh"]
            token = RefreshToken(refresh)
            token.blacklist()
            # # tell client to reset the view (back to login page)
            return Response(status=status.HTTP_205_RESET_CONTENT) 
        except Exception as e:
            return Response(data=e.__cause__,status=status.HTTP_400_BAD_REQUEST)


class UserChangePasswordView(APIView):
    def get_object(self, pk):
        return get_object_or_404(User, pk=pk)

    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = UserChangePasswordSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data="Password change successful.", status=status.HTTP_200_OK)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)