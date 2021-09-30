from django.urls import path
from . import views

app_name = 'sales_app'
urlpatterns = [

    path('sales_list', views.sales_list.as_view(), name='sales_list'),
  # path('', views.sales_detail.as_view(), name='sales_detail'),
    path('sales_summary/', views.sales_summary, name="sales_summary"),
    
    path('staff_list/', views.staff_list.as_view(), name='staff_list'),
    path('staff_detail/<int:user_id>/', views.staff_detail, name='staff_detail'),

    path('create_svg/<int:user_id>/', views.create_svg, name='create_svg'),
    path('create_bar_svg/<int:user_id>/', views.create_bar_svg, name='create_bar_svg'),
 
    # path('plot/', views.get_svg, name='bar'),
    # path('stats/total', views.barchart, name="img_stats_total"),
    # path('analysis/', views.analysis_screen, name='analysis_screen'),
    # path('analysis/plot', views.img_plot, name="img_plot"),

]