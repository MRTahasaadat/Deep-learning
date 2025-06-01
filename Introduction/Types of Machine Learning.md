 Types of Machine Learning | انواع یادگیری ماشین
🧠 Supervised Learning

یادگیری نظارت‌شده

    EN: In supervised learning, the model is trained on a labeled dataset — each input has a corresponding correct output.
    FA: در یادگیری نظارت‌شده، مدل با استفاده از مجموعه‌داده‌ی برچسب‌خورده آموزش می‌بیند — یعنی هر ورودی دارای خروجی صحیح است.

Examples | نمونه‌ها:

    Email spam detection | تشخیص اسپم در ایمیل

    House price prediction | پیش‌بینی قیمت خانه

    Image classification | طبقه‌بندی تصویر

Common Algorithms | الگوریتم‌های رایج:

    Linear Regression | رگرسیون خطی

    Logistic Regression | رگرسیون لجستیک

    Decision Trees | درخت تصمیم

    Neural Networks | شبکه‌های عصبی

🔍 Unsupervised Learning

یادگیری بدون نظارت

    EN: The model is trained on unlabeled data and must find hidden structures or patterns in the input.
    FA: در یادگیری بدون نظارت، مدل با داده‌های بدون برچسب کار می‌کند و باید الگوها یا ساختارهای پنهان را در داده‌ها بیابد.

Examples | نمونه‌ها:

    Customer segmentation | تقسیم‌بندی مشتریان

    Market basket analysis | تحلیل سبد خرید

    Anomaly detection | کشف ناهنجاری

Common Algorithms | الگوریتم‌های رایج:

    K-Means Clustering | خوشه‌بندی K-Means

    Hierarchical Clustering | خوشه‌بندی سلسله‌مراتبی

    PCA (Principal Component Analysis) | تجزیه مؤلفه‌های اصلی


⚖️ 3. Semi-Supervised Learning

یادگیری نیمه‌نظارتی

    EN: Combines a small amount of labeled data with a large amount of unlabeled data to improve learning.
    FA: در یادگیری نیمه‌نظارتی، از ترکیبی از مقدار کمی داده‌ی برچسب‌خورده و مقدار زیادی داده‌ی بدون برچسب برای آموزش مدل استفاده می‌شود.

Why important? | چرا مهم است؟

    Labeled data is expensive, unlabeled data is abundant.

    داده‌ی برچسب‌خورده معمولاً کمیاب و پرهزینه است، ولی داده‌ی خام به وفور یافت می‌شود.

Examples | نمونه‌ها:

    Image recognition with few labeled images | تشخیص تصویر با تعداد کمی تصویر برچسب‌خورده

    Text classification with limited annotations | دسته‌بندی متن با داده‌های محدود

Techniques:

    Pseudo-labeling

    Consistency regularization

    Graph-based models


🕹️ Reinforcement Learning

یادگیری تقویتی

    EN: The model (called an agent) interacts with an environment and learns by receiving rewards or penalties for its actions.
    FA: در یادگیری تقویتی، مدل (عامل) با یک محیط تعامل دارد و از طریق پاداش‌ها و جریمه‌هایی که دریافت می‌کند، یاد می‌گیرد چگونه رفتار بهینه را اتخاذ کند.

Examples | نمونه‌ها:

    Game-playing agents (like AlphaGo) | عامل‌های بازی‌ساز مانند آلفاگو

    Robotics | رباتیک

    Self-driving cars | خودروهای خودران

Key Concepts | مفاهیم کلیدی:

    Agent | عامل

    Environment | محیط

    Reward | پاداش

    Policy | سیاست یادگیری

    Q-Learning, Deep Q-Network (DQN) | الگوریتم‌های RL رایج



| Type                     | Uses Labels?  | Input Type     | Goal                        | Example                           |
| ------------------------ | ------------- | -------------- | --------------------------- | --------------------------------- |
| Supervised Learning      | ✅ Yes         | Labeled data   | Predict output              | Spam detection                    |
| Unsupervised Learning    | ❌ No          | Unlabeled data | Discover hidden patterns    | Customer segmentation             |
| Semi-Supervised Learning | ⚠️ Few labels | Mixed data     | Improve with limited labels | Image classification (few labels) |
| Reinforcement Learning   | ❌ (Reward)    | Environment    | Maximize reward             | Robot navigation, games           |

📌 Summary in One Line

    EN: ML can be supervised, unsupervised, semi-supervised, or reinforcement-based, depending on how data and feedback are used.
    FA: یادگیری ماشین بسته به نحوه‌ی استفاده از داده و بازخورد، می‌تواند نظارت‌شده، بدون‌نظارت، نیمه‌نظارتی یا تقویتی باشد.
