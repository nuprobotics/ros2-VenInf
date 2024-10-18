import rclpy
from std_msgs.msg import String
from rclpy.node import Node

class Receiver(Node):
    def __init__ (self) :
        super (Receiver,self).__init__("node")
        timer_period = 0.5
        self.subscriber = self.create_subscription(String, '/spgc/sender', self.subscriber_callback, qos_profile=10)

    def subscriber_callback(self,msg):
        self.get_logger().info(msg.data)



def main():
    rclpy.init()
    node = Receiver()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == " __main__ ":
    main()

