from django.urls import path
from .views import BlacklistTokenUpdateView, UserCreate #, UserView, LogoutView, RegisterView, LoginView,

urlpatterns = [
    path('register/', UserCreate.as_view()),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),
         name='blacklist')    
    # login
    # refresh 
         
    # path('login', LoginView.as_view()),
    # path('logout', LogoutView.as_view()),
]

