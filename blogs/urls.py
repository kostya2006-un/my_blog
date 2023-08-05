from django.urls import path

from blogs.views import index,posts_list,post_detail,new_post,edit_post,delete_post
app_name = 'blogs'

urlpatterns = [
    path('',index,name = 'index'),
    path('posts',posts_list,name = 'posts_list'),
    path('post/<int:post_id>/',post_detail,name = 'post_detail'),
    path('post/create',new_post,name = 'new_post'),
    path('post/edit/<int:post_id>/',edit_post,name = 'edit_post'),
    path('post_delete/<int:post_id>/',delete_post,name = 'post_delete')
]