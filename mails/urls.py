from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
	path('upload/',views.upload,name="upload"),
	path('mail/<int:mail_id>/',views.mail_detail,name="mail_detail"),
	path('settings/',views.settings,name="settings"),
	path('update-settings/',views.updateSettings,name='update_settings')
]
