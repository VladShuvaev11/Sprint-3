from rest_framework import routers
from .views import MountainsViewSet, get_data, MountainsList, submit_data, update_data
from django.urls import path, include





router = routers.DefaultRouter()
router.register(r'mountains', MountainsViewSet, basename='mountains')


urlpatterns = [
    path('', include(router.urls)),
    path('submitdata/', MountainsList.as_view(), name='mountains_list'),
    path('api/submitdata/<int:pk>/', get_data, name='get_data'),
    path('submitData/create/', submit_data, name='submit_data'),
    path('api/submitData/<int:pk>/update/', update_data, name='update_data'),
]