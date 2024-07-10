
    document.getElementById("loginForm").addEventListener("submit", function(event) {
        event.preventDefault();
        
        var username = document.getElementById("username").value;
        var password = document.getElementById("password").value;
        
        if (username === "admin" && password === "admin123") {
            window.location.href = "/administrador/index_admin.html";
        } else {
            alert("Usuario o contraseña incorrectos. Por favor, inténtalo de nuevo.");
        }
    });
    