import os

# 1. 设置 Hugging Face 镜像站点 (仅在本地开发且位于中国大陆时需要)
# 部署到海外云服务器 (如 Railway/Render) 时，建议注释掉下面这行，直接连接官方源更稳定
# os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"

# 2. 尝试清除系统代理设置 (解决 ProxyError 问题)
# 如果您的系统开启了全局代理，Python 有时无法正确连接，这里强制清除代理环境变量
os.environ.pop("HTTP_PROXY", None)
os.environ.pop("HTTPS_PROXY", None)
os.environ.pop("http_proxy", None)
os.environ.pop("https_proxy", None)

import torch
from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import numpy as np

class TransformerIQA:
    def __init__(self):
        # Initialize model and processor
        # We use a lightweight version of CLIP for efficiency
        # openai/clip-vit-base-patch32 is a good balance
        try:
            self.model_id = "openai/clip-vit-base-patch32"
            self.device = "cuda" if torch.cuda.is_available() else "cpu"
            print(f"Loading Transformer Model on {self.device}...")
            
            # Force download timeout and retries
            # Sometimes HF library hangs on download without timeout
            # We will use a local cache directory if possible
            
            print("  - Initializing CLIP model structure...")
            self.model = CLIPModel.from_pretrained(self.model_id).to(self.device)
            print("  - Initializing CLIP processor...")
            self.processor = CLIPProcessor.from_pretrained(self.model_id)
            
            # Define prompts for quality assessment
            self.prompts = ["a high quality photo", "a low quality photo"]
            print("Transformer Model Loaded Successfully.")
            self.is_available = True
        except Exception as e:
            print(f"Failed to load Transformer model: {e}")
            self.is_available = False

    def calculate_score(self, image_np: np.ndarray) -> float:
        """
        Calculate AI Aesthetic Score using CLIP.
        Returns a score between 0 and 100.
        """
        if not self.is_available:
            return 0.0

        try:
            # Convert numpy array (BGR) to PIL Image (RGB)
            # OpenCV uses BGR, PIL uses RGB
            image_rgb = image_np[..., ::-1] 
            pil_image = Image.fromarray(image_rgb)

            # Process inputs
            inputs = self.processor(
                text=self.prompts, 
                images=pil_image, 
                return_tensors="pt", 
                padding=True
            ).to(self.device)

            # Inference
            with torch.no_grad():
                outputs = self.model(**inputs)
                logits_per_image = outputs.logits_per_image # this is the image-text similarity score
                probs = logits_per_image.softmax(dim=1) # softmax to get probabilities

            # Get probability of "high quality photo" (index 0)
            high_quality_prob = probs[0][0].item()
            
            # Convert to 0-100 score
            return float(high_quality_prob * 100)

        except Exception as e:
            print(f"Error in Transformer IQA: {e}")
            return 0.0
