from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('contact/',views.contact),
    path('products/',views.products),
    path('news/',views.news),
    path('fashion/',views.fashion),
    path('updateProfile/',views.updateProfile),
    path('showdatapage/',views.showdatapage),
    path('notes/',views.notes,name='notes'),
    path('emaillogout/',views.emaillogout),
    path('upload_image/', views.upload_image, name='upload_image'),
    path('image_list/', views.image_list, name='image_list'),

]


# Serving the media files in development mode
# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# else:
#     urlpatterns += staticfiles_urlpatterns()