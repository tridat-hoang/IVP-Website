/* ==========================================================================
   IVP Website — viewer.js
   Global image lightbox viewer (shared across all pages)
   ========================================================================== */
(function(){
  var viewer = document.getElementById('globalImageViewer');
  var viewerImg = document.getElementById('globalViewerImage');
  if (!viewer || !viewerImg) return;
  var closeBtn = viewer.querySelector('.viewer-close');
  var skipSelector = '.cover-banner, .topbar, .logo-wrap, .flags, .floating, .global-image-viewer, .sticky-nav';
  document.querySelectorAll('img').forEach(function(img){
    if (img.closest(skipSelector)) return;
    img.dataset.previewable = 'true';
    img.addEventListener('click', function(e){
      e.preventDefault();
      e.stopPropagation();
      viewerImg.src = img.currentSrc || img.src;
      viewerImg.alt = img.alt || 'Xem ảnh lớn';
      viewer.classList.add('show');
      viewer.setAttribute('aria-hidden','false');
      document.body.classList.add('no-scroll');
    }, true);
  });
  function closeViewer(){
    viewer.classList.remove('show');
    viewer.setAttribute('aria-hidden','true');
    viewerImg.src = '';
    document.body.classList.remove('no-scroll');
  }
  closeBtn.addEventListener('click', closeViewer);
  viewer.addEventListener('click', function(e){ if (e.target === viewer) closeViewer(); });
  document.addEventListener('keydown', function(e){ if(e.key === 'Escape' && viewer.classList.contains('show')) closeViewer(); });
})();
