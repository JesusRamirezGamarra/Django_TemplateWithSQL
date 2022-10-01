
let numero0 = document.getElementById("numero0");
let numero1 = document.getElementById("numero1");
let numero2 = document.getElementById("numero2");
let numero3 = document.getElementById("numero3");
let numero4 = document.getElementById("numero4");
let numero5 = document.getElementById("numero5");
let numero6 = document.getElementById("numero6");
let numero7 = document.getElementById("numero7");
let numero8 = document.getElementById("numero8");
let numero9 = document.getElementById("numero9");
let punto = document.getElementById("punto");
let borrar = document.getElementById("borrar");
let menos = document.getElementById("menos");
let mas = document.getElementById("mas");
let muttiplicar = document.getElementById("muttiplicar");
let dividir = document.getElementById("dividir");
let porcentaje = document.getElementById("porcentaje");
let AC = document.getElementById("AC");
let masmenos = document.getElementById("masmenos");
let igual = document.getElementById("igual");
let input = document.getElementById("input").value;
let numeroa="";
let numerob="";
let operador="";
let resultado="";

numero1.addEventListener("click",()=>{
    operador==""?numeroa+="1":numerob+="1";
    input = document.getElementById("input").value+="1";
})
numero2.addEventListener("click",()=>{
    operador==""?numeroa+="2":numerob+="2";
    input = document.getElementById("input").value+="2";
})
numero3.addEventListener("click",()=>{
    operador==""?numeroa+="3":numerob+="3";
    input = document.getElementById("input").value+="3";
})
numero4.addEventListener("click",()=>{
    operador==""?numeroa+="4":numerob+="4";
    input = document.getElementById("input").value+="4";
})
numero5.addEventListener("click",()=>{
    operador==""?numeroa+="5":numerob+="5";
    input = document.getElementById("input").value+="5";
})
numero6.addEventListener("click",()=>{
    operador==""?numeroa+="6":numerob+="6";
    input = document.getElementById("input").value+="6";
})
numero7.addEventListener("click",()=>{
    operador==""?numeroa+="7":numerob+="7";
    input = document.getElementById("input").value+="7";
})
numero8.addEventListener("click",()=>{
    operador==""?numeroa+="8":numerob+="8";
    input = document.getElementById("input").value+="8";
})
numero9.addEventListener("click",()=>{
    operador==""?numeroa+="9":numerob+="9";
    input = document.getElementById("input").value+="9";
})
numero0.addEventListener("click",()=>{
    operador==""?numeroa+="0":numerob+="0";
    input = document.getElementById("input").value+="0";
})

punto.addEventListener("click",()=>{
    operador==""?numeroa+=".":numerob+=".";
    input = document.getElementById("input").value+=".";
})

mas.addEventListener("click",()=>{
    operador="+";
    input = document.getElementById("input").value+="+";
})
menos.addEventListener("click",()=>{
    operador="-";
    input = document.getElementById("input").value+="-";
})

muttiplicar.addEventListener("click",()=>{
    operador="*";
    input = document.getElementById("input").value+="*";
})
dividir.addEventListener("click",()=>{
    operador="/";
    input = document.getElementById("input").value+="/";
})




igual.addEventListener("click",()=>{
    switch(operador)
    {
        case '+':
            resultado=parseFloat(numeroa)+parseFloat(numerob) ;
            break
        case '-':
            resultado=parseFloat(numeroa)-parseFloat(numerob) ;
            break
        case '*':
            resultado=parseFloat(numeroa)*parseFloat(numerob) ;
            break   
        case '/':
            resultado=parseFloat(numeroa)/parseFloat(numerob) ;
            break                                                       
        case '%':
            resultado=parseFloat(numeroa)/100 ;
            break
        case '+/-':
            resultado=parseFloat(numeroa)*-1 ;
            break  
        case 'rand':
            resultado= Math.random();
            break                                                                                                              
    }
    numeroDecimales =0 ;
    numeroDecimales = (resultado % 1 == 0) ? numeroDecimales : 4;
    
    input = document.getElementById("input").value=resultado.toFixed(numeroDecimales); 
    numeroa=resultado.toFixed(numeroDecimales); 
    numerob="";
    operador="";
    resultado="";
    
})
rand.addEventListener("click",()=>{
    operador="rand";
    igual.click();
})
porcentaje.addEventListener("click",()=>{
    operador="%";
    igual.click();
})
masmenos.addEventListener("click",()=>{
    operador="+/-";
    igual.click();
})



borrar.addEventListener("click",()=>{
    input = document.getElementById("input").value="";
    numeroa="";
    numerob="";
    operador="";
    resultado="";
}
)


function showVal(newVal){
    document.getElementById("valBox").innerHTML=` donation : ${newVal} PEN` ;
}