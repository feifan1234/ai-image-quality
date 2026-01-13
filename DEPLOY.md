# 🚀 部署指南 (Deployment Guide)

本指南将帮助您将 **AI 图像质量检测系统** 部署到云端，让所有人都能访问。

我们将使用 **Railway** 部署后端，使用 **Vercel** 部署前端。这两个平台都提供免费且易用的服务。

---

## 第一步：准备代码 (GitHub)

1.  **创建 GitHub 仓库**
    *   登录 [GitHub](https://github.com/)。
    *   创建一个新的空仓库 (例如 `ai-image-quality`)。

2.  **上传代码**
    在您的项目根目录 (`e:\Project\Photo_measure\image_quality_system`) 打开终端，执行以下命令：

    ```bash
    git init
    git add .
    git commit -m "Initial commit"
    git branch -M main
    git remote add origin https://github.com/YOUR_USERNAME/ai-image-quality.git
    git push -u origin main
    ```
    *(请将 `YOUR_USERNAME` 替换为您的 GitHub 用户名)*

---

## 第二步：部署后端 (Railway)

1.  **注册/登录 Railway**
    *   访问 [Railway.app](https://railway.app/) 并使用 GitHub 账号登录。

2.  **创建新项目**
    *   点击 **"New Project"** -> **"Deploy from GitHub repo"**。
    *   选择您刚才创建的 `ai-image-quality` 仓库。

3.  **配置服务**
    *   Railway 会自动检测到 `Procfile` 并开始构建。
    *   等待构建完成（Build 过程可能需要几分钟，因为要安装 PyTorch 等依赖）。

4.  **生成域名**
    *   部署成功后，点击项目卡片，进入 **"Settings"** -> **"Networking"**。
    *   点击 **"Generate Domain"**。
    *   复制生成的域名 (例如 `ai-image-quality-production.up.railway.app`)。
    *   **重要**：这是您的后端 API 地址，请记下来！

---

## 第三步：部署前端 (Vercel)

1.  **修改前端配置**
    *   打开本地代码中的 `frontend/index.html`。
    *   找到第 486 行左右的代码：
        ```javascript
        const API_BASE_URL = window.location.hostname === 'localhost' ...
            ? "http://localhost:8000"
            : "https://your-backend-url-here.up.railway.app"; // CHANGE THIS
        ```
    *   将 `"https://your-backend-url-here.up.railway.app"` 替换为您在第二步中获得的 **Railway 域名**（注意要加 `https://`）。
    *   保存文件，提交并推送到 GitHub：
        ```bash
        git add frontend/index.html
        git commit -m "Update API URL"
        git push
        ```

2.  **注册/登录 Vercel**
    *   访问 [Vercel.com](https://vercel.com/) 并使用 GitHub 账号登录。

3.  **导入项目**
    *   点击 **"Add New..."** -> **"Project"**。
    *   在 "Import Git Repository" 中选择您的 `ai-image-quality` 仓库。

4.  **配置构建设置**
    *   **Root Directory (根目录)**: 点击 Edit，选择 `frontend` 文件夹。这一步很重要！因为我们的网页在 frontend 子目录下。
    *   点击 **"Deploy"**。

5.  **完成！**
    *   等待几十秒，Vercel 会生成一个访问链接 (例如 `ai-image-quality.vercel.app`)。
    *   点击链接，您的网站就已经上线了！

---

## 常见问题 (FAQ)

*   **Q: 部署后上传图片报错 "Analysis failed"？**
    *   A: 检查 `frontend/index.html` 中的 `API_BASE_URL` 是否正确填写了 Railway 的域名。
    *   A: 检查 Railway 后端日志，看是否有报错。如果是 CORS 错误，可能需要在 `backend/main.py` 中更新 `allow_origins`。

*   **Q: Railway 构建失败？**
    *   A: 检查 `requirements.txt` 是否包含了 `opencv-python-headless` (而不是 `opencv-python`)。云服务器通常不支持带 GUI 的 OpenCV。

*   **Q: 分析速度很慢？**
    *   A: 免费版的云服务器 CPU 性能有限，且 Transformer 模型计算量大。这是正常现象。
