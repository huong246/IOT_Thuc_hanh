import pika
import datetime


def callback(ch, method, properties, body):
    now = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"Da nhan message: {body.decode()}")
    print(f"Thoi gian nhan: {now}")


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='iot_lab_queue')
    channel.basic_consume(queue='iot_lab_queue', on_message_callback=callback, auto_ack=True)

    print(' [*] Đang chờ message. Nhấn CTRL+C để thoát.')
    channel.start_consuming()


if __name__ == '__main__':
    main()