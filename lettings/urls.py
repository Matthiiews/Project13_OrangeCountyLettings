from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'lettings'


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:letting_id>/', views.letting, name='letting'),
]

if settings.DEBUG:

    # This allows the error pages to be debugged during developement
    urlpatterns += static(
          settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += [
#         path("404/", views.page_not_found, kwargs={"exception": Exception("Page not Found")}),
#         path("500/", views.server_error),
#     ]
