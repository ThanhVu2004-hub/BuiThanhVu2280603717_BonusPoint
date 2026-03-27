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

# GIAO DIỆN PREMIUM DARK DASHBOARD
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DevOps Dashboard - {{ name }}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root { --bg: #0f172a; --card-bg: #1e293b; --accent: #38bdf8; --text-main: #f1f5f9; }
        body { background-color: var(--bg); color: var(--text-main); font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; overflow-x: hidden; }
        .glass-card { background: var(--card-bg); border: 1px solid rgba(255,255,255,0.1); border-radius: 20px; backdrop-filter: blur(10px); transition: transform 0.3s ease; }
        .glass-card:hover { transform: translateY(-5px); border-color: var(--accent); }
        .status-pulse { width: 12px; height: 12px; border-radius: 50%; display: inline-block; margin-right: 8px; position: relative; }
        .pulse-green { background: #22c55e; box-shadow: 0 0 10px #22c55e; animation: pulse 2s infinite; }
        .pulse-red { background: #ef4444; box-shadow: 0 0 10px #ef4444; }
        @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.4; } 100% { opacity: 1; } }
        .hero-title { background: linear-gradient(to right, #38bdf8, #818cf8); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 800; letter-spacing: -1px; }
        .info-label { color: #94a3b8; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 1px; }
    </style>
</head>
<body>
    <div class="container py-5">
        <div class="text-center mb-5">
            <h1 class="hero-title display-4 mb-2">DevOps Control Panel</h1>
            <p class="text-secondary">Quản lý và Giám sát Container Real-time</p>
        </div>

        <div class="row g-4 justify-content-center">
            <div class="col-lg-6">
                <div class="glass-card p-4 h-100">
                    <div class="d-flex justify-content-between align-items-center mb-4">
                        <h5 class="mb-0"><i class="fas fa-user-circle me-2 text-info"></i>Thông tin Sinh viên</h5>
                        <span class="badge bg-primary rounded-pill">Version 2.0</span>
                    </div>
                    <div class="row mt-3">
                        <div class="col-6">
                            <p class="info-label mb-1">Họ và Tên</p>
                            <h5 class="fw-bold">{{ name }}</h5>
                        </div>
                        <div class="col-6 text-end">
                            <p class="info-label mb-1">Mã số Sinh viên</p>
                            <h5 class="fw-bold text-accent">{{ mssv }}</h5>
                        </div>
                    </div>
                    <hr class="my-4 opacity-10">
                    <div class="d-flex align-items-center p-3 rounded-4 bg-dark bg-opacity-25 border border-secondary border-opacity-25">
                        <div class="flex-shrink-0">
                            <div class="status-pulse {% if 'thành công' in status %}pulse-green{% else %}pulse-red{% endif %}"></div>
                        </div>
                        <div class="flex-grow-1 ms-2 small">
                            <strong>Trạng thái DB:</strong> <span class="text-secondary">{{ status }}</span>
                        </div>
                    </div>
                </div>
            </div>

            <div class="col-lg-4">
                <div class="glass-card p-4 h-100">
                    <h5 class="mb-4"><i class="fas fa-code me-2 text-warning"></i>API Endpoint</h5>
                    <div class="mb-3">
                        <p class="info-label mb-2">POST Request</p>
                        <div class="bg-black bg-opacity-50 p-3 rounded-3 family-monospace small text-accent">
                            <code>/update</code>
                        </div>
                    </div>
                    <p class="small text-secondary mt-3">
                        Gửi dữ liệu JSON qua Postman để cập nhật thông tin hệ thống ngay lập tức.
                    </p>
                    <button class="btn btn-outline-info w-100 btn-sm mt-2 rounded-pill">Copy Endpoint</button>
                </div>
            </div>
        </div>

        <div class="text-center mt-5">
            <p class="small text-secondary">
                <i class="fab fa-github me-1"></i> Deployed by <strong>GitHub Actions</strong> 
                <span class="mx-2">|</span>
                <i class="fab fa-docker me-1"></i> Powered by <strong>Docker Desktop</strong>
            </p>
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
        db_status = "Đã kết nối cơ sở dữ liệu"
        conn.close()
    except Exception as e:
        db_status = f"Lỗi: {str(e)[:45]}..."

    return render_template_string(HTML_TEMPLATE, name=name, mssv=mssv, status=db_status)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)