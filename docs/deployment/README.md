# 部署文档

## 系统要求
- Python 3.8+
- Django 5.1+
- PostgreSQL 12+
- Redis 6.0+ (可选,用于缓存)

## 安装步骤

### 1. 准备环境

```bash
创建项目目录
mkdir -p /opt/django/CloudManagementPlatformApi
cd /opt/django/CloudManagementPlatformApi
创建虚拟环境
python -m venv venv
source venv/bin/activate # Linux
或
.\venv\Scripts\activate # Windows
```

### 2. 安装依赖
```bash
pip install -r requirements/base.txt # 基础环境
pip install -r requirements/production.txt # 生产环境额外依赖
```

### 3. 配置环境变量
创建 .env 文件:
```bash
Django配置
DJANGO_SETTINGS_MODULE=config.settings.production
DJANGO_SECRET_KEY=your-secret-key
DJANGO_ALLOWED_HOSTS=example.com,www.example.com
数据库配置
DATABASE_URL=postgres://user:password@localhost:5432/dbname
邮件配置
EMAIL_HOST=smtp.example.com
EMAIL_HOST_USER=your-email@example.com
EMAIL_HOST_PASSWORD=your-password
云平台配置
ALIYUN_ACCESS_KEY=your-key
ALIYUN_ACCESS_SECRET=your-secret
```

### 4. 数据库配置
```sql
CREATE DATABASE cloud_management;
CREATE USER cloud_user WITH PASSWORD 'your-password';
GRANT ALL PRIVILEGES ON DATABASE cloud_management TO cloud_user;
```

### 5. 初始化数据库
```bash
python manage.py migrate
python manage.py createsuperuser

### 6. 收集静态文件
bash
python manage.py collectstatic

### 7. 配置Nginx
```nginx
server {
    listen 80;
    server_name example.com;
    location /static/ {
    alias /opt/django/CloudManagementPlatformApi/staticfiles/;
    }
    location /media/ {
    alias /opt/django/CloudManagementPlatformApi/media/;
    }
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### 8. 配置Gunicorn
创建 gunicorn.conf.py:

```python
bind = '127.0.0.1:8000'
workers = 3
timeout = 120
```

### 9. 配置Supervisor
创建 /etc/supervisor/conf.d/cloud_management.conf:
```ini
[program:cloud_management]
command=/opt/django/CloudManagementPlatformApi/venv/bin/gunicorn config.wsgi:application -c gunicorn.conf.py
directory=/opt/django/CloudManagementPlatformApi
user=www-data
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=/var/log/supervisor/cloud_management.log
```

### 10. 启动服务
supervisorctl reread
supervisorctl update
supervisorctl start cloud_management


启动Nginx
```bash
sudo service nginx restart
```

## 监控和维护
- 使用 Prometheus + Grafana 监控系统性能
- 配置日志轮转
- 定期备份数据库