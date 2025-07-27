function validateForm() {
    var name = document.getElementById("name").value.trim();
    var email = document.getElementById("email").value.trim();
    var phone = document.getElementById("phone").value.trim();

    var emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    var phonePattern = /^[0-9]{10}$/;

    if (name === "") {
        alert("Name is required");
        return false;
    }
    if (!emailPattern.test(email)) {
        alert("Invalid email format");
        return false;
    }
    if (!phonePattern.test(phone)) {
        alert("Phone number must be 10 digits");
        return false;
    }

    alert("Form submitted successfully!");
    return true;
}
