from django.urls import path, include
from rest_framework import routers

from accounts.api.views import(
    UserAuthenticatedProfileViewSet,
    UserRegistrationCreateAPIView,
    UserChangePasswordAPIView, UserReadOnlyViewSet,
    UserAuthenticatedFollowingsAPIView,
    UserAuthenticatedFollowersAPIView, DestroyFollowingAPIView,
    EmployerRegistrationCreateAPIView, LoginAPIView
)


user_info = routers.SimpleRouter()
user_info.register('user', UserReadOnlyViewSet, basename='user-info')


urlpatterns = [
    path('user/register/', UserRegistrationCreateAPIView.as_view(),
         name='user-register'),
    path('changepassword/', UserChangePasswordAPIView.as_view(), name='change-password'),
    path('profile/', UserAuthenticatedProfileViewSet.as_view(), name='user-profile'),
    path('profile/followings/', UserAuthenticatedFollowingsAPIView.as_view(), name='user-profile-followings'),
    path('profile/followers/', UserAuthenticatedFollowersAPIView.as_view(), name='user-profile-followers'),
    path('profile/unfollow/<int:pk>', DestroyFollowingAPIView.as_view(), name='following-destroy'),
    path('employer/register/', EmployerRegistrationCreateAPIView.as_view()),
    path('login/', LoginAPIView.as_view(), name='login'),

    path('', include(user_info.urls)),
]