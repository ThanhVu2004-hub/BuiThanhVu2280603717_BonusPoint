from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

# Cấu hình kết nối Database từ biến môi trường (Docker Compose sẽ truyền vào)
def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST', 'db_server'),
        database=os.getenv('DB_NAME', 'my_database'),
        user=os.getenv('DB_USER', 'user_admin'),
        password=os.getenv('DB_PASS', 'password123')
    )
    return conn

@app.route('/')
def hello():
    name = "Bùi Thanh Vũ" 
    mssv = "2280603717"
    
    db_status = "Chưa kết nối"
    try:
        conn = get_db_connection()
        db_status = "Kết nối CSDL thành công!"
        conn.close()
    except Exception as e:
        db_status = f"Lỗi kết nối CSDL: {e}"

    return f"""
        <h1>Bài tập Docker của: {name} - {mssv}</h1>
        <p><b>Trạng thái:</b> {db_status}</p>
        <hr>
        <p>Để chỉnh sửa thông tin, hãy dùng Postman gửi POST đến <code>/update</code></p>
    """

# YÊU CẦU: Chỉnh sửa thông tin cá nhân
@app.route('/update', methods=['POST'])
def update_info():
    data = request.json
    new_name = data.get('name', 'N/A')
    # Ở đây bạn có thể viết thêm lệnh SQL UPDATE vào Database
    return jsonify({
        "message": "Cập nhật thông tin thành công (Giả lập)",
        "new_name": new_name
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)