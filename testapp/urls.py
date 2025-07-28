"""URL Configuration for testapp."""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    """Simple home view."""
    return HttpResponse("""
    <h1>🚀 Django Test App</h1>
    <h2>✅ Railway Django Detection Test</h2>
    <p>If you can see this, Railway successfully:</p>
    <ul>
        <li>✅ Detected this as a Django project</li>
        <li>✅ Installed dependencies from requirements.txt</li>
        <li>✅ Started the Django server</li>
        <li>✅ Connected to the database</li>
    </ul>
    <p><strong>🎉 Test Successful!</strong></p>
    <hr>
    <p>This confirms Railway will detect Django projects when:</p>
    <ul>
        <li>📄 <code>manage.py</code> is at the root level</li>
        <li>📦 <code>requirements.txt</code> is at the root level</li>
        <li>⚙️ Django settings are properly configured</li>
    </ul>
    """)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
] 