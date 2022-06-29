function Guardar (){
    let Producto= document.ElementById("Producto").value;
    if( Producto == "")
    {
        alert("Nombre Producto no ingresado");
        hasError = true;
        return false;
    }
    let Usuario= document.getElementById("Categoria").value;
    if( Categoria == "")
    {
        alert("Nombre Categoria no ingresado");
        hasError = true;
        return false;
    }
    let Valor= document.getElementById("Valor").value;
    if( Valor == "")
    {
        alert("Valor no ingresado");
        hasError = true;
        return false;
    }
    let Id= document.getElementById("Id").value;
    if( Id== "")
    {
        alert("Id no ingresado");
        hasError = true;
        return false;
    }
    let Codigo= document.getElementById("Codigo").value;
    if( Codigo == "")
    {
        alert("Codigo no ingresado");
        hasError = true;
        return false;
    }
    let Descripcion= document.getElementById("Descripcion").value;
    if( Descripcion == "")
    {
        alert("Descripcion no ingresada");
        hasError = true;
        return false;
    }
}   
