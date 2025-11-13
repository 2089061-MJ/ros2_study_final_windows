# teleop_turtlesim_rosbridge.py
import roslibpy
import keyboard
import time

# ROSBridge
ROS_HOST = '192.168.112.128'  
ROS_PORT = 9090

# ROSBridge 연결
client = roslibpy.Ros(host=ROS_HOST, port=ROS_PORT)
client.run()
print("ROSBridge 서버에 연결됨")

# cmd_vel 퍼블리셔
publisher = roslibpy.Topic(client, '/turtle1/cmd_vel', 'geometry_msgs/Twist')

linear_speed = 2.0   # Turtlesim용 속도
angular_speed = 2.0  # Turtlesim용 속도

try:
    print("Turtlesim 키보드 제어 시작! (↑↓←→), q로 종료")
    while True:
        twist = {
            'linear': {'x': 0.0, 'y': 0.0, 'z': 0.0},
            'angular': {'x': 0.0, 'y': 0.0, 'z': 0.0}
        }

        if keyboard.is_pressed('up'):
            twist['linear']['x'] = linear_speed
        elif keyboard.is_pressed('down'):
            twist['linear']['x'] = -linear_speed
        elif keyboard.is_pressed('left'):
            twist['angular']['z'] = angular_speed
        elif keyboard.is_pressed('right'):
            twist['angular']['z'] = -angular_speed
            
        elif keyboard.is_pressed('w'):
            twist['linear']['x'] = linear_speed
        
        elif keyboard.is_pressed('s'):
            twist['linear']['x'] = -linear_speed
            
        elif keyboard.is_pressed('a'):
            twist['angular']['z'] = angular_speed
            
        elif keyboard.is_pressed('d'):
            twist['angular']['z'] = -angular_speed
            
        elif keyboard.is_pressed('q'):
            print("종료")
            break
        else:
            # 아무 키도 안 눌리면 정지
            twist['linear']['x'] = 0.0
            twist['angular']['z'] = 0.0

        # 퍼블리시
        publisher.publish(twist)

        # 루프 주기 (속도 제한)
        time.sleep(0.05)

finally:
    publisher.unadvertise()
    client.terminate()
    print("종료 완료")
