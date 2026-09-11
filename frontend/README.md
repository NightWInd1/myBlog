# 晚风的博客 · Vue 前端

参考 Firefly 设计的 Vue 3 + Vite 8 博客前端，数据来自 Django REST API。

```sh
npm ci
npm run dev
```

开发地址：http://localhost:3000/（需要同时在 8000 端口运行 Django）。

```sh
npm run build
```

生产资源输出到 `../static/`，URL 前缀 `/static/`。

外观、资料和横幅在 `src/config/site.js` 调整。完整架构与部署说明见根目录 `docs/firefly-redesign.md`。
