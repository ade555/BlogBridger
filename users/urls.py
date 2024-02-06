from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from.views import Signup, RetrieveUpdateDeleteUserView
urlpatterns = [
    path('create/', Signup.as_view(), name="signup"),
    path('login/', TokenObtainPairView.as_view(), name="login"),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('details/<int:pk>/', RetrieveUpdateDeleteUserView.as_view(), name='user-details'),
]
