from django.urls import path

from . import views

# url patterns will all ook like
# path(<url pattern>, <template>, name=<view name>)
app_name = 'polls'
urlpatterns = [
	# ex: /polls/
	path('', views.index, name='index'),
	# ex: /polls/5
	path('specifics/<int:question_id>/', views.detail, name='detail'),
	# ex: /polls/5/results
	path('<int:question_id>/results/', views.results, name='results'),
	# ex: /polls/5/vote/
	path('<int:question_id>/vote/', views.vote, name='vote'),
	path('signup', views.signup, name='signup'),
	path('login', views.login, name='login'),
	path('logout', views.logout, name='logout')
]