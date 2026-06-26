document.addEventListener('DOMContentLoaded', function() {
    const fileInput = document.getElementById('fileInput');
    const fileNameDisplay = document.getElementById('fileName');
    const resultMessage = document.getElementById('resultMessage');
    const confidenceText = document.getElementById('confidenceText');
    const imagePreviewContainer = document.getElementById('imagePreviewContainer');
    const uploadedImage = document.getElementById('uploadedImage');
    let currentFileURL = null;

    // When file input changes, display the file name and reset results
    fileInput.addEventListener('change', function() {
        const fileName = fileInput.files[0] ? fileInput.files[0].name : 'No file selected';
        fileNameDisplay.textContent = fileName;
        resultMessage.textContent = "";
        confidenceText.textContent = "";
    });

    // Handle the form submission
    document.getElementById('uploadForm').addEventListener('submit', async function(event) {
        event.preventDefault();
        const file = fileInput.files[0];

        if (file) {
            // Free the previous object URL if any
            if (currentFileURL) {
                URL.revokeObjectURL(currentFileURL);
            }

            // Display the uploaded image preview
            currentFileURL = URL.createObjectURL(file);
            uploadedImage.src = currentFileURL;
            imagePreviewContainer.style.display = 'block';

            // Indicate the processing status
            resultMessage.textContent = "Processing...";

            // Prepare form data to send to the Flask backend
            const formData = new FormData();
            formData.append('image', file);

            try {
                // Send the image file via a POST request to Flask
                const response = await fetch('/imagepredict', {
                    method: 'POST',
                    body: formData
                });

                // Check if the response is valid
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }

                // Parse the response data from the backend
                const data = await response.json();

                // Display the result text and confidence level
                resultMessage.textContent = data.resultText;
                confidenceText.textContent = data.confidenceText;

            } catch (error) {
                // Handle any errors during processing
                resultMessage.textContent = "Error occurred during processing.";
                console.error('Error:', error);
            }
        } else {
            // No file selected
            resultMessage.textContent = "Please upload an image file.";
        }
    });
});
