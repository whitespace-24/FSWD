const slider = document.getElementById("brightness-slider");
const label = document.getElementById("brightness-label");
const overlay = document.getElementById("darkness-overlay");

function updateBrightness(value) {
    let darknessAmount = 1 - (value / 100);
    overlay.style.opacity = darknessAmount;
    label.innerText = value + "%";
}

slider.addEventListener("input", function() {
    let currentValue = parseInt(slider.value);
    
    if (Math.random() < 0.15) {
        let jitter = Math.floor(Math.random() * 21) - 10; 
        currentValue = Math.max(0, Math.min(100, currentValue + jitter));
        slider.value = currentValue;
    }
    
    updateBrightness(currentValue);
});

slider.addEventListener("change", function() {
    let finalValue = Math.floor(Math.random() * 101);
    
    slider.value = finalValue;
    updateBrightness(finalValue);
    
    label.innerText = finalValue + "% (Optimized)";
});