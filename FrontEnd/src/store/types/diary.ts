export interface DiaryListItem {
    "diaryListId": string,
    "title": string,
    "brief": string,
    "coverImg": string,
    "isShow": boolean,
    "viewedCount": string,
    "createdTime": string,
    "modifiedTime": string,
    "timelinePointColor": string
}

export interface DiaryContentItem {
    "diaryListId": number,
    "title": string,
    "brief": string,
    "coverImg": string,
    "isShow": boolean,
    "viewedCount": number,
    "createdTime": string,
    "modifiedTime": string,
    "markdownContent": string,
    "htmlContent": string,
    "imageUrls": string[],
    "renderedMarkdown": string
}