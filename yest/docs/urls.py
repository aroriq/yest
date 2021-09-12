from django.urls import path
from .views import customerList, DocsHiyomeisai
from docs import views

urlpatterns = [
    path("staff_top/", views.staff_top, name="staff_top"),
    path("staff_new/", views.staff_new, name="staff_new"),
    path("staff/<int:staff_id>/", views.staff_detail, name="staff_detail"),
    path("staff/<int:staff_id>/edit/", views.staff_edit, name="staff_edit"),

    path('customerlist/', customerList, name='customerlist'),
    path('hiyomeisai/', DocsHiyomeisai, name='hiyomeisai'),
    # path('review_detail/<int:pk>', ReviewDetail.as_view(), name='review_detail'),
    # path('review_create/', ReviewCreate.as_view(), name='review_create'),
    # path('review_delete/<int:pk>', ReviewDelete.as_view(), name='review_delete'),
    # path('review_update/<int:pk>', ReviewUpdate.as_view(), name='review_update'),
]