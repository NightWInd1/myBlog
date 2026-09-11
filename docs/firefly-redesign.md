# 晚风博客 · Firefly 风格改版

本次参考 [Firefly](https://github.com/CuteLeaf/Firefly) 的横幅、圆角卡片、双侧栏和主题自定义设计，以 Vue 组件重新实现。继续使用 Django + DRF + SQLite 和原有后台，无需迁移内容或数据库。

## 页面与交互

- 首页：山湖横幅、作者卡片、公告、分类快捷入口、置顶文章、最近更新和真实站点统计。
- 文章列表：列表/网格布局、置顶/时间排序、URL 分页、加载占位、错误重试和空状态。
- `/categories`：分类总览，支持父子分类；`/category/:slug`：分类文章列表，保留原有 tech/life 等路径。
- `/archives`：按年展示全部已发布文章。
- 搜索：Ctrl/Cmd + K 打开原生模态对话框，Esc 关闭，支持键盘焦点管理。
- 阅读页：正文 HTML 清理、H2/H3 自动目录、图片、代码与表格排版、评论及阅读时长。
- 关于页、404 页面、手机导航和滚动回顶。
- 浅色/深色/跟随系统、主题色滑块及列表布局保存在 localStorage。

## 结构与配置

`frontend/src/App.vue` 统一挂载头部、横幅、双侧栏、页脚，页面只负责内容。

- `config/site.js`：站名、个人资料、社交链接、公告、横幅、技能、默认主题色。
- `composables/useAppearance.js`：主题和布局偏好。
- `composables/useSite.js`：共享站点数据。
- `components/PostCollection.vue`：列表、分类和搜索共用的数据加载、取消过期请求、排序和分页。
- `components/PostCard.vue`：共用文章卡片和封面兜底。
- `style.css`：统一设计变量、组件样式及响应式断点。

桌面使用双侧栏，1150px 以下隐藏右栏，720px 以下采用单列内容及折叠菜单。尊重系统减少动态效果设置。

## API 调整

- 新增 `GET /api/stats/`：真实文章、分类、评论数量与最近更新时间。
- 新增 `GET /api/archives/`：归档文章与月份统计。
- 新增 `GET /feed/`：真实 RSS XML，替代原来的 SPA 回退。
- 分类接口返回所有根分类（包含没有子分类的分类），递归 `children` 和已发布文章 `post_count`。
- 父分类查询包含任意层级后代；列表默认置顶优先，支持 `ordering=latest`，同时间以 ID 稳定排序。
- 文章增加 `category_slug`、`reading_minutes`，摘要以纯文本返回，空摘要从正文提取。
- 最新文章按创建时间排序；评论与统计只包含公开文章的数据。
- 正文继续支持原有 HTML/纯文本内容，不要求改写为 Markdown。阅读时长按每分钟约 400 字估算。

## 本地开发

环境要求：Python 3.12+、Node 22.12+（本次验证使用 Python 3.12、Node 24）。原仓库中的 venv 来自 Linux，macOS 应重新创建虚拟环境。

```sh
python3.12 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python manage.py runserver 127.0.0.1:8000
```

另一个终端：

```sh
cd frontend
npm ci
npm run dev
```

访问 http://localhost:3000/。开发模式 Vite base 为 `/`，API、后台及 RSS 转发到本机 8000。生产构建 base 保持 `/static/`，构建输出仍为根目录 `static/`，兼容现有 Django/Nginx 部署。

```sh
cd frontend
npm run build
# 在服务器部署代码和构建结果后：
systemctl restart django-myblog
```

没有模型变更，不需要新数据库迁移。`package-lock.json` 的下载地址由腾讯云内网镜像替换为公共 npm registry，版本完整性校验保留。新增 DOMPurify 负责正文 HTML 清理。

## 验证

- `npm run build`：生产构建。
- `python manage.py test blog`：7 项接口回归测试，覆盖多级分类、排序、分页、搜索、摘要、公开数据边界和 RSS。
- 浏览器：桌面及 390px 手机视口，浅色/深色、列表/网格、主题色持久化、导航、搜索、分类、归档、关于及文章切换。
- 原有 django-ckeditor 4.22.1 组件仍会输出上游维护与安全警告；本次改版没有更换后台编辑器。

## 设计与素材来源

布局灵感：[CuteLeaf/Firefly](https://github.com/CuteLeaf/Firefly)，页脚保留设计来源链接。Vue 实现为本项目重新编写，未复制 Firefly 的源码或游戏角色素材。

横幅为本地山湖照片 `frontend/src/assets/landscape.jpg`，来源：
https://images.unsplash.com/photo-1470770841072-f978cf4d019e?auto=format&fit=crop&w=1920&q=80

图片来源平台：[Unsplash](https://unsplash.com/license)。不会在每次访问时请求远程横幅。头像与叶片 favicon 为本项目的 SVG 图形，可直接编辑。没有使用 AI 生成图片。
