from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from django_tiptap2_demo.demo_app.views import NoteCreateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", NoteCreateView.as_view(), name="note-add"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
