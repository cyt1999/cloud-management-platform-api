# Cloud Management Platform API

## 项目简介

Cloud Management Platform API 是一个基于 Django 的 RESTful API 项目，旨在管理云服务器、客户信息、域名等资源。该平台提供了用户注册、身份验证、资源管理等功能。

## 功能

- **用户注册和身份验证**：使用 JWT 进行用户身份验证。
- **客户管理**：管理客户的基本信息，包括名称、云平台类型、账号等。
- **云服务器管理**：管理云服务器的基本信息，包括实例名称、状态、IP 地址等。
- **域名管理**：管理域名的基本信息，包括域名名称、状态、注册时间等。
- **监控数据管理**：存储和管理云服务器的监控数据，包括 CPU 使用率、内存使用率等。
- **云平台数据同步**：使用 APScheduler 定时任务，每天自动同步云服务器和域名信息。

## 使用技术

- **Django**：作为 Web 框架。
- **Django REST Framework**：用于构建 RESTful API。
- **Simple JWT**：用于实现 JSON Web Token 身份验证。
- **APScheduler**：用于定时任务调度，实现云平台数据的自动同步。

## 目录结构

- **CloudManagementPlatformApi**：主项目目录，包含项目配置、URL 配置、调度器配置等。
- **CustomerApp**：客户管理应用，包含客户模型、序列化器、视图等。
- **CloudServerApp**：云服务器管理应用，包含云服务器模型、序列化器、视图、管理命令等。
- **DomainApp**：域名管理应用，包含域名模型、序列化器、视图等。
- **UserAuthApp**：用户认证应用，包含用户注册、序列化器、视图等。
- **cloud_providers**：云平台客户端模块，包含阿里云和火山引擎的客户端实现。

## 安装与运行

1. 克隆项目到本地：
   ```bash
   git clone <repository-url>
   ```

2. 进入项目目录并安装依赖：
   ```bash
   cd CloudManagementPlatformApi
   pip install -r requirements.txt
   ```

3. 运行数据库迁移：
   ```bash
   python manage.py migrate
   ```

4. 启动开发服务器：
   ```bash
   python manage.py runserver
   ```

5. 访问 `http://127.0.0.1:8000/` 查看 API。

## 贡献

欢迎提交问题和请求合并。请确保在提交请求前运行所有测试。