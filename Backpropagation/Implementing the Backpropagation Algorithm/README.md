Error at Output Layer

محاسبه خطا در خروجی

At the output layer, the first step in Backpropagation is to compute the error — the difference between the predicted value $$y^$$ and the true label 

در لایه خروجی، اولین قدم در پراپگیشن به عقب، محاسبه خطا یا تفاوت بین مقدار پیش‌بینی شده y^​ و مقدار واقعی y است:

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

$$\sigma'\big(z^{(l)}\big)$$

   is derivative of activation at layer ll.

This formula recursively distributes the error backward.

