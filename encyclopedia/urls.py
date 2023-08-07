from django.urls import path

from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search_box , name ='search'),
    path("make entry", views.make_entry, name = "make entry"),
    path("editpage/<title>/",views.editpage, name = "editpage"),
    path("randompage", views.random, name = "random page"),
    path("save_new_entry/<tit>/", views.save_new_entry, name = 'save_new_entry'),
    path("<str:tit>", views.title, name = "title"),
 
    
]
   