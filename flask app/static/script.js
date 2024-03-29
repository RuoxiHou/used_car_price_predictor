// script.js
document.addEventListener('DOMContentLoaded', function() {
    var selectedMakeDropdown = document.getElementById('selected_make');
    var selectedModelDropdown = document.getElementById('selected_model');
    var selectedTrimDropdown = document.getElementById('selected_trim');

    // Function to update model dropdown based on selected make
    function updateModelDropdown() {
        var selectedMake = selectedMakeDropdown.value;
        var xhr = new XMLHttpRequest();
        xhr.open('GET', '/models?make=' + selectedMake, true);
        xhr.onload = function() {
            if (xhr.status === 200) {
                var models = JSON.parse(xhr.responseText);
                selectedModelDropdown.innerHTML = '';
                models.forEach(function(model) {
                    var option = document.createElement('option');
                    option.textContent = model;
                    option.value = model;
                    selectedModelDropdown.appendChild(option);
                });
                // Trigger update for trim dropdown when models are updated
                updateTrimDropdown(); // Update trim dropdown here
            } else {
                console.log('Request failed. Returned status of ' + xhr.status);
            }
        };
        xhr.send();
    }

    // Function to update trim dropdown based on selected make and model
    function updateTrimDropdown() {
        var selectedMake = selectedMakeDropdown.value;
        var selectedModel = selectedModelDropdown.value;
        var xhr = new XMLHttpRequest();
        xhr.open('GET', '/trims?make=' + selectedMake + '&model=' + selectedModel, true);
        xhr.onload = function() {
            if (xhr.status === 200) {
                var trims = JSON.parse(xhr.responseText);
                selectedTrimDropdown.innerHTML = '';
                trims.forEach(function(trim) {
                    var option = document.createElement('option');
                    option.textContent = trim;
                    option.value = trim;
                    selectedTrimDropdown.appendChild(option);
                });
            } else {
                console.log('Request failed. Returned status of ' + xhr.status);
            }
        };
        xhr.send();
    }

    // Event listeners
    selectedMakeDropdown.addEventListener('change', updateModelDropdown);
    selectedModelDropdown.addEventListener('change', updateTrimDropdown); 

    // Initial population of model dropdown
    updateModelDropdown();
});

