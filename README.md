# Calculator-GUI-M.pro-01 💻
Welcome to Calculator-GUI-M.pro-01! This project utilizes the powerful Kivy library to create a sleek and user-friendly graphical user interface (GUI) for your calculator needs.

## 🌟 Features:
Intuitive Design: Built with a clean and intuitive interface for ease of use.
Efficient Functionality: Harnessing the capabilities of Kivy library to ensure smooth and efficient performance.
Customizable Layout: Utilizing modules such as App, Button, BoxLayout, GridLayout, and Label to create a customizable and visually appealing calculator experience.
## 🚀 Usage:
Clone this repository to your local machine.
Ensure you have Python and Kivy installed.
Run the application and start calculating effortlessly!
## 🤝 Contribution:
Contributions are welcome! Whether it's bug fixes, feature enhancements, or UI improvements, feel free to submit a pull request.

## 📝 License:
This project is licensed under the MIT License, allowing for both personal and commercial use.

## 🙏 Acknowledgements:
Special thanks to the developers behind the Kivy library for providing such a versatile tool for GUI development.

# Commit type Emoji
Initial commit 🎉 General update ⚡ Reverting changes ⏪ Critical hotfix 🚑 Merging branches 🔀

<div dir="rtl">

### اجزای اصلی و مشترک در پروژه‌های Kivy

کتابخانه کیوی (Kivy) یک فریم‌ورک اپن سورس برای ساخت رابط کاربری (UI) و اپلیکیشن‌های مولتی‌تاچ و گرافیکی در پایتون است. این کتابخانه به دلیل انعطاف‌پذیری و امکانات گسترده‌ای که دارد، به خصوص در توسعه اپلیکیشن‌های موبایل و دسکتاپ، بسیار محبوب است. در اینجا به بررسی اجزای اصلی و مشترک استفاده از این کتابخانه می‌پردازیم:

1. **کلاس اپلیکیشن (App Class)**:
    - هر پروژه کیوی شامل یک کلاس اپلیکیشن است که از `App` ارث‌بری می‌کند. این کلاس نقطه شروع برنامه شما است و شامل متد `build` است که ویجت ریشه (root widget) را برمی‌گرداند.
    ```python
    from kivy.app import App

    class MyApp(App):
        def build(self):
            return SomeWidget()

    if __name__ == '__main__':
        MyApp().run()
    ```

2. **ویجت‌ها (Widgets)**:
    - ویجت‌ها اجزای اصلی ساخت رابط کاربری در کیوی هستند. کیوی ویجت‌های مختلفی مانند `Button`, `Label`, `TextInput`, `BoxLayout`, `GridLayout` و غیره را فراهم می‌کند.
    ```python
    from kivy.uix.button import Button
    from kivy.uix.label import Label
    ```

3. **لی‌اوت‌ها (Layouts)**:
    - برای مرتب‌سازی و مدیریت ویجت‌ها از لی‌اوت‌ها استفاده می‌شود. لی‌اوت‌های رایج عبارتند از `BoxLayout`, `GridLayout`, `AnchorLayout` و غیره.
    ```python
    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.gridlayout import GridLayout
    ```

4. **اتصال رویدادها (Event Binding)**:
    - در کیوی می‌توان رویدادها را به متدها یا توابع متصل کرد. برای مثال، زمانی که کاربر روی یک دکمه کلیک می‌کند، می‌توان یک تابع خاص را اجرا کرد.
    ```python
    button.bind(on_press=self.on_button_press)

    def on_button_press(self, instance):
        print("Button pressed")
    ```

5. **ویجت ریشه (Root Widget)**:
    - ویجت ریشه به عنوان پایه و اساس رابط کاربری شما عمل می‌کند. در متد `build` از کلاس اپلیکیشن، این ویجت بازگردانده می‌شود.
    ```python
    class MyApp(App):
        def build(self):
            root = BoxLayout(orientation='vertical')
            root.add_widget(Button(text='Hello'))
            return root
    ```

6. **تنظیمات و پیکربندی (Configuration)**:
    - کیوی امکان پیکربندی اپلیکیشن را فراهم می‌کند. شما می‌توانید از فایل‌های `.kv` برای تعریف و تنظیم رابط کاربری به صورت جداگانه از کد پایتون استفاده کنید.

### نمونه کد:
در کدی که شما ارائه داده‌اید، یک اپلیکیشن ماشین حساب ساده پیاده‌سازی شده است. در اینجا به بخش‌های مختلف آن اشاره می‌کنیم:

1. **ساخت ویجت ریشه و تنظیم لی‌اوت‌ها**:
    - استفاده از `BoxLayout` برای لی‌اوت اصلی و `GridLayout` برای دکمه‌های ماشین حساب.
    ```python
    root_widget = BoxLayout(orientation='vertical')
    button_grid = GridLayout(cols=4, size_hint_y=2)
    ```

2. **ایجاد و افزودن دکمه‌ها و لیبل‌ها**:
    - دکمه‌ها با استفاده از حلقه `for` ایجاد و به `GridLayout` افزوده می‌شوند. همچنین یک `Label` برای نمایش خروجی تعریف شده است.
    ```python
    output_label = Label(size_hint_y=0.75, font_size=50)
    for symbol in button_symbols:
        button_grid.add_widget(Button(text=symbol))
    ```

3. **اتصال رویدادها به دکمه‌ها**:
    - برای هر دکمه، رویداد `on_press` به یک تابع متصل شده است تا متن دکمه را به لیبل اضافه کند.
    ```python
    def print_button_text(instance):
        output_label.text += instance.text

    for button in button_grid.children[1:]:
        button.bind(on_press=print_button_text)
    ```

4. **ارزیابی نتیجه و پاک کردن لیبل**:
    - دکمه 'Clear' برای پاک کردن لیبل و دکمه '=' برای ارزیابی عبارت ریاضی نوشته شده است.
    ```python
    def evaluate_result(instance):
        try:
            output_label.text = str(eval(output_label.text))
        except SyntaxError:
            output_label.text = 'Python Syntax error!'

    def clear_label(instance):
        output_label.text = " "
    ```

5. **نهایی‌سازی رابط کاربری**:
    - افزودن لیبل، گرید دکمه‌ها و دکمه پاک کردن به ویجت ریشه و بازگرداندن آن.
    ```python
    root_widget.add_widget(output_label)
    root_widget.add_widget(button_grid)
    root_widget.add_widget(clear_button)
    return root_widget
    ```

</div>
