from django.urls import path
from . import views

urlpatterns = [
    #http://localhost:8000/cereals
    path('', views.index, name="cereal-index"),
    path('<int:id>', views.get_cereal_by_id, name="cereal_details"),
    path('create_cereal', views.create_cereal, name="create_cereal"),
    path('delete_cereal/<int:id>', views.delete_cereal, name="delete_cereal"),
    path('update_cereal/<int:id>', views.update_cereal, name="update_cereal")
]
