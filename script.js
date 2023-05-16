// Get road, car, and obstacle elements
const road = document.getElementById('road');
const car = document.getElementById('car');

// Initialize car position
let carX = 175;

// Update car position
function updateCarPosition() {
  car.style.left = carX + 'px';
}

// Move car left or right based on arrow key presses
document.addEventListener('keydown', (event) => {
  const key = event.key;

  if (key === 'ArrowLeft') {
    carX -= 10;
    if (carX < 0) {
      carX = 0;
    }
  } else if (key === 'ArrowRight') {
    carX += 10;
    if (carX > 350) {
      carX = 350;
    }
  }

  updateCarPosition();
});

// Generate obstacles randomly every 1 second
setInterval(() => {
  const obstacle = document.createElement('div');
  obstacle.classList.add('obstacle');

  const randomX = Math.floor(Math.random() * 351); // Random X position between 0 and 350
  obstacle.style.left = randomX + 'px';

  road.appendChild(obstacle);

  // Animate obstacles falling down the road
  let topPosition = 0;
  const obstacleInterval = setInterval(() => {
    topPosition += 10;
    obstacle.style.top = topPosition + 'px';

    // Check collision with car
    const carRect = car.getBoundingClientRect();
    const obstacleRect = obstacle.getBoundingClientRect();

    if (
      carRect.left < obstacleRect.right &&
      carRect.right > obstacleRect.left &&
      carRect.top < obstacleRect.bottom &&
      carRect.bottom > obstacleRect.top
    ) {
      alert('Game Over! You crashed into an obstacle.');
      clearInterval(obstacleInterval);
      road.removeChild(obstacle);
    }

    // Remove obstacle when it reaches the bottom of the road
    if (topPosition > 600) {
      clearInterval(obstacleInterval);
      road.removeChild(obstacle);
    }
  }, 100);
}, 1000);
