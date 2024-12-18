# 开发文档

## 项目结构
```
CloudManagementPlatformApi/
├── api/ # API版本控制
│ └── v1/ # V1版本API
├── apps/ # Django应用
│ ├── customer/ # 客户管理
│ ├── cloud_server/ # 云服务器管理
│ └── domain/ # 域名管理
├── common/ # 通用工具
│ ├── utils/ # 工具函数
│ └── middleware/ # 中间件
├── config/ # 项目配置
│ ├── settings/ # 配置文件
│ └── urls.py # URL配置
├── docs/ # 文档
├── logs/ # 日志文件
├── static/ # 静态文件
├── tests/ # 测试用例
└── manage.py # Django管理脚本
```


## 开发规范

### 代码风格
- 遵循PEP 8规范
- 使用4个空格缩进
- 行长度限制在120字符以内
- 使用类型注解

### Git提交规范
- feat: 新功能
- fix: 修复bug
- docs: 文档更新
- style: 代码格式调整
- refactor: 重构代码
- test: 测试相关
- chore: 构建过程或辅助工具的变动


### API开发规范
- 使用RESTful风格
- 版本控制放在URL中
- 使用JWT进行认证
- 统一的响应格式

### 测试规范
- 单元测试覆盖核心业务逻辑
- 集成测试覆盖API接口
- 使用pytest进行测试
- 保持测试代码整洁

## 开发流程

### 1. 环境搭建
```bash
克隆项目
git clone <repository-url>
创建虚拟环境
python -m venv venv
source venv/bin/activate
安装依赖
pip install -r requirements/development.txt
```


### 2. 数据库迁移
```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. 运行测试
```bash
运行所有测试
python manage.py test
运行特定测试
python manage.py test tests.unit.test_cloud_providers
```

### 4. 本地开发
```bash
python manage.py runserver
```

### 5. API文档
- 使用Swagger/OpenAPI记录API
- 访问 `/api/docs/` 查看API文档

## 常见问题

### 1. 数据库迁移冲突
- 删除migrations文件夹
- 重新生成迁移文件
- 使用`--fake`参数

### 2. 定时任务调试
- 使用Django shell
- 手动触发任务
- 查看日志输出

### 3. 性能优化
- 使用Django Debug Toolbar
- 优化数据库查询
- 添加缓存层

## 部署检查清单
- [ ] 更新依赖
- [ ] 运行测试
- [ ] 检查配置文件
- [ ] 备份数据库
- [ ] 收集静态文件
- [ ] 更新文档