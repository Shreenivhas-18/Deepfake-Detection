document.addEventListener('DOMContentLoaded', function() {
    const fileInput = document.getElementById('fileInput');
    const fileNameDisplay = document.getElementById('fileName');
    const videoPlayerContainer = document.getElementById('videoPlayerContainer');
    const uploadedVideo = document.getElementById('uploadedVideo');
    const resultMessage = document.getElementById('resultMessage');
    const confidenceText = document.getElementById('confidenceText');
    let currentFileURL = null;

    // When file input changes, display the file name
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

            // Create a new object URL for the uploaded video
            currentFileURL = URL.createObjectURL(file);
            uploadedVideo.src = currentFileURL;
            videoPlayerContainer.style.display = 'block';

            // Indicate the processing status
            resultMessage.textContent = "Processing...";

            // Prepare form data to send to the Flask backend
            const formData = new FormData();
            formData.append('video', file);

            try {
                // Send the video file via a POST request
                const response = await fetch('/deepfakespredict', {
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
                confidenceText.textContent = ` ${data.confidenceText}`;

                // Handle result video URL if provided
                if (data.videoUrl) {
                    // Example: Use data.videoUrl if needed to replace or display another video
                }
            } catch (error) {
                // Handle any errors during processing
                resultMessage.textContent = "No Human Face Detected.";
                console.error('Error:', error);
            }
        } else {
            // No file selected
            resultMessage.textContent = "Please upload a video file.";
        }
    });
});
