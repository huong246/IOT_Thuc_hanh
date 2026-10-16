import pika
import json
import time
import random


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='sensor_data_queue')
    print(" [*] Bắt đầu gửi dữ liệu cảm biến. Nhấn CTRL+C để thoát.")

    try:
        while True:
            data = {
                "device_id": "sensor01",
                "temperature": round(random.uniform(20.0, 45.0), 1),
                "humidity": round(random.uniform(30.0, 80.0), 1)
            }
            message = json.dumps(data)

            channel.basic_publish(exchange='', routing_key='sensor_data_queue', body=message)
            print(f" [x] Đã gửi: {message}")

            time.sleep(3)
    except KeyboardInterrupt:
        print("\nĐã dừng gửi dữ liệu.")
    finally:
        connection.close()


if __name__ == '__main__':
    main()