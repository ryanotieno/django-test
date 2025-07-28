# 🧪 Django Railway Detection Test

This is a **minimal Django application** designed to test Railway's Django auto-detection.

## ✅ What This Tests

- **Django Detection**: Does Railway recognize this as a Django project?
- **Nixpacks Usage**: Does Railway use Nixpacks instead of Docker?
- **Dependency Installation**: Does `requirements.txt` get processed correctly?
- **Application Startup**: Does the Django server start successfully?

## 📁 Project Structure

```
test-django-railway/
├── manage.py              ← 🎯 KEY: Django detection signal
├── requirements.txt       ← 🎯 KEY: Python project detection
├── testapp/               ← Django settings package
│   ├── __init__.py
│   ├── settings.py        ← Local development settings
│   ├── settings_production.py ← Railway production settings
│   ├── urls.py            ← URL routing with test view
│   └── wsgi.py            ← WSGI application
├── railway.json           ← Railway configuration
├── nixpacks.toml          ← Nixpacks configuration
└── .dockerignore          ← Force Nixpacks (not Docker)
```

## 🚀 Expected Railway Behavior

1. **Auto-detect** as Django project (due to `manage.py` at root)
2. **Use Nixpacks** for building (due to `.dockerignore` and `nixpacks.toml`)
3. **Install dependencies** from `requirements.txt`
4. **Run migrations** and collect static files
5. **Start Gunicorn** server

## 🎯 Success Indicators

If the test is successful, you should see:
- ✅ Railway detects "Django" project type
- ✅ Build uses Nixpacks (not Docker)
- ✅ Application starts successfully
- ✅ Home page shows success message

## 📝 Deployment Steps

1. Push this to a GitHub repository
2. Connect to Railway
3. Deploy and observe the build process
4. Visit the deployed URL

If Railway doesn't auto-detect Django, something is wrong with the project structure or Railway's detection logic. 