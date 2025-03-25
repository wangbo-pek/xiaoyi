import {defineStore} from "pinia";
import type NoteListItem from "@/store/types/note.ts";

const useNoteStore = defineStore('note', {
    state: () => {
        return {
            noteList: [] as NoteListItem[]
        }
    }
})
export default useNoteStore

// title = models.CharField(verbose_name='标题', max_length=32)
// brief = models.CharField(verbose_name='摘要', max_length=64, blank=True, null=True)
// is_show = models.BooleanField(verbose_name='是否显示', default=True)
// created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
// modified_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)
// note = models.OneToOneField(to='Note', on_delete=models.CASCADE)
// second_classification = models.ForeignKey(to='SecondClassification', on_delete=models.CASCADE)
// tags = models.ManyToManyField(to='Tag')
// cover_img = models.ImageField(verbose_name='封面图', upload_to='note_covers/', blank=True, null=True, default='default_cover.jpg')