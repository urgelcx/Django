$(document).ready(function(){
    var accunt = document.getElementById("accunt")
    var accunterr = document.getElementById("accunterr")
    var checkerr = document.getElementById("checkerr")

    var pass = document.getElementById("pass")
    var passwd = document.getElementById("passwd")

    accunt.addEventListener("focus", function(){
        accunterr.style.display = "none"
        checkerr.style.display = "none"
    },false)
    accunt.addEventListener("blur", function(){
        instr = this.value
        if (instr.length < 6 || instr.length > 12){
            accunterr.style.display = "block"
            return
        }

        $.post("/checkuserid/", {"userid":instr}, function(data){
            if (data.status == "error"){
                checkerr.style.display = "block"
            }
        })
    },false)

})