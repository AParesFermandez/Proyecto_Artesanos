document.getElementById('imagen').addEventListener('change', function(event) {
    const input = event.target;
    const previewImage = document.getElementById('previewImage');

    if (input.files && input.files[0]) {
        const reader = new FileReader();

        reader.onload = function(e) {
            previewImage.src = e.target.result;
        };

        reader.readAsDataURL(input.files[0]);
    }
});