نورون‌ها چگونه شبکه عصبی می‌سازند؟
How Neurons Form Neural Networks
 1. نورون به‌تنهایی چیست؟

     A neuron is a simple computational unit that receives inputs, weights them, sums, and produces an output.
    
     نورون یک واحد محاسباتی ساده است که ورودی‌ها را دریافت و با وزن‌دهی و جمع‌بندی آنها، خروجی تولید می‌کند.

فرمول نورون:
y=f(∑i=1nwixi+b)
y=f(i=1∑n​wi​xi​+b)
 2. ساختن لایه از نورون‌ها

 Multiple neurons arranged side by side form a layer. Each neuron receives the same inputs but has its own weights and bias.
    
  وقتی چند نورون کنار هم قرار می‌گیرند، یک لایه (Layer) ساخته می‌شود. هر نورون ورودی‌های مشابهی دریافت می‌کند ولی وزن‌ها و بایاس‌های خاص خودش را دارد.

مثال ساده:

  ورودی‌ها: x1,x2,x3x1​,x2​,x3​

  لایه 4 نورونه: هر نورون وزن‌های خودش wijwij​ دارد.

کد پایتون (NumPy) برای محاسبه خروجی لایه 4 نورونه
      
      import numpy as np
      
      X = np.array([0.5, 0.3, 0.2])  
      W = np.array([
          [0.4, 0.2, 0.1],  
          [0.7, 0.5, 0.3],  
          [0.6, 0.9, 0.4],  
          [0.1, 0.2, 0.8]   
      ])
      
      b = np.array([0.1, 0.2, 0.3, 0.1])
      def relu(z):
          return np.maximum(0, z)
      
      Z = np.dot(W, X) + b
      output = relu(Z)
      
      print("Layer output:", output)
      
       توضیح:

    ورودی XX به همه نورون‌ها ارسال می‌شود

    هر نورون وزن‌های خود را دارد و خروجی مخصوص به خود را تولید می‌کند

    خروجی لایه، یک آرایه با اندازه تعداد نورون‌ها است

 3. اتصال لایه‌ها: شکل‌گیری شبکه


     The output of one layer becomes the input to the next layer. Stacking layers forms a neural network.
    
     خروجی یک لایه، ورودی لایه بعدی می‌شود. با این روش چند لایه پشت سر هم شبکه عصبی (Neural Network) ساخته می‌شود.

شبکه ساده:

    لایه ورودی (3 ورودی)

    لایه پنهان (4 نورون)

    لایه خروجی (1 نورون)

کد با TensorFlow/Keras برای این شبکه:
    
    import tensorflow as tf
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Dense
    
    model = Sequential([
        Dense(4, input_shape=(3,), activation='relu'),  # لایه پنهان با 4 نورون
        Dense(1, activation='sigmoid')                   # لایه خروجی با 1 نورون
    ])
    
    model.summary()

خروجی خلاصه مدل:
output

    output -->
    Layer (type)                 Output Shape              Param #
    =================================================================
    dense (Dense)                (None, 4)                 16
    dense_1 (Dense)              (None, 1)                 5
    =================================================================
    Total params: 21
    Trainable params: 21
    Non-trainable params: 0

 تحلیل دقیق‌تر:

  پارامترها (Weights & Biases):
  تعداد پارامترها = (تعداد ورودی × تعداد نورون) + تعداد بایاس‌ها
  برای لایه اول: 3×4+4=163×4+4=16
  برای لایه دوم: 4×1+1=54×1+1=5

  چرا پارامتر؟
  وزن‌ها و بایاس‌ها همان پارامترهای قابل یادگیری مدل هستند.

 خلاصه روند کار:

| مرحله | توضیح (FA)                                               | Explanation (EN)                                  |
| ----- | -------------------------------------------------------- | ------------------------------------------------- |
| 1     | هر نورون ورودی‌ها را وزن‌دهی می‌کند و خروجی تولید می‌کند | Each neuron weights inputs and produces an output |
| 2     | چند نورون کنار هم یک لایه می‌سازند                       | Multiple neurons side by side form a layer        |
| 3     | خروجی یک لایه ورودی لایه بعدی است                        | One layer’s output is the next layer’s input      |
| 4     | چند لایه متوالی، شبکه عصبی را تشکیل می‌دهند              | Stacking layers forms the neural network          |


خلاصه کد کلی: شبکه کوچک سه لایه

    import tensorflow as tf
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Dense
    
    model = Sequential([
        Dense(4, input_shape=(3,), activation='relu'),  # لایه مخفی 4 نورونه
        Dense(3, activation='relu'),                     # لایه دوم 3 نورونه
        Dense(1, activation='sigmoid')                   # خروجی 1 نورون
    ])
    
    model.summary()
