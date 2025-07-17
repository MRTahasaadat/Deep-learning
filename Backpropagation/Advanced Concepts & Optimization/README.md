Underfitting & Overfitting 

Overfitting(بیش‌برازش):

The model fits the training data too well but fails to generalize on new or unseen data. High training accuracy but low testing accuracy.

مدل بیش از حد خودش را با داده‌های آموزشی تطبیق داده است و نمی‌تواند تعمیم خوبی روی داده‌های جدید یا دیده‌نشده داشته باشد. نشانه‌ی آن دقت بسیار بالا در داده آموزش و دقت پایین در تست است.

Underfitting(کم‌برازش):

The model is too simple and fails to capture the underlying patterns of the data. Low training and testing accuracy

مدل نتوانسته روابط بین ویژگی‌ها و برچسب‌ها را در داده‌های آموزش یاد بگیرد. در نتیجه، دقت در هر دو مجموعه آموزش و تست پایین است.

 روش‌های مقابله با Overfitting

1. Regularization (نرمال‌سازی):
   
L1 Regularization: $$\lambda \sum |w|$$


L2 Regularization: $$\lambda \sum w^2$$


2. Dropout:

Randomly deactivate neurons during training.

در هر تکرار آموزشی، برخی نورون‌ها را به طور تصادفی غیرفعال می‌کنیم تا از وابستگی زیاد به برخی مسیرها جلوگیری شود.

3. Early Stopping:

Stop training when validation error starts increasing.

   آموزش مدل را زمانی متوقف می‌کنیم که خطای مجموعه اعتبارسنجی شروع به افزایش کند.

4.Data Augmentation (افزایش داده):

Create synthetic training data using transformations like rotation, flipping, etc.

تکنیک‌هایی برای ساخت داده‌های مصنوعی (چرخش، برش، وارونه‌سازی تصویر و غیره).


 Initialization Strategies (استراتژی‌های مقداردهی اولیه وزن‌ها)

 Proper initialization is crucial to ensure gradients don’t vanish or explode.

 مقداردهی اولیه وزن‌ها اهمیت بسیار زیادی دارد چون اگر اشتباه انجام شود، مدل ممکن است یاد نگیرد یا دچار نوسان شدید شود.

 Popular Methods:

 انواع معروف:

 Zeros Initialization:

 All weights = 0 → symmetry problem

 همه وزن‌ها صفر = شکست کامل یادگیری (همه نورون‌ها یکسان رفتار می‌کنند)

 Random Initialization:

 Small random values, prone to instability

 انتخاب تصادفی مقادیر کوچک = قابل قبول، ولی ممکن است باعث گرادیان‌های ناپایدار شود.

 Xavier Initialization (Glorot):
 
Good for sigmoid/tanh

مناسب برای توابع فعال‌سازی مثل sigmoid و tanh

   $$W \sim \mathcal{N}\left(0, \frac{1}{n_{\text{in}}}\right)$$

            

He Initialization:

Designed for ReLU

مخصوص ReLU و مشتقات آن

   $$W \sim \mathcal{N}\left(0, \frac{1}{n_{\text{in}}}\right)$$


Gradient Vanishing / Exploding Problem

In deep networks, gradients during backpropagation may:

    Shrink too much → Vanishing gradient

    Grow too much → Exploding gradient


در شبکه‌های عمیق، در هنگام backpropagation ممکن است گرادیان‌ها:

    کوچک‌تر و کوچک‌تر شوند → مشکل vanishing gradient

    بزرگ‌تر و بزرگ‌تر شوند → مشکل exploding gradient
    
Result:

Training becomes unstable or the model fails to learn.
نتیجه:

یادگیری مختل می‌شود و مدل یا اصلاً یاد نمی‌گیرد یا ناپایدار می‌شود.

 راه‌حل‌ها / Solutions:

    استفاده از ReLU و He Initialization

    Normalization (BatchNorm)

    Residual Connections (در شبکه‌های ResNet)

    Gradient Clipping: محدودسازی مقدار گرادیان

مقایسه Backprop دستی و خودکار

   <table>
     <thead>
       <tr>
         <th>روش</th>
         <th>مزایا</th>
         <th>معایب</th>
       </tr>
     </thead>
     <tbody>
       <tr>
         <td><strong>دستی (Manual Backprop)</strong></td>
         <td>درک عمیق مفاهیم، کنترل کامل روی فرآیند</td>
         <td>پیچیدگی بالا، خطای انسانی، مقیاس‌ناپذیری</td>
       </tr>
       <tr>
         <td><strong>خودکار (Automatic Differentiation)</strong></td>
         <td>سریع، مطمئن، مناسب پروژه‌های واقعی</td>
         <td>پنهان شدن جزئیات الگوریتم</td>
       </tr>
  





بهینه‌سازی گرادیان‌ها با Optimizerها

 
 <table>
   <thead>
     <tr>
       <th>Optimizer</th>
       <th>فرمول کلی</th>
       <th>ویژگی‌ها</th>
     </tr>
   </thead>
   <tbody>
     <tr>
       <td><strong>SGD (Stochastic Gradient Descent)</strong></td>
       <td>θ ← θ − η ∇J(θ)</td>
       <td>ساده، ممکن است نوسان داشته باشد</td>
     </tr>
     <tr>
       <td><strong>Momentum</strong></td>
       <td>θ ← θ − η ∇J(θ) + γv</td>
       <td>نوسان کمتر، با حافظه گرادیان قبلی</td>
     </tr>
     <tr>
       <td><strong>RMSProp</strong></td>
       <td>θ ← θ − η / sqrt(E[∇2]) ∇J(θ)</td>
       <td>تنظیم تطبیقی نرخ یادگیری</td>
     </tr>
     <tr>
       <td><strong>Adam</strong></td>
       <td>ترکیب RMSProp و Momentum</td>
       <td>بهترین عملکرد در بسیاری از کاربردها</td>
     </tr>
   </tbody>
 </table>

 
