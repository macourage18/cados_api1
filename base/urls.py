from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    # TokenRefreshView,
)
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
# from django.conf import settings
# from django.conf.urls.static import static



urlpatterns = [
  path('', views.endpoints),

  path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('advocates/', views.advocate_list, name="advocates"),
  path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon/favicon.ico'))),
  # path('advocates/<str:username>/', views.advocate_details),
  path('advocates/<str:username>/', views.AdvocateDetial.as_view()),

  #companies
  path('companies/', views.companies_list),

  #compianies id
  path('companies/<str:name>/', views.companies_details)
] 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)