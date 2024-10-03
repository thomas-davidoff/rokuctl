let interactiveMode = true;

function toggleInteractiveMode() {
    interactiveMode = !interactiveMode;
    const button = document.getElementById('toggleInteractiveMode');
    if (interactiveMode) {
        button.textContent = 'Disable Interactive Mode';
        button.classList.add('interactive-mode');
    } else {
        button.textContent = 'Enable Interactive Mode';
        button.classList.remove('interactive-mode');
    }
}

document.addEventListener('keydown', function (event) {
    if (interactiveMode) {
        switch (event.key) {
            case 'ArrowUp':
                sendCommand('up');
                break;
            case 'ArrowDown':
                sendCommand('down');
                break;
            case 'ArrowLeft':
                sendCommand('left');
                break;
            case 'ArrowRight':
                sendCommand('right');
                break;
            case 'Enter':
                sendCommand('select');
                break;
            case ' ':
                sendCommand('play_pause');
                break;
            case 'm':
                sendCommand('mute');
                break;
            case 'u':
                sendCommand('volume_up');
                break;
            case 'd':
                sendCommand('volume_down');
                break;
            case 'h':
                sendCommand('home');
                break;
            case 'b':
                sendCommand('back');
                break;
            case 'i':
                sendCommand('info');
                break;
        }
    }
});

function sendCommand(command) {
    const formData = new FormData();
    formData.append('command', command);

    fetch('/send_command', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (response.ok) {
            console.log(`Command '${command}' sent successfully.`);
        } else {
            console.error(`Failed to send command '${command}'.`);
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
