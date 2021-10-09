from django.urls import path
from boards import views

urlpatterns = [
    path("", views.boards_top, name="home"),
    path('<int:pk>', views.board_topics, name='board_topics'),
    path('<int:pk>/new/', views.new_topic, name='new_topic'),

    # path("culc/", views.CulcView.as_view(), name="culc"),

    # path('review_detail/<int:pk>', ReviewDetail.as_view(), name='review_detail'),
    # path('review_create/', ReviewCreate.as_view(), name='review_create'),
    # path('review_delete/<int:pk>', ReviewDelete.as_view(), name='review_delete'),
    # path('review_update/<int:pk>', ReviewUpdate.as_view(), name='review_update'),
]