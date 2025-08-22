Deploy notes for Render

1) Environment variables to set on Render (Service -> Environment):
   - DJANGO_SECRET_KEY: (your secret key)
   - DJANGO_DEBUG: False
   - DJANGO_ALLOWED_HOSTS: <your-app>.onrender.com

2) Build command (Render):
   - pip install -r requirements.txt

3) Start command (Render):
   - gunicorn meditation_site.wsgi --log-file -

4) Static files / CSS & images issues:
   - Ensure `STATIC_ROOT` is set (we added `staticfiles` in settings).
   - Render runs `collectstatic` automatically if `DISABLE_COLLECTSTATIC` is not set; if static assets are missing, run `python manage.py collectstatic --noinput` during build.
   - Confirm your templates use `{% load static %}` and reference static files with `{% static 'path' %}` (your project already does this).

5) Common fixes if CSS/images still missing:
   - Verify the `staticfiles` folder is present after `collectstatic`.
   - Ensure WhiteNoise is in `MIDDLEWARE` and `STATICFILES_STORAGE` is set (we added both).

6) Local test commands:
   - python -m venv venv; .\venv\Scripts\Activate
   - pip install -r requirements.txt
   - python manage.py collectstatic --noinput
   - python manage.py migrate
   - python manage.py runserver

If you want, I can add a small management check command or GitHub Actions workflow to automate deployment.
