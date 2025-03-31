export interface DiaryListItem {
    "diaryListId":string,
    "title":string,
    "brief":string,
    "coverImg":string,
    "isShow":boolean,
    "viewedCount": string,
    "createdTime": string,
    "modifiedTime": string,
}

export interface DiaryContentItem {
    "diaryListId":string,
    "title":string,
    "brief":string,
    "coverImg":string,
    "isShow":boolean,
    "viewedCount": string,
    "createdTime": string,
    "modifiedTime": string,
    "markdownContent": string,
    "htmlContent": string,
    "imageUrls": string[],
    "renderedMarkdown": string
}