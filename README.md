# Báo cáo thực hành AMQP Python

## Broker sử dụng
Sử dụng RabbitMQ chạy trên localhost. Thư viện kết nối AMQP: `pika`.

## Cách chạy từng chương trình
Mở các terminal (hoặc command prompt) riêng biệt để chạy. Luôn chạy Consumer trước để đảm bảo queue được lắng nghe, sau đó mới chạy Producer.

- **Bài 1:**
  Terminal 1: `python consumer_bai1.py`
  Terminal 2: `python producer_bai1.py`
  
- **Bài 2:**
  Terminal 1: `python monitor_consumer_bai2.py`
  Terminal 2: `python sensor_producer_bai2.py`
  
- **Bài 3:**
  Terminal 1: `python warning_consumer_bai3.py`
  Terminal 2: `python critical_consumer_bai3.py`
  Terminal 3: `python alert_producer_bai3.py`

## Kết quả đạt được
- **Bài 1:** Thông báo chào mừng có chứa chuỗi được gửi vào broker và nhận thành công.
- **Bài 2:** Payload JSON được gửi tuần hoàn. Consumer phân tích đúng trường dữ liệu nhiệt độ và độ ẩm, hiển thị chính xác cảnh báo khi thông số nằm ngoài ngưỡng cho phép.
- **Bài 3:** Message sử dụng routing key 'warning' chỉ chuyển đến `warning_consumer_bai3.py` và message có key 'critical' chuyển đến `critical_consumer_bai3.py`, chứng minh việc phân luồng của direct exchange hoạt động tốt.