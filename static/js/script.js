const sizeInput = document.getElementById('size');
const colorInput = document.getElementById('color');

sizeInput.addEventListener('input', () => {
  if (sizeInput.value < 32) {
    sizeInput.value = 32;
  } else if (sizeInput.value > 512) {
    sizeInput.value = 512;
  }
});

colorInput.addEventListener('change', () => {
  if (colorInput.value === 'random') {
    document.body.style.backgroundColor = '#fff';
  } else if (colorInput.value === 'red') {
    document.body.style.backgroundColor =
