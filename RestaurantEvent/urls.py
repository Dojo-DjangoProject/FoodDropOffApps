from django.urls import path #Include path function
from . import views # import views file within the same folder (from .)

# RESTful
urlpatterns = [
    path('restaurant_event',views.index),
    # path('restaurant_event/new', views.new),
    path('restaurant_event/new/create',views.create),
    # path('restaurant_event/<int:show_id>', views.show_info),
    # path('restaurant_event/<int:show_id>/edit', views.edit),
    # path('restaurant_event/<int:show_id>/edit/update', views.update),
    # path('restaurant_event/<int:show_id>/destroy', views.destroy),
]