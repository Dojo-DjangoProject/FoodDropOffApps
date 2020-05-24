from django.urls import path #Include path function
from . import views # import views file within the same folder (from .)

# RESTful
urlpatterns = [
    path('user_order',views.index),
    # path('user_order/new', views.new),
    # path('user_order/new/create',views.create),
    # path('user_order/<int:show_id>', views.show_info),
    # path('user_order/<int:show_id>/edit', views.edit),
    # path('user_order/<int:show_id>/edit/update', views.update),
    # path('user_order/<int:show_id>/destroy', views.destroy),
]