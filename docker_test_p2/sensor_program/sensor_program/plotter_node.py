import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import matplotlib.pyplot as plt
import time

class PlotterNode(Node):
    def __init__(self):
        super().__init__('plotter_node')
        self.subscription = self.create_subscription(
            String,
            'sensor_data',
            self.plot_callback,
            10
        )
        self.data = []

    def plot_callback(self, msg):
        # Extraemos el valor numérico del mensaje
        try:
            temp_str = msg.data.split(":")[1].strip().replace("C", "")
            temp_value = float(temp_str)
            self.data.append(temp_value)
            self.get_logger().info(f"Recibido: {temp_value} °C")
        except Exception as e:
            self.get_logger().error(f"Error al procesar el mensaje: {e}")

def main(args=None):
    rclpy.init(args=args)
    node = PlotterNode()

    try:
        while rclpy.ok():
            rclpy.spin_once(node, timeout_sec=5.0)
            if node.data:
                plt.figure(figsize=(6,4))
                plt.plot(node.data, marker='o')
                plt.title('Temperatura del sensor')
                plt.xlabel('Mediciones')
                plt.ylabel('Temperatura (°C)')
                plt.grid(True)
                plt.tight_layout()
                plt.savefig('/ros2_ws/data/sensor_plot.png')
                plt.close()
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

