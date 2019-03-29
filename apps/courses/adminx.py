import xadmin
from courses.models import Course, Lesson, Video, CourseResource


class CourseAdmin(object):
    list_display = ['name', 'description', 'detail', 'degree', 'learn_times',
                    'student_numbers', 'collection_numbers', 'image', 'click_numbers', 'add_time']
    list_filter = ['name', 'description', 'detail', 'degree', 'learn_times',
                   'student_numbers', 'collection_numbers', 'image', 'click_numbers', 'add_time']
    search_fields = ['name', 'description', 'detail', 'degree', 'learn_times',
                     'student_numbers', 'collection_numbers', 'image', 'click_numbers']


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    list_filter = ['course__name', 'name', 'add_time']
    search_fields = ['course', 'name']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    list_filter = ['lesson__name', 'name', 'add_time']
    search_field = ['lesson', 'name']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    list_filter = ['course__name', 'name', 'download', 'add_time']
    search_field = ['course', 'name', 'download']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
