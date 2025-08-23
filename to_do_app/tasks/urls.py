from django.urls import path
from . import views
from django.views.generic import TemplateView
urlpatterns = [
    path('',views.index,name="index"),
    #path('post_user/',views.post_user,name="post_user")
    # path("Contacs",views.contacs)
    # path('about/',TemplateView.as_view(template_name="tasks/about.html")),
    # path('Contacs/',TemplateView.as_view(template_name="tasks/Contacs.html",
    #                                      extra_context={"header":"О сайте"}))
    # path('tasks/<int:task_id>/', views.view_task,name="view_task"),
    # path("tasks/new/",views.create_task,name="create_task"),
    # path("tasks/<int:task_id>/edit",views.edit_task,name="edit_task"),
    # path("tasks/<int:task_id>/delete/",views.delete_task,name="delete_task")
]
