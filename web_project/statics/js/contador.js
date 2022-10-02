window.onload = function() {
    setInterval(muestraReloj, 1000);
}
let timeLimit = 5

function muestraReloj() {

    if(timeLimit<=0 ){
        window.location.replace("../donar")
    }
    updateDisplay(timeLimit--);

}
function updateDisplay(val) {
    document.getElementById("counter-label").innerHTML = val;
}


