# 🧠 Neural Network from Scratch with NumPy

این پروژه یک پیاده‌سازی ساده و آموزشی از شبکه‌های عصبی (Neural Network) با استفاده از `NumPy` است. در اینجا از الگوریتم **Backpropagation** برای آموزش مدل استفاده شده و داده‌های تصویری ارقام دست‌نویس از دیتاست `load_digits` (مینی MNIST) موجود در `scikit-learn` استفاده می‌شود.

---

## 🔍 ویژگی‌ها

- بدون استفاده از TensorFlow یا PyTorch — فقط `NumPy`
- دارای:
  - توابع فعال‌سازی `Sigmoid` و مشتق آن
  - اعمال Normalization دستی (شبیه `StandardScaler`)
  - One-hot encoding دستی برای برچسب‌ها
  - تقسیم دستی داده‌ها (Train/Test)
  - مصورسازی نمودارهای:
    - خطای آموزش و تست
    - دقت آموزش و تست
    - زمان سپری‌شده آموزش
- جلوگیری از Overfitting با:
  - کاهش ظرفیت مدل
  - تنظیم داده‌های آموزش و تست
  - رسم نمودارهای ارزیابی

---

## 📦 پیش‌نیازها

```bash
pip install numpy matplotlib scikit-learn

🚀 اجرا

فایل neural_net_digits.py را اجرا کنید:

python neural_net_digits.py

📊 خروجی‌ها

در پایان آموزش، نمودارهایی به صورت زیر نمایش داده خواهند شد:

    Training vs Test Loss

    Training vs Test Accuracy

    Training Time (per epoch)

و همچنین دقت نهایی تست نیز چاپ می‌شود، مثلاً:

✅ Final Test Accuracy: 72.85%

🧠 معماری شبکه عصبی

    ورودی: 64 ویژگی (تصویر 8x8 پیکسل)

    لایه مخفی: 16 نورون + تابع فعال‌سازی Sigmoid

    خروجی: 10 نورون (one-hot برای ارقام 0 تا 9) + Sigmoid

⚙️ پارامترهای قابل تنظیم

در فایل اصلی می‌توانید این مقادیر را تغییر دهید:


lr = 0.00051
epochs = 6500


📚 منابع

    Scikit-learn Digits Dataset

    Backpropagation - Wikipedia

    CS231n - Stanford Neural Networks

📌 نکات آموزشی

    یادگیری معماری ساده شبکه عصبی بدون استفاده از فریم‌ورک‌های سطح بالا

    درک بهتر از فرایند forward pass و backpropagation

    مشاهده اثر overfitting و نحوه کنترل آن با کاهش ظرفیت مدل
