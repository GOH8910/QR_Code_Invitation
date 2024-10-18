const video = document.getElementById("video");
const canvas = document.getElementById("canvas");
const resultDiv = document.getElementById("result");
const ctx = canvas.getContext("2d");

// Access the camera using getUserMedia
navigator.mediaDevices.getUserMedia({ video: { facingMode: "environment" } })
    .then((stream) => {
        video.srcObject = stream;
        video.play();
        requestAnimationFrame(scanQRCode); // Start scanning after video starts
    })
    .catch((error) => {
        console.error("Error accessing camera:", error);
        resultDiv.textContent = "Camera access is required to scan QR codes.";
    });

function scanQRCode() {
    const width = video.videoWidth;
    const height = video.videoHeight;

    if (width && height) {
        canvas.width = width;
        canvas.height = height;
        ctx.drawImage(video, 0, 0, width, height);

        const imageData = ctx.getImageData(0, 0, width, height);
        const qrCode = jsQR(imageData.data, imageData.width, imageData.height);

        if (qrCode) {
            // Parse the URL to extract parameters
            const url = new URL(qrCode.data);
            const name = decodeURIComponent(url.searchParams.get("name"));
            const attendees = decodeURIComponent(url.searchParams.get("attendees"));

            // Format and display the result
            resultDiv.textContent = `Welcome ${name}, ${attendees}`;
            console.log("Decoded QR code:", qrCode.data);

            // Pause for a moment to allow the user to see the result, then resume scanning
            setTimeout(() => {
                requestAnimationFrame(scanQRCode);
            }, 2000); // 2-second delay before resuming scanning
        } else {
            // If no QR code found, keep scanning
            requestAnimationFrame(scanQRCode);
        }
    } else {
        // Retry scanning if video dimensions are not yet available
        requestAnimationFrame(scanQRCode);
    }
}

const ghost = document.getElementById("ghost");

function triggerGhostJump() {
    // Add the animation class to the ghost image
    ghost.classList.add("ghost-jump");

    // Remove the animation class after the animation ends (2 seconds in this example)
    setTimeout(() => {
        ghost.classList.remove("ghost-jump");
    }, 5000); // Match this with the animation duration
}

// Set interval to trigger the ghost jump every 30 seconds
setInterval(triggerGhostJump, 6000);