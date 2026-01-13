from .sharpness import calculate_sharpness
from .brightness import calculate_brightness
from .contrast import calculate_contrast
from .noise import estimate_noise
from .colorfulness import calculate_colorfulness
from .transformer_iqa import TransformerIQA

# Initialize Transformer model once (Global singleton to avoid reloading)
# In a production app, this might be handled by dependency injection
transformer_iqa = TransformerIQA()

class QualityScorer:
    def _score_comfort_zone(self, value, min_val, max_val, optimal_min, optimal_max):
        """
        Calculate score based on a comfort zone (trapezoidal function).
        """
        if optimal_min <= value <= optimal_max:
            return 100.0
        elif value < min_val or value > max_val:
            return 0.0
        elif value < optimal_min:
            return ((value - min_val) / (optimal_min - min_val)) * 100.0
        else:
            return ((max_val - value) / (max_val - optimal_max)) * 100.0

    def analyze(self, image):
        # 1. Traditional CV Metrics
        sharpness = calculate_sharpness(image)
        brightness = calculate_brightness(image)
        contrast = calculate_contrast(image)
        noise = estimate_noise(image)
        colorfulness = calculate_colorfulness(image)
        
        # 2. Transformer AI Score
        ai_score = transformer_iqa.calculate_score(image)
        
        # --- Scoring Logic (Hybrid) ---
        
        # Traditional Scores
        raw_s_score = min(100, (sharpness / 300.0) * 100)
        b_score = self._score_comfort_zone(brightness, 40, 215, 90, 170)
        c_score = self._score_comfort_zone(contrast, 10, 120, 40, 90)
        n_score = max(0, 100 - (noise / 20.0) * 100)
        col_score = self._score_comfort_zone(colorfulness, 0, 150, 30, 90)
        
        # Penalty Logic
        if n_score < 60: 
            penalty_factor = 0.5 + (0.5 * (n_score / 60.0))
            raw_s_score *= penalty_factor
        s_score = raw_s_score

        # Calculate Traditional Weighted Score
        traditional_score = (s_score * 0.35) + \
                            (b_score * 0.20) + \
                            (c_score * 0.15) + \
                            (col_score * 0.20) + \
                            (n_score * 0.10)
                            
        # Final Hybrid Score
        # We give AI score a 60% weight to make it the most dominant factor
        # "Aesthetic Quality" (AI) > "Technical Quality" (CV)
        # If Transformer is not available (e.g. load failed), fall back to traditional only
        if transformer_iqa.is_available:
            final_score = (traditional_score * 0.4) + (ai_score * 0.6)
        else:
            final_score = traditional_score
        
        # Grading
        if final_score >= 85:
            grade = "Excellent"
        elif final_score >= 70:
            grade = "Good"
        elif final_score >= 50:
            grade = "Average"
        else:
            grade = "Poor"
            
        # Suggestions
        suggestions = []
        # AI Specific Suggestion
        if transformer_iqa.is_available and ai_score < 60:
            suggestions.append("AI 认为这张照片的构图或观感一般，建议调整拍摄角度。")
            
        if s_score < 60:
            if n_score < 50:
                suggestions.append("图像噪点较多，导致细节模糊。建议降低ISO或改善光线。")
            else:
                suggestions.append("主体不够清晰。建议拍摄时保持手稳，或检查对焦。")
        
        if b_score < 70:
            if brightness < 90:
                suggestions.append("画面整体偏暗。建议增加环境光或开启闪光灯。")
            else:
                suggestions.append("画面过曝，高光溢出。建议降低曝光补偿。")
            
        if col_score < 50:
            suggestions.append("色彩较为平淡。可以尝试捕捉色彩更丰富的场景。")
            
        if not suggestions:
            if final_score >= 90:
                suggestions.append("完美的杰作！技术指标与 AI 审美评分都极高。")
            else:
                suggestions.append("整体质量不错，看起来很舒服。")

        return {
            "metrics": {
                "sharpness": round(sharpness, 2),
                "brightness": round(brightness, 2),
                "contrast": round(contrast, 2),
                "noise": round(noise, 2),
                "colorfulness": round(colorfulness, 2),
                "ai_score": round(ai_score, 1)
            },
            "scores": {
                "sharpness_score": round(s_score, 1),
                "brightness_score": round(b_score, 1),
                "contrast_score": round(c_score, 1),
                "noise_score": round(n_score, 1),
                "colorfulness_score": round(col_score, 1),
                "ai_aesthetic_score": round(ai_score, 1)
            },
            "final_score": round(final_score, 1),
            "grade": grade,
            "suggestions": suggestions
        }
