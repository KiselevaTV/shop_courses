from django.urls import path, include
from api.models import CourseResource, CategoryResource
from tastypie.api import Api


api = Api(api_name='v1')
course_recource = CourseResource()
category_recource = CategoryResource()
api.register(course_recource)
api.register(category_recource)

# api/v1/courses/        GET, POST
# api/v1/courses/1/      GET, DELETE
# api/v1/categories/     GET
# api/v1/categories/1/   GET

# For POST, DELETE add header
# Key: Authorization
# Value: ApiKey tatyana:123456789absd

urlpatterns = [
    path('', include(api.urls), name='index')
]
