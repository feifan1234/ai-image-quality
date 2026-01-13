为了引入 **Transformer** 模型进行深度学习图像质量评估，我建议采用 **CLIP-IQA** 方案。

### 为什么选择 CLIP-IQA？
CLIP (Contrastive Language-Image Pre-Training) 是 OpenAI 推出的基于 **Transformer (ViT)** 架构的多模态模型。通过计算图像与“高质量照片” vs “低质量照片”文本描述的匹配度，可以非常准确地模拟人类的审美判断。这比单纯的 OpenCV 算法更懂“意境”和“构图”。

### 实施计划

#### 1. 引入深度学习依赖
我们需要安装 PyTorch 和 Hugging Face Transformers 库。
*   更新 `requirements.txt`：增加 `torch`, `transformers`, `pillow`。

#### 2. 构建 Transformer 分析核心
创建新模块 `backend/analyzer/transformer_iqa.py`：
*   **模型**：加载 `openai/clip-vit-base-patch32` (基于 Vision Transformer)。
*   **原理**：将图像输入模型，同时输入一组正负向提示词（如 "Good photo", "Bad photo"）。
*   **计算**：计算图像与正向提示词的余弦相似度，将其转化为 **0-100** 的“AI 美学评分”。

#### 3. 融合传统与现代算法
修改 `backend/analyzer/scorer.py`：
*   在现有的 OpenCV 指标（清晰度、亮度等）基础上，加入 **Transformer Score**。
*   调整综合评分公式，让深度学习评分占据一定权重（例如 30%），使最终分数既有技术指标的严谨，又有人工智能的审美。

#### 4. 前端可视化升级
修改 `frontend/index.html`：
*   新增一个醒目的 **"AI 深度学习评分 (Transformer)"** 仪表盘或进度条，展示这个由神经网络计算出的“高级感”分数。
