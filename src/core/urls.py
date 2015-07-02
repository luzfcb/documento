from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^list/$',
        views.DocumentListView.as_view(),
        name='document_list'
        ),
    url(r'^create/$',
        views.DocumentCreateView.as_view(),
        name='document_create'
        ),
    url(r'^update/(?P<pk>\d+)/$',
        views.DocumentUpdateView.as_view(),
        name='document_update'
        ),
    url(r'^versions/(?P<pk>\d+)/$',
        views.DocumentRevertView.as_view(),
        name='document_revert'
        ),
]
