<?php
if( isset( $_POST['my_button'] ) ){
    $backColor = 0xFFFF00;
    $foreColor = 0xFF00FF;

    // Создаем QR код в формате SVG
    QRcode::svg("45123456778sd7fds4fd65h4fds6ghg4", $_POST['nickid'], "Q", 4, 4, false, $backColor, $foreColor);
    
}
    


?>
