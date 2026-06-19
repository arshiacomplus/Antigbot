# Antigbot (Anti Guest Mode)

A lightweight and efficient Telegram bot designed to manage and restrict the "Guest Mode" bots in Telegram groups. By default, it instantly deletes any messages from unauthorized guest bots, along with the user's prompt (the replied message). Group administrators can explicitly allow specific bots to operate.

## Features
- **Automatic Cleanup**: Deletes both the unauthorized guest bot's message and the user's triggering message.
- **Admin Only**: Configuration commands can only be executed by group creators or administrators.
- **Persistent Storage**: Uses an asynchronous SQLite database (`aiosqlite`) to reliably store allowed bot lists per group.

## Requirements
- Python 3.8 or higher
- A Telegram Bot Token (from [@BotFather](https://t.me/BotFather))

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/arshiacomplus/Antigbot.git
   cd Antigbot
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory and add your bot token:
   ```env
   BOT_TOKEN=your_telegram_bot_token_here
   ```

4. Run the bot:
   ```bash
   python main.py
   ```

## Commands
*All commands are restricted to group administrators.*

- `/allow @bot_username` - Adds a bot to the group's whitelist.
- `/remove @bot_username` - Removes a bot from the group's whitelist.
- `/list` - Displays all currently allowed bots in the group.

**Important Note:** The bot must be added to your group as an administrator with the **Delete Messages** permission to function properly.

---

# Antigbot (مقابله با حالت مهمان)

یک ربات تلگرامی سبک و کارآمد که برای مدیریت و محدود کردن ربات‌های "حالت مهمان" (Guest Mode) در گروه‌های تلگرامی طراحی شده است. این ربات به صورت پیش‌فرض پیام‌ ربات‌های مهمان غیرمجاز و همچنین پیام کاربری که آن‌ها را فراخوانده است را بلافاصله پاک می‌کند. مدیران گروه می‌توانند ربات‌های خاصی را برای فعالیت مجاز کنند.

## ویژگی‌ها
- **پاکسازی خودکار**: حذف همزمان پیام ربات غیرمجاز و پیام کاربری که به آن ریپلای شده است.
- **محدودیت دسترسی**: دستورات تنظیمات تنها توسط سازنده و مدیران گروه قابل اجرا است.
- **ذخیره‌سازی پایدار**: استفاده از دیتابیس غیرهمزمان SQLite (`aiosqlite`) برای ذخیره مطمئن لیست ربات‌های مجاز هر گروه.

## پیش‌نیازها
- پایتون نسخه 3.8 یا بالاتر
- توکن ربات تلگرام (دریافت از [@BotFather](https://t.me/BotFather))

## نصب و راه‌اندازی

۱. ریپازیتوری را کلون کنید:
   ```bash
   git clone https://github.com/arshiacomplus/Antigbot.git
   cd Antigbot
   ```

۲. پیش‌نیازها را نصب کنید:
   ```bash
   pip install -r requirements.txt
   ```

۳. یک فایل `.env` در مسیر اصلی پروژه ایجاد کرده و توکن ربات خود را قرار دهید:
   ```env
   BOT_TOKEN=your_telegram_bot_token_here
   ```

۴. ربات را اجرا کنید:
   ```bash
   python main.py
   ```

## دستورات
*تمامی دستورات تنها برای مدیران گروه قابل استفاده است.*

- `/allow @bot_username` - افزودن یک ربات به لیست مجاز گروه.
- `/remove @bot_username` - حذف یک ربات از لیست مجاز گروه.
- `/list` - نمایش تمامی ربات‌های مجاز گروه.

**نکته مهم:** برای عملکرد صحیح، این ربات باید با دسترسی **حذف پیام‌ها** (Delete Messages) به عنوان مدیر در گروه شما ادمین شود.