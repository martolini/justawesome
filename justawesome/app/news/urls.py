from django.conf.urls import patterns, include, url


viewpatterns = patterns('justawesome.app.news.views',
	url(r'^nominate/$', 'nominate_view', name='nominate'),
)


ajaxpatterns = patterns('justawesome.app.news.ajax',
	url(r'^nominate/nominate_ajax/$', 'nominate_ajax', name='nominate_ajax'),
)

urlpatterns = viewpatterns + ajaxpatterns