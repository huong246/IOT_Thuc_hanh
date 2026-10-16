import pika


def callback(ch, method, properties, body):
    print(f"[critical_queue] Da nhan: {body.decode()}")


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='iot_alert_exchange', exchange_type='direct')

    channel.queue_declare(queue='critical_queue')
    # Bind queue với routing key 'critical'[cite: 1]
    channel.queue_bind(exchange='iot_alert_exchange', queue='critical_queue', routing_key='critical')

    channel.basic_consume(queue='critical_queue', on_message_callback=callback, auto_ack=True)
    print(' [*] Chờ cảnh báo mức CRITICAL. Nhấn CTRL+C để thoát.')
    channel.start_consuming()


if __name__ == '__main__':
    main()