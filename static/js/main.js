// JavaScript Interactivity for Leaf Disease Detection App
document.addEventListener('DOMContentLoaded', () => {
    // ----------------------------------------
    // Drag & Drop Upload Handlers (upload.html)
    // ----------------------------------------
    const uploadArea = document.getElementById('upload-area');
    const fileInput = document.getElementById('file-input');
    const previewContainer = document.getElementById('preview-container');
    const imagePreview = document.getElementById('image-preview');
    const uploadForm = document.getElementById('upload-form');
    if (uploadArea && fileInput) {
        // Trigger click on file input
        uploadArea.addEventListener('click', () => fileInput.click());
        // Highlight upload area on drag over
        ['dragenter', 'dragover'].forEach(eventName => {
            uploadArea.addEventListener(eventName, (e) => {
                e.preventDefault();
                e.stopPropagation();
                uploadArea.classList.add('dragover');
            }, false);
        });
        // Remove highlights
        ['dragleave', 'drop'].forEach(eventName => {
            uploadArea.addEventListener(eventName, (e) => {
                e.preventDefault();
                e.stopPropagation();
                uploadArea.classList.remove('dragover');
            }, false);
        });
        // Handle dropped files
        uploadArea.addEventListener('drop', (e) => {
            const dt = e.dataTransfer;
            const files = dt.files;
            if (files.length) {
                fileInput.files = files;
                showPreview(files[0]);
            }
        });
        // Handle file selection via explorer
        fileInput.addEventListener('change', (e) => {
            if (fileInput.files.length) {
                showPreview(fileInput.files[0]);
            }
        });
    }
    function showPreview(file) {
        if (file && file.type.startsWith('image/')) {
            const reader = new FileReader();
            reader.onload = (e) => {
                imagePreview.src = e.target.result;
                previewContainer.style.display = 'block';
            };
            reader.readAsDataURL(file);
        }
    }
    // ----------------------------------------
    // Live Webcam Feature (upload.html)
    // ----------------------------------------
    const btnOpenCamera = document.getElementById('btn-open-camera');
    const btnCapture = document.getElementById('btn-capture');
    const btnCloseCamera = document.getElementById('btn-close-camera');
    const cameraContainer = document.getElementById('camera-container');
    const webcam = document.getElementById('webcam');
    const cameraCanvas = document.getElementById('camera-canvas');
    let webcamStream = null;
    if (btnOpenCamera && webcam) {
        btnOpenCamera.addEventListener('click', async () => {
            try {
                webcamStream = await navigator.mediaDevices.getUserMedia({
                    video: { facingMode: 'environment' },
                    audio: false
                });
                webcam.srcObject = webcamStream;
                cameraContainer.style.display = 'block';
                if (previewContainer) previewContainer.style.display = 'none';
            } catch (err) {
                console.error("Camera access failed:", err);
                alert("Unable to access camera. Please check permissions or upload an image file instead.");
            }
        });
        btnCloseCamera.addEventListener('click', stopWebcam);
        btnCapture.addEventListener('click', () => {
            if (webcamStream) {
                const ctx = cameraCanvas.getContext('2d');
                cameraCanvas.width = webcam.videoWidth || 640;
                cameraCanvas.height = webcam.videoHeight || 480;
                
                ctx.drawImage(webcam, 0, 0, cameraCanvas.width, cameraCanvas.height);
                
                cameraCanvas.toBlob((blob) => {
                    if (blob) {
                        const capturedFile = new File([blob], 'captured_leaf.png', { type: 'image/png' });
                        const dataTransfer = new DataTransfer();
                        dataTransfer.items.add(capturedFile);
                        fileInput.files = dataTransfer.files;
                        
                        showPreview(capturedFile);
                    }
                    stopWebcam();
                }, 'image/png');
            }
        });
    }
    function stopWebcam() {
        if (webcamStream) {
            webcamStream.getTracks().forEach(track => track.stop());
            webcamStream = null;
        }
        if (webcam) webcam.srcObject = null;
        if (cameraContainer) cameraContainer.style.display = 'none';
    }
    // ----------------------------------------
    // Circle Progress Animation (detect.html)
    // ----------------------------------------
    const circleProgressHealthy = document.querySelector('.circle-progress-healthy');
    const circleProgressDiseased = document.querySelector('.circle-progress-diseased');
    if (circleProgressHealthy) {
        const pct = parseFloat(circleProgressHealthy.getAttribute('data-pct'));
        const radius = 40;
        const circumference = 2 * Math.PI * radius;
        const offset = circumference - (pct / 100) * circumference;
        
        circleProgressHealthy.style.strokeDasharray = `${circumference} ${circumference}`;
        // Trigger reflow to start transition
        circleProgressHealthy.getBoundingClientRect();
        circleProgressHealthy.style.strokeDashoffset = offset;
    }
    if (circleProgressDiseased) {
        const pct = parseFloat(circleProgressDiseased.getAttribute('data-pct'));
        const radius = 40;
        const circumference = 2 * Math.PI * radius;
        const offset = circumference - (pct / 100) * circumference;
        
        circleProgressDiseased.style.strokeDasharray = `${circumference} ${circumference}`;
        circleProgressDiseased.getBoundingClientRect();
        circleProgressDiseased.style.strokeDashoffset = offset;
    }
    // ----------------------------------------
    // Text-To-Speech (TTS) voice playback (detect.html)
    // ----------------------------------------
    let selectedLang = 'en'; // Default
    const langBtns = document.querySelectorAll('.lang-btn');
    const btnSpeak = document.getElementById('btn-speak');
    if (langBtns.length && btnSpeak) {
        langBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                langBtns.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                selectedLang = btn.getAttribute('data-lang');
            });
        });
        btnSpeak.addEventListener('click', () => {
            speakResults();
        });
    }
    function speakResults() {
        if (!('speechSynthesis' in window)) {
            alert('Your browser does not support Speech Synthesis. Please use Chrome, Safari or Edge.');
            return;
        }
        // Stop any current speech
        window.speechSynthesis.cancel();
        let textToSpeak = '';
        let langCode = 'en-US';
        if (selectedLang === 'en') {
            const name = document.getElementById('speak-name-en').innerText;
            const health = document.getElementById('speak-health').innerText;
            const disease = document.getElementById('speak-disease').innerText;
            const advice = document.getElementById('speak-advice-en').innerText;
            
            textToSpeak = `Disease Analysis. Diagnostic result: ${name}. Healthy leaf area: ${health} percent. Diseased leaf area: ${disease} percent. Treatment advice: ${advice}`;
            langCode = 'en-US';
        } else if (selectedLang === 'ta') {
            const name = document.getElementById('speak-name-ta').innerText;
            const health = document.getElementById('speak-health').innerText;
            const disease = document.getElementById('speak-disease').innerText;
            const advice = document.getElementById('speak-advice-ta').innerText;
            textToSpeak = `நோய் பகுப்பாய்வு முடிவுகள். கண்டறியப்பட்ட நோய்: ${name}. ஆரோக்கியமான இலை பரப்பளவு: ${health} சதவீதம். நோய் பாதிப்புக்குள்ளான இலை பரப்பளவு: ${disease} சதவீதம். சிகிச்சை அறிவுரை: ${advice}`;
            langCode = 'ta-IN';
        }
        const utterance = new SpeechSynthesisUtterance(textToSpeak);
        utterance.lang = langCode;
        utterance.rate = 0.9; // Slightly slower for clear pronunciation
        utterance.pitch = 1.0;
        // Try to match a native voice for the selected language
        const voices = window.speechSynthesis.getVoices();
        const matchedVoice = voices.find(voice => voice.lang.includes(langCode) || voice.lang.startsWith(selectedLang));
        if (matchedVoice) {
            utterance.voice = matchedVoice;
        }
        window.speechSynthesis.speak(utterance);
    }
    // Trigger loading voices (necessary for Chrome/Safari load delays)
    if ('speechSynthesis' in window) {
        window.speechSynthesis.getVoices();
    }
    // Auto-fade flash alerts
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.opacity = '0';
            alert.style.transition = 'opacity 0.5s ease';
            setTimeout(() => alert.remove(), 500);
        }, 4000);
    });
});
