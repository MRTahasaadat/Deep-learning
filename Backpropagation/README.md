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

    LL: final loss

    z=w⋅x+bz=w⋅x+b: a linear operation

    a=σ(z)a=σ(z): activation

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
      <td>σ(x) = 1 / (1 + e<sup>−x</sup>)</td>
      <td>σ(x) × (1 − σ(x))</td>
    </tr>
    <tr>
      <td><strong>Tanh</strong></td>
      <td>tanh(x) = (e<sup>x</sup> − e<sup>−x</sup>) / (e<sup>x</sup> + e<sup>−x</sup>)</td>
      <td>1 − tanh(x)<sup>2</sup></td>
    </tr>
    <tr>
      <td><strong>ReLU</strong></td>
      <td>f(x) = max(0, x)</td>
      <td>
        f′(x) = 
        <span style="white-space: nowrap;">
          {
          1 if x &gt; 0,
          0 if x ≤ 0
          }
        </span>
      </td>
    </tr>
    <tr>
      <td><strong>Leaky ReLU</strong></td>
      <td>f(x) = max(αx, x)</td>
      <td>
        f′(x) = 
        <span style="white-space: nowrap;">
          {
          1 if x &gt; 0,
          α if x ≤ 0
          }
        </span>
      </td>
    </tr>
    <tr>
      <td><strong>Softmax</strong></td>
      <td>softmax(xᵢ) = e<sup>xᵢ</sup> / ∑ e<sup>xⱼ</sup></td>
      <td>Jacobian matrix – often combined with CrossEntropy</td>
    </tr>
  </tbody>
</table>
