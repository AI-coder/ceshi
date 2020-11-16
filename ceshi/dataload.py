import  os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ceshi.settings")
import django
django.setup()

def main():
    from data.models import Person
    data_list = [["xu","mam"],["xu","mam"],["xu","mam"],["xu","mam"],["xu","mam"],["xu","mam"],]
    for dat in data_list:
        Person.objects.create(name = dat[0],gender = dat[1])
    print("done")



if __name__ == '__main__':
    main()