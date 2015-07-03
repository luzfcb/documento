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


    url(r'^phome/$',
        views.PessoaListView.as_view(),
        name='pessoa_home'
        ),
    url(r'^plist/$',
        views.PessoaListView.as_view(),
        name='pessoa_list'
        ),
    url(r'^pcreate/$',
        views.PessoaCreateView.as_view(),
        name='pessoa_create'
        ),
    url(r'^pupdate/(?P<pk>\d+)/$',
        views.PessoaUpdateView.as_view(),
        name='pessoa_update'
        ),
    url(r'^phistory/(?P<pk>\d+)/$',
        views.PessoaHistoryView.as_view(),
        name='pessoa_history'
        ),
    url(r'^prevert/(?P<pk>\d+)/$',
        views.PessoaRevertView.as_view(),
        name='pessoa_revert'
        ),
]
