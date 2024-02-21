// Get a reference to the registration form
const registrationForm = document.getElementById('registrationForm');

document.addEventListener('DOMContentLoaded', function() {
    // Check if the form element is found
    if (registrationForm) {
        // Add event listener for form submission
        registrationForm.addEventListener('submit', async (e) => {
            e.preventDefault(); // Prevent form submission

            // Get form values
            const username = registrationForm['username'].value;
            const email = registrationForm['email'].value;
            const weight = parseInt(registrationForm['weight'].value);
            const height = parseInt(registrationForm['height'].value);
            const age = parseInt(registrationForm['age'].value);
            const about = registrationForm['about'].value;
            const password = registrationForm['password'].value;

            try {
                // Create user in Firebase Authentication
                const userCredential = await firebase.auth().createUserWithEmailAndPassword(email, password);
                const user = userCredential.user;

                // Add user details to Realtime Database
                await firebase.database().ref('users/' + user.uid).set({
                    username: username,
                    email: email,
                    weight: weight,
                    height: height,
                    age: age,
                    about: about
                });

                console.log("User registered successfully!");
                // Redirect or show success message
            } catch (error) {
                console.log("Error registering user: ", error);
                // Handle error
            }
        });
    } else {
        console.log("Registration form element not found.");
    }
});
