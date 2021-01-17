from django.urls import path

from .views import ChildCreate, ParentCreate, parent_create, get_parent_id

urlpatterns = [
    path('', ChildCreate.as_view(), name='child-create'),
    path('parent/create2', ParentCreate.as_view(), name='parent-create2'),
    path('parent/create', parent_create, name='parent-create'),
    path('ajax/get_parent_id/', get_parent_id, name='get-parent-id'),
]
