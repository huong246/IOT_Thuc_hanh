import pika
import json


def callback(ch, method, properties, body):
    data = json.loads(body)

    print(f"Device: {data['device_id']}")
    print(f"Temperature: {data['temperature']}")
    print(f"Humidity: {data['humidity']}")

    if data['temperature'] > 35:
        print("CANH BAO: Nhiet do cao")
    if data['humidity'] < 40:
        print("CANH BAO: Do am thap")
    print("-" * 20)


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='sensor_data_queue')
    channel.basic_consume(queue='sensor_data_queue', on_message_callback=callback, auto_ack=True)

    print(' [*] Đang chờ dữ liệu cảm biến. Nhấn CTRL+C để thoát.')
    channel.start_consuming()


if __name__ == '__main__':
    main()