from BackEnd import models
import random

IMAGE_URL = [
    r'https://images.unsplash.com/photo-1742268350465-35d7baae61fa?q=80&w=3174&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
    r'https://images.unsplash.com/photo-1742268350537-c5b0fb98f8c3?q=80&w=3174&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
    r'https://images.unsplash.com/photo-1741851374411-9528e6d2f33f?q=80&w=3270&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
    r'https://images.unsplash.com/photo-1741724821902-9251d2ba9252?q=80&w=3080&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
    r'https://images.unsplash.com/photo-1742654230443-7c19cb55cd46?q=80&w=3271&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
    r'https://images.unsplash.com/photo-1741603558151-e1f3822051bc?q=80&w=3270&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
    r'https://images.unsplash.com/photo-1742885203450-e2bdf135f0da?q=80&w=3266&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
    r'https://images.unsplash.com/photo-1742206506252-7f7504f5de9a?q=80&w=3270&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
    r'https://images.unsplash.com/photo-1710405152558-f13f4cecbf20?q=80&w=3270&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
    r'https://images.unsplash.com/photo-1742827871492-72428a28106b?q=80&w=3270&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
]


# 创建note
def create_note_with_extra(title, content, second_classification, tags):
    note_obj = models.Note.objects.create(
        title=title,
        markdown_content=content
    )

    note_list_obj = models.NoteList.objects.create(
        note=note_obj,
        second_classification=second_classification,
        cover_img=random.choice(IMAGE_URL),
        title=title,
        subtitle=note_obj.markdown_content[:15],
        brief=note_obj.markdown_content[:85]
    )
    note_list_obj.tags.set(tags)

    return note_obj
