import re

with open('c:/Users/Admin/Claude/Projects/IVP Website/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# I will replace the previously inserted section
# The old section started with '<section class="section home-section anim-fade">' and contained 'TRUNG TÂM NUÔI CÂY MÔ IVP – DẤU ẤN MỚI'
# It ended right before '<section class="section home-section nursery-section anim-fade">'

pattern = re.compile(r'<section class=\"section home-section anim-fade\">\s*<article>\s*<h2 data-lang-vi=\"TRUNG TÂM NUÔI CÂY MÔ IVP – DẤU ẤN MỚI.*?</section>', re.DOTALL)

new_section = '''<section class="section home-section anim-fade">
    <article>
      <h2 data-lang-vi="TRUNG TÂM NUÔI CÂY MÔ IVP – DẤU ẤN MỚI VỚI GIỐNG DỨA KIM CƯƠNG ĐƯỢC CÔNG BỐ LƯU HÀNH" data-lang-en="IVP TISSUE CULTURE CENTER – NEW MILESTONE WITH THE CIRCULATION ANNOUNCEMENT OF KIM CUONG PINEAPPLE">TRUNG TÂM NUÔI CÂY MÔ IVP – DẤU ẤN MỚI VỚI GIỐNG DỨA KIM CƯƠNG ĐƯỢC CÔNG BỐ LƯU HÀNH</h2>
      
      <p data-lang-vi-html="Ngày 19/05/2026 đánh dấu một cột mốc đáng chú ý trong quá trình nghiên cứu và phát triển giống cây trồng của Công ty Cổ phần Giống cây trồng và Dược liệu IVP. Giống dứa Kim Cương do IVP thực hiện chọn dòng và nhân giống bằng phương pháp nuôi cấy mô thực vật đã được ghi nhận trên Hệ thống thông tin giải quyết thủ tục hành chính của <a href='https://motcua.mae.gov.vn/Pages/TuCongBo.aspx' target='_blank' rel='noopener noreferrer' style='color:var(--primary); font-weight:bold; text-decoration:underline;'>Bộ Nông nghiệp và Môi trường với hình thức tự công bố lưu hành giống cây trồng</a>." data-lang-en-html="May 19, 2026 marks a notable milestone in the research and development of plant varieties by IVP Seedlings and Medicinal Plants JSC. The Kim Cuong pineapple variety, selected and propagated by IVP using plant tissue culture methods, has been recorded on the administrative procedure information system of the <a href='https://motcua.mae.gov.vn/Pages/TuCongBo.aspx' target='_blank' rel='noopener noreferrer' style='color:var(--primary); font-weight:bold; text-decoration:underline;'>Ministry of Agriculture and Environment under the form of self-declaration for circulation of plant varieties</a>.">Ngày 19/05/2026 đánh dấu một cột mốc đáng chú ý trong quá trình nghiên cứu và phát triển giống cây trồng của Công ty Cổ phần Giống cây trồng và Dược liệu IVP. Giống dứa Kim Cương do IVP thực hiện chọn dòng và nhân giống bằng phương pháp nuôi cấy mô thực vật đã được ghi nhận trên Hệ thống thông tin giải quyết thủ tục hành chính của <a href="https://motcua.mae.gov.vn/Pages/TuCongBo.aspx" target="_blank" rel="noopener noreferrer" style="color:var(--primary); font-weight:bold; text-decoration:underline;">Bộ Nông nghiệp và Môi trường với hình thức tự công bố lưu hành giống cây trồng</a>.</p>
      
      <h3 data-lang-vi="Dứa Kim Cương – Mắt nông, ruột vàng, thơm ngon, mềm mịn, không xơ" data-lang-en="Kim Cuong Pineapple – Shallow eyes, golden flesh, delicious, smooth, fiberless" style="font-size:1.15rem; font-weight:bold; margin-top:20px; color:#1a1a2e;">Dứa Kim Cương – Mắt nông, ruột vàng, thơm ngon, mềm mịn, không xơ</h3>
      
      <p data-lang-vi="Dứa Kim Cương là giống dứa có nguồn gốc từ Đài Loan, được IVP nghiên cứu và nhân giống thành công bằng phương pháp nuôi cấy mô thực vật. Công nghệ này giúp nhân nhanh giống mới trong thời gian ngắn để đưa vào sản xuất. IVP nỗ lực nghiên cứu quy trình kỹ thuật canh tác giống Dứa Kim Cương phù hợp với điều kiện khí hậu, thổ nhưỡng địa phương." data-lang-en="The Kim Cuong pineapple originated from Taiwan, successfully researched and propagated by IVP using plant tissue culture methods. This technology helps multiply new varieties rapidly for production. IVP strives to research cultivation techniques for Kim Cuong Pineapple suitable for local climate and soil conditions.">Dứa Kim Cương là giống dứa có nguồn gốc từ Đài Loan, được IVP nghiên cứu và nhân giống thành công bằng phương pháp nuôi cấy mô thực vật. Công nghệ này giúp nhân nhanh giống mới trong thời gian ngắn để đưa vào sản xuất. IVP nỗ lực nghiên cứu quy trình kỹ thuật canh tác giống Dứa Kim Cương phù hợp với điều kiện khí hậu, thổ nhưỡng địa phương.</p>
      
      <p data-lang-vi="Một số thông tin của giống Dứa Kim Cương" data-lang-en="Some information about the Kim Cuong Pineapple variety" style="font-weight:bold; margin-top:15px; color:#1a1a2e;">Một số thông tin của giống Dứa Kim Cương</p>
      
      <ul style="list-style:none; padding-left:0; margin-top:10px;">
        <li style="margin-bottom:10px;"><span data-lang-vi-html="👉 <strong>Sinh trưởng:</strong> Sinh trưởng khoẻ, mép lá không gai, có màu xanh lục vàng, trong điều kiện thời tiết cực đoan trên mặt lá có màu đỏ hồng. Chiều dài lá 90-100 cm." data-lang-en-html="👉 <strong>Growth:</strong> Vigorous growth, spineless leaf margins, yellow-green color, turning pink-red under extreme weather. Leaf length 90-100 cm.">👉 <strong>Sinh trưởng:</strong> Sinh trưởng khoẻ, mép lá không gai, có màu xanh lục vàng, trong điều kiện thời tiết cực đoan trên mặt lá có màu đỏ hồng. Chiều dài lá 90-100 cm.</span></li>
        <li style="margin-bottom:10px;"><span data-lang-vi-html="👉 <strong>Thời gian sinh trưởng:</strong> Thời gian từ trồng đến kết thúc thu hoạch 17 tháng." data-lang-en-html="👉 <strong>Growth period:</strong> 17 months from planting to harvest completion.">👉 <strong>Thời gian sinh trưởng:</strong> Thời gian từ trồng đến kết thúc thu hoạch 17 tháng.</span></li>
        <li style="margin-bottom:10px;"><span data-lang-vi-html="👉 <strong>Năng suất:</strong> Giống dứa Kim Cương có tiềm năng năng suất cao, có thể đạt 74 tấn/ha trong điều kiện canh tác phù hợp." data-lang-en-html="👉 <strong>Yield:</strong> High yield potential, up to 74 tons/ha under suitable farming conditions.">👉 <strong>Năng suất:</strong> Giống dứa Kim Cương có tiềm năng năng suất cao, có thể đạt 74 tấn/ha trong điều kiện canh tác phù hợp.</span></li>
        <li style="margin-bottom:10px;"><span data-lang-vi-html="👉 <strong>Quả dứa và chất lượng quả:</strong> Quả có hình nón thuôn dài hoặc hình bầu dục, vỏ cứng, mắt nông, có mùi thơm đặc trưng. Vỏ chuyển từ màu xanh lá sang màu vàng kim, cam và nâu khi chín. Thịt quả có màu vàng sẫm hoặc vàng kim, mềm mịn, không xơ. Trọng lượng quả đạt trung bình 1,4 kg/quả. Độ brix đạt 16,3%, độ chua thấp." data-lang-en-html="👉 <strong>Fruit quality:</strong> Elongated conical or oval shape, hard shell, shallow eyes, distinct aroma. Shell turns from green to golden, orange and brown when ripe. Flesh is deep yellow or golden, smooth, fiberless. Average weight 1.4 kg/fruit. Brix level 16.3%, low acidity.">👉 <strong>Quả dứa và chất lượng quả:</strong> Quả có hình nón thuôn dài hoặc hình bầu dục, vỏ cứng, mắt nông, có mùi thơm đặc trưng. Vỏ chuyển từ màu xanh lá sang màu vàng kim, cam và nâu khi chín. Thịt quả có màu vàng sẫm hoặc vàng kim, mềm mịn, không xơ. Trọng lượng quả đạt trung bình 1,4 kg/quả. Độ brix đạt 16,3%, độ chua thấp.</span></li>
      </ul>
      
      <h3 data-lang-vi="Mang sản phẩm dứa chất lượng cao đến người tiêu dùng Việt Nam" data-lang-en="Bringing high-quality pineapple products to Vietnamese consumers" style="font-size:1.15rem; font-weight:bold; margin-top:20px; color:#1a1a2e;">Mang sản phẩm dứa chất lượng cao đến người tiêu dùng Việt Nam</h3>
      
      <p data-lang-vi="Việc giống dứa Kim Cương được công bố lưu hành là một dấu mốc quan trọng, thể hiện định hướng của IVP trong việc nghiên cứu, chọn tạo, nhân giống và đưa các giống cây trồng có giá trị cao vào sản xuất." data-lang-en="The circulation announcement of Kim Cuong pineapple is a crucial milestone, showing IVP's direction in researching, selecting, breeding and putting high-value crops into production.">Việc giống dứa Kim Cương được công bố lưu hành là một dấu mốc quan trọng, thể hiện định hướng của IVP trong việc nghiên cứu, chọn tạo, nhân giống và đưa các giống cây trồng có giá trị cao vào sản xuất.</p>
      
      <p data-lang-vi="Với định hướng từ Nghiên cứu – Nhân giống – Trồng – Phát triển sản phẩm, IVP không chỉ tập trung vào việc tạo ra nguồn cây giống mà còn hướng tới việc đưa giống Dứa Kim Cương vào các dự án sản xuất dứa thương phẩm của công ty. Mục tiêu là phát triển sản phẩm dứa tươi chất lượng cao với giá trị tốt nhất cho người tiêu dùng trong nước. IVP mong muốn mọi người dân dễ dàng thưởng thức loại trái cây thơm ngon này." data-lang-en="With the direction from Research - Propagation - Planting - Product Development, IVP focuses not only on seedlings but also on commercial pineapple production projects. The goal is to develop high-quality fresh pineapple products with the best value for domestic consumers. IVP wants everyone to easily enjoy this delicious fruit.">Với định hướng từ Nghiên cứu – Nhân giống – Trồng – Phát triển sản phẩm, IVP không chỉ tập trung vào việc tạo ra nguồn cây giống mà còn hướng tới việc đưa giống Dứa Kim Cương vào các dự án sản xuất dứa thương phẩm của công ty. Mục tiêu là phát triển sản phẩm dứa tươi chất lượng cao với giá trị tốt nhất cho người tiêu dùng trong nước. IVP mong muốn mọi người dân dễ dàng thưởng thức loại trái cây thơm ngon này.</p>
      
      <p data-lang-vi="Đây cũng là định hướng thể hiện cam kết của IVP trong việc gắn kết Nghiên cứu với Sản xuất thực tế, đưa thành quả của công nghệ nuôi cấy mô từ phòng thí nghiệm đến vùng sản xuất và cuối cùng là đến người tiêu dùng." data-lang-en="This also reflects IVP's commitment to linking Research with practical Production, bringing tissue culture technology from the lab to production zones and ultimately to consumers.">Đây cũng là định hướng thể hiện cam kết của IVP trong việc gắn kết Nghiên cứu với Sản xuất thực tế, đưa thành quả của công nghệ nuôi cấy mô từ phòng thí nghiệm đến vùng sản xuất và cuối cùng là đến người tiêu dùng.</p>
      
      <p data-lang-vi="Xem chi tiết Bản tự công bố lưu hành giống trong tài liệu đính kèm bên dưới:" data-lang-en="See details of the self-declaration for circulation of plant varieties in the attached document below:" style="margin-top:15px; font-weight: 500;">Xem chi tiết Bản tự công bố lưu hành giống trong tài liệu đính kèm bên dưới:</p>
      
      <div style="margin-top:15px; margin-bottom: 20px; text-align:left;">
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
    <figure style="display:flex; flex-direction:column; gap:15px; align-items:center; justify-content:center; align-self:start;">
       <img loading="lazy" class="photo" data-previewable="true" src="assets/images/kim-cuong-1.png" alt="Dứa Kim Cương" style="max-height: 450px; width: auto; object-fit: contain; border-radius: 8px;">
       <img loading="lazy" class="photo" data-previewable="true" src="assets/images/kim-cuong-2.jpg" alt="Vườn dứa Kim Cương" style="width: 100%; max-height: 350px; object-fit: cover; border-radius: 8px;">
    </figure>
  </section>'''

if pattern.search(html):
    new_html = pattern.sub(new_section, html)
    with open('c:/Users/Admin/Claude/Projects/IVP Website/index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Replaced section successfully")
else:
    print("Pattern not found!")
