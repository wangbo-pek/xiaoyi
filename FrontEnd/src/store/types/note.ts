export interface NoteListItem {
    "noteListId": number,
    "title": string,
    "subtitle": string,
    "brief": string,
    "coverImg": string,
    "isShow": boolean,
    "isPinned": boolean,
    "isRecommended": boolean,
    "viewedCount": string,
    "likedCount": string,
    "disgustedCount": string,
    "encouragedCount": string,
    "createdTime": string,
    "modifiedTime": string,
    "tagsName": string[],
    "firstClassification": string,
    "secondClassification": string,
}

export interface NoteContentItem {
    "noteListId": number,
    "title": string,
    "subtitle": string,
    "brief": string,
    "coverImg": string,
    "isShow": boolean,
    "isPinned": boolean,
    "isRecommended": boolean,
    "viewedCount": number,
    "likedCount": number,
    "disgustedCount": number,
    "encouragedCount": number,
    "createdTime": string,
    "modifiedTime": string,
    "tagsName": string[],
    "firstClassification": string,
    "secondClassification": string,
    "markdownContent": string,
    "htmlContent": string,
    "imageUrls": string[],
    "renderedMarkdown": string,
    "tableOfContent": string
}
