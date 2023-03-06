
      // head swiper start here

      const swiper = new Swiper(".swiper", {
        autoplay: {
          delay: 3000,
          disableOnInteraction: false,
        },
        loop: true,

        // If we need pagination
        pagination: {
          el: ".swiper-pagination",
        },

        // Navigation arrows
        navigation: {
          nextEl: ".swiper-button-next",
          prevEl: ".swiper-button-prev",
        },
      });

      // head swiper end here

      // special swiper start here
          
      function right_btn(){
            document.getElementById('scroll').scrollLeft +=500;
        }
        function left_btn(){
            document.getElementById('scroll').scrollLeft -=500;
        }

          // special swiper end here
