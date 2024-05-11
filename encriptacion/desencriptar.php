<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Desencriptador César</title>
</head>
<body>
    <form method="post">
        <label for="mensaje_encriptado">Ingrese el mensaje encriptado:</label><br>
        <input type="text" id="mensaje_encriptado" name="mensaje_encriptado"><br>
        <label for="desplazamiento">Ingrese el desplazamiento utilizado:</label><br>
        <input type="number" id="desplazamiento" name="desplazamiento"><br><br>
        <input type="submit" value="Desencriptar">
    </form>

    <?php
    function descifrarCesar($mensajeEncriptado, $desplazamiento) {
        $resultado = '';

        // Recorremos cada carácter del mensaje encriptado
        for ($i = 0; $i < strlen($mensajeEncriptado); $i++) {
            // Obtenemos el código ASCII del carácter actual
            $codigoAscii = ord($mensajeEncriptado[$i]);
            
            // Aplicamos el desplazamiento inverso al código ASCII para descifrar
            $nuevoCodigoAscii = $codigoAscii - $desplazamiento;

            // Verificamos si el carácter es una letra mayúscula
            if (ctype_upper($mensajeEncriptado[$i])) {
                // Aseguramos que el nuevo código ASCII esté dentro del rango de letras mayúsculas
                while ($nuevoCodigoAscii < ord('A')) {
                    $nuevoCodigoAscii += 26; // El alfabeto tiene 26 letras
                }
            }
            // Verificamos si el carácter es una letra minúscula
            elseif (ctype_lower($mensajeEncriptado[$i])) {
                // Aseguramos que el nuevo código ASCII esté dentro del rango de letras minúsculas
                while ($nuevoCodigoAscii < ord('a')) {
                    $nuevoCodigoAscii += 26; // El alfabeto tiene 26 letras
                }
            }
            // Concatenamos el carácter desencriptado al resultado
            $resultado .= chr($nuevoCodigoAscii);
        }

        return $resultado;
    }

    // Verificar si se ha enviado el formulario
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        // Obtener el mensaje encriptado y el desplazamiento desde el formulario
        $mensajeEncriptado = $_POST["mensaje_encriptado"];
        $desplazamiento = (int)$_POST["desplazamiento"];

        // Descifrar el mensaje encriptado
        $mensajeDesencriptado = descifrarCesar($mensajeEncriptado, $desplazamiento);
        echo "<br>Mensaje desencriptado: $mensajeDesencriptado";
    }
    ?>
</body>
</html>