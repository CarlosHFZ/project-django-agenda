from contact.models import Contact
import os
import django

# Configura o settings do seu projeto Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()


c = Contact.objects.all()

for contato in c:
    print(contato)
