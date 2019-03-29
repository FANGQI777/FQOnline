import xadmin
from operation.models import UserAsk, CourseComment, UserFavorite, UserMessage, UserCourse


class UserAskAdmin(object):
    list_display = ['name', 'mobile', 'course_name', 'add_time']
    list_filter = ['name', 'mobile', 'course_name', 'add_time']
    search_field = ['name', 'mobile', 'course_name']


class CourseCommentAdmin(object):
    list_display = ['user', 'course', 'comments', 'add_time']
    list_filter = ['user__username', 'course__name', 'comments', 'add_time']
    search_field = ['user', 'course', 'comments']


class UserFavoriteAdmin(object):
    list_display = ['user', 'favorite_id', 'favorite_type', 'add_time']
    list_filter = ['user__username', 'favorite_id', 'favorite_type', 'add_time']
    search_field = ['user', 'favorite_id', 'favorite_type']


class UserMessageAdmin(object):
    list_display = ['user', 'message', 'has_read', 'add_time']
    list_filter = ['user', 'message', 'has_read', 'add_time']
    search_field = ['user', 'message', 'has_read']


class UserCourseAdmin(object):
    list_display = ['user', 'course', 'add_time']
    list_filter = ['user__username', 'course__name', 'add_time']
    search_field = ['user', 'course', 'add_time']


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComment, CourseCommentAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
