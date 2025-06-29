###    مقدمه‌ای بر مفهوم Backpropagation


Backpropagation is the core learning algorithm used to train neural networks.
It allows the model to update its internal parameters (weights and biases) by computing the gradient of a loss function with respect to those parameters.
These gradients are used by optimization algorithms like Gradient Descent to minimize the loss function over training


پراپگیشن به عقب (Backpropagation) هسته‌ی اصلی فرایند یادگیری در شبکه‌های عصبی است.
این الگوریتم با محاسبه گرادیان تابع خطا نسبت به پارامترهای مدل (وزن‌ها و بایاس‌ها)،
به شبکه اجازه می‌دهد وزن‌های خود را به گونه‌ای به‌روزرسانی کند که مقدار خطا کاهش یابد. این گرادیان‌ها در الگوریتم‌هایی مثل گرادیان نزولی (Gradient Descent) برای مینیمم‌سازی خطا به کار می‌روند.


قانون زنجیره‌ای (Chain Rule) در شبکه‌های چندلایه

In a multilayer neural network, the loss depends on weights across several layers. Therefore,
to update each layer’s weights, we need the derivative of the loss with respect to those weights. This is where the chain rule of calculus is used.

در شبکه‌های عصبی چندلایه، تابع خطا (Loss) به وزن‌های چندین لایه وابسته است. بنابراین برای اینکه وزن‌های هر لایه به درستی به‌روزرسانی شوند، باید مشتق تابع خطا نسبت به آن وزن‌ها را داشته باشیم. اینجا دقیقاً جایی‌ست که قانون زنجیره‌ای مشتق‌گیری وارد عمل می‌شود.
Let’s consider:

 final loss :

   $$ LL $$

a linear operation:

   $$z = w \cdot x + b$$


activation: 

   $$a = \sigma(z)$$
    

Then:    
    
$$\frac{d w}{d L} = \frac{d a}{d L} \cdot \frac{d z}{d a} \cdot \frac{d w}{d z}$$

  
  مشتق‌گیری از توابع فعال‌سازی معروف


<table>
  <thead>
    <tr>
      <th>تابع</th>
      <th>تعریف ریاضی</th>
      <th>مشتق</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Sigmoid</strong></td>
      <td><code>\sigma(x) = \frac{1}{1 + e^{-x}}</code></td>
      <td><code>\sigma'(x) = \sigma(x)(1 - \sigma(x))</code></td>
    </tr>
    <tr>
      <td><strong>Tanh</strong></td>
      <td><code>\tanh(x) = \frac{e^{x} - e^{-x}}{e^{x} + e^{-x}}</code></td>
      <td><code>1 - \tanh^2(x)</code></td>
    </tr>
    <tr>
      <td><strong>ReLU</strong></td>
      <td><code>f(x) = \max(0, x)</code></td>
      <td><code>f'(x) = \begin{cases} 1 & x > 0 \\ 0 & x \leq 0 \end{cases}</code></td>
    </tr>
    <tr>
      <td><strong>Leaky ReLU</strong></td>
      <td><code>f(x) = \max(\alpha x, x)</code></td>
      <td><code>f'(x) = \begin{cases} 1 & x > 0 \\ \alpha & x \leq 0 \end{cases}</code></td>
    </tr>
    <tr>
      <td><strong>Softmax</strong></td>
      <td><code>\text{softmax}(x_i) = \frac{e^{x_i}}{\sum_j e^{x_j}}</code></td>
      <td>Complex (Jacobian matrix) – often combined with CrossEntropy</td>
    </tr>
  </tbody>
</table>


فرمول Backpropagation برای لایه Dense

فرض کنید داریم یک لایه با وزن$$WW$$و بایاس $$bb$$:
$$z = W \cdot x + b, \quad a = \sigma(z), \quad \hat{y} = a, \quad L = \text{loss}(\hat{y}, y)$$

گام‌های محاسبه گرادیان:

   مشتق تابع خطا نسبت به خروجی لایه:
   $$\frac{\partial L}{\partial \hat{y}} \quad \text{و} \quad \frac{\partial \hat{y}}{\partial L}$$

   
   ضرب در مشتق تابع فعال‌سازی:
  $$\delta = \frac{\partial L}{\partial \hat{y}} \cdot \sigma'(z)$$

   
   مشتق نسبت به وزن:
   $$\frac{\partial L}{\partial W} = \delta \cdot x^T$$

   مشتق نسبت به بایاس:
$$\frac{\partial L}{\partial b} = \delta$$


 مقدار گرادیان برای لایه قبلی:
$$\delta_{\text{prev}} = W^T \cdot \delta$$



