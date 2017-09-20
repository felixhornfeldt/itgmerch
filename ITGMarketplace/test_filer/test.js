function calculate() {
    var myAntal = document.getElementById ("quantity").value;
    var result = document.getElementById ("total-price");
    var myResult = 80 * myAntal;
    result.value = myResult + '.00';
}

function remove(){
	document.getElementById("section1").style.display="none";
}

function show() {
	document.getElementById('section1').style.display="block";
}

