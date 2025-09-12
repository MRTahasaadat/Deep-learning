1) Introduction to Optimization

1) مقدمه‌ای بر بهینه‌سازی در شبکه‌های عصبی 

هدفِ یادگیری، کمینه‌کردن تابع هزینه/خطا `J(θ)` است؛ که `θ` مجموعه‌ی وزن‌ها و بایاس‌هاست.  
برای یک مسئله‌ی نظارت‌شده:

$$
\frac{1}{N} \sum_{i=1}^{N} L\big(f(x_i; \theta), \; y_i\big)
$$

چالش اصلی: منظرِ خطا (Loss Landscape) غیرکوژ (non‑convex) است → مینیمم‌های محلی، نواحی تخت (plateaus)، زین‌نقطه‌ها (saddles) و درّه‌های باریک (ravines).

ابزار اصلی: گرادیان `∇θJ(θ)` که جهتِ بیشترین افزایش را نشان می‌دهد؛  
پس جهتِ نزول `-∇` است.  

سه پارامتر ذهنی مهم:

- نرخ یادگیری `η`: قدمِ حرکت روی سطح خطا؛  
 خیلی بزرگ → جهش و ناپایداری  
  خیلی کوچک → همگرایی کند  

- مقیاس‌گذاری ویژگی‌ها (Normalization / Standardization): بهبود هندسه‌ی منظر و سرعت همگرایی.  

- تصادفی‌بودن (Batching / Noise): نویز گرادیان گاهی کمک می‌کند از زین‌نقطه‌ها فرار کنیم.


2) Basic Gradient Descent

2) گرادیان‌نزولی پایه (Batch/Vanilla GD)


فرمول اصلی | Core update:




$$\theta_{t+1} = \theta_t - \eta \nabla_{\theta} J(\theta_t)$$



Batch GD یعنی گرادیان را روی کل داده محاسبه می‌کنیم (پرهزینه ولی دقیق). برای رگرسیون مربعی با خروجی:

$$\hat{y} = f(x; \theta)$$

$$J(\theta) = \frac{1}{2N} \sum_{i=1}^{N} \big(\hat{y}^{\,i} - y^i \big)^2$$

$$\nabla_{\theta} J = \frac{1}{N} \sum_{i=1}^{N} \big(\hat{y}^{\,i} - y^i \big) \, \frac{\partial \hat{y}^{\,i}}{\partial \theta}$$

نکات عملی | Practical notes

Feature scaling (StandardScaler) تقریباً همیشه کمک می‌کند.

Schedule نرخ یادگیری (مثلاً ExponentialDecay) می‌تواند همگرایی را بهبود دهد.
افزودن L2 (Weight Decay) گرادیان را به سمت کوچک‌کردن وزن‌ها بایاس می‌کند:

$$J_{\text{reg}} = J + \frac{\lambda}{2} \, \lVert \theta \rVert_2^2$$

$$J_{\text{reg}} \;=\; J \;+\; \frac{\lambda}{2} \, \lVert \theta \rVert_2^2$$


2.1) پیاده‌سازی از صفر با NumPy (رگرسیون خطی تک‌ویژگی)
