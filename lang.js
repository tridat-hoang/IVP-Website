/**
 * IVP Language Switcher (lang.js)
 * ================================
 * Script dùng chung cho TẤT CẢ các trang của website IVP.
 *
 * HƯỚNG DẪN SỬ DỤNG:
 * -------------------
 * 1) Nội dung thuần văn bản → dùng data-lang-vi + data-lang-en
 *    (script sẽ đổi textContent)
 *    Ví dụ:  <h2 data-lang-vi="Sản phẩm" data-lang-en="Products">Sản phẩm</h2>
 *
 * 2) Nội dung có chứa HTML bên trong (br, strong, em…)
 *    → dùng data-lang-vi-html + data-lang-en-html (script sẽ đổi innerHTML)
 *    Lưu ý:  Trong giá trị attribute, viết &lt;br&gt; thay cho <br>
 *    Ví dụ:  <p data-lang-vi-html="Dòng 1&lt;br&gt;Dòng 2"
 *               data-lang-en-html="Line 1&lt;br&gt;Line 2">Dòng 1<br>Dòng 2</p>
 *
 * 3) Thêm <script src="lang.js"></script> trước thẻ </body> ở mỗi trang.
 *
 * Lưu ý quan trọng:
 * - Ngôn ngữ mặc định: 'vi' (Tiếng Việt).
 * - Lựa chọn được lưu vào localStorage (key: 'ivp-lang').
 * - Khi chuyển trang (vd: index.html → products.html), ngôn ngữ giữ nguyên.
 * - Script nhận diện nút cờ qua thuộc tính aria-label="Tiếng Việt" / "English".
 */
(function () {
  var STORAGE_KEY = 'ivp-lang';
  var DEFAULT_LANG = 'vi';

  /* ---------- Đọc ngôn ngữ đã lưu ---------- */
  function getCurrentLang() {
    return localStorage.getItem(STORAGE_KEY) || DEFAULT_LANG;
  }

  /* ---------- Áp dụng ngôn ngữ lên toàn bộ phần tử ---------- */
  function applyLang(lang) {

    /* Bước 1 – Đổi textContent cho các phần tử có data-lang-vi & data-lang-en */
    document.querySelectorAll('[data-lang-vi][data-lang-en]').forEach(function (el) {
      var val = el.getAttribute('data-lang-' + lang);
      if (val !== null) el.textContent = val;
    });

    /* Bước 2 – Đổi innerHTML cho các phần tử có data-lang-vi-html & data-lang-en-html */
    document.querySelectorAll('[data-lang-vi-html][data-lang-en-html]').forEach(function (el) {
      var html = el.getAttribute('data-lang-' + lang + '-html');
      if (html !== null) el.innerHTML = html;
    });

    /* Bước 3 – Cập nhật thuộc tính lang trên thẻ <html> */
    document.documentElement.lang = lang;

    /* Bước 4 – Highlight nút cờ đang được chọn */
    document.querySelectorAll('.flag-btn').forEach(function (btn) {
      var label = btn.getAttribute('aria-label');
      var isActive = (lang === 'vi' && label === 'Tiếng Việt') ||
                     (lang === 'en' && label === 'English');
      btn.classList.toggle('flag-active', isActive);
    });
  }

  /* ---------- Lưu + áp dụng ngôn ngữ ---------- */
  function setLang(lang) {
    localStorage.setItem(STORAGE_KEY, lang);
    applyLang(lang);
    /* Phát sự kiện để các script khác trên trang cập nhật nội dung động */
    document.dispatchEvent(new CustomEvent('ivp-lang-change', { detail: { lang: lang } }));
  }

  /* ---------- Gắn sự kiện click cho các nút cờ ---------- */
  document.querySelectorAll('.flag-btn').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var label = btn.getAttribute('aria-label');
      setLang(label === 'English' ? 'en' : 'vi');
    });
  });

  /* ---------- Áp dụng ngôn ngữ ngay khi tải trang ---------- */
  applyLang(getCurrentLang());

  /* Expose để các script khác re-apply ngôn ngữ sau khi thêm nội dung động */
  window.ivpApplyLang = function() { applyLang(getCurrentLang()); };

})();
