Error at Output Layer

محاسبه خطا در خروجی

At the output layer, the first step in Backpropagation is to compute the error — the difference between the predicted value y^ and the true label y.

در لایه خروجی، اولین قدم در پراپگیشن به عقب، محاسبه خطا یا تفاوت بین مقدار پیش‌بینی شدهy^​ و مقدار واقعی y است:

$$y$$

$$\text{Error} = \hat{y} - y$$

This error signal is what will be propagated backward through the network.

این سیگنال خطاست که به لایه‌های قبلی فرستاده می‌شود تا وزن‌ها به‌روزرسانی شوند.

 انتقال خطا به عقب: مشتقات لایه به لایه (Backward Pass)

 The essence of Backpropagation is to propagate this error backwards through the network, calculating gradients for each parameter.
For each layer ll, the error term δ(l)δ(l) is computed as:

اصل اصلی پراپگیشن به عقب این است که خطا را لایه به لایه به عقب منتقل کنیم و گرادیان هر وزن را محاسبه کنیم.
برای هر لایه ll، مقدار خطا یا سیگنال گرادیان به صورت زیر محاسبه می‌شود:

$$\delta^{(l)} = \left(W^{(l+1)}\right)^T \delta^{(l+1)} \odot \sigma'\big(z^{(l)}\big)$$


where

 $$\odot$$ is element-wise multiplication,

ضرب عنصر به عنصر است، $$\odot$$

$$\sigma'\big(z^{(l)}\big)$$

   is derivative of activation at layer $$l$$.

مشتق تابع فعال‌سازی لایه $$l$$ است.

This formula recursively distributes the error backward.

این معادله خطا را به صورت بازگشتی به عقب هدایت می‌کند.


Gradient checking is a method to verify the correctness of your backpropagation implementation. It compares the analytically computed gradient with a numerical approximation using finite differences.

Given a parameter θθ, approximate the derivative by:




Where ϵϵ is a very small number (e.g., 10−710−7).


بررسی درست بودن گرادیان با تست گرادیان (Gradient Checking)


Gradient checking is a method to verify the correctness of your backpropagation implementation. It compares the analytically computed gradient with a numerical approximation using finite differences.

Given a parameter $$θ$$, approximate the derivative by:


تست گرادیان یک روش برای صحت‌سنجی پیاده‌سازی Backpropagation است. در این روش، گرادیان محاسبه شده به صورت تحلیلی با گرادیان عددی که از مشتق محدود (finite difference) به دست می‌آید مقایسه می‌شود.

برای پارامتر θθ، مشتق عددی به صورت زیر محاسبه می‌شود:

$$\frac{\partial L}{\partial \theta} \approx \frac{L(\theta + \epsilon) - L(\theta - \epsilon)}{2\epsilon}$$


Where ϵϵ is a very small number (e.g., 10−710−7).

که ϵϵ یک عدد بسیار کوچک است (مثلاً 10−710−7).

If the numerical gradient is close to analytical gradient, your backpropagation is likely correct.

اگر مقدار عددی نزدیک به مقدار تحلیلی باشد، پیاده‌سازی شما درست است.

