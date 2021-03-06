# Car + WebRTC + GPS

Este repositorio incluye el código utilizado en el video: "Manejé un carro a 3000 kilómetros de distancia utilizando la red celular".

# Raspberry Pi

La carpeta de raspberry_pi contiene 3 sub-carpetas:

1) control: La cual contiene el código referente para mover los motores del robot.

2) gps: La cual contiene el código referente al GPS del robot.

3) video_streaming: La cual contiene el código para inicializar el video streaming del robot.

# Server

La carpeta de server contiene 2 sub-carpetas:

1) car_control_gps: La cual contiene un websocket server que es utilizado como un relay para mandar comandos del browser al servidor central y este al robot. Además escucha por nuevas coordenadas de GPS del robot y las envia a la web app para actualizar el mapa con la posición actual del robot.

2) webapp: La cual contiene la web app para que el piloto pueda ver el video streaming del carro y el mapa con la posición actual del robot.

# Notas

Para poder hacer funcionar el video streaming utilizando la tecnología de WebRTC, es necesario instalar Janus Gateway. Les dejo los tutoriales que utilicé para hacerlo funcionar en mi servidor de Ubuntu 18.04 LTS:

1) https://medium.com/good-robot/how-to-run-janus-on-a-google-cloud-compute-instance-and-build-your-own-webrtc-streaming-server-14144f9efb8
2) https://ourcodeworld.com/articles/read/1197/how-to-install-janus-gateway-in-ubuntu-server-18-04

Para poder hacer funcionar el video streaming desde la Raspberry Pi utilizando WebRTC, es necesario instalar UV4L. Les dejo los tutoriales que utilicé para hacerlo funcionar con mi Raspberry Pi 4:

1) https://www.linux-projects.org/uv4l/
2) https://www.linux-projects.org/uv4l/installation/
3) https://www.linux-projects.org/uv4l/tutorials/janus-gateway/

Parte del código que es utilizado para la comunicación de los motores y servos del robot fue obtenido del los tutoriales del kit de robótica:

1) https://github.com/Freenove/Freenove_4WD_Smart_Car_Kit_for_Raspberry_Pi
