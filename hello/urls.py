from django.urls import path
from hello.views import hello_world, hello_china, hello_html, article_list, search, render_html, request_info, response, \
    json_response, file_response, not_found, find_page, index, tag, extend

urlpatterns = [
    path('world/', hello_world, name='hello_world'),
    path('china/', hello_china, name='hello_china'),
    path('html/', hello_html, name='hello_html'),
    path('article/<int:month>', article_list, name='article_list'),
    path('search', search, name='search'),
    path('render/', render_html, name='render_html'),
    path('req/', request_info, name='request_info'),
    path('resp/', response, name='response'),
    path('json', json_response, name='json_response'),
    path('file', file_response, name='file_response'),
    path('not/found', not_found, name='not_found'),
    path('find/<int:article_id>', find_page, name='find_page'),
    path('index', index, name='index'),
    path('tag', tag, name='tag'),
    path('extend', extend, name='extend')
]