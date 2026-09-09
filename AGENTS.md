# MyBlog 项目文档

基于 Django 6.0 + Vue 3 的个人博客系统。

## 技术栈

| 层 | 技术 |
|---|------|
| 后端框架 | Django 6.0.6 (Python 3.12) |
| API 框架 | Django REST Framework 3.17 |
| 前端框架 | Vue 3.5 + Vite 8 + vue-router 4 |
| 后台 UI | django-simpleui (2026.1.13) |
| 数据库 | SQLite (db.sqlite3) |
| 反向代理 | Nginx 1.24 + Let's Encrypt SSL |
| 部署 | systemd (Django + Nginx) |
| 服务器 | 腾讯云 CVM, 内网 10.0.0.11, 公网 101.43.37.151 |

## 域名与访问

| 项目 | 值 |
|------|-----|
| 域名 | bytefun.site |
| HTTPS | https://bytefun.site |
| 后台 | https://bytefun.site/admin/ |
| 安全组 | 需放行 TCP 80 和 443 |

## 目录结构

```
/opt/myBlog/
├── manage.py              # Django 管理入口
├── db.sqlite3             # SQLite 数据库
├── myblog/                # Django 项目配置
│   ├── settings.py        # 项目设置
│   ├── urls.py            # 根 URL 路由
│   └── wsgi.py
├── blog/                  # Django 博客应用
│   ├── models.py          # 数据模型 (Post/Category/Comment)
│   ├── views.py           # REST API 视图
│   ├── serializers.py     # DRF 序列化器
│   ├── urls.py            # API URL 路由
│   └── admin.py           # 后台注册
├── frontend/              # Vue 3 前端源码
│   ├── public/
│   │   └── favicon.svg    # 像素赛博朋克风 Logo
│   ├── src/
│   │   ├── api.js         # API 请求封装
│   │   ├── router/index.js # Vue Router 路由
│   │   ├── pages/         # 页面组件（见下）
│   │   ├── components/    # UI 组件（见下）
│   │   └── style.css      # 全局主题 CSS (light/dark)
│   ├── vite.config.js      # Vite 配置
│   └── package.json
├── static/                # Vue 构建输出 (也用作 Django STATICFILES_DIRS 和 TEMPLATES DIRS)
│   ├── index.html         # SPA 入口
│   └── assets/            # 打包后的 JS/CSS/images
└── venv/                  # Python 虚拟环境
```

## 前端页面

| 页面 | 路由 | 文件 |
|------|------|------|
| 首页 | `/` | `pages/Home.vue` |
| 技术笔记 | `/category/tech` | `pages/TechNotes.vue` |
| 生活随笔 | `/category/life` | `pages/LifeNotes.vue` |
| 关于我 | `/about` | `pages/About.vue` |
| 文章详情 | `/post/:slug` | `pages/PostDetail.vue` |
| 搜索结果 | `/search?q=关键词` | `pages/SearchResults.vue` |

## 前端组件

| 组件 | 文件 | 功能 |
|------|------|------|
| ParticleBg | `components/ParticleBg.vue` | Canvas 粒子背景，根据主题改变颜色 |
| Header | `components/Header.vue` | 顶部导航，搜索框(CtrlK)，明暗主题切换，响应式菜单 |
| Hero | `components/Hero.vue` | 轮播 Banner，代码窗口装饰，自动轮播 |
| PinnedPosts | `components/PinnedPosts.vue` | 置顶文章卡片，3列网格 |
| PostList | `components/PostList.vue` | 文章列表，图文混排，分页 |
| Sidebar | `components/Sidebar.vue` | 个人信息、最新评论、最新文章、RSS 订阅 |
| Footer | `components/Footer.vue` | 页脚版权信息 |
| BackToTop | `components/BackToTop.vue` | 返回顶部按钮 |

## 数据模型

| 模型 | 字段 | 说明 |
|------|------|------|
| Category | name, slug | 文章分类 |
| Post | title, slug, author, category, content, excerpt, cover_image, status(draft/published), is_pinned, created_at, updated_at | 博客文章 |
| Comment | post, author_name, email, content, created_at | 文章评论 |

排序规则：`['-is_pinned', '-created_at']`（置顶优先，同组按时间倒序）

## REST API 接口

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/api/posts/` | 文章列表（分页，支持 `?category=slug` 筛选） |
| GET | `/api/posts/pinned/` | 置顶文章（最多3篇） |
| GET | `/api/posts/latest/` | 最新文章（5篇） |
| GET | `/api/posts/search/?q=关键词` | 搜索文章（标题/摘要/正文模糊匹配） |
| GET | `/api/posts/:slug/` | 文章详情（含评论） |
| GET | `/api/comments/latest/` | 最新评论（5条） |

## 常用命令

### Django

```bash
# 激活虚拟环境
source /opt/myBlog/venv/bin/activate

# 运行 Django 开发服务器（手动方式）
python manage.py runserver 127.0.0.1:8000

# 运行迁移
python manage.py migrate

# 创建迁移
python manage.py makemigrations

# 创建超级用户
python manage.py createsuperuser

# Django shell
python manage.py shell
```

### systemd 服务管理

```bash
# Django 服务
systemctl status django-myblog
systemctl restart django-myblog
journalctl -u django-myblog -f

# Nginx 服务
systemctl status nginx
systemctl reload nginx
```

### Vue 前端

```bash
# 安装依赖（已安装无需重复）
cd /opt/myBlog/frontend && npm install

# 开发模式（热更新，监听 0.0.0.0:3000）
npm run dev

# 生产构建（输出到 ../static/）
npm run build
```

### SSL 证书管理

```bash
# 查看证书状态
certbot certificates

# 手动续签
certbot renew

# 测试续签（不实际执行）
certbot renew --dry-run
```

### 完整部署流程

```bash
cd /opt/myBlog/frontend && npm run build    # 构建前端
systemctl restart django-myblog             # 重启 Django
```

## 关键配置

### Django settings.py 要点

- `ALLOWED_HOSTS`: `['101.43.37.151', 'bytefun.site', 'localhost', '127.0.0.1']`
- `INSTALLED_APPS`: simpleui 必须在 django.contrib.admin 之前
- `LANGUAGE_CODE`: `zh-hans`（简体中文）
- `STATICFILES_DIRS`: `[BASE_DIR / 'static']` — 指向 Vue 构建输出
- `TEMPLATES DIRS`: `[BASE_DIR / 'static']` — 使 Django 能渲染 index.html
- `DEBUG`: `True`

### HTTPS/CSRF 设置

```python
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
CSRF_TRUSTED_ORIGINS = ['https://bytefun.site']
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

### Vite 配置要点

- `base: '/static/'` — **必须与 Django STATIC_URL 匹配**，否则生产环境资源 404
- `build.outDir: '../static'` — 构建到 Django 的 static 目录
- `server.proxy`: 开发时代理 `/api`, `/admin`, `/static/admin` 到 Django 8000

### Nginx 配置

- 监听 80 (HTTP → 跳转 HTTPS) 和 443 (HTTPS + SSL)
- 反向代理到 Django `127.0.0.1:8000`
- 传递 `X-Forwarded-Proto: $scheme` 使 Django 识别 HTTPS
- **不使用 `location /static/` 的 alias** — 静态文件统一由 Django 提供服务（simpleui 的 JS/CSS 在 venv site-packages 中，Nginx 无法直接找到）

### systemd 服务

- Django 绑定 `127.0.0.1:8000`（仅内网，不对外暴露）
- SSL 证书自动续签已由 certbot 配置

### Django URL 路由

- `/admin/` → Django 后台（simpleui 主题）
- `/api/` → REST API 接口
- 其他所有路径 → Vue SPA (index.html)，由前端 vue-router 接管

## 管理员账号

| 字段 | 值 |
|------|-----|
| 用户名 | nightwind |
| 密码 | Admin@123 |
| 邮箱 | 2163392313@qq.com |
| 昵称 | 晚风 |

后台地址: https://bytefun.site/admin/

## 注意事项

1. **前端构建后必须重启 Django**：systemd 不会自动检测 static 文件变化
2. **Vite base 路径**：必须为 `/static/`，与 Django `STATIC_URL='static/'` 一致
3. **ALLOWED_HOSTS**：变更域名或 IP 时需要更新
4. **安全组**：腾讯云安全组需放行 TCP 80 和 443 端口
5. **SSL 证书**：Let's Encrypt 90 天有效期，certbot 已配置自动续签
6. **静态文件**：不要用 Nginx alias 提供 `/static/`，必须由 Django 提供（simpleui 依赖）
7. **数据库迁移**：添加/修改模型后需运行 `makemigrations` + `migrate`
8. **开发模式**：使用 `npm run dev` 启动 Vite dev server (3000 端口)

## 编辑器配置

- 全局 CSS 主题变量定义在 `frontend/src/style.css`，支持 light/dark 双主题
- dark 主题通过 `[data-theme="dark"]` 选择器切换
- 主题持久化在 localStorage key `blog-theme`
- 字体: Inter (正文), JetBrains Mono (代码), Noto Sans SC (中文)
