history.pushState(null, null, location.href);
window.onpopstate = function(event) {
    history.go(1);
};



function removeBack(){
    history.pushState(null, null, '');
    window.addEventListener('popstate', function () {
        //тут какие то другие действия пишем если надо 
        history.pushState(null, null, '');
    });
    };

function gen_password(len){
    var password = "";
    var symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!№;%:?*()_+=";
    for (var i = 0; i < len; i++){
        password += symbols.charAt(Math.floor(Math.random() * symbols.length));     
    }
    return password;
}

function tocatalog() {

    var check = $("input:first").val()
    if(document.getElementById("nickid") ){
       if (document.getElementById("nickid").value != "" &&
            document.getElementById("emailid").value.indexOf('@') != -1 && document.getElementById("emailid").value.indexOf('.') != -1 &&
            document.getElementById("passid").value.length >= 8 && document.getElementById("passid").value == document.getElementById("passconid").value) {

		
      	    window.location.replace('check2.html');
		
    }
       }
        

    else {
       
        if(document.getElementById("emailid") == null){
           window.location.replace('katalogis_face.html');
           }
        if (document.getElementById("emailid").value.indexOf('@') != -1 && document.getElementById("emailid").value.indexOf('.') != -1 &&
        document.getElementById("passid").value.length >= 8) {


        window.location.replace('katalogis.html');

    }
       

}
}
function kf(){
    window.location.replace('katalogis_face.html');
}

function kk(){
    window.location.replace('katalogis.html');
}

function tovideo() {

    var check = $("input:first").val()
    if (document.getElementById("emailid").value.indexOf('@') != -1 && document.getElementById("emailid").value.indexOf('.') != -1 &&
        document.getElementById("passid").value.length >= 8 && document.getElementById("passid").value == document.getElementById("passconid").value) {
        
        
        window.location.replace('check.html')
    }
}

function qr_for_next(){
    window.location.replace('qr_for_next.html')
}

function qr_for_info(){
    window.location.replace('qr_for_info.html')
}
function qr_for_next(){
    window.location.replace('qr_for_next.html')
}

function toQr_check(){
    window.location.replace('check2.html');
}

function Qr(){
    window.location.replace('QR.html');
    }

function face(){
    window.location.replace('info_face_by_wall.html')
}

function min_18_katalog(){
    window.location.replace('min18.html');
}