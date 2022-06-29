function Registrarse (){
    
    let Usuario= document.getElementById("Usuario").value;
    if( Usuario == "")
    {
        alert("Nombre usuario no ingresado");
        hasError = true;
        return false;
    }
    let Nombre= document.getElementById("Nombre").value;
    if( Nombre == "")
    {
        alert("Nombre no ingresado");
        hasError = true;
        return false;
    }
    
    let Apellido = document.getElementById("Apellido").value;
    if( Apellido == "")
    {
        alert("Apellido no ingresado");
        hasError = true;
        return false;
    }
    let Rut = document.getElementById("Rut").value;
    if(Rut.length < 7){
        alert("Rut no ingresado");
        hasError = true;
        return false;
    } 
    let Dv = document.getElementById("Dv").value;
    if( Dv == "" )
    {
        alert("Dv no ingresado");
        hasError = true;
        return false;
    } 
    let Telefono = document.getElementById("Telefono").value;
    var digitos =/^\d{9}$/;
    var vale= digitos.test(Telefono);
    if( Telefono == "" || vale == false )
    {
        alert("Telefono no ingresado");
        hasError = true;
        return false;
    } 

    let Contraseña1 = document.getElementById("Contraseña1").value;
    let Contraseña2 = document.getElementById("Contraseña2").value;
    if( Contraseña1.length < 6)
    {
        alert("Contraseña no ingresado");
        hasError = true;
        return false;
    } 

    if (Contraseña1 != Contraseña2)
    {
        alert("Las claves son distintas");
        hasError = true;
        return false;
    }
    let Correo = document.getElementById("Correo").value;
   {
    var expReg = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    var esValido = expReg.test(Correo); 
    if (esValido == false){
        alert("Correo no ingresado")
        hasError = true;
        return false;}
    }  
    let fecha = document.getElementById("Date").value;
    if(!fecha) { 
        alert("Ingrese fecha nacimiento")
        hasError = true;
        return false;
        document.getElementById("Date").focus
    }
    
    opciones = document.getElementsByName("Terminos");
    if(!document.querySelector('input[name="Terminos"]:checked')) {
        alert('Selecciona si aceptas los terminos y condiciones');
        hasError = true;
        return false;
        }
        opciones = document.getElementsByName("PromoCorreo");
        if(!document.querySelector('input[name="PromoCorreo"]:checked')) {
            alert('Selecciona si deseas recibir promociones al correo');
            hasError = true;
            return false;
            }
    document.location.href="suscribrise.html";
   }
   
    

  