from django.contrib import admin
from django.urls import path
from mainApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('talabalar/', talabalar_royxati),
    path('loyihalar/', loyihalar_royxati),
    path('tugallanmagan_loyihalar/', tugallanmagan_loyihalar),
    path('uchinchi_kurs/', uchinchi_kurs_talabalar),
    path('yangi_reja/', yangi_reja_qoshish),
    path('bitiruvchilar/', bitiruvchilar_rejalari),
    path('yoshi_kattalar/', yoshi_kattalar),


]
