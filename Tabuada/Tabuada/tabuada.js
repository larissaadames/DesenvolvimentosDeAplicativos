function tabuada(){
    var numero = parseInt(document.getElementById("numero").value);
    var resposta = document.getElementById("resposta");
    var tabuada= "";

    for(var contador=1; contador<=10 ; contador++)
        tabuada += numero + "x" + contador + "=" + numero * contador + "<br>";
        resposta.innerHTML = tabuada;
}