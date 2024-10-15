var div = document.getElementById("resp");

function calculadora(){

    let val_01 = parseFloat(document.getElementById("val_01").value);
    let Fahrenheit;
    let Kelvin;
    Fahrenheit_Kelvin = `<p>Fahrenheit <br> (${val_01} x 1,8) + 32 = ${(val_01*1.8)+32} °F  <br>Kelvin <br> ${val_01} + 273,15 = ${val_01+273,15} K </p>`;
    div.innerHTML = Fahrenheit_Kelvin;
}