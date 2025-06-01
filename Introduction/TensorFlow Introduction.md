TensorFlow Introduction (High-level)
(معرفی سطح‌بالای تنسورفلو)

 مقدمه | Introduction

  TensorFlow is an open-source machine learning framework developed by Google. It allows you to build and train deep learning models efficiently.
    
     
  تنسورفلو یک فریم‌ورک متن‌باز برای یادگیری ماشین است که توسط گوگل توسعه یافته و امکان ساخت و آموزش مدل‌های یادگیری عمیق را فراهم می‌کند.

 نصب تنسورفلو | Installing TensorFlow

    pip install tensorflow


 مفاهیم کلیدی در TensorFlow (High-level API - Keras)

مفهوم	توضیح
         | مفهوم        | توضیح                                              |
| ------------ | -------------------------------------------------- |
| `Model`      | کلاس پایه برای تعریف مدل‌ها                        |
| `Sequential` | مدلی ساده برای ساخت لایه‌ به لایه (stacked layers) |
| `Layer`      | اجزای تشکیل‌دهنده مدل‌ها (Dense, Conv2D, etc.)     |
| `compile()`  | مشخص کردن optimizer، loss function، metrics        |
| `fit()`      | آموزش مدل                                          |
| `evaluate()` | ارزیابی عملکرد مدل                                 |
| `predict()`  | پیش‌بینی نتایج جدید                                |

 ساخت یک مدل ساده طبقه‌بندی با Keras API

 
 مثال: طبقه‌بندی دیتاست MNIST (دست‌نویس ارقام)
    
    import tensorflow as tf
    from tensorflow.keras.datasets import mnist
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Dense, Flatten
    from tensorflow.keras.utils import to_categorical
    
    # Load Data
    (X_train, y_train), (X_test, y_test) = mnist.load_data()
    
    # Normalize
    X_train, X_test = X_train / 255.0, X_test / 255.0
    
    # One-hot encoding labels
    y_train = to_categorical(y_train, 10)
    y_test = to_categorical(y_test, 10)
    
    # Define model
    model = Sequential([
        Flatten(input_shape=(28, 28)),
        Dense(128, activation='relu'),
        Dense(10, activation='softmax')
    ])
    
    # Compile
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    
    # Train
    model.fit(X_train, y_train, epochs=5, validation_data=(X_test, y_test))
    
    # Evaluate
    loss, acc = model.evaluate(X_test, y_test)
    print("Accuracy:", acc)

 ساختار پروژه با TensorFlow

    
    project/
    ├── data/                ← داده‌های ورودی
    ├── notebooks/           ← نوت‌بوک‌های آموزشی
    ├── models/              ← فایل مدل‌های ذخیره‌شده
    ├── scripts/             ← اسکریپت‌های آموزش یا پیش‌بینی
    └── README.md            ← توضیحات پروژه

 مزایای استفاده از TensorFlow (Keras API)
| ویژگی          | توضیح                                                 |
| -------------- | ----------------------------------------------------- |
| 👶 سادگی       | API سطح بالا بسیار ساده و قابل فهم است                |
| ⚡ سرعت         | پشتیبانی از GPU و TPU                                 |
| 🧪 ابزار       | TensorBoard، Model Checkpoint، EarlyStopping          |
| 🌐 مقیاس‌پذیری | مناسب برای تولید و مقیاس صنعتی                        |
| 🔄 سازگاری     | تعامل با TFLite، TensorFlow\.js، و TensorFlow Serving |
