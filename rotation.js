// Select all the images on the page
var images = document.querySelectorAll('.images img');

// Set the initial position and rotation for each image
for (var i = 0; i < images.length; i++) {
  var xPos = (i + 1) * 150;
  var yPos = (i + 1) * 100;
  var rotation = (i + 1) * 20;
  
  images[i].style.transform = `translate(${xPos}px, ${yPos}px) rotate(${rotation}deg)`;
}

// Function to animate the images
function animateImages() {
  for (var i = 0; i < images.length; i++) {
    var xPos = (i + 1) * 150;
    var yPos = (i + 1) * 100;
    var rotation = (i + 1) * 20;
    images[i].style.transform = `translate(${xPos}px, ${yPos}px) rotate(${rotation}deg)`;
  }
}

// Call the animateImages function every 2 seconds
setInterval(animateImages, 2000);