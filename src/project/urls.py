from django.urls import path

from project.views import (
	create_project_view,
	detail_project_view,
	edit_project_view,
)

app_name = 'project'

urlpatterns = [
    path('create/', create_project_view, name="create"),
    path('<slug>/', detail_project_view, name="detail"),
    path('<slug>/edit/', edit_project_view, name="edit"),
 ]

