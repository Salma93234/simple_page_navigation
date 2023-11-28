from django.urls import path,include
from . import views
urlpatterns = [
    # path('navigation/', include ('navigation.urls')),
    path('about/', views.about),
    path('contact/', views.contact),
]
