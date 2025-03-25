from BackEnd import models
import random

IMAGE_URL = [
    'https://live.staticflickr.com/65535/49322672587_77dd9b5a70.jpg',
    'https://live.staticflickr.com/65535/49963593921_c4a1849f7c.jpg',
    'https://channel-jk.com/wp-content/uploads/2023/05/shinei_is_god-1622374461134766081-20230206_081948-img1-320x320.jpg',
    'https://live.staticflickr.com/1913/43477078460_d823a3a238.jpg',
    'https://i.ebayimg.com/images/g/WokAAOSw9mpaQJWn/s-l400.jpg',
    'https://th.bing.com/th/id/R.37f4c96f4bb8dafd84c7fa4f471db919?rik=kvJTqKRmzw%2b%2b%2fA&riu=http%3a%2f%2fi0.sinaimg.cn%2fhs%2foverseas%2fjapan%2f2010-10-25%2fU3871P62T3D354849F72DT20101025171908.jpg&ehk=oTxffb3GuA2OWlaMygkB4HBTH%2fAH6MQT8fWenbhuENo%3d&risl=&pid=ImgRaw&r=0',
    'https://img95.699pic.com/photo/50224/5484.jpg_wh300.jpg!/fh/300/quality/90',
    'https://th.bing.com/th/id/R.c4f247ff426d939fc0cda4b4661cb5fc?rik=VNYYdKTsYYvp4A&riu=http%3a%2f%2fn.sinaimg.cn%2fsinakd2020613s%2f234%2fw620h414%2f20200613%2f9f82-iuzasxr9337710.jpg&ehk=Kz1WGMMY7FZVWIipCoz3T5Kz8hIjuXaiSLrzK0MnLsc%3d&risl=&pid=ImgRaw&r=0',
    'https://tse1-mm.cn.bing.net/th/id/OIP-C.cs5B_iRaEQKR9V1sGImjVAHaE7?rs=1&pid=ImgDetMain',
    'https://tse2-mm.cn.bing.net/th/id/OIP-C.uayzt42DRgUsuffASU8KJAHaFJ?rs=1&pid=ImgDetMain',
]


# 创建note
def create_note_with_extra(title, content, second_classification, tags):
    note_obj = models.Note.objects.create(
        title=title,
        content=content
    )

    note_list_obj = models.NoteList.objects.create(
        note=note_obj,
        second_classification=second_classification,
        cover_img=random.choice(IMAGE_URL),
        title=title,
        brief=note_obj.content[:64]
    )
    note_list_obj.tags.set(tags)

    models.NoteInfo.objects.create(
        note=note_obj
    )

    return note_obj
