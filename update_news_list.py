import re

with open('c:/Users/Admin/Claude/Projects/IVP Website/news.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find the newsList section
pattern = re.compile(r'(<section class="news-grid anim-fade" id="newsList">)(.*?)(</section>)', re.DOTALL)
match = pattern.search(html)

if match:
    inner = match.group(2)
    # Increment all existing data-news="x" by 1
    def inc_match(m):
        return f'data-news="{int(m.group(1)) + 1}"'
    new_inner = re.sub(r'data-news="(\d+)"', inc_match, inner)
    
    new_button = '''
    <button class="news-card" type="button" data-news="0">
      <span class="news-card-body">
        <span class="news-card-title" data-lang-vi="TRUNG TÂM NUÔI CÂY MÔ IVP – DẤU ẤN MỚI VỚI GIỐNG DỨA KIM CƯƠNG ĐƯỢC CÔNG BỐ LƯU HÀNH" data-lang-en="IVP TISSUE CULTURE CENTER – NEW MILESTONE WITH THE CIRCULATION ANNOUNCEMENT OF KIM CUONG PINEAPPLE">TRUNG TÂM NUÔI CÂY MÔ IVP – DẤU ẤN MỚI VỚI GIỐNG DỨA KIM CƯƠNG ĐƯỢC CÔNG BỐ LƯU HÀNH</span>
        <span class="news-card-date">19/05/2026</span>
        <span class="news-card-foot">
          <span class="news-readmore" data-lang-vi="Đọc tiếp →" data-lang-en="Read more →">Đọc tiếp →</span>
          <span class="news-vtag" style="background: #d32f2f; color: white;">📄 PDF</span>
        </span>
      </span>
    </button>
'''
    new_html = html.replace(match.group(0), match.group(1) + new_button + new_inner + match.group(3))
    
    with open('c:/Users/Admin/Claude/Projects/IVP Website/news.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print('Updated successfully!')
else:
    print('Pattern not found')
