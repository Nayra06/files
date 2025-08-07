document.getElementById('wordSelect').addEventListener('change', function () {
  const word = this.value;
  const display = document.getElementById('imageDisplay');

  if (word === '') {
    display.innerHTML = "<p>Select a word to see its sign language image.</p>";
  } else {
    display.innerHTML = `<img src="images/${word}.jpg" alt="${word} sign language">`;
  }
});
