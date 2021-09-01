from django.urls import path
from .views import customerList, DocsHiyomeisai

urlpatterns = [
    path('customerlist/', customerList, name='customerlist'),
    path('hiyomeisai/', DocsHiyomeisai, name='hiyomeisai'),
    # path('review_detail/<int:pk>', ReviewDetail.as_view(), name='review_detail'),
    # path('review_create/', ReviewCreate.as_view(), name='review_create'),
    # path('review_delete/<int:pk>', ReviewDelete.as_view(), name='review_delete'),
    # path('review_update/<int:pk>', ReviewUpdate.as_view(), name='review_update'),
]