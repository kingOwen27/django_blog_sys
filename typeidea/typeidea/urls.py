"""typeidea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from blog.views import (
    IndexView,
    CategoryView,
    TagView,
    PostDetailView,
    SearchView,
    AuthorView,
)
from config.views import LinkListView
from .custom_site import custom_site
from comment.views import CommentView
from rest_framework.routers import DefaultRouter
from blog.apis import PostViewSet,CategoryViewSet
from rest_framework.documentation import include_docs_urls
from django.views.decorators.cache import cache_page

router=DefaultRouter()
router.register(r'post',PostViewSet,base_name='api-post')
router.register(r'category',CategoryViewSet,base_name='api_category')

urlpatterns = [
    url(r'^super_admin/', admin.site.urls, name='super-admin'),
    url(r'^admin/', custom_site.urls, name='admin'),

    url(r'^$', IndexView.as_view(), name='index'),
    # url(r'^$', cache_page(60*20,key_prefix='index_chache_')(IndexView.as_view()),name='index'),
    url(r'^category/(?P<category_id>\d+)/$', CategoryView.as_view(), name='category-list'),
    url(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name='tag-list'),
    url(r'^post/(?P<post_id>\d+).html$', PostDetailView.as_view(), name='post-detail'),
    url(r'search/$', SearchView.as_view(), name='search'),
    url(r'author/(?P<owner_id>\d+)/$', AuthorView.as_view(), name='author'),
    url(r'^links/$', LinkListView.as_view(), name='links'),
    url(r'^comment/$', CommentView.as_view(), name='comment'),
    url(r'^api/', include(router.urls,namespace="api")),
    url(r'^api/docs/', include_docs_urls(title='typeidea apis')),
]

# from django.conf import settings
from .settings import base
if base.DEBUG:
    import debug_toolbar
    urlpatterns+=[
        url(r'^__debug__',include(debug_toolbar.urls)),
    ]


