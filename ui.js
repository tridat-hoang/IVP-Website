/* ==========================================================================
   IVP Website — ui.js
   Sticky nav, hamburger menu, back-to-top, scroll animations, touch dropdown
   ========================================================================== */
(function(){
  // === Generate Sticky Nav from Hero Nav (no duplicate HTML needed) ===
  var hero = document.querySelector('.hero');
  var heroNav = document.querySelector('.hero .nav');
  var stickyNav = null;

  if(hero && heroNav){
    // Create sticky nav element dynamically
    stickyNav = document.createElement('div');
    stickyNav.id = 'stickyNav';
    stickyNav.className = 'sticky-nav';
    stickyNav.setAttribute('aria-hidden', 'true');

    // Logo
    var logoDiv = document.createElement('div');
    logoDiv.className = 'nav-logo';
    logoDiv.innerHTML = '<img src="assets/images/logo.jpg" alt="IVP">';
    stickyNav.appendChild(logoDiv);

    // Hamburger
    var hamburger = document.createElement('button');
    hamburger.className = 'hamburger';
    hamburger.type = 'button';
    hamburger.setAttribute('aria-label', 'Menu');
    hamburger.innerHTML = '<span></span><span></span><span></span>';
    stickyNav.appendChild(hamburger);

    // Clone nav items
    var navItems = document.createElement('nav');
    navItems.className = 'nav-items';
    navItems.innerHTML = heroNav.innerHTML;
    stickyNav.appendChild(navItems);

    // Insert at start of body
    document.body.insertBefore(stickyNav, document.body.firstChild);

    // Scroll handler
    window.addEventListener('scroll', function(){
      var scrollY = window.pageYOffset || document.documentElement.scrollTop;
      var heroBottom = hero.offsetTop + hero.offsetHeight;
      if(scrollY > heroBottom - 50){
        stickyNav.classList.add('show');
        stickyNav.setAttribute('aria-hidden', 'false');
      } else {
        stickyNav.classList.remove('show');
        stickyNav.setAttribute('aria-hidden', 'true');
      }
    }, {passive:true});
  }

  // === Hamburger Menu ===
  function setupHamburgers(){
    document.querySelectorAll('.hamburger').forEach(function(btn){
      if(btn._ivpBound) return;
      btn._ivpBound = true;
      btn.addEventListener('click', function(e){
        e.stopPropagation();
        btn.classList.toggle('open');
        var container = btn.closest('.hero-inner, .sticky-nav');
        if(container){
          var navMenu = container.querySelector('.nav, .nav-items');
          if(navMenu) navMenu.classList.toggle('nav-open');
        }
      });
    });
  }
  setupHamburgers();

  // === Touch-friendly Dropdown ===
  function setupDropdowns(){
    document.querySelectorAll('.nav-dropdown').forEach(function(dd){
      var toggle = dd.querySelector('.nav-toggle');
      if(!toggle || toggle._ivpBound) return;
      toggle._ivpBound = true;
      toggle.addEventListener('click', function(e){
        e.preventDefault();
        e.stopPropagation();
        document.querySelectorAll('.nav-dropdown.open').forEach(function(other){
          if(other !== dd) other.classList.remove('open');
        });
        dd.classList.toggle('open');
      });
    });
  }
  setupDropdowns();

  // Close dropdown when clicking outside
  document.addEventListener('click', function(){
    document.querySelectorAll('.nav-dropdown.open').forEach(function(dd){
      dd.classList.remove('open');
    });
  });

  // === Back to Top ===
  var backBtn = document.getElementById('backToTop');
  if(backBtn){
    window.addEventListener('scroll', function(){
      var scrollY = window.pageYOffset || document.documentElement.scrollTop;
      if(scrollY > 400){
        backBtn.classList.add('show');
      } else {
        backBtn.classList.remove('show');
      }
    }, {passive:true});
    backBtn.addEventListener('click', function(){
      window.scrollTo({top:0, behavior:'smooth'});
    });
  }

  // === Scroll Animations (IntersectionObserver) ===
  var animElements = document.querySelectorAll('.anim-fade');
  if(animElements.length > 0 && 'IntersectionObserver' in window){
    var observer = new IntersectionObserver(function(entries){
      entries.forEach(function(entry){
        if(entry.isIntersecting){
          entry.target.classList.add('anim-visible');
          observer.unobserve(entry.target);
        }
      });
    }, {threshold:0.1, rootMargin:'0px 0px -40px 0px'});
    animElements.forEach(function(el){ observer.observe(el); });
  } else {
    animElements.forEach(function(el){ el.classList.add('anim-visible'); });
  }

  // === Close nav on link click (mobile) ===
  document.querySelectorAll('.nav a, .nav-sub a, .nav-items a').forEach(function(link){
    link.addEventListener('click', function(){
      document.querySelectorAll('.nav.nav-open, .nav-items.nav-open').forEach(function(n){ n.classList.remove('nav-open'); });
      document.querySelectorAll('.hamburger.open').forEach(function(h){ h.classList.remove('open'); });
      document.querySelectorAll('.nav-dropdown.open').forEach(function(dd){ dd.classList.remove('open'); });
    });
  });

  // Re-setup dropdowns after sticky nav is created
  if(stickyNav) setupDropdowns();
  if(stickyNav) setupHamburgers();
})();
