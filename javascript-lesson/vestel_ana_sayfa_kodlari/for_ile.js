for (let index = 1; index <= 10; index++) {
    const div = document.querySelector(`div[data-swiper-slide-index="${index}"]`);
    if (div) {
      const img = div.querySelector('img');
      if (img && img.src === 'https://statics.vestel.com.tr/bannerimages/iot-yeniyil-banner-1920x480_2022122013035181256.jpg') {
        const a = div.querySelector('a');
        if (a) {
          a.href = 'https://www.vestel.com.tr/saat2-minidots-yilbasi-urunleri-c-1692';
        }
      }
    }
  }
