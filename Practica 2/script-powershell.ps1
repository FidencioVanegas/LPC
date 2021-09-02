#---------------------------funcion---------------------------#
function tabla-mul{
    #--------------------------ciclo--------------------------#
    for($i = 1; $i -lt 11; $i++){
        Write-Host $i 'x' $num '=' ($i*$num)
    }
}
Write-Host "`ntabla de multiplicar de numeros positivos"
#--------------------------variable----------------------------#
[int]$num = [int](Read-Host -Prompt "Escribe un numero: ")
#------------------------------if------------------------------#
if($num -ge 0){
    tabla-mul($num)
}
else{
    Write-Host "El numero es negativo"
}


