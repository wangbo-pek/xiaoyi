from django.db import models


# 日记
class Diary(models.Model):
    title = models.CharField(verbose_name='日记标题', max_length=32)
    brief = models.CharField(verbose_name='日记摘要', max_length=64)
    content = models.TextField(verbose_name='日记内容')
    cover_img = models.ImageField(verbose_name='封面图', upload_to='diary_covers/', blank=True, null=True,
                                  default='default_cover.jpg')
    is_show = models.BooleanField(verbose_name='是否显示', default=True)
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    modified_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    class Meta:
        ordering = ['-created_time']

    def __str__(self):
        return self.title


class BaseInfo(models.Model):
    viewed_count = models.IntegerField(verbose_name='被浏览次数', default=0)
    liked_count = models.IntegerField(verbose_name='被赞次数', default=0)
    disgusted_count = models.IntegerField(verbose_name='被踩次数', default=0)
    encouraged_count = models.IntegerField(verbose_name='被鼓励次数', default=0)

    class Meta:
        abstract = True


# 文章
class Essay(models.Model):
    title = models.CharField(verbose_name='文章标题', max_length=32)
    brief = models.CharField(verbose_name='文章摘要', max_length=64, blank=True, null=True)
    content = models.TextField(verbose_name='文章内容')
    cover_img = models.ImageField(verbose_name='封面图', upload_to='diary_covers/', blank=True, null=True,
                                  default='default_cover.jpg')
    is_show = models.BooleanField(verbose_name='是否显示', default=True)
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    modified_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    is_reprint = models.BooleanField(verbose_name='是否转载', default=False)
    reprint_from = models.CharField(verbose_name='转载源', max_length=64, blank=True, null=True)
    reprint_whom = models.CharField(verbose_name='原作者', max_length=64, blank=True, null=True)

    # 文章 n:n 标签
    tags = models.ManyToManyField(to='Tag')

    class Meta:
        ordering = ['-created_time']

    def __str__(self):
        return self.title


# 文章信息
class EssayInfo(BaseInfo):
    # 文章信息 1:1 文章
    essay = models.OneToOneField(to='Essay', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.essay.title}的信息'


# 笔记
class Note(models.Model):
    title = models.CharField(verbose_name='笔记标题', max_length=32)
    brief = models.CharField(verbose_name='笔记摘要', max_length=64, blank=True, null=True)
    content = models.TextField(verbose_name='笔记内容')
    cover_img = models.ImageField(verbose_name='封面图', upload_to='diary_covers/', blank=True, null=True,
                                  default='default_cover.jpg')
    is_show = models.BooleanField(verbose_name='是否显示', default=True)
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    modified_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    # 笔记 1:n 二级分类
    second_classification = models.ForeignKey(to='SecondClassification', on_delete=models.CASCADE)
    # 笔记 n:n 标签
    tags = models.ManyToManyField(to='Tag')

    class Meta:
        ordering = ['-created_time']

    def get_note_first_classification(self):
        return self.second_classification.first_classification

    def __str__(self):
        return self.title


# 笔记信息
class NoteInfo(BaseInfo):
    # 笔记信息 1:1 笔记
    note = models.OneToOneField(to='Note', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.note.title}的信息'


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
