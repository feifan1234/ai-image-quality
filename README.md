<div align="center">

# 📸 AI 图像质量检测与自动分类系统
### AI-based Image Quality Assessment and Classification System

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109.0-009688?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.9.0-5C3EE8?style=for-the-badge&logo=opencv)](https://opencv.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

<p align="center">
  <strong>一键分析图像质量 • 智能评分与分级 • 专业的优化建议</strong>
</p>

[查看演示](#-演示) • [快速开始](#-快速开始) • [API 文档](#-api-接口说明)

</div>

---

## 📖 项目简介

**AI 图像质量检测系统** 是一款基于计算机视觉技术的自动化分析工具。它能够深入分析用户上传的每一张图片，从**清晰度、亮度、对比度、噪声**四个核心维度进行量化评估，并基于综合算法给出最终的质量评分与等级。

无论是摄影爱好者筛选照片，还是开发者需要自动化筛选高质量素材，本系统都能提供强有力的支持。

## ✨ 核心功能

| 功能模块 | 描述 |
| :--- | :--- |
| 🔍 **多维深度分析** | 自动计算 **清晰度** (Laplacian Variance)、**亮度** (HSV Value)、**对比度** (RMS) 和 **噪声水平**。 |
| 📊 **智能评分系统** | 将复杂的数学指标归一化为 **0-100** 的直观分数，让质量一目了然。 |
| 🏆 **自动分级分类** | 自动将图像划分为 `Excellent` (优秀), `Good` (良好), `Average` (一般), `Poor` (较差)。 |
| 💡 **智能优化建议** | "太暗了？" "有点模糊？" —— 系统会自动分析短板并给出针对性的改进建议。 |
| 🖥️ **现代化 UI** | 简洁美观的 Web 界面，支持**拖拽上传**、**实时预览**和**可视化图表展示**。 |

## 🛠️ 技术架构

本系统采用前后端分离架构，确保高性能与可扩展性。

*   **Frontend**: HTML5, CSS3 (Modern UI), Vanilla JavaScript
*   **Backend**: Python FastAPI (高性能异步框架)
*   **Core AI**: OpenCV (计算机视觉库), NumPy (科学计算)

## 📂 项目目录结构

```text
image_quality_system/
├── 🐍 backend/                # 后端核心服务
│   ├── 🧠 analyzer/           # 图像分析算法模块
│   │   ├── sharpness.py       # 清晰度检测算法
│   │   ├── brightness.py      # 亮度分析算法
│   │   ├── contrast.py        # 对比度分析算法
│   │   └── noise.py           # 噪声评估算法
│   ├── 🛠️ utils/              # 通用工具库
│   └── ⚡ main.py              # FastAPI 启动入口
│
├── 🎨 frontend/               # 前端用户界面
│   └── index.html             # 单页应用入口
│
└── 📄 requirements.txt        # 项目依赖清单
```

## 🚀 快速开始

只需几步，即可在本地运行完整的系统。

### 1. 环境准备
确保您的环境已安装 Python 3.8+。

### 2. 安装依赖
```bash
pip install -r requirements.txt
```

### 3. 启动后端
进入后端目录并启动 FastAPI 服务：
```bash
cd backend
python main.py
```
> 服务将在 `http://localhost:8000` 启动。

### 4. 访问前端
直接在浏览器中打开 `frontend/index.html` 文件即可体验。
*推荐使用简单的 HTTP Server 以获得最佳体验：*
```bash
# 在项目根目录下运行
python -m http.server 3000 -d frontend
```
访问：`http://localhost:3000`

## 📝 API 接口说明

系统提供标准的 RESTful API。

### POST `/analyze`

上传图像文件进行质量分析。

**请求参数**: `file` (Multipart/form-data)

**响应示例**:

```json
{
  "metrics": {
    "sharpness": 120.5,
    "brightness": 130.2,
    "contrast": 45.3,
    "noise": 5.2
  },
  "scores": {
    "sharpness_score": 80.0,
    "brightness_score": 95.0,
    "contrast_score": 70.0,
    "noise_score": 88.0
  },
  "final_score": 85.5,
  "grade": "Excellent",
  "suggestions": [
    "图像质量非常棒！"
  ]
}
```

---

<div align="center">
  <p>Made with ❤️ by Finks</p>
</div>
