const images = document.querySelectorAll('.image-container img');
const a = 200; // major axis
const b = 100; // minor axis
const duration = 10000; // 10s

const timing = {
  duration: duration,
  loop: true
};

images.forEach((image, index) => {
    anime({
      targets: image,
      translateX: (a * Math.cos(2 * Math.PI * index / images.length)) + 'px',
      translateY: (b * Math.sin(2 * Math.PI * index / images.length)) + 'px',
      rotate: 360,
      easing: 'linear',
      ...timing
    });
});
