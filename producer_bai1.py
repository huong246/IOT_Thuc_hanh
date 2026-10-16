import pika


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='iot_lab_queue')

    message = "Xin chao tu ung dung Python AMQP"
    channel.basic_publish(exchange='', routing_key='iot_lab_queue', body=message)
    print(f" [x] Đã gửi: '{message}'")

    connection.close()


if __name__ == '__main__':
    main()