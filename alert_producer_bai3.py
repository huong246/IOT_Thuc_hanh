import pika
import time


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Tạo direct exchange[cite: 1]
    channel.exchange_declare(exchange='iot_alert_exchange', exchange_type='direct')

    # Danh sách các cảnh báo[cite: 1]
    alerts = [
        ('info', 'He thong dang hoat dong binh thuong'),
        ('warning', 'Nhiet do phong may vuot nguong warning'),
        ('critical', 'Cam bien kho lanh mat ket noi critical')
    ]

    for routing_key, message in alerts:
        channel.basic_publish(exchange='iot_alert_exchange', routing_key=routing_key, body=message)
        print(f" [x] Đã gửi [{routing_key}]: '{message}'")
        time.sleep(1)

    connection.close()


if __name__ == '__main__':
    main()