function validate() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    if (username == "admin" && password == "user") {
        alert("Login Successfully!");
        window.open("dls.html");
    }
    else {
        alert("Login failed!");
    }
}

function register() {
    pass = document.getElementById("password").value;
    cpass = document.getElementById("cpassword").value;

    if (pass != cpass) {
         alert("Registration failed confirm password...");
    }
}
