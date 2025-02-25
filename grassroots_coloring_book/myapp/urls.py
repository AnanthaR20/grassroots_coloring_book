# Made this file with youtube tutorial
from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("home",views.home,name="home"),
    path("base",views.base,name="base"),
    path("hello",views.hello_page,name="hello"),
    path("todos/",views.todos,name="Todos"),
    path("display_prompt",views.display_prompt,name="display_prompt")
]
"""note: the first parameter triggers the view precisely the way it is spelled here. 
no backlash means no backslash"""