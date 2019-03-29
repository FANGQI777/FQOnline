import xadmin

from organization.models import CourseOrganization, CityDict, Teacher


class CourseOrganizationAdmin(object):
    list_display = ['name', 'description', 'click_numbers', 'collection_numbers', 'image',
                    'address', 'city', 'add_time']
    list_filter = ['name', 'description', 'click_numbers', 'collection_numbers', 'image',
                   'address', 'city__name', 'add_time']
    search_field = ['name', 'description', 'click_numbers', 'collection_numbers', 'image',
                    'address', 'city']


class CityDictAdmin(object):
    list_display = ['name', 'description', 'add_time']
    list_filter = ['name', 'description', 'add_time']
    search_field = ['name', 'description']


class TeacherAdmin(object):
    list_display = ['organization__name', 'name', 'work_years', 'work_company', 'work_position',
                    'points', 'click_numbers', 'collection_numbers', 'add_time']
    list_filter = ['organization__name', 'name', 'work_years', 'work_company', 'work_position',
                   'points', 'click_numbers', 'collection_numbers', 'add_time']
    search_field = ['organization__name', 'name', 'work_years', 'work_company', 'work_position',
                    'points', 'click_numbers', 'collection_numbers', 'add_time']


xadmin.site.register(CourseOrganization, CourseOrganizationAdmin)
xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
