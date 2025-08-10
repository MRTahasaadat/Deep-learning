Introduction
In a neural network, each neuron takes an input signal, combines it with weights and a bias, and then passes the result through an activation function.
Without this activation function, the output of the neuron would just be a linear combination of inputs, meaning that the entire network — even with multiple layers — could only model linear relationships.
Therefore, activation functions are essential for solving complex problems that require non-linearity

در یک شبکه عصبی، هر نورون یک سیگنال ورودی را دریافت می‌کند، آن را با وزن‌ها و بایاس ترکیب می‌کند و سپس نتیجه را از یک تابع فعال‌سازی عبور می‌دهد.
اگر این تابع فعال‌سازی وجود نداشته باشد، خروجی نورون فقط یک ترکیب خطی از ورودی‌ها خواهد بود، و کل شبکه — حتی اگر چندین لایه داشته باشد — فقط می‌تواند روابط خطی را مدل کند.
در نتیجه، برای حل مسائل پیچیده که نیاز به غیرخطی‌بودن (Non-linearity) دارند، توابع فعال‌سازی ضروری هستند.

Why is Non-Linearity Important?

چرا غیرخطی‌بودن مهم است؟ 



Imagine you want to build a neural network to classify data distributed in a circular shape. If you only use linear functions, the model cannot learn complex boundaries and, at best, will draw a straight line to separate points.
By adding nonlinear functions, the model can learn complex shapes like circles, spirals, or any irregular pattern.

فرض کنید می‌خواهید یک شبکه عصبی برای طبقه‌بندی داده‌هایی بسازید که به شکل دایره‌ای توزیع شده‌اند. اگر فقط از توابع خطی استفاده کنید، مدل نمی‌تواند مرزهای پیچیده را یاد بگیرد و در بهترین حالت، یک خط مستقیم ترسیم می‌کند که نقاط را جدا کند.
با اضافه‌کردن توابع غیرخطی، مدل می‌تواند اشکال پیچیده مانند دایره، مارپیچ یا هر الگوی نامنظم دیگری را یاد بگیرد.



General Neuron Formula
فرمول کلی یک نورون

یک نورون ورودی‌ها را با وزن‌ها و بایاس ترکیب کرده و از تابع فعال‌سازی عبور می‌دهد:

$$
z = \sum_{i=1}^{n} w_i x_i + b
$$
$$
y = f(z)
$$

 inputs

$$xi​$$ 

 weights

$$wiwi​$$

 bias

$$bb$$

 activation function

$$ff$$


Code Example Python (NumPy)

**

      import numpy as np
      
      x = np.array([0.5, -0.2, 0.1])
      w = np.array([0.4, 0.7, -0.5])
      b = 0.1
      
      def sigmoid(z):
          return 1 / (1 + np.exp(-z))
      
      z = np.dot(w, x) + b
      y = sigmoid(z)
      
      print("Linear Output (z):", z)
      print("Activated Output (y):", y)
**

Without activation functions, a neural network becomes a simple linear model, unable to capture complex non-linear patterns.
   
  بدون تابع فعال‌سازی، مدل فقط یک ترکیب خطی از ورودی‌ها خواهد بود و توانایی یادگیری روابط پیچیده را نخواهد داشت.

     
 نقش تابع فعال‌سازی:

  اضافه‌کردن غیرخطی بودن به مدل

   کنترل عبور سیگنال‌ها (مثل فیلتر)

   کمک به همگرایی سریع‌تر در آموزش

  انواع توابع فعال‌سازی رایج:

1. Step Function (تابع پله‌ای)

قدیمی و غیرقابل مشتق — برای مدل‌سازی نورون‌های باینری

$$f(z) =\begin{cases}1 & \text{if } z \geq 0 \\\\0 & \text{if } z < 0\end{cases}$$

✅ ساده و قابل فهم

❌ نامناسب برای یادگیری عمیق (گرادیان صفر)

2. Sigmoid Function (سیگموید)

$$f(z) = \frac{1}{1 + e^{-z}}$$

📈 خروجی بین (0, 1)

🧠 مناسب برای مسائل باینری

✅ خروجی احتمال‌گونه

❌ مشکل Vanishing Gradient در شبکه‌های عمیق

3. Tanh Function (تانژانت هیپربولیک)

$$f(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}}$$

📈 خروجی بین (-1, 1)

✅ مرکزیت حول صفر → آموزش بهتر نسبت به Sigmoid

❌ هنوز مشکل گرادیان کوچک دارد در لایه‌های عمیق

4. ReLU (Rectified Linear Unit)

$$f(z)=max(0,z)$$

📈 معروف‌ترین و پرکاربردترین تابع فعال‌سازی

✅ سادگی، مشتق‌پذیری، عملکرد عالی

❌ مشکل "مرگ نورون" (Dead Neurons) – اگر ورودی همیشه منفی باشد، نورون خاموش می‌ماند

5. Leaky ReLU

 $$f(z) =\begin{cases}z & \text{if } z \geq 0 \\\\\alpha z & \text{if } z < 0 \quad (\alpha \approx 0.01)\end{cases}$$

✅ حل مشکل مرگ نورون در ReLU

✅ اجازه عبور اندک از بخش منفی

6. Softmax

$$f(z_i) = \frac{e^{z_i}}{\sum_j e^{z_j}}$$


📈 تبدیل خروجی‌ها به احتمال برای طبقه‌بندی چند‌کلاسه

✅ مجموع خروجی‌ها = 1

✅ مناسب برای لایه‌ی خروجی شبکه‌های دسته‌بندی

📊 جدول مقایسه‌ای:


| تابع       | دامنه خروجی  | مشتق‌پذیری | کاربرد                |
| ---------- | ------------ | ---------- | --------------------- |
| Step       | 0 یا 1       | ❌          | مدل‌های ساده یا قدیمی |
| Sigmoid    | (0, 1)       | ✅          | طبقه‌بندی باینری      |
| Tanh       | (-1, 1)      | ✅          | میان‌لایه‌های RNN     |
| ReLU       | \[0, ∞)      | ✅          | CNN، شبکه‌های عمیق    |
| Leaky ReLU | (-∞, ∞)      | ✅          | جایگزین ReLU          |
| Softmax    | \[0, 1], Σ=1 | ✅          | طبقه‌بندی چندکلاسه    |


 Activation Functions Analysis & Comparison
 
 تحلیل و مقایسه توابع فعال‌سازی 

 In this section, our goal is to understand when to use which activation function and why choosing the right one is crucial for model performance.

 در این بخش، هدف ما این است که بفهمیم چه زمانی از کدام تابع استفاده کنیم و چرا انتخاب درست تابع فعال‌سازی برای عملکرد مدل بسیار مهم است.

  
  
   Practical Recommendations
  
  توصیه‌های عملی 

  لایه‌های پنهان (Hidden Layers): اغلب از ReLU یا نسخه‌های آن استفاده کنید.

لایه خروجی (Output Layer): بسته به مسئله:

    Binary Classification → Sigmoid

    Multi-class Classification → Softmax

    Regression → بدون تابع فعال‌سازی یا ReLU


   مثال ترکیب توابع – Mixed Activation Example


A neural network for MNIST digit recognition:

    Hidden layers → ReLU

    Output layer → Softmax
    
یک شبکه عصبی برای تشخیص ارقام MNIST:

    لایه‌های پنهان → ReLU

    لایه خروجی → Softmax
    
 **
 
    import tensorflow as tf
    
    model = tf.keras.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    
 **
    
