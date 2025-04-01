from django.db import models


# 日记、日记列表
class Diary(models.Model):
    title = models.CharField(verbose_name='标题', max_length=32)
    markdown_content = models.TextField(verbose_name='渲染前的md', blank=True, null=True)
    image_urls = models.JSONField(verbose_name='插图链接列表', blank=True, null=True)

    def __str__(self):
        return self.diarylist.title


class DiaryList(models.Model):
    title = models.CharField(verbose_name='标题', max_length=32)
    brief = models.CharField(verbose_name='摘要', max_length=128, blank=True, null=True)
    is_show = models.BooleanField(verbose_name='是否显示', default=True)
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    modified_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    cover_img = models.ImageField(verbose_name='封面图', max_length=512, blank=True, null=True,
                                  default='diary_covers')
    # 日记 1:1 日记列表
    diary = models.OneToOneField(to='Diary', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}的列表'


# 文章、文章列表
# class Essay(models.Model):
#     title = models.CharField(verbose_name='标题', max_length=32)
#     markdown_content = models.TextField(verbose_name='渲染前的md', blank=True, null=True)
#     image_urls = models.JSONField(verbose_name='插图链接列表', blank=True, null=True)
#     html_content = models.TextField(verbose_name='渲染后的HTML', blank=True, null=True)
#
#     def __str__(self):
#         return self.essaylist.title
#
#
# class EssayList(models.Model):
#     title = models.CharField(verbose_name='标题', max_length=32)
#     subtitle = models.CharField(verbose_name='副标题', max_length=32)
#     brief = models.CharField(verbose_name='摘要', max_length=128, blank=True, null=True)
#     is_show = models.BooleanField(verbose_name='是否显示', default=True)
#     viewed_count = models.IntegerField(verbose_name='被浏览次数', default=0)
#     created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
#     modified_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)
#     is_recommended = models.BooleanField(verbose_name='是否推荐', default=False)
#     is_reprint = models.BooleanField(verbose_name='是否转载', default=False)
#     reprint_source = models.CharField(verbose_name='转载源', max_length=64, blank=True, null=True)
#     reprint_author = models.CharField(verbose_name='原作者', max_length=64, blank=True, null=True)
#     cover_img = models.ImageField(verbose_name='封面图', max_length=512, blank=True, null=True,
#                                   upload_to='essay_covers')
#     # 文章 1:1 文章列表
#     essay = models.OneToOneField(to='Essay', on_delete=models.CASCADE)
#     # 文章 n:n 标签
#     tags = models.ManyToManyField(to='Tag')
#
#     def __str__(self):
#         return f'{self.title}的列表'


# 笔记、笔记信息、笔记列表
class Note(models.Model):
    title = models.CharField(verbose_name='标题', max_length=32)
    markdown_content = models.TextField(verbose_name='渲染前的md', blank=True, null=True)
    image_urls = models.JSONField(verbose_name='插图链接列表', blank=True, null=True)

    def __str__(self):
        return self.notelist.title


class NoteList(models.Model):
    title = models.CharField(verbose_name='标题', max_length=32)
    subtitle = models.CharField(verbose_name='副标题', max_length=32)
    brief = models.CharField(verbose_name='摘要', max_length=128, blank=True, null=True)
    is_show = models.BooleanField(verbose_name='是否显示', default=True)
    viewed_count = models.IntegerField(verbose_name='被浏览次数', default=0)
    liked_count = models.IntegerField(verbose_name='被赞次数', default=0)
    disgusted_count = models.IntegerField(verbose_name='被踩次数', default=0)
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    modified_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    is_pinned = models.BooleanField(verbose_name='是否置顶', default=False)
    is_recommended = models.BooleanField(verbose_name='是否推荐', default=False)
    cover_img = models.URLField(verbose_name='封面图', max_length=512, blank=True, null=True)

    # 笔记 1:1 笔记列表
    note = models.OneToOneField(to='Note', on_delete=models.CASCADE)
    # 笔记 1:n 二级分类
    second_classification = models.ForeignKey(to='SecondClassification', on_delete=models.CASCADE)
    # 笔记 n:n 标签
    tags = models.ManyToManyField(to='Tag')

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
    is_show = models.BooleanField(verbose_name='是否显示', default=True)
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    modified_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    # 一级分类 1:n 二级分类
    first_classification = models.ForeignKey(to='FirstClassification', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
