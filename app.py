from flask import Flask, request, jsonify, render_template_string
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST', 'db_server'),
        database=os.getenv('DB_NAME', 'my_database'),
        user=os.getenv('DB_USER', 'user_admin'),
        password=os.getenv('DB_PASS', 'password123')
    )
    return conn

# Giao diện HTML được viết trực tiếp vào đây với Bootstrap 5
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Docker Assignment - {{ name }}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Inter', sans-serif; background-color: #f8f9fa; }
        .main-card { max-width: 600px; margin: 80px auto; border: none; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); }
        .status-badge { font-size: 0.9rem; padding: 8px 15px; border-radius: 20px; }
        .header-bg { background: linear-gradient(135deg, #0d6efd, #0b5ed7); color: white; border-radius: 15px 15px 0 0; padding: 30px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="card main-card">
            <div class="header-bg text-center">
                <h2 class="mb-0">DOCKER ASSIGNMENT</h2>
            </div>
            <div class="card-body p-4">
                <div class="mb-4">
                    <label class="text-muted small text-uppercase fw-bold">Sinh viên thực hiện</label>
                    <h3 class="text-dark fw-bold">{{ name }}</h3>
                    <p class="text-muted">MSSV: {{ mssv }}</p>
                </div>

                <div class="mb-4">
                    <label class="text-muted small text-uppercase fw-bold">Trạng thái hệ thống</label>
                    <div class="mt-2">
                        {% if "thành công" in status %}
                            <span class="status-badge bg-success-subtle text-success fw-bold border border-success">● {{ status }}</span>
                        {% else %}
                            <span class="status-badge bg-danger-subtle text-danger fw-bold border border-danger">● {{ status }}</span>
                        {% endif %}
                    </div>
                </div>

                <div class="p-3 bg-light rounded-3 border">
                    <p class="mb-0 small text-secondary">
                        <strong>Hướng dẫn:</strong> Sử dụng Postman để gửi <code>POST</code> đến 
                        <span class="badge bg-dark">/update</span> để cập nhật thông tin.
                    </p>
                </div>
            </div>
            <div class="card-footer text-center bg-white border-0 pb-4">
                <small class="text-muted">© 2026 - {{ name }} | Deployed with GitHub Actions</small>
            </div>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def hello():
    name = "Bùi Thanh Vũ" 
    mssv = "2280603717"
    
    try:
        conn = get_db_connection()
        db_status = "Kết nối CSDL thành công!"
        conn.close()
    except Exception as e:
        db_status = f"Lỗi kết nối CSDL: {str(e)[:50]}..."

    return render_template_string(HTML_TEMPLATE, name=name, mssv=mssv, status=db_status)

@app.route('/update', methods=['POST'])
def update_info():
    data = request.json
    new_name = data.get('name', 'N/A')
    return jsonify({
        "status": "success",
        "message": "Cập nhật thông tin thành công (Simulated)",
        "new_name": new_name
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)