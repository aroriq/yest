from django.urls import path
from . import views

app_name = 'sales_app'
urlpatterns = [
    path('analysis/', views.analysis_screen, name='analysis_screen'),
    path('analysis/plot', views.img_plot, name="img_plot"),

    path('', views.sales_index.as_view(), name='sales_index'),
    # path('', views.sales_detail.as_view(), name='sales_detail'),
    path('stats/', views.stats_top, name='stats_top'),
    path('stats/total', views.barchart, name="img_stats_total"),

    path('data/', views.salesdata, name="salesdata"),

    path('stats2/', views.Index2, name="Index2"),
]