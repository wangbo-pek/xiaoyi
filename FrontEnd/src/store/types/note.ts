export default interface NoteListItem {
    "id": number,
    "title": string,
    "brief": string,
    "coverImg": string,
    "isShow": boolean,
    "createdTime": string,
    "modifiedTime": string,
    "tagsName": string[],
    "firstClassification": string,
    "secondClassification": string,
}
