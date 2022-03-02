# روبات تلگرامی همسنگ

## چگونگی اجرا

وارد مسیر bot شوید
```bash
cd bot
cp config.py.default config.py
```
توکن روبات را از تلگرام دریافت کنید در فایل config.py قرار دهید.  
برای این کار خط زیر را در این فایل تغییر دهید:
```python
bot_token = ""
```

روبات را اجرا کنید
```bash
python3 run_me.py
```
