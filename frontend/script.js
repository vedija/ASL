document.addEventListener("DOMContentLoaded", function () {
    const startBtn = document.getElementById("start-btn");
    const outputText = document.getElementById("output-text");
    const videoContainer = document.getElementById("video-container");
    const loadingIndicator = document.getElementById("loading-indicator");

    videoContainer.innerHTML = "";

    if (!("webkitSpeechRecognition" in window)) {
        alert("Speech Recognition is not supported in this browser. Try using Chrome.");
        return;
    }

    const recognition = new webkitSpeechRecognition();
    recognition.continuous = false;
    recognition.lang = "en-US";

    startBtn.addEventListener("click", function () {
        if (recognition.running) {
            console.warn("Speech recognition is already running.");
            return;
        }
        startBtn.disabled = true;
        outputText.textContent = "Listening...";
        recognition.start();
    });

    recognition.onresult = function (event) {
        let speechText = event.results[0][0].transcript.toLowerCase().trim();
        outputText.textContent = `Recognized: ${speechText}`;
        loadingIndicator.classList.remove("hidden");

        fetch("http://127.0.0.1:5000/convert", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text: speechText }) 
        })
        .then(response => response.json())
        .then(data => {
            loadingIndicator.classList.add("hidden");  // Hide loading indicator

            if (!data.videos || data.videos.length === 0) {
                outputText.textContent = "No ASL video found for the recognized text.";
                return;
            }

            displayASLVideos(data.videos);
        })
        .catch(error => {
            console.error("Error fetching ASL video:", error);
            outputText.textContent = "Error: Unable to fetch ASL video.";
            loadingIndicator.classList.add("hidden");
        })
        .finally(() => {
            startBtn.disabled = false;
        });
    };

    recognition.onerror = function (event) {
        console.error("Speech recognition error:", event.error);
        outputText.textContent = "Error: Speech recognition failed.";
        startBtn.disabled = false;
        loadingIndicator.classList.add("hidden");
    };

    // function displayASLVideos(videoList) {
    //     videoContainer.innerHTML = "";  // Clear previous videos

    //     let index = 0;
    //     function playNextVideo() {
    //         if (index >= videoList.length) return;

    //         let videoElement = document.createElement("video");
    //         videoElement.src = videoList[index].url;
    //         videoElement.controls = true;
    //         videoElement.autoplay = true;
    //         videoElement.style.margin = "10px";
    //         videoElement.width = 300;

    //         videoContainer.appendChild(videoElement);

    //         videoElement.onended = function () {
    //             index++;
    //             playNextVideo();
    //         };
    //     }

    //     playNextVideo();
    // }
    function displayASLVideos(videoList) {
        videoContainer.innerHTML = "";  // ✅ Clear previous videos
    
        let index = 0;
    
        function playNextVideo() {
            if (index >= videoList.length) return; // Stop when all videos are played
    
            let videoElement = document.createElement("video");
            videoElement.src = videoList[index].url;
            videoElement.controls = true;
            videoElement.autoplay = true;
            videoElement.style.margin = "10px";
            videoElement.width = 250;
    
            videoContainer.appendChild(videoElement);
    
            videoElement.onended = function () {
                index++; // Move to the next video
                playNextVideo(); // Play next video when current one ends
            };
        }
    
        playNextVideo(); // Start playing the first video
    }
    
    
});
