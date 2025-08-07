// Recycling Data
const recyclingData = {
  "battery": "🚨 Take to battery recycling center (hazardous waste)",
  "pizza box": "📦 If clean: compost. If greasy: trash",
  "plastic bottle": "♻️ Rinse and put in plastic recycling",
  "glass": "🫙 Rinse and recycle with glass",
  "paper": "📄 Recycle if clean and dry"
};

// Initialize
document.addEventListener('DOMContentLoaded', function() {
  loadTheme();
  loadChallenges();
});

// Theme Toggle
document.getElementById('themeToggle').addEventListener('click', function() {
  const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
  const newTheme = currentTheme === 'light' ? 'dark' : 'light';
  document.documentElement.setAttribute('data-theme', newTheme);
  localStorage.setItem('theme', newTheme);
  this.textContent = newTheme === 'light' ? '🌙' : '☀️';
});

function loadTheme() {
  const savedTheme = localStorage.getItem('theme') || 'light';
  document.documentElement.setAttribute('data-theme', savedTheme);
  document.getElementById('themeToggle').textContent = savedTheme === 'light' ? '🌙' : '☀️';
}

// Recycling Guide
function searchItem() {
  const item = document.getElementById('searchItem').value.toLowerCase();
  const resultDiv = document.getElementById('result');
  
  if (recyclingData[item]) {
    resultDiv.innerHTML = `✅ <strong>${item}</strong>: ${recyclingData[item]}`;
    resultDiv.classList.add('animate__animated', 'animate__pulse');
    setTimeout(() => resultDiv.classList.remove('animate__pulse'), 1000);
  } else {
    resultDiv.innerHTML = "❌ Item not found. Try: battery, pizza box, plastic...";
  }
}

// Challenges System
function loadChallenges() {
  const challenges = document.querySelectorAll('#challengeList input');
  
  challenges.forEach(challenge => {
      if (localStorage.getItem(challenge.id)) {
        challenge.checked = true;
      }
      
      challenge.addEventListener('change', function() {
        if (this.checked) {
          localStorage.setItem(this.id, 'true');
          updateProgress();
        } else {
          localStorage.removeItem(this.id);
          updateProgress();
        }
      });
    });
  
  updateProgress();
}

function updateProgress() {
  const challenges = document.querySelectorAll('#challengeList input');
  const checkedChallenges = document.querySelectorAll('#challengeList input:checked').length;
  const totalChallenges = challenges.length;
  const progress = (checkedChallenges / totalChallenges) * 100;

  // Update progress bar
  const progressBar = document.getElementById('progressBar');
  progressBar.style.width = `${progress}%`;
  progressBar.setAttribute('aria-valuenow', progress);

  // Level system
  let levelText = "";
  let barColor = "";
  if (checkedChallenges === totalChallenges && totalChallenges > 0) {
    levelText = "🌟 Eco Champion!";
    barColor = "linear-gradient(90deg, #FFD700, #FFA500)";
    showConfetti();
  } else if (checkedChallenges >= Math.ceil(totalChallenges * 0.7)) {
    levelText = "🌱 Eco Hero";
    barColor = "linear-gradient(90deg, #4CAF50, #8BC34A)";
  } else if (checkedChallenges >= 1) {
    levelText = "🌿 Eco Warrior";
    barColor = "linear-gradient(90deg, #2196F3, #00BCD4)";
  } else {
    levelText = "🌎 Eco Beginner";
    barColor = "linear-gradient(90deg, #BDBDBD, #EEEEEE)";
  }
  document.getElementById('levelText').textContent = levelText;
  progressBar.style.background = barColor;

  // Show motivational message
  const messageDiv = document.getElementById('motivation');
  if (checkedChallenges === totalChallenges && totalChallenges > 0) {
    messageDiv.textContent = "Congratulations! You've completed all challenges!";
  } else if (checkedChallenges > 0) {
    messageDiv.textContent = `Great job! Only ${totalChallenges - checkedChallenges} left to go!`;
  } else {
    messageDiv.textContent = "Start your first eco challenge!";
  }
}

// Confetti animation for completion
function showConfetti() {
  if (window.confetti) {
    window.confetti({
      particleCount: 100,
      spread: 70,
      origin: { y: 0.6 }
    });
  }
}

// Reset progress feature
document.getElementById('resetChallenges').addEventListener('click', function() {
  const challenges = document.querySelectorAll('#challengeList input');
  challenges.forEach(challenge => {
    challenge.checked = false;
    localStorage.removeItem(challenge.id);
  });
  updateProgress();
});

// Add keyboard accessibility for progress bar
document.getElementById('progressBar').setAttribute('tabindex', '0');
document.getElementById('progressBar').setAttribute('role', 'progressbar');
document.getElementById('progressBar').setAttribute('aria-valuemin', '0');
document.getElementById('progressBar').setAttribute('aria-valuemax', '100');

// --- Advanced Features: Interactive Map & More ---

// 1. Add a map showing recycling centers using Leaflet.js (requires leaflet.js and leaflet.css in HTML)
function initMap() {
  // Create map container if not present
  let mapDiv = document.getElementById('recycleMap');
  if (!mapDiv) {
    mapDiv = document.createElement('div');
    mapDiv.id = 'recycleMap';
    mapDiv.style = 'height: 300px; margin: 20px 0; border-radius: 12px; box-shadow: 0 2px 8px #0002;';
    document.body.insertBefore(mapDiv, document.getElementById('challengeList'));
  }

  // Initialize map
  const map = L.map('recycleMap').setView([40.7128, -74.0060], 12); // Default: New York City

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
  }).addTo(map);

  // Example recycling centers (replace with real data as needed)
  const centers = [
    { name: "Green Battery Center", lat: 40.715, lng: -74.002, type: "battery" },
    { name: "Eco Glass Depot", lat: 40.722, lng: -74.01, type: "glass" },
    { name: "Plastic Drop-off", lat: 40.709, lng: -74.015, type: "plastic" }
  ];

  centers.forEach(center => {
    L.marker([center.lat, center.lng])
      .addTo(map)
      .bindPopup(`<b>${center.name}</b><br>Accepts: ${center.type}`);
  });

  // Try to locate user
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(pos => {
      map.setView([pos.coords.latitude, pos.coords.longitude], 13);
      L.marker([pos.coords.latitude, pos.coords.longitude])
        .addTo(map)
        .bindPopup("You are here").openPopup();
    });
  }
}

// 2. Add fun fact generator
const ecoFacts = [
  "Recycling one aluminum can saves enough energy to run a TV for 3 hours.",
  "Glass can be recycled endlessly without loss in quality.",
  "Plastic takes up to 1,000 years to decompose in landfills.",
  "Composting food waste reduces methane emissions.",
  "Recycling one ton of paper saves 17 trees."
];

function showRandomFact() {
  const factDiv = document.getElementById('ecoFact');
  if (!factDiv) {
    const newDiv = document.createElement('div');
    newDiv.id = 'ecoFact';
    newDiv.style = 'margin: 16px 0; font-style: italic; color: #388e3c;';
    document.body.insertBefore(newDiv, document.getElementById('challengeList'));
  }
  const fact = ecoFacts[Math.floor(Math.random() * ecoFacts.length)];
  document.getElementById('ecoFact').textContent = "🌟 Eco Fact: " + fact;
}

// 3. Add animated progress badge
function updateBadge() {
  const badgeDiv = document.getElementById('ecoBadge');
  if (!badgeDiv) {
    const newDiv = document.createElement('div');
    newDiv.id = 'ecoBadge';
    newDiv.style = 'margin: 12px 0; font-size: 2em; text-align: center;';
    document.body.insertBefore(newDiv, document.getElementById('motivation'));
  }
  const checked = document.querySelectorAll('#challengeList input:checked').length;
  const total = document.querySelectorAll('#challengeList input').length;
  let badge = "🔰";
  if (checked === total && total > 0) badge = "🏆";
  else if (checked >= Math.ceil(total * 0.7)) badge = "🥇";
  else if (checked >= 1) badge = "🥈";
  document.getElementById('ecoBadge').textContent = badge;
}

// 4. Enhance updateProgress to update badge and show fact
const originalUpdateProgress = updateProgress;
updateProgress = function() {
  originalUpdateProgress();
  updateBadge();
  showRandomFact();
};

// 5. Initialize map and show first fact on DOMContentLoaded
document.addEventListener('DOMContentLoaded', function() {
  initMap();
  showRandomFact();
  updateBadge();
});