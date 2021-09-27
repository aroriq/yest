from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('yhauth/', include('django.contrib.auth.urls')), #  追加
    # path('yhauth/', include('yhauth.urls')), #  追加
    path('admin/', admin.site.urls),
    path('', include('yhauth.urls')),
    path('docs/', include('docs.urls')),
    path('sales/', include('sales.urls')),
    # path('blog/', include('blog.urls')),
]

#Modify Site Header
admin.site.site_header = 'Yes&Home'
#Modify Site Title
admin.site.site_title = 'Yes&Home'
#Modify Site Index Title
admin.site.index_title = 'Yes&Home Database'
#Modify Site URL
admin.site.site_urls= '/admin'