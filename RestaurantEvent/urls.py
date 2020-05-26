from django.urls import path #Include path function
from . import views # import views file within the same folder (from .)

# RESTful
#Root path is events/
urlpatterns = [
    path('restaurant_event',views.index),
    path('new/', views.newEvent),
    path('new/create',views.createEvent),
    # path('restaurant_event/<int:show_id>', views.show_info),
    # path('restaurant_event/<int:show_id>/edit', views.edit),
    # path('restaurant_event/<int:show_id>/edit/update', views.update),
    # path('restaurant_event/<int:show_id>/destroy', views.destroy),
]