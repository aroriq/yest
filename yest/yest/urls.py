from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('yhauth.urls')),
    # path('docs/', include('docs.urls')),
    # path('sales/', include('sales.urls')),
    # path('blog/', include('blog.urls')),
]

#Modify Site Header
admin.site.site_header = 'Yes&Home Administration'
#Modify Site Title
admin.site.site_title = 'Yes&Home'
#Modify Site Index Title
admin.site.index_title = 'Yes&Home Administration'
#Modify Site URL
admin.site.site_urls= '/admin'