from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from .api.classroom import ClassroomList, ClassroomDetail
from .api.comparator import CompareAPI
from .api.convertor import PdfMergeAPI
from .api.core import Signup
from .api.mindmap import MindmapList, MindmapDetail
from .api.notetaker import ProcessAPI
from .api.user import UserDetail
from .views import get_csrf_token

urlpatterns = [
    path('note', ProcessAPI.as_view()),
    path('pdf', PdfMergeAPI.as_view()),
    path('compare', CompareAPI.as_view()),

    path('rest/mindmaps/', MindmapList.as_view()),
    path('rest/mindmaps/<int:pk>/', MindmapDetail.as_view()),

    path('rest/classrooms/', ClassroomList.as_view()),
    path('rest/classrooms/<int:pk>/', ClassroomDetail.as_view()),

    path('rest/users/<int:pk>/', UserDetail.as_view()),

    path('csrf', get_csrf_token),

    path('auth/obtain_token', TokenObtainPairView.as_view()),
    path('auth/refresh_token', TokenRefreshView.as_view()),
    path('auth/verify_token', TokenVerifyView.as_view()),

    path('auth/signup', Signup.as_view())
]
