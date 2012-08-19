from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    '',
    url(r'^upload/', 'ckeditor.views.upload', name='ckeditor_upload'),
    url(r'^browse/', 'ckeditor.views.index', name='ckeditor_browse'),
    url(r'^connector/', 'ckeditor.views.connector'),
    url(r'^sounds/', 'ckeditor.views.sounds'),

)
