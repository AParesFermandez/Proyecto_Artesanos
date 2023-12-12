

document.getElementById('imagen').addEventListener("change", function () {
    const selectedImage = imageInput.files[0];
    if (selectedImage) {
        const objectURL = URL.createObjectURL(selectedImage);

        // Update the source of the profile image with the selected image
        const profileImage = document.getElementById("profileImage");
        profileImage.src = objectURL;

        document.getElementById("uploadButton").style.display = "block";
    } else {
        // If no image is selected, reset the source of the profile image
        const profileImage = document.getElementById("profileImage");
        profileImage.src = "{{ url_for('static', 'img', filename='lana.png') }"; // aqui va la imagen por defecto

        document.getElementById("uploadButton").style.display = "none";
    }
});