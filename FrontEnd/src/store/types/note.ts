export interface NoteListItem {
    "noteListId": number,
    "title": string,
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
    "category": string,
}

export interface NoteContentItem {
    "noteListId": number,
    "title": string,
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
    "category": string,
    "markdownContent": string,
    "htmlContent": string,
    "imageUrls": string[],
    "renderedMarkdown": string,
    "tableOfContent": string
}
