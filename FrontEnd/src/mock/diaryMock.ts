import useDiaryStore from "@/store/diary.ts";

const diaryStore = useDiaryStore()

let testDiaryList = [
    {
        "diaryListId": 1,
        "title": '测试日记01',
        "brief": '诸葛亮字孔明，琅琊阳都人也。汉司隶校尉诸葛丰后也。',
        "coverImg": '',
        "isShow": true,
        "viewedCount": 10,
        "createdTime": '2022-9-18',
        "modifiedTime": '2022-9-18',
        "markdownContent": '”亮答曰：“自董卓已来，豪杰并起，跨州连郡者不可胜数。曹操比於袁绍，则名微而众寡，然操遂能克绍，以弱为强者，非惟天时，抑亦人谋也。今操已拥百万之众，挟天子而令诸侯，此诚不可与争锋。孙权据有江东，已历三世，国险而民附，贤能为之用，此可以为援而不可图也。荆州北据汉、沔，利尽南海，东连吴会，西通巴、蜀，此用武之国，而其主不能守，此殆天所以资将军，将军岂有意乎？益州险塞，沃野千里，天府之土，高祖因之以成帝业。刘璋闇弱，张鲁在北，民殷国富而不知存恤，智能之士思得明君。将军既帝室之胄，信义著於四海，总揽英雄，思贤如渴，若跨有荆、益，保其岩阻，西和诸戎，南抚夷越，外结好孙权，内脩政理；天下有变，则命一上将将荆州之军以向宛、洛，将军身率益州之众出於秦川，百姓孰敢不箪食壶浆以迎将军者乎？诚如是，则霸业可成，汉室可兴矣。”',
        "htmlContent": '',
        "imageUrls": [],
        "renderedMarkdown": '',
        timelinePointColor: diaryStore.timelinePointColor[Math.floor(Math.random() * diaryStore.timelinePointColor.length)]
    },
    {
        "diaryListId": 2,
        "title": '测试日记02',
        "brief": '诸葛亮字孔明，琅琊阳都人也。汉司隶校尉诸葛丰后也。',
        "coverImg": '',
        "isShow": true,
        "viewedCount": 10,
        "createdTime": '2022-9-20',
        "modifiedTime": '2022-9-20',
        "markdownContent": '”亮答曰：“自董卓已来，豪杰并起，跨州连郡者不可胜数。曹操比於袁绍，则名微而众寡，然操遂能克绍，以弱为强者，非惟天时，抑亦人谋也。今操已拥百万之众，挟天子而令诸侯，此诚不可与争锋。孙权据有江东，已历三世，国险而民附，贤能为之用，此可以为援而不可图也。荆州北据汉、沔，利尽南海，东连吴会，西通巴、蜀，此用武之国，而其主不能守，此殆天所以资将军，将军岂有意乎？益州险塞，沃野千里，天府之土，高祖因之以成帝业。刘璋闇弱，张鲁在北，民殷国富而不知存恤，智能之士思得明君。将军既帝室之胄，信义著於四海，总揽英雄，思贤如渴，若跨有荆、益，保其岩阻，西和诸戎，南抚夷越，外结好孙权，内脩政理；天下有变，则命一上将将荆州之军以向宛、洛，将军身率益州之众出於秦川，百姓孰敢不箪食壶浆以迎将军者乎？诚如是，则霸业可成，汉室可兴矣。”',
        "htmlContent": '',
        "imageUrls": [],
        "renderedMarkdown": '',
        timelinePointColor: diaryStore.timelinePointColor[Math.floor(Math.random() * diaryStore.timelinePointColor.length)]
    },
    {
        "diaryListId": 3,
        "title": '测试日记03',
        "brief": '诸葛亮字孔明，琅琊阳都人也。汉司隶校尉诸葛丰后也。',
        "coverImg": '',
        "isShow": true,
        "viewedCount": 10,
        "createdTime": '2022-9-30',
        "modifiedTime": '2022-9-30',
        "markdownContent": '”亮答曰：“自董卓已来，豪杰并起，跨州连郡者不可胜数。曹操比於袁绍，则名微而众寡，然操遂能克绍，以弱为强者，非惟天时，抑亦人谋也。今操已拥百万之众，挟天子而令诸侯，此诚不可与争锋。孙权据有江东，已历三世，国险而民附，贤能为之用，此可以为援而不可图也。荆州北据汉、沔，利尽南海，东连吴会，西通巴、蜀，此用武之国，而其主不能守，此殆天所以资将军，将军岂有意乎？益州险塞，沃野千里，天府之土，高祖因之以成帝业。刘璋闇弱，张鲁在北，民殷国富而不知存恤，智能之士思得明君。将军既帝室之胄，信义著於四海，总揽英雄，思贤如渴，若跨有荆、益，保其岩阻，西和诸戎，南抚夷越，外结好孙权，内脩政理；天下有变，则命一上将将荆州之军以向宛、洛，将军身率益州之众出於秦川，百姓孰敢不箪食壶浆以迎将军者乎？诚如是，则霸业可成，汉室可兴矣。”',
        "htmlContent": '',
        "imageUrls": [],
        "renderedMarkdown": '',
        timelinePointColor: diaryStore.timelinePointColor[Math.floor(Math.random() * diaryStore.timelinePointColor.length)]
    },
    {
        "diaryListId": 4,
        "title": '测试日记01',
        "brief": '诸葛亮字孔明，琅琊阳都人也。汉司隶校尉诸葛丰后也。',
        "coverImg": '',
        "isShow": true,
        "viewedCount": 10,
        "createdTime": '2022-10-7',
        "modifiedTime": '2022-10-8',
        "markdownContent": '”亮答曰：“自董卓已来，豪杰并起，跨州连郡者不可胜数。曹操比於袁绍，则名微而众寡，然操遂能克绍，以弱为强者，非惟天时，抑亦人谋也。今操已拥百万之众，挟天子而令诸侯，此诚不可与争锋。孙权据有江东，已历三世，国险而民附，贤能为之用，此可以为援而不可图也。荆州北据汉、沔，利尽南海，东连吴会，西通巴、蜀，此用武之国，而其主不能守，此殆天所以资将军，将军岂有意乎？益州险塞，沃野千里，天府之土，高祖因之以成帝业。刘璋闇弱，张鲁在北，民殷国富而不知存恤，智能之士思得明君。将军既帝室之胄，信义著於四海，总揽英雄，思贤如渴，若跨有荆、益，保其岩阻，西和诸戎，南抚夷越，外结好孙权，内脩政理；天下有变，则命一上将将荆州之军以向宛、洛，将军身率益州之众出於秦川，百姓孰敢不箪食壶浆以迎将军者乎？诚如是，则霸业可成，汉室可兴矣。”',
        "htmlContent": '',
        "imageUrls": [],
        "renderedMarkdown": '',
        timelinePointColor: diaryStore.timelinePointColor[Math.floor(Math.random() * diaryStore.timelinePointColor.length)]
    },
    {
        "diaryListId": 5,
        "title": '测试日记01',
        "brief": '诸葛亮字孔明，琅琊阳都人也。汉司隶校尉诸葛丰后也。',
        "coverImg": '',
        "isShow": true,
        "viewedCount": 10,
        "createdTime": '2022-10-10',
        "modifiedTime": '2022-10-11',
        "markdownContent": '”亮答曰：“自董卓已来，豪杰并起，跨州连郡者不可胜数。曹操比於袁绍，则名微而众寡，然操遂能克绍，以弱为强者，非惟天时，抑亦人谋也。今操已拥百万之众，挟天子而令诸侯，此诚不可与争锋。孙权据有江东，已历三世，国险而民附，贤能为之用，此可以为援而不可图也。荆州北据汉、沔，利尽南海，东连吴会，西通巴、蜀，此用武之国，而其主不能守，此殆天所以资将军，将军岂有意乎？益州险塞，沃野千里，天府之土，高祖因之以成帝业。刘璋闇弱，张鲁在北，民殷国富而不知存恤，智能之士思得明君。将军既帝室之胄，信义著於四海，总揽英雄，思贤如渴，若跨有荆、益，保其岩阻，西和诸戎，南抚夷越，外结好孙权，内脩政理；天下有变，则命一上将将荆州之军以向宛、洛，将军身率益州之众出於秦川，百姓孰敢不箪食壶浆以迎将军者乎？诚如是，则霸业可成，汉室可兴矣。”',
        "htmlContent": '',
        "imageUrls": [],
        "renderedMarkdown": '',
        timelinePointColor: diaryStore.timelinePointColor[Math.floor(Math.random() * diaryStore.timelinePointColor.length)]
    },
]

export default testDiaryList
