# Car + WebRTC + GPS

Este repositorio incluye el código utilizado en el video: "Manejé un carro a 3000 kilómetros de distancia utilizando la red celular".

# Raspberry Pi

La carpeta de raspberry_pi contiene 3 sub-carpetas:

1) control: La cual contiene el código referente a mover los motores del robot.

2) gps: La cual contiene el código referente al GPS del robot.

3) video_streaming: La cual contiene el código para initializar el video streaming del robot.

# Server

La carpeta de server contiene 2 sub-carpetas:

1) car_control_gps: La cual contiene un websocket server que es utilizado como un relay para mandar comandos del browser al servidor central y este al robot. Además escucha por nuevas coordenadas de GPS del robot y se las manda a la webapp para actualizar el mapa con la posición actual del robot.

2) webapp: La cual contiene la web app para que el piloto pueda ver el video streaming del carro y el mapa con la posición actual del robot.
