🧠 MNIST Digit Classifier with TensorFlow

این پروژه یک شبکه عصبی چند لایه (MLP) ساده را با استفاده از TensorFlow پیاده‌سازی می‌کند تا ارقام دست‌نویس دیتاست معروف MNIST را شناسایی کند. هدف این پروژه، پیاده‌سازی پایه‌ای یادگیری عمیق بدون استفاده از API سطح بالا مثل model.fit() است، برای درک بهتر مفاهیم پایه مانند پراپگیشن رو به جلو، تابع هزینه و گرادیان‌گیری دستی.
🔧 ویژگی‌ها

    استفاده از دو لایه‌ی وزن (ورودی → مخفی → خروجی)

    فعال‌سازی ReLU در لایه پنهان

    استفاده از Softmax در لایه خروجی

    آموزش با Cross Entropy

    بهینه‌سازی دستی با GradientTape

    رسم نمودار تغییرات تابع هزینه در هر epoch

🗂 ساختار فایل

mnist_tf_manual/
├── main.py       # کد اصلی آموزش و ارزیابی مدل
└── README.md     # مستندات پروژه

🚀 نحوه اجرا
1. نصب پیش‌نیازها

مطمئن شوید که Python 3.7+ و pip نصب شده باشد، سپس کتابخانه‌های لازم را نصب کنید:

pip install tensorflow matplotlib numpy

2. اجرای پروژه

python main.py

📊 خروجی‌ها

    در هر epoch، مقدار تابع هزینه چاپ می‌شود.

    در پایان آموزش، دقت مدل روی داده‌های تست محاسبه و چاپ می‌شود.

    نمودار کاهش loss به صورت تصویری نمایش داده می‌شود.

📘 توضیح کد
آماده‌سازی داده‌ها

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0
x_train = x_train.reshape(-1, 784)
x_test = x_test.reshape(-1, 784)

    داده‌های MNIST به صورت 28x28 پیکسل هستند. آن‌ها را نرمال‌سازی و صاف (flatten) می‌کنیم.

y_train_ohe = to_categorical(y_train, 10)

    لیبل‌ها را به one-hot encoding تبدیل می‌کنیم.

ساخت مدل به صورت دستی

W1 = tf.Variable(tf.random.normal([784, 128], stddev=0.1))
b1 = tf.Variable(tf.zeros([128]))
W2 = tf.Variable(tf.random.normal([128, 10], stddev=0.1))
b2 = tf.Variable(tf.zeros([10]))

    تعریف وزن‌ها و بایاس‌ها با مقداردهی اولیه مناسب

حلقه آموزش (Training Loop)

with tf.GradientTape() as tape:
    ...
    loss = tf.reduce_mean(tf.keras.losses.categorical_crossentropy(y_batch, y_pred))

    با استفاده از GradientTape گرادیان‌ها را نسبت به وزن‌ها محاسبه می‌کنیم.

    سپس وزن‌ها را با یادگیری نرخ 0.01 به‌روزرسانی می‌کنیم.

رسم نمودار تابع هزینه

plt.plot(loss_history)

    کاهش loss در هر epoch را برای بررسی عملکرد مدل نمایش می‌دهیم.

ارزیابی روی داده‌های تست

correct_preds = tf.equal(tf.argmax(y_pred, axis=1), tf.argmax(y_test_ohe, axis=1))
accuracy = tf.reduce_mean(tf.cast(correct_preds, tf.float32))

    مقایسه پیش‌بینی مدل با لیبل‌های واقعی و محاسبه دقت

📈 نتایج نمونه

    دقت معمول در اجرای اولیه: بین 91% تا 94% (بدون Dropout یا بهینه‌سازی خاص)

    تعداد پارامترها:

        W1: 784 × 128 = 100352

        W2: 128 × 10 = 1280

        مجموع: ~101,632 پارامتر

📌 نکات و بهبودها

    اضافه کردن لایه‌های بیشتر (مثلاً لایه پنهان دوم)

    استفاده از Dropout برای جلوگیری از Overfitting

    استفاده از Optimizerهای پیشرفته‌تر مثل Adam

    ذخیره مدل آموزش‌دیده برای بارگذاری مجدد

🧠 منابع

    TensorFlow Documentation

    MNIST Dataset

    مفاهیم پایه شبکه‌های عصبی: Neural Networks and Deep Learning

