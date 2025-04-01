from BackEnd import models


models.Tag.objects.create(
    name='英语'
)

models.Tag.objects.create(
    name='vue'
)

models.Tag.objects.create(
    name='工具心得'
)

models.Tag.objects.create(
    name='产品经理'
)

models.Tag.objects.create(
    name='随笔'
)

fc_obj1 = models.FirstClassification.objects.create(
    name='英语学习'
)

models.SecondClassification.objects.create(
    name='学习方法',
    first_classification=fc_obj1
)
