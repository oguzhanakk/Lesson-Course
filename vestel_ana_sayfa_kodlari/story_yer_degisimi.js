let matches = document.querySelector(".persona-slider-story-wrapper").querySelectorAll(".swiper-slide");

for(i = matches.length - 1; i >= 0; i--){
  if( matches[i].querySelector('a').href === 'https://www.vestel.com.tr/mixgo-blenderlar-c-36' ) {
      let element1 = document.querySelector('#personaEvcUrunleri');
      let element2 = matches[i].querySelector('a').parentNode;
        
      let parent = element1.parentNode;
      parent.insertBefore(element2, element1);
  }
}