/* <script src="https://kit.fontawesome.com/28d049d17c.js" crossorigin="anonymous"></script> */
function validarFormulario(){
 let nombre=document.getElementById("name").value;
 let correoe=document.getElementById("email").value;
 const fileInput = document.getElementById('fileInput');
 document.write(nombre);
 document.write(correoe);
 if(nombre==""||correoe==""){
         alert("Por favor, no dejes campos vacios!");
         return false;
     }
      return true;   

fileInput.addEventListener('change', function() {
          const file = fileInput.files[0];
          console.log('Archivo seleccionado:', file.name, file.size);
         
      });
 }

