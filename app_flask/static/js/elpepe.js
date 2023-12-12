document.getElementById('imagen').addEventListener("change", function () {
    const imageInput = document.getElementById('imagen');
    const previewImage = document.getElementById('previewImage');
    const uploadButton = document.getElementById('uploadButton');

    const selectedImage = imageInput.files[0];

    if (selectedImage) {
        const objectURL = URL.createObjectURL(selectedImage);

        // Actualiza la fuente de la imagen de vista previa con la imagen seleccionada
        previewImage.src = objectURL;

        // Muestra el botón de carga
        uploadButton.style.display = "block";
    } else {
        // Si no se selecciona ninguna imagen, restablece la fuente de la imagen de vista previa
        previewImage.src = "/static/img/lana.jpeg"; // Cambia esto a la imagen por defecto

        // Oculta el botón de carga
        uploadButton.style.display = "none";
    }
});