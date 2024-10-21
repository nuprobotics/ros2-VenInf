import rclpy
from std_msgs.msg import String
from rclpy.node import Node

class Sender(Node):
    def __init__ (self) :
        super (Sender,self).__init__("node")
        timer_period = 0.5
        self.declare_parameter("topic_name", "")
        self.topic_name = self.get_parameter("topic_name").get_parameter_value().string_value 
        self.declare_parameter("text", "Hello, ROS2!")
        self.text = self.get_parameter("text").get_parameter_value().string_value
        self.publisher = self.create_publisher(String, self.topic_name, 1)
        self.timer = self.create_timer(timer_period, self.timer_callback)
    
    def timer_callback(self):
        msg = String()
        msg.data = self.text
        self.publisher.publish(msg)



def main():
    rclpy.init()
    node = Sender()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == " __main__ ":
    main()

