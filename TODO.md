# TODO

## Deployment removal (keep only runserver)
- [x] Remove deployment packages (`gunicorn`, `whitenoise`) from `requirements.txt`.
- [x] Remove deployment-only settings (`STATIC_ROOT`) from `weducation_web/settings.py`.
- [x] Leave DEBUG + `static()` media serving for runserver.
- [x] Run `python manage.py runserver` to verify startup.




