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
    blog_name = models.CharField(verbose_name='博客名称', max_length=64, default='XiaoYi_Blog')
    my_name = models.CharField(verbose_name='我的名字', max_length=64, default='Wang')
    my_motto = models.CharField(verbose_name='我的座右铭', max_length=128, default='')
    my_wisdom = models.CharField(verbose_name='我的警示名言', max_length=256, default='')
    my_location = models.CharField(verbose_name='我的所在地', max_length=64, default='北京')
    my_career = models.CharField(verbose_name='我的职业', max_length=64, default='产品经理')
    my_short_intro = models.CharField(verbose_name='我的简短介绍', max_length=128, default='')
    my_formal_intro = models.CharField(verbose_name='我的介绍', max_length=256, default='')
    blog_articles_count = models.IntegerField(verbose_name='总文章数', default=0)
    blog_words_count = models.IntegerField(verbose_name='总字数', default=0)
    blog_viewed_count = models.IntegerField(verbose_name='总访问量', default=0)
    blog_duration_running = models.IntegerField(verbose_name='已运行天数', default=0)
    my_wechat = models.CharField(verbose_name='我的微信', max_length=64, default='wboo1225')
    my_mail = models.EmailField(verbose_name='我的邮箱', max_length=64, default='wangbo.pek@gmail.com')
    coffee_by_wechat = models.URLField(verbose_name='微信支付', max_length=512, blank=True, null=True)
    coffee_by_alipay = models.URLField(verbose_name='支付宝', max_length=512, blank=True, null=True)


# 访客记录
class VisitorLog(models.Model):
    uuid = models.CharField(verbose_name='访客唯一标识', max_length=64, db_index=True)
    ip_addr = models.GenericIPAddressField()
    user_agent = models.TextField()
    referer = models.TextField(blank=True, null=True)
    path = models.CharField(verbose_name='访问路径', max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.uuid} - {self.path}@{self.timestamp}'