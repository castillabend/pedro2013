from __future__ import absolute_import
from celery import current_app
from shipper.models import FileUploat
import pandas as re


app = current_app


@app.task
def test_shipper():
    print('Hi im shipper')


@app.task
def import_file(id):
    f = FileUploat.objects.get(pk=id)
    print(f.name.name)
import pandas as re
#@app.task
def read_excel():
    archivo_excel = re.read_excel('/home/pedro/pycharmproject/django_celery/medias/User-2018-06-29.xls')
    print(archivo_excel.columns)
    values = archivo_excel['Identificador'].values
    print(values)
    columnas = ['id', 'last_login', 'is_superuser', 'username', 'first_name',
                'last_name', 'email', 'is_staff', 'is_active', 'date_joined']
    df_seleccionados = archivo_excel[columnas]
    print(df_seleccionados)


    # f = FileUploat.objects.get(pk=id)
    # with re.Excelfile(archivo, opciones) as excel:
    #     df = re.read_excel(excel, opciones)


# ipath = 'austion_weather.xlsx'
# df = pd.read_excel(ipath)
# df.head()

#
# df = pd.read_excel(ipath, skiprows=26)
# df.head()
#
# df.info()
