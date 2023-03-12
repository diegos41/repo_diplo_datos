# Si no estamos en un entorno Linux podemos definir nuestra propia wget
# Esta función nos ayuda a descargar archivos desde la web, no es necesaria para archivos locales
# No es necesario entender cómo funciona, se las mostramos sólo por si alguno llega a necesitarla

# Importamos la libreria requests (luego veremos qué es una librería)
import requests

def wget(url):
    r = requests.get(url, allow_redirects=True)
    with open(url[url.rfind('/') + 1::], 'wb') as f:
        f.write(r.content)

wget("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Introductorio_Datos/noticia.txt")



#En realidad se puede descargar para Windows con Chocolatey y en MacOS con brew. O también puede descargarse una versión binaria.
# Otra forma rápida y válida para todo OS es usar la librería wget de Python.


