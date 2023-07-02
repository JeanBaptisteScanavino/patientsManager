from django.contrib.auth.models import User

# python manage.py runscript create_first_user_for_dev

user = User.objects.create_user("Shinji", "eva01@nerv.com", "ReiEva00")
user.save()
