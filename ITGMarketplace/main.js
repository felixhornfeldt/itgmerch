function calculate() {
    var myAntal = document.getElementById ("antal").value;
    var result = document.getElementById ("result");
    var myResult = 80 * myAntal;
    result.value = myResult  + "kr.";
}

function calculate1() {
    var myAntal = document.getElementById ("antal1").value;
    var result = document.getElementById ("result1");
    var myResult = 180 * myAntal;
    result.value = myResult + "kr.";
}

// For hesret.html

/*function calculate() {
    var price = document.getElementById ("price");
    var myAntal = document.getElementById ("antal").value;
    var result = document.getElementById ("result");
    var myResult = price * myAntal;
    result.value = myResult  + "kr.";
}*/



