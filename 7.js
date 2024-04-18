let wasans = 0
    window.addEventListener('scroll', function() {
      if (document.documentElement.scrollHeight - window.innerHeight - window.scrollY < 1500 && wasans == 0) {
        document.querySelector('.css-qtq074').click();
        wasans = 1
        setTimeout(() => { wasans = 0 }, 500)
      }
    });
// function wasans() { document.querySelector(".css-qtq074").click(); setTimeout(() => { wasans() }, 500) } wasans()
