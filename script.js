const CLIENT_ID = '58972522609-60qei3jnf6fg3fic9lds81lc8em087c2.apps.googleusercontent.com';
const CLIENT_SECRET = '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';
const REDIRECT_URI = 'https://developers.google.com/oauthplayground';
const REFRESH_TOKEN = '1//04VBS-3kmjUpKCgYIARAAGAQSNwF-L9Irrqr3aTfDq6b-5379fORTqOOWePn6ceNE0crre_SCHh1_V2RDUKY8FWqWXMBB37lnx-U';
const FILE_ID = '1YhNy0xWA108a1ue53zRquQi-72ms8SPx'; // Google Drive file ID



document.getElementById('send-button').addEventListener('click', async () => {
    const newMessageTextarea = document.getElementById('new-message');
    const usernameInput = document.getElementById('username');
    const message = newMessageTextarea.value.trim();
    const username = usernameInput.value.trim();
    
    if (message && username) {
        const formattedMessage = `${username}: ${message}`;
        await saveMessage(formattedMessage);
        newMessageTextarea.value = ''; // Clear the input
        usernameInput.value = ''; // Clear the username input
        loadMessages(); // Reload messages to show the newly added one
    } else {
        document.getElementById('status').textContent = 'Please enter both username and message.';
    }
});

/**
 * Get access token using refresh token
 */
async function getAccessToken() {
    const response = await fetch('https://oauth2.googleapis.com/token', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: new URLSearchParams({
            client_id: CLIENT_ID,
            client_secret: CLIENT_SECRET,
            refresh_token: REFRESH_TOKEN,
            grant_type: 'refresh_token'
        })
    });
    const data = await response.json();
    return data.access_token;
}

/**
 * Load messages from Google Drive
 */
async function loadMessages() {
    const accessToken = await getAccessToken();
    const response = await fetch(`https://www.googleapis.com/drive/v3/files/${FILE_ID}?alt=media`, {
        headers: new Headers({ 'Authorization': `Bearer ${accessToken}` })
    });

    if (response.ok) {
        const content = await response.text();
        document.getElementById('messages').textContent = content;
    } else {
        console.error('Failed to load messages:', response.statusText);
    }
}

/**
 * Save new message to Google Drive
 */
async function saveMessage(newMessage) {
    const accessToken = await getAccessToken();
    const existingMessages = document.getElementById('messages').textContent;
    const updatedMessages = existingMessages + (existingMessages ? '\n' : '') + newMessage;

    const metadata = {
        mimeType: 'text/plain'
    };

    const form = new FormData();
    form.append('metadata', new Blob([JSON.stringify(metadata)], { type: 'application/json' }));
    form.append('file', new Blob([updatedMessages], { type: 'text/plain' }));

    const response = await fetch(`https://www.googleapis.com/upload/drive/v3/files/${FILE_ID}?uploadType=multipart`, {
        method: 'PATCH',
        headers: new Headers({ 'Authorization': `Bearer ${accessToken}` }),
        body: form
    });

    if (response.ok) {
        document.getElementById('status').textContent = 'Message saved successfully.';
    } else {
        console.error('Error saving message:', response.statusText);
        document.getElementById('status').textContent = 'Error saving message. Please try again.';
    }
}

// Initial load of messages
loadMessages();