from django.urls import path #Include path function
from . import views # import views file within the same folder (from .)

# RESTful
urlpatterns = [
    # path('messages',views.index),
    # path('messages/new', views.new),
    # path('messages/new/create',views.create),
    # path('messages/<int:show_id>', views.show_info),
    # path('messages/<int:show_id>/edit', views.edit),
    # path('messages/<int:show_id>/edit/update', views.update),
    # path('messages/<int:show_id>/destroy', views.destroy),
]