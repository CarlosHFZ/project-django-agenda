import os
import django

# Configura o settings do seu projeto Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()


if __name__ == '__main__':
    from contact.models import Contact
    c = Contact.objects.all()

    for contato in c:
        print(contato)
