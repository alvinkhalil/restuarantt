from postbloq import views
from django.urls import path

app_name = "postbloq"

urlpatterns = [

  path("",views.post_list, name="post_list"),
  path("<int:id>",views.post_detail, name="post_detail"),
  path("tags=<slug:tag>",views.post_tags, name="post_tags"),
  path("category=<slug:category>",views.post_category, name="post_category"),
  path("search",views.post_list, name="search"),


]
