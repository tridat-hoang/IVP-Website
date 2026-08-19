import re

with open('c:/Users/Admin/Claude/Projects/IVP Website/news.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove the first button from newsList (data-news='0')
# and decrement all other data-news attributes by 1
pattern_list = re.compile(r'(<section class="news-grid anim-fade" id="newsList">)(.*?)(</section>)', re.DOTALL)
match = pattern_list.search(html)
if match:
    inner = match.group(2)
    # Remove the first button
    inner = re.sub(r'<button class="news-card" type="button" data-news="0">.*?</button>\s*', '', inner, count=1, flags=re.DOTALL)
    # Decrement data-news
    def dec_match(m):
        return f'data-news="{int(m.group(1)) - 1}"'
    inner = re.sub(r'data-news="(\d+)"', dec_match, inner)
    html = html.replace(match.group(0), match.group(1) + inner + match.group(3))

# 2. Remove the first item from newsData array
pattern_data = re.compile(r'(const newsData = \[\s*\{\s*title: \'TRUNG TÂM NUÔI CÂY MÔ IVP.*?pdfUrl: \'assets/docs/dua-kim-cuong.pdf\'\s*\},)', re.DOTALL)
html = pattern_data.sub('const newsData = [', html)

with open('c:/Users/Admin/Claude/Projects/IVP Website/news.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Reverted news.html successfully!')
