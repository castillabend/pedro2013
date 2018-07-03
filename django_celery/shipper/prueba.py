import pandas as re
#@app.task
#from django.contrib.auth.models import User
from django.contrib.auth.models import User

from shipper.models import FileUploat


def read_excel(val_id):
    file = FileUploat.objects.get(id=val_id)
    val = re.read_excel(file.name.path)
    #print(archivo_excel.columns)
    #values = archivo_excel['id'].values

    # for index, row in re.iterrows():
    #     print(row["name"], row["age"])



    for index, row in re.iterrows():
        user = User.objects.create_user(id=val['id'], last_login =val['last_login'], is_superuser =val['is_superuser'],
                                        username=val['username'], first_name=val['first_name'], last_name=val['last_name'],
                                        email=row['email'], is_staff=val['is_staff'], is_active=val['is_active'], date_joined=val['date_joined']
                                        )  # creamos el usuario y clave

        # columnas = ['id', 'last_login', 'is_superuser', 'username', 'first_name',
        #             'last_name', 'email', 'is_staff', 'is_active', 'date_joined']
        #user.is_superuser = True  # permisos de superusuario
        #user.is_staff = True  # definimos si es parte del staff
        user.save()  # guardamos los datos.

        #row['c1'], row['c2']
    #columnas = ['id', 'last_login', 'is_superuser', 'username', 'first_name',
    #             'last_name', 'email', 'is_staff', 'is_active', 'date_joined']
    # df_seleccionados = archivo_excel[columnas]
    # print(df_seleccionados)

read_excel()