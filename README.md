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

<p>Para poder controlar el dispositivo de forma remota podemos utilizar algún servicio de DDNS. En este caso, hemos utilizado   NO-IP, siguiendo las indicaciones del enlace: https://www.realdroid.es/2016/10/29/configurar-no-ip-para-raspberry-pi-y-de-paso-que-es-no-ip/
</p>

<h3>Automatización</h3>
<p> Para que se inicialice automáticamente la lectura de datos, crearemos un script que lance automáticamente la aplicación. Para ello, ejecutamos el siguiente comando. Esto nos crea un documento en la ruta /etc/init.d/ llamado "gps-ini"
<pre><code>sudo nano /etc/init.d/gps-init</code></pre>
</p>
<cite>hols</cite>

<h3>Curiosidades</h3>
<p>El dispositivo está pensado para instalarlo en un vehículo perteneciente a una flota, por lo que, para identificarlo más facilmente se asigna la matrícula del vehículo como hostname de la Raspberry Pi. 
<pre></code>sudo nano /etc/hostname</code></pre>
</p>

