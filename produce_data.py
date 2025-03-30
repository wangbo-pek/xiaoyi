from BackEnd import models


models.Tag.objects.create(
    name='django'
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
    name='开发技术'
)

fc_obj2 = models.FirstClassification.objects.create(
    name='产品管理'
)

fc_obj3 = models.FirstClassification.objects.create(
    name='文化素养'
)

models.SecondClassification.objects.create(
    name='Python',
    first_classification=fc_obj1
)

models.SecondClassification.objects.create(
    name='JavaScript',
    first_classification=fc_obj1
)

models.SecondClassification.objects.create(
    name='产品设计',
    first_classification=fc_obj2
)

models.SecondClassification.objects.create(
    name='产品思维',
    first_classification=fc_obj2
)

models.SecondClassification.objects.create(
    name='历史文化',
    first_classification=fc_obj3
)
