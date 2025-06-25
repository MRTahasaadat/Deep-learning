
 Multi-Layer Perceptron (MLP)

The basic Perceptron is a single-layer model that can only solve linearly separable problems.

در ساده‌ترین حالت، Perceptron یک مدل یادگیری ماشین است که تنها یک لایه خروجی دارد و قادر است تنها مسائل خطی‌قابل‌تفکیک (linearly separable) را حل کند.

The Multi-Layer Perceptron (MLP) includes:

اما Multi-Layer Perceptron یا MLP شامل:

    an input layer

    one or more hidden layers

    and an output layer

    یک لایه ورودی

    یک یا چند لایه پنهان (Hidden Layers)

    و یک لایه خروجی

This architecture allows MLP to solve non-linear problems.

است. این ساختار چندلایه باعث می‌شود که MLP بتواند مسائل غیرخطی را نیز حل کند.

مهم‌ترین تفاوت‌ها:


     
     
     | ویژگی            | Perceptron ساده       | Multi-Layer Perceptron (MLP)      |
     | ---------------- | --------------------- | --------------------------------- |
     | تعداد لایه‌ها    | ۱ (فقط خروجی)         | حداقل ۳ (ورودی + پنهان + خروجی)   |
     | توانایی حل مسائل | فقط خطی‌قابل‌تفکیک    | توانایی درک روابط پیچیده و غیرخطی |
     | تابع فعال‌سازی   | Step Function (قدیمی) | ReLU، Tanh، Sigmoid و ...         |
     | الگوریتم آموزش   | بدون Backpropagation  | با Backpropagation                |
     








