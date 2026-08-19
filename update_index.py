import re

with open('c:/Users/Admin/Claude/Projects/IVP Website/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_section = '''
  <section class="section home-section anim-fade">
    <article>
      <h2 data-lang-vi="TRUNG TÂM NUÔI CÂY MÔ IVP – DẤU ẤN MỚI VỚI GIỐNG DỨA KIM CƯƠNG ĐƯỢC CÔNG BỐ LƯU HÀNH" data-lang-en="IVP TISSUE CULTURE CENTER – NEW MILESTONE WITH THE CIRCULATION ANNOUNCEMENT OF KIM CUONG PINEAPPLE">TRUNG TÂM NUÔI CÂY MÔ IVP – DẤU ẤN MỚI VỚI GIỐNG DỨA KIM CƯƠNG ĐƯỢC CÔNG BỐ LƯU HÀNH</h2>
      <p data-lang-vi-html="Ngày 19/05/2026 đánh dấu một cột mốc đáng chú ý trong quá trình nghiên cứu và phát triển giống cây trồng của Công ty Cổ phần Giống cây trồng và Dược liệu IVP. Giống dứa Kim Cương do IVP thực hiện chọn lọc và nhân giống bằng phương pháp nuôi cấy mô thực vật đã được ghi nhận trên Hệ thống thông tin giải quyết thủ tục hành chính của <a href='https://motcua.mae.gov.vn/Pages/TuCongBo.aspx' target='_blank' rel='noopener noreferrer' style='color:var(--primary); font-weight:bold; text-decoration:underline;'>Bộ Nông nghiệp và Môi trường với hình thức tự công bố lưu hành giống cây trồng</a>." data-lang-en-html="May 19, 2026 marks a notable milestone in the research and development of plant varieties by IVP Seedlings and Medicinal Plants JSC. The Kim Cuong pineapple variety, selected and propagated by IVP using plant tissue culture methods, has been recorded on the administrative procedure information system of the <a href='https://motcua.mae.gov.vn/Pages/TuCongBo.aspx' target='_blank' rel='noopener noreferrer' style='color:var(--primary); font-weight:bold; text-decoration:underline;'>Ministry of Agriculture and Environment under the form of self-declaration for circulation of plant varieties</a>.">Ngày 19/05/2026 đánh dấu một cột mốc đáng chú ý trong quá trình nghiên cứu và phát triển giống cây trồng của Công ty Cổ phần Giống cây trồng và Dược liệu IVP. Giống dứa Kim Cương do IVP thực hiện chọn lọc và nhân giống bằng phương pháp nuôi cấy mô thực vật đã được ghi nhận trên Hệ thống thông tin giải quyết thủ tục hành chính của <a href="https://motcua.mae.gov.vn/Pages/TuCongBo.aspx" target="_blank" rel="noopener noreferrer" style="color:var(--primary); font-weight:bold; text-decoration:underline;">Bộ Nông nghiệp và Môi trường với hình thức tự công bố lưu hành giống cây trồng</a>.</p>
      
      <p data-lang-vi="🍍 Dứa Kim Cương - Mắt nông, ruột vàng, thơm ngon, mềm mịn, không xơ" data-lang-en="🍍 Kim Cuong Pineapple - Shallow eyes, golden flesh, delicious, smooth, fiberless">🍍 Dứa Kim Cương - Mắt nông, ruột vàng, thơm ngon, mềm mịn, không xơ</p>
      
      <p data-lang-vi="👉 Xem chi tiết Bản tự công bố lưu hành giống trong tài liệu đính kèm bên dưới:" data-lang-en="👉 See details of the self-declaration for circulation of plant varieties in the attached document below:">👉 Xem chi tiết Bản tự công bố lưu hành giống trong tài liệu đính kèm bên dưới:</p>
      
      <div style="margin-top:20px; text-align:left;">
          <a href="assets/docs/cong-bo-dua-kim-cuong.pdf" target="_blank" rel="noopener noreferrer" style="display:inline-flex; align-items:center; gap:8px; text-decoration:none; color:#ff6600; font-size:1.1rem; transition: opacity 0.2s;" onmouseover="this.style.opacity='0.8';" onmouseout="this.style.opacity='1';">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M19 3H5C3.89 3 3 3.89 3 5V19C3 20.1 3.89 21 5 21H19C20.1 21 21 20.1 21 19V5C21 3.89 20.1 3 19 3Z" fill="#E5252A"/>
              <path d="M11.5 9.5H10V14.5H11V12.5H11.5C12.33 12.5 13 11.83 13 11V11C13 10.17 12.33 9.5 11.5 9.5ZM11.5 11.5H11V10.5H11.5V11.5Z" fill="white"/>
              <path d="M8.5 9.5H6.5V14.5H7.5V12.5H8.5C9.33 12.5 10 11.83 10 11V11C10 10.17 9.33 9.5 8.5 9.5ZM8.5 11.5H7.5V10.5H8.5V11.5Z" fill="white"/>
              <path d="M16.5 9.5H14V14.5H15V12.5H16V11.5H15V10.5H16.5V9.5Z" fill="white"/>
            </svg>
            <span>Công bố lưu hành dứa Kim Cương.pdf</span>
          </a>
      </div>
    </article>
    <figure>
       <img loading="lazy" class="photo" data-previewable="true" src="assets/images/kim-cuong-1.png" alt="Dứa Kim Cương">
       <img loading="lazy" class="photo" data-previewable="true" src="assets/images/kim-cuong-2.jpg" alt="Vườn dứa Kim Cương" style="margin-top:20px;">
    </figure>
  </section>
'''

target_string = "  </section>\n\n  <section class=\"section home-section nursery-section anim-fade\">"
if target_string in html:
    new_html = html.replace(target_string, f"  </section>\n{new_section}\n  <section class=\"section home-section nursery-section anim-fade\">")
    with open('c:/Users/Admin/Claude/Projects/IVP Website/index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Updated index.html successfully")
else:
    print("Target string not found!")
