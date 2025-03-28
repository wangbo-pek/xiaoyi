from unittest import defaultTestLoader

from django.db import models


class Test(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField()
    img = models.ImageField(max_length=128, upload_to='test_cover/', blank=True, null=True)


class BaseList(models.Model):
    title = models.CharField(verbose_name='标题', max_length=32)
    subtitle = models.CharField(verbose_name='副标题', max_length=32)
    brief = models.CharField(verbose_name='摘要', max_length=64, blank=True, null=True)
    is_show = models.BooleanField(verbose_name='是否显示', default=True)
    is_pinned = models.BooleanField(verbose_name='是否置顶', default=False)
    is_recommended = models.BooleanField(verbose_name='是否推荐', default=False)
    viewed_count = models.IntegerField(verbose_name='被浏览次数', default=0)
    liked_count = models.IntegerField(verbose_name='被赞次数', default=0)
    disgusted_count = models.IntegerField(verbose_name='被踩次数', default=0)
    encouraged_count = models.IntegerField(verbose_name='被鼓励次数', default=0)
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    modified_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    class Meta:
        abstract = True


# 日记、日记列表
class Diary(models.Model):
    title = models.CharField(verbose_name='标题', max_length=32)
    content = models.TextField(verbose_name='日记内容')

    def __str__(self):
        return self.diarylist.title


class DiaryList(BaseList):
    # 日记 1:1 日记列表
    diary = models.OneToOneField(to='Diary', on_delete=models.CASCADE)
    cover_img = models.CharField(verbose_name='封面图', max_length=512, blank=True, null=True,
                                  default='default_cover.jpg')

    def __str__(self):
        return f'{self.title}的列表'


# 文章、文章列表
class Essay(models.Model):
    title = models.CharField(verbose_name='标题', max_length=32)
    content = models.TextField(verbose_name='文章内容')

    def __str__(self):
        return self.essaylist.title


class EssayList(BaseList):
    # 文章 1:1 文章列表
    essay = models.OneToOneField(to='Essay', on_delete=models.CASCADE)
    # 文章 n:n 标签
    tags = models.ManyToManyField(to='Tag')
    cover_img = models.CharField(verbose_name='封面图', max_length=512, blank=True, null=True,
                                 default='default_cover.jpg')
    is_reprint = models.BooleanField(verbose_name='是否转载', default=False)
    reprint_source = models.CharField(verbose_name='转载源', max_length=64, blank=True, null=True)
    reprint_author = models.CharField(verbose_name='原作者', max_length=64, blank=True, null=True)

    def __str__(self):
        return f'{self.title}的列表'


# 笔记、笔记信息、笔记列表
class Note(models.Model):
    title = models.CharField(verbose_name='标题', max_length=32)
    content = models.TextField(verbose_name='笔记内容')

    def __str__(self):
        return self.notelist.title


class NoteList(BaseList):
    # 笔记 1:1 笔记列表
    note = models.OneToOneField(to='Note', on_delete=models.CASCADE)
    # 笔记 1:n 二级分类
    second_classification = models.ForeignKey(to='SecondClassification', on_delete=models.CASCADE)
    # 笔记 n:n 标签
    tags = models.ManyToManyField(to='Tag')
    cover_img = models.CharField(verbose_name='封面图', max_length=512, blank=True, null=True,
                                 default='default_cover.jpg')

    def __str__(self):
        return f'{self.title}的列表'

    def get_note_first_classification(self):
        return self.second_classification.first_classification


# 标签
class Tag(models.Model):
    name = models.CharField(verbose_name='标签名称', max_length=16, unique=True)
    is_show = models.BooleanField(verbose_name='是否显示', default=True)
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    modified_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    def __str__(self):
        return self.name


# 一级分类
class FirstClassification(models.Model):
    name = models.CharField(verbose_name='一级分类', max_length=16)
    is_show = models.BooleanField(verbose_name='是否显示', default=True)
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    modified_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    def __str__(self):
        return self.name


# 二级分类
class SecondClassification(models.Model):
    name = models.CharField(verbose_name='二级分类', max_length=16)
    # 如果一级分类被隐藏，则该一级分类下所有二级分类也需要隐藏
    is_show = models.BooleanField(verbose_name='是否显示', default=True)
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    modified_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    # 一级分类 1:n 二级分类
    first_classification = models.ForeignKey(to='FirstClassification', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
