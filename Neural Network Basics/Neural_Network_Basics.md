What is a Neural Network ?

 شبکه عصبی چیست؟



Neural networks are computational models inspired by the structure of the human brain.

They consist of layers of artificial neurons that process input data to learn patterns and make decisions or predictions.

شبکه‌های عصبی مدل‌هایی محاسباتی هستند که با الهام از ساختار مغز انسان طراحی شده‌اند.

این شبکه‌ها از لایه‌هایی از نورون‌های مصنوعی تشکیل شده‌اند که ورودی را پردازش می‌کنند تا الگوها را یاد بگیرند و تصمیم یا پیش‌بینی انجام دهند.

1. Components of a Neural Network
 

1. اجزای اصلی یک شبکه عصبی

 Layers

    Input Layer: where the data enters the network

    Hidden Layer(s): intermediate layers where features are extracted

    Output Layer: final layer that gives prediction or decision

 لایه‌ها


    لایه ورودی: جایی که داده وارد شبکه می‌شود

    لایه‌های پنهان: لایه‌های میانی که ویژگی‌های داده را استخراج می‌کنند

    لایه خروجی: لایه نهایی که پیش‌بینی یا تصمیم را تولید می‌کند

Neurons (Units)

 نورون‌ها (یونیت‌ها)

Each layer consists of neurons (also called units or nodes).

Each neuron receives inputs, multiplies them by weights, adds a bias, and applies an activation function.

هر لایه از نورون‌ها (که گاهی به آن‌ها گره یا یونیت هم گفته می‌شود) تشکیل شده است.

هر نورون، ورودی‌هایی را دریافت می‌کند، آن‌ها را در وزن‌ها ضرب می‌کند، بایاس را اضافه می‌کند و سپس تابع فعال‌سازی را اعمال می‌کند.

Connections

 اتصالات


Neurons in one layer are fully connected to the neurons in the next layer.
Each connection has a weight that determines the influence of the input.

نورون‌ها در یک لایه به طور کامل به نورون‌های لایه بعدی وصل هستند.
هر اتصال دارای یک وزن (Weight) است که میزان تأثیر ورودی را تعیین می‌کند.

Visual Representation

        Input Layer      Hidden Layer     Output Layer
      [ x1 ] ——┐       [ h1 ]           [ y1 ]
      [ x2 ] ——┼——→    [ h2 ] ——→       [ y2 ]
      [ x3 ] ——┘       [ h3 ]


Simple Math Behind a Layer

ریاضیات ساده پشت یک لایه

For one hidden layer with 3 inputs and 1 neuron:

برای یک لایه پنهان با ۳ ورودی و ۱ نورون:
    
    z = w1 * x1 + w2 * x2 + w3 * x3 + b
    a = activation(z)


$wi​$: وزن‌ها

$xixi$​: ورودی‌ها

$bb$: بایاس

$aa$: خروجی نورون پس از فعال‌سازی
        
        | مفهوم              | انگلیسی                  | فارسی                   |
        | ------------------ | ------------------------ | ----------------------- |
        | Data Entry         | Input Layer              | لایه ورودی              |
        | Feature Extraction | Hidden Layer(s)          | لایه‌های پنهان          |
        | Prediction         | Output Layer             | لایه خروجی              |
        | Math Operation     | Neuron Computation       | محاسبه در نورون         |
        | Learning           | Adjusting weights/biases | تنظیم وزن‌ها و بایاس‌ها |


Forward Propagation

پراپگیشن رو به جلو (انتقال رو به جلوی داده در شبکه)

What is Forward Propagation?

پراپگیشن رو به جلو چیست؟

Forward propagation is the process of passing input data through the network, layer by layer, to compute the final output (prediction).
At each neuron, the inputs are combined, transformed, and passed forward to the next layer.

پراپگیشن رو به جلو به فرآیندی گفته می‌شود که در آن داده‌ی ورودی از طریق لایه‌های شبکه عبور می‌کند تا خروجی نهایی (پیش‌بینی) تولید شود.
در هر نورون، ورودی‌ها ترکیب، پردازش و به لایه بعدی منتقل می‌شوند.

Step-by-Step Process

فرآیند مرحله‌به‌مرحله

Step 1: Weighted Sum

مرحله ۱: مجموع وزنی

Each neuron calculates a weighted sum of its inputs plus a bias.

هر نورون مجموع وزنی از ورودی‌های خود به همراه یک بایاس را محاسبه می‌کند:

      z = w₁x₁ + w₂x₂ + ... + wₙxₙ + b


Step 2: Activation

 مرحله ۲: تابع فعال‌سازی

Apply an activation function to add non-linearity:

برای اضافه کردن غیرخطی بودن به مدل، تابع فعال‌سازی به خروجی اعمال می‌شود:

    a = activation(z)

Example with Numbers
    
    Inputs (x):  [1.0, 2.0, 3.0]
    Weights (w): [0.5, -1.0, 0.7]
    Bias (b): 0.1

Calculation of z

    z = (0.5*1.0) + (-1.0*2.0) + (0.7*3.0) + 0.1
    = 0.5 - 2.0 + 2.1 + 0.1 = 0.7
    
If the activation function is ReLU

    a = max(0, 0.7) = 0.7


Python Example with NumPy

    import numpy as np
    
    X = np.array([1.0, 2.0, 3.0])
    W = np.array([0.5, -1.0, 0.7])
    b = 0.1
    
    z = np.dot(W, X) + b
  
    a = np.maximum(0, z) --> # ReLU activation 
    
    print("Output:", a)

  output --> 

    Output: 0.7

Repeat for All Neurons and Layers
    
 تکرار برای همه نورون‌ها و لایه‌ها


 Forward propagation is repeated for each neuron in each layer, passing the results forward to the next layer.

 
پراپگیشن رو به جلو برای تمام نورون‌ها در تمام لایه‌ها تکرار می‌شود، و نتایج مرحله به مرحله به لایه‌های بعدی منتقل می‌شوند.

Summary 
      
      | گام | انگلیسی      | فارسی                |
      | --- | ------------ | -------------------- |
      | 1   | Weighted Sum | مجموع وزنی           |
      | 2   | Add Bias     | افزودن بایاس         |
      | 3   | Activation   | اعمال تابع فعال‌سازی |
      | 4   | Forward Pass | انتقال به لایه بعدی  |

Loss Function

تابع خطا (تابع هزینه)

What is a Loss Function?

 تابع خطا چیست؟
 

A loss function is a mathematical way to measure how wrong the model's predictions are compared to the actual (true) values.
It returns a single number that represents the error.


تابع خطا یک روش ریاضی برای اندازه‌گیری میزان اشتباه مدل است؛ یعنی تفاوت بین خروجی پیش‌بینی‌شده توسط مدل و مقدار واقعی.
این تابع یک عدد برمی‌گرداند که میزان خطا را نشان می‌دهد.

 Why Is It Important?

🎯 چرا مهم است؟
    
It guides the learning process: the model tries to minimize the loss.
A smaller loss means the model is doing better.


تابع خطا راهنمای فرایند یادگیری است: مدل تلاش می‌کند که مقدار این خطا را کاهش دهد.
هرچه خطا کمتر باشد، یعنی مدل بهتر یاد گرفته است


General Form

      Loss = loss_function(y_true, y_pred)


Types of Loss Functions

انواع تابع خطا

1. Mean Squared Error (MSE)

 Common for regression tasks

Formula:

$$\text{MSE} = \frac{1}{n} \sum_{i=1}^n \left( y_{\text{true}, i} - y_{\text{pred}, i} \right)^2$$

Explanation: Measures average squared difference between predicted and actual values. Penalizes large errors more heavily.

توضیح: میانگین اختلاف مربع شده پیش‌بینی و مقدار واقعی را محاسبه می‌کند. خطاهای بزرگ را بیشتر جریمه می‌کند.

Python example:

    import numpy as np
    
    y_true = np.array([3.0, 2.5, 1.0])
    y_pred = np.array([2.5, 2.0, 0.5])
    
    mse = np.mean((y_true - y_pred)**2)
    print("MSE:", mse)

2. Mean Absolute Error (MAE)

Use case: Regression

کاربرد: رگرسیون

Formula:
فرمول:

$$\text{MAE} = \frac{1}{n} \sum_{i=1}^{n} \left| y_i - \hat{y}_i \right|$$

Explanation: Measures average absolute difference between predicted and true values. More robust to outliers than MSE.

توضیح: میانگین اختلاف قدرمطلق پیش‌بینی و مقدار واقعی را محاسبه می‌کند. نسبت به داده‌های پرت مقاوم‌تر است.

Python example:
    
    import numpy as np
    
    y_true = np.array([3.0, 2.5, 1.0])
    y_pred = np.array([2.5, 2.0, 0.5])
    
    mae = np.mean(np.abs(y_true - y_pred))
    print("MAE:", mae)


3. Binary Cross-Entropy (Log Loss)

Use case: Binary classification

کاربرد: دسته‌بندی دودویی

$$\text{BCE} = -\frac{1}{n} \sum_{i=1}^{n} \left[ y_i \log(p_i) + (1 - y_i) \log(1 - p_i) \right]$$


Explanation: Measures difference between true labels and predicted probabilities. Penalizes confident wrong predictions heavily

توضیح: تفاوت بین برچسب‌های واقعی و احتمال‌های پیش‌بینی شده را اندازه‌گیری می‌کند و خطاهای پیش‌بینی قطعی اشتباه را شدیدتر جریمه می‌کند.


Python example:

    imoprt numpy as np
    
    y_true = np.array([1, 0, 1])
    y_pred = np.array([0.9, 0.2, 0.8])
    
    bce = -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))
    print("Binary Cross-Entropy:", bce)



4. Categorical Cross-Entropy

Use case: Multi-class classification

کاربرد: دسته‌بندی چندکلاسه

Formula:

فرمول:

$$\text{CCE} = - \sum_{i=1}^{n} \sum_{j=1}^{k} y_{ij} \log(p_{ij})$$

where kk is number of classes, yijyij​ is true label (one-hot encoded), and pijpij​ is predicted probability.

Explanation: Measures difference between one-hot true labels and predicted class probabilities from softmax output.

که kk تعداد کلاس‌ها است، yijyij​ برچسب واقعی به صورت وان-هات، و pijpij​ احتمال پیش‌بینی شده است.

توضیح: تفاوت بین برچسب‌های وان-هات واقعی و احتمال‌های پیش‌بینی شده از خروجی softmax را اندازه می‌گیرد.


Python example (TensorFlow):

      import tensorflow as tf
      
      loss_fn = tf.keras.losses.CategoricalCrossentropy()
      
      y_true = [[0, 0, 1]]
      y_pred = [[0.1, 0.2, 0.7]]
      
      loss = loss_fn(y_true, y_pred).numpy()
      print("Categorical Cross-Entropy:", loss)


5. Hinge Loss

Use case: SVM classification

کاربرد: طبقه‌بندی با SVM

Formula:

فرمول:

$$\text{Hinge} = \sum_{i=1}^{n} \max\left(0, 1 - y_i \hat{y}_i\right)$$

$$where yi∈{−1,1}yi​∈{−1,1}.$$

Explanation: Penalizes predictions that are not confidently correct.

No simple Python example here, but often used in SVM libraries

که yiyi​ برچسب واقعی است که مقدار آن -1 یا +1 است.

توضیح: جریمه می‌کند پیش‌بینی‌هایی که با اطمینان کافی درست نیستند.

Learning Process and Weight Update

مفهوم یادگیری و به‌روزرسانی وزن‌ها 
---
What is Learning in Neural Networks?

یادگیری در شبکه‌های عصبی چیست؟

Learning in neural networks refers to the process of adjusting the model’s weights to reduce prediction error. The model learns by comparing its prediction to the actual output and using that error to update its internal parameters.


یادگیری در شبکه‌های عصبی به فرآیند تنظیم وزن‌های مدل برای کاهش خطای پیش‌بینی گفته می‌شود. مدل با مقایسه خروجی پیش‌بینی شده با مقدار واقعی و به‌روزرسانی وزن‌ها بر اساس خطا، به مرور بهتر می‌شود.

 Step-by-Step Learning Process

  مراحل یادگیری گام‌به‌گام

  
 1. Initialization of Weights

At the beginning, the weights of the network are randomly initialized (usually small numbers).

در ابتدای کار، وزن‌های شبکه به‌صورت تصادفی مقداردهی اولیه می‌شوند (معمولاً مقادیر کوچک).

    import numpy as np
    weights = np.random.randn(3) * 0.01


 2. Forward Pass

    Input data is passed through the network to generate predictions.
    
 داده ورودی از طریق شبکه عبور می‌کند تا خروجی یا پیش‌بینی تولید شود.

    def forward(x, weights):
        return np.dot(x, weights)


 3. Compute Loss

The loss function calculates how far the prediction is from the actual target.

 تابع خطا مشخص می‌کند که خروجی چقدر با مقدار واقعی تفاوت دارد.

    def loss(y_true, y_pred):
       return (y_true - y_pred) ** 2  # MSE ساده


 4. Backward Pass

Use calculus (derivatives) to compute how much each weight contributed to the error. This is the gradient.

 با استفاده از مشتق‌گیری مشخص می‌شود که هر وزن چقدر در خطا نقش داشته است. به این مقدار گرادیان گفته می‌شود.

    def gradient(x, y_true, y_pred):
        return -2 * x * (y_true - y_pred)


 5. Update Weight

 We adjust the weights in the opposite direction of the gradient to reduce error.
 
 وزن‌ها در جهت مخالف گرادیان به‌روزرسانی می‌شوند تا خطا کاهش یابد.
     
     
     learning_rate = 0.01
     weights = weights - learning_rate * grad
     
Simple Learning Example
     
     x = np.array([2.0, 3.0])
     y_true = 13.0  # چون 2*2 + 3*3 = 4 + 9 = 13
     
     weights = np.random.randn(2) * 0.01
     learning_rate = 0.1
     
     for epoch in range(100):
         y_pred = np.dot(x, weights)
         error = y_true - y_pred
         grad = -2 * x * error
         weights -= learning_rate * grad
     
         if epoch % 10 == 0:
             print(f"Epoch {epoch}: y_pred = {y_pred:.4f}, loss = {error**2:.4f}")
     
     print("Weights after training:", weights)


 tensorflow
     
      import tensorflow as tf
     
     x = tf.constant([2.0, 3.0])  # x1 = 2, x2 = 3
     y_true = tf.constant(13.0)   # هدف: 2*2 + 3*3 = 13
     
     weights = tf.Variable(tf.random.normal([2]), name="weights")
     
     learning_rate = 0.1
     
     for epoch in range(100):
         with tf.GradientTape() as tape:
             y_pred = tf.reduce_sum(x * weights)
             loss = tf.square(y_true - y_pred)
     
         gradients = tape.gradient(loss, [weights])
     
         weights.assign_sub(learning_rate * gradients[0])
     
         if epoch % 10 == 0:
             print(f"Epoch {epoch}: y_pred = {y_pred.numpy():.4f}, loss = {loss.numpy():.4f}")
     
     print("Weights after training:", weights.numpy())

     
Backpropagation 

پس‌انتشار خطا


 What is Backpropagation?

Backpropagation is an algorithm used to calculate the gradients of the loss function with respect to each weight in the network. These gradients are used to update the weights using Gradient Descent.

«پس‌انتشار» الگوریتمی برای محاسبه گرادیان‌های وزن‌ها در یک شبکه عصبی است. این گرادیان‌ها برای به‌روزرسانی وزن‌ها (با استفاده از Gradient Descent یا روش‌های مشابه) استفاده می‌شوند.

مراحل کلی الگوریتم Backpropagation
    
    | گام | مرحله                | شرح فارسی                             | English Description                          |
    | --- | -------------------- | ------------------------------------- | -------------------------------------------- |
    | 1️⃣ | **Forward Pass**     | عبور داده از شبکه و محاسبه خروجی      | Pass input through network to get prediction |
    | 2️⃣ | **Loss Computation** | محاسبه خطا بین خروجی واقعی و پیش‌بینی | Calculate loss                               |
    | 3️⃣ | **Backward Pass**    | محاسبه گرادیان خطا نسبت به وزن‌ها     | Compute gradients of loss w\.r.t. weights    |
    | 4️⃣ | **Update Weights**   | اصلاح وزن‌ها با گرادیان               | Update weights using optimizer               |


 مثالی با فرمول ریاضی برای یک نورون ساده

فرض کنیم:

   ورودی: $$xx$$

   وزن: $$ww$$

   بایاس: $$bb$$

   خروجی: $$y^=σ(wx+b)y^​=σ(wx+b)$$

   تابع خطا: Mean Squared Error (MSE)

گام‌های ریاضی:

1.Forward Pass:


$$z = w x + b \quad ; \quad \hat{y} = \sigma(z)$$

2. Loss Function:

$$L = \frac{1}{2} (y - \hat{y})^2$$

3. Gradient of Loss w.r.t. output:

$$\frac{\partial L}{\partial \hat{y}} = \hat{y} - y$$


4. Chain Rule:


$$\frac{\partial L}{\partial w} = \frac{\partial L}{\partial \hat{y}} \cdot \frac{\partial \hat{y}}{\partial z} \cdot \frac{\partial z}{\partial w}
= (\hat{y} - y) \cdot \sigma'(z) \cdot x$$


چرا Chain Rule؟

Backpropagation به‌شدت بر قانون زنجیره‌ای در مشتق‌گیری (chain rule in calculus) متکی است:

$$\frac{\partial L}{\partial w} = \frac{\partial L}{\partial \hat{y}} \cdot \frac{\partial \hat{y}}{\partial z} \cdot \frac{\partial z}{\partial w}$$

این یعنی گرادیان نهایی از توزیع خطا به عقب، از لایه خروجی تا لایه‌های قبلی پخش می‌شود — که اسمش شده back-propagation!


جمع‌بندی تصویری مراحل Backpropagation


    Input (x)
       ↓
    [ Weighted Sum: z = wx + b ]
       ↓
    [ Activation: ŷ = σ(z) ]
       ↓
    [ Loss: L(y, ŷ) ]
       ↑
    [ Backward: dL/dw, dL/db ]
       ↑
    [ Update weights ]













