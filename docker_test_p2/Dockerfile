# ===========================
# Dockerfile para ROS2 Jazzy
# Proyecto: ros2_ws (sensor_program)
# ===========================

# 1. Imagen base
FROM osrf/ros:jazzy-desktop

# 2. Instalar dependencias básicas de ROS y utilidades
RUN apt update && apt upgrade -y && \
    apt install -y python3-colcon-common-extensions python3-pip nano

# 3. Definir variables de entorno ROS
ENV ROS_DISTRO=jazzy
ENV ROS_WS=/ros2_ws

# 4. Crear el workspace
WORKDIR $ROS_WS/src

# 5. Copiar el paquete desde el host al contenedor
# Asegúrate de que tu carpeta sensor_program está junto al Dockerfile
COPY sensor_program/ ./sensor_program/

# 6. Compilar el workspace
WORKDIR $ROS_WS
SHELL ["/bin/bash", "-c"]
RUN source /opt/ros/$ROS_DISTRO/setup.bash && \
    colcon build

# 7. Configurar el entorno para que quede “sourced” automáticamente
RUN echo "source /opt/ros/$ROS_DISTRO/setup.bash" >> ~/.bashrc && \
    echo "source $ROS_WS/install/setup.bash" >> ~/.bashrc

# 8. Verificación automática al construir
RUN /bin/bash -c "source /opt/ros/$ROS_DISTRO/setup.bash && \
    source $ROS_WS/install/setup.bash && \
    ros2 pkg list | grep sensor_program"

# 9. Establecer el directorio de trabajo final
WORKDIR $ROS_WS

# 10. Comando por defecto
CMD ["bash"]
