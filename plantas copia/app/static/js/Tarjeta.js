function Suscribirse(){
    let Numero = document.getElementById("Numero").value;
    var cantidad =/^\d{16}$/;
    var bueno= cantidad.test(Numero);
    if( Numero == "" || bueno == false ){
        alert("Numero no ingresado")
        hasError = true
        return false;
    }

    let Nombre= document.getElementById("Nombre").value;
    if( Nombre == "")
    {
        alert("Nombre no ingresado");
        hasError = true;
        return false;
    }
    let fecha = document.getElementById("Fecha").value;
    if(fecha == "") { 
        alert("Ingrese fecha de vencimiento")
        hasError = true;
        return false;
    }
    let CVV = document.getElementById("CVV").value;
    if(CVV.length < 3){
        alert("CVV no ingresado")
        hasError = true;
        return false;
    }
    
    document.location.href="plantas.html";
    }
