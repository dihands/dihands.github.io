function handleSubmit(event) {
    event.preventDefault();
    
    // Get form values
    const fullName = document.getElementById('fullName').value;

    const password = document.getElementById('password').value;
    
    // Store data in localStorage (for demonstration purposes)
    localStorage.setItem('fullName', fullName);

    localStorage.setItem('password', password);
    
    // Redirect to profile page
    window.location.href = 'welcome';
}

// Display user details on profile.html
window.onload = function() {
    const fullName = localStorage.getItem('fullName');

    const password = localStorage.getItem('password');

    
    if (fullName && email) {
        const profileDetails = document.getElementById('profileDetails');
        profileDetails.innerHTML = `
            <p><strong>Name:</strong> ${fullName}</p>

            <p><strong>Password:</strong> ${password}</p>
        `;
        
        // Optional: Clear localStorage after displaying details
        // localStorage.removeItem('fullName');
        // localStorage.removeItem('email');
    }
}


