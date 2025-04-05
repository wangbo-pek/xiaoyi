from django.db import models


# 日记、日记列表
class Diary(models.Model):
    title = models.CharField(verbose_name='标题', max_length=64)
    markdown_content = models.TextField(verbose_name='渲染前的md', blank=True, null=True)
    image_urls = models.JSONField(verbose_name='插图链接列表', blank=True, null=True)

    def __str__(self):
        return self.diarylist.title


class DiaryList(models.Model):
    title = models.CharField(verbose_name='标题', max_length=64)
    brief = models.CharField(verbose_name='摘要', max_length=128, blank=True, null=True)
    is_show = models.BooleanField(verbose_name='是否显示', default=True)
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    modified_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    cover_img = models.URLField(verbose_name='封面图', max_length=512, blank=True, null=True)
    # 日记 1:1 日记列表
    diary = models.OneToOneField(to='Diary', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}的列表'


# 笔记、笔记信息、笔记列表
class Note(models.Model):
    title = models.CharField(verbose_name='标题', max_length=64)
    markdown_content = models.TextField(verbose_name='渲染前的md', blank=True, null=True)
    image_urls = models.JSONField(verbose_name='插图链接列表', blank=True, null=True)

    def __str__(self):
        return self.notelist.title


class NoteList(models.Model):
    title = models.CharField(verbose_name='标题', max_length=64)
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
    # 笔记 1:n 分类
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE)
    # 笔记 n:n 标签
    tags = models.ManyToManyField(to='Tag')

    def __str__(self):
        return f'{self.title}的列表'


# 标签
class Tag(models.Model):
    name = models.CharField(verbose_name='标签名称', max_length=16, unique=True)
    is_show = models.BooleanField(verbose_name='是否显示', default=True)
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    modified_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    def __str__(self):
        return self.name


# 分类
class Category(models.Model):
    name = models.CharField(verbose_name='分类', max_length=16, default='default')
    is_show = models.BooleanField(verbose_name='是否显示', default=True)
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    modified_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    def __str__(self):
        return self.name


# 网站信息
class BlogInfo(models.Model):
    blog_name = models.CharField(verbose_name='博客名称', max_length=32, default='XiaoYi_Blog')
    my_name = models.CharField(verbose_name='我的名字', max_length=32, default='Wang')
    blog_article_count = models.IntegerField(verbose_name='总文章数', default=0)
    blog_words_count = models.IntegerField(verbose_name='总字数', default=0)
    blog_viewed_count = models.IntegerField(verbose_name='总访问量', default=0)
    blog_duration_running = models.IntegerField(verbose_name='已运行天数', default=0)
