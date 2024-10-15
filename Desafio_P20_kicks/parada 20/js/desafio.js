function verifica_valor(){

    let x = parseInt(document.getElementById("valor_1").value);
    let y = parseInt(document.getElementById("valor_2").value);
    let z = parseInt(document.getElementById("valor_3").value);

    let div = document.getElementById("resp");
    let text = "";

    let media = (x + y + z) / 3
    if(media >= 6){
        text = "Parabéns, voce foi aprovado com média superior ou igual a 6";
    }else{
        text = "Infelizmente voce foi reprovado com média abaixo de 6!";
    }
    div.innerHTML = text;
}