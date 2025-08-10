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
