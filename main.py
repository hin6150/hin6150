import feedparser, time, pathlib

URL = "https://hin6150.tistory.com/rss"
FEED = feedparser.parse(URL)

MAX_RETRO, MAX_DEV = 1, 2
retro_posts, dev_posts = [], []

for e in FEED.entries:
    # 1) Tistory RSS는 tags 리스트 안의 term 필드에 카테고리/태그가 들어있음
    tags = [t.term for t in getattr(e, "tags", [])]
    # published = time.strftime("%Y/%m/%d", e.published_parsed)
    # line = f"[{published} - {e.title}]({e.link}) <br/>\n"
    line = f"[{e.title}]({e.link}) <br/>\n"
    
    if "회고록" in tags and len(retro_posts) < MAX_RETRO:
        retro_posts.append(line)
    elif "개발" in tags and len(dev_posts) < MAX_DEV:
        dev_posts.append(line)

    if len(retro_posts) == MAX_RETRO and len(dev_posts) == MAX_DEV:
        break

markdown = f"""
## 👨‍💻 소개
- 🌱 현재 **React, React Native**, 그리고 **Next.js** 중심으로 프론트엔드 개발을 공부하고 있어요.
- 🤝 **소통과 협업**을 중시하며, 팀과 함께 성장하는 과정을 즐깁니다.
- 🎯 제가 만든 서비스가 **실제 사용자에게 닿는 경험**을 만드는 것이 목표예요.

[좀 더 자세히 보기](https://hin6150.notion.site)

## 📊 GitHub 활동
<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=hin6150&show_icons=true" />
  <img src="https://github-readme-streak-stats.herokuapp.com?user=hin6150" />
</p>


## ✍🏻 최근 블로그 글

### 📘 회고록
{''.join(retro_posts) if retro_posts else '업데이트된 회고 글이 없습니다.'}

### 💻 개발
{''.join(dev_posts) if dev_posts else '업데이트된 개발 글이 없습니다.'}
"""

pathlib.Path("README.md").write_text(markdown, encoding="utf-8")
