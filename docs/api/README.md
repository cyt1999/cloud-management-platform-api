# API 文档

## 认证
所有API请求需要在Header中携带JWT Token:

```bash
Authorization: Bearer <your_token>
```

## 认证接口
### 获取Token
- URL: `/api/login/`
- Method: `POST`
- Body:

```json
{
"username": "your_username",
"password": "your_password"
}
```

- Response:

```json
{
"access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
"refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

### 刷新Token
- URL: `/api/token/refresh/`
- Method: `POST`
- Body:

```json
{
"refresh": "your_refresh_token"
}
```

## API接口

### 客户管理
#### 获取客户列表
- URL: `/api/customers/`
- Method: `GET`
- Query Parameters:
  - `page`: 页码
  - `page_size`: 每页数量
- Response:

```json
{
    "count": 100,
    "next": "http://api.example.org/customers/?page=2",
    "previous": null,
    "results": [
        {
        "id": 1,
        "name": "客户A",
        "cloud_platform_type": "aliyun",
        "account": "account_a",
        "regions": ["cn-hangzhou"]
        }
    ]
}
```


#### 创建客户
- URL: `/api/customers/`
- Method: `POST`
- Body:
```json
{
    "name": "新客户",
    "cloud_platform_type": "aliyun",
    "account": "account_x",
    "access_key_id": "your_key",
    "access_key_secret": "your_secret",
    "regions": ["cn-hangzhou"]
}
```

### 云服务器管理
#### 获取服务器列表
- URL: `/api/cloud-servers/`
- Method: `GET`
- Query Parameters:
  - `page`: 页码
  - `page_size`: 每页数量
  - `customer`: 客户ID
  - `status`: 服务器状态

#### 获取即将到期服务器
- URL: `/api/cloud-servers/expiring-soon/`
- Method: `GET`
- Query Parameters:
  - `days`: 天数阈值(默认7天)

### 域名管理
#### 获取域名列表
- URL: `/api/domains/`
- Method: `GET`
- Query Parameters:
  - `page`: 页码
  - `page_size`: 每页数量
  - `customer`: 客户ID
  - `status`: 域名状态

#### 获取即将到期域名
- URL: `/api/domains/expiring-soon/`
- Method: `GET`
- Query Parameters:
  - `days`: 天数阈值(默认7天)

## 错误码说明
- 200: 请求成功
- 201: 创建成功
- 400: 请求参数错误
- 401: 未认证
- 403: 权限不足
- 404: 资源不存在
- 500: 服务器内部错误