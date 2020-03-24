from django.conf.urls import url
from django.contrib import admin
from myapp.views import IndexTemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^myapp/', IndexTemplateView.as_view()),
]