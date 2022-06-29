function Iniciar (){
let Nombre= document.getElementById("Nombre").value;

    if( Nombre == "")
    {
        alert("Nombre no ingresado");
        hasError = true;
        return false;
    }  
    if(Nombre == 'admin'){
        document.location.href="Articulosadmin.html";
    }
    let Contraseña = document.getElementById("Contraseña").value;
    if ( Contraseña == "" ){
        alert("Ingrese contraseña");
        hasError = true;
        return false;
    } 
    document.location.href="plantas.html";
}