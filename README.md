# GPS Y RASPBERRY PI

Creación de una aplicación para la lectura de datos gps utilizando una raspberry pi 3, con un módulo GPS <a href="https://www.dx.com/p/gy-neo6mv2-flight-controller-gps-module-blue-232595#.W_P0_ej7SUk" target="_blank">GY-NEO-6Mv2</a>

<h3>Requerimientos</h3>
<ul>
  <li> Python 2.7</li>
  <li> Es necesario la instalación de la librería <a href= "https://github.com/Knio/pynmea2">pynmea2</a>:
  <pre><code>pip install pynmea2</code></pre></li> 
</ul>

<h3>Pasos a seguir</h3>
<p> En primer lugar, procederemos a clonar el proyecto en la carpeta /home/pi/GPS
</p>

<p> Una vez realizado esto, deberemos acceder al archivo de configuración de la raspberry y deberemos habilitar puerto serie y deshabiltar el acceso serial por consola</p>

<p>Para poder controlar el dispositivo de forma remota podemos utilizar algún servicio de DDNS. En este caso, hemos utilizado   NO-IP, siguiendo las indicaciones del enlace: <a href="https://www.realdroid.es/2016/10/29/configurar-no-ip-para-raspberry-pi-y-de-paso-que-es-no-ip/" target="_blank">Configurar No-Ip</a>
</p>

<h3>Automatización</h3>
<p> Para que se inicialice automáticamente la lectura de datos, crearemos un script que lance automáticamente la aplicación. Para ello, ejecutamos el siguiente comando. Esto nos crea un documento en la ruta /etc/init.d/ llamado "gps-ini"
<pre><code>sudo nano /etc/init.d/gps-init</code></pre>
</p>
<p> Dentro del archivo copiamos el siguiente código:
  <pre><code>
  #! /bin/sh
  # /etc/init.d/detector-init
  <br/>
  ### BEGIN INIT INFO
  # Provides:----------gps-init
  # Required-Start:----$all
  # Required-Stop:      $remote_fs $syslog
  # Default-Start:         2 3 4 5
  # Default-Stop:         0 1 6
  # Short-Description: Inicio automático GPS
  # Description:            Script para arrancar el lector de gps
  ### END INIT INFO
  <br/>
  # Dependiendo de los parámetros que se le pasen al programa se usa una opción u otra
  case "$1" in
   start)
     echo "Arrancando gps-init"
  # Aquí hay que poner el programa que quieras arrancar automáticamente
     sh /home/pi/GPS/iniciar_gps.sh
     ;;
   stop)
     echo "Deteniendo gps-init"
  <br/>
     ;;
   *)
     echo "Modo de uso: /etc/init.d/gps-init {start|stop}"
     exit 1
     ;;
  esac
  <br/>
  exit 0
</code></pre>
</p> 

<p>El dispositivo está pensado para instalarlo en un vehículo perteneciente a una flota, por lo que, para identificarlo más facilmente se asigna la matrícula del vehículo como hostname de la Raspberry Pi. 
<pre></code>sudo nano /etc/hostname</code></pre>
</p>

