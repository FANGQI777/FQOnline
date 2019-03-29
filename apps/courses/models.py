from datetime import datetime

from django.db import models


# Course Information
class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"课程名")
    description = models.CharField(max_length=300, verbose_name=u"课程描述")
    detail = models.TextField(verbose_name=u"课程详情")
    degree = models.CharField(choices=(("junior", u"初级"), ("medium", u"中级"), ("senior", u"高级")),
                              max_length=10, verbose_name=u"课程级别")
    learn_times = models.IntegerField(default=0, verbose_name=u"学习市场-->分钟数")
    student_numbers = models.IntegerField(default=0, verbose_name=u"学习人数")
    collection_numbers = models.IntegerField(default=0, verbose_name=u"收藏人数")
    image = models.ImageField(upload_to="course/%Y%m", verbose_name=u"课程封面")
    click_numbers = models.IntegerField(default=0, verbose_name=u"点击量")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# Chapter
class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=u"课程")
    name = models.CharField(max_length=100, verbose_name=u"章节名称")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程章节"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# Video
class Video(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name=u"章节名称")
    name = models.CharField(max_length=100, verbose_name=u"视频名称")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程视频"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# Course Resource
class CourseResource(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="课程")
    name = models.CharField(max_length=100, verbose_name=u"资源名称")
    download = models.FileField(upload_to="course/resource/%Y%m", verbose_name=u"资源文件", max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程资源"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
