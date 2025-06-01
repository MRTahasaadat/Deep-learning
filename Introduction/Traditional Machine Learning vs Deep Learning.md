Traditional Machine Learning vs Deep Learning

 مقدمه | Introduction

    EN: While both Traditional Machine Learning and Deep Learning are subsets of Artificial Intelligence, they differ in how they process data, their dependence on features, and their ideal use-cases.
    FA: در حالی که یادگیری ماشین سنتی و یادگیری عمیق هر دو زیرمجموعه‌های هوش مصنوعی هستند، در نحوه‌ی پردازش داده، وابستگی به ویژگی‌ها و موارد کاربرد تفاوت‌های اساسی دارند.

⚖️ تفاوت‌های کلیدی | Key Differences
| ویژگی                   | Traditional ML (یادگیری ماشین سنتی)              | Deep Learning (یادگیری عمیق)           |
| ----------------------- | ------------------------------------------------ | -------------------------------------- |
| **ورودی داده‌ها**       | نیازمند استخراج ویژگی دستی (Feature Engineering) | خودکار ویژگی‌ها را استخراج می‌کند      |
| **حجم داده‌ی موردنیاز** | با داده‌ی کم هم قابل استفاده                     | نیازمند حجم بالای داده برای عملکرد خوب |
| **مدل‌ها**              | رگرسیون، درخت تصمیم، SVM و ...                   | شبکه‌های عصبی (ANN, CNN, RNN)          |
| **سرعت آموزش**          | سریع‌تر و سبک‌تر                                 | سنگین‌تر و نیازمند GPU                 |
| **درک ویژگی‌ها**        | قابل توضیح‌تر                                    | مانند جعبه‌ سیاه (کم‌تر قابل فهم)      |
| **کاربردها**            | داده‌های ساخت‌یافته                              | داده‌های پیچیده مثل تصویر، صوت، ویدیو  |
مثال واقعی از تفاوت‌ها | Real-World Example

🎯 تشخیص چهره در تصویر
| Traditional ML                                                              | Deep Learning                                              |
| --------------------------------------------------------------------------- | ---------------------------------------------------------- |
| مرحله ۱: استخراج ویژگی‌هایی مانند فاصله بین چشم‌ها، لبه‌ها و ... توسط انسان | مرحله ۱: تصویر خام را وارد مدل می‌کنیم                     |
| مرحله ۲: استفاده از SVM یا KNN برای طبقه‌بندی                               | مرحله ۲: استفاده از CNN برای یادگیری ویژگی‌ها و تصمیم‌گیری |



کد مقایسه‌ای ساده
Traditional ML – طبقه‌بندی با استفاده از ویژگی‌های دستی


    from sklearn.datasets import load_iris
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.model_selection import train_test_split
    
    data = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2)
    
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    
    print("Accuracy (Traditional ML):", model.score(X_test, y_test))
    
Deep Learning – طبقه‌بندی همان داده‌ها با شبکه عصبی ساده

    import tensorflow as tf
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Dense
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    
    data = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2)
    
    model = Sequential([
        Dense(10, activation='relu', input_shape=(4,)),
        Dense(3, activation='softmax')
    ])
    
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model.fit(X_train, y_train, epochs=100, verbose=0)
    
    loss, acc = model.evaluate(X_test, y_test, verbose=0)
    print("Accuracy (Deep Learning):", acc)

🧠 چه زمانی Traditional و چه زمانی Deep Learning؟
شرایط شما	توصیه
داده‌ی کم + ویژگی‌های مشخص	Traditional ML
داده‌ی پیچیده (تصویر، صدا) + داده‌ی زیاد	Deep Learning
نیاز به شفافیت و توضیح‌پذیری	Traditional ML
انعطاف بالا و استخراج خودکار ویژگی‌ها	Deep Learning
📌 نتیجه‌گیری

    EN: Traditional ML is ideal for small, structured problems; Deep Learning shines with complex, high-volume data.
    FA: یادگیری ماشین سنتی برای مسائل ساده با داده‌ی کم مناسب است، در حالی که یادگیری عمیق در شرایط پیچیده با داده‌ی زیاد می‌درخشد.
