from django import forms
from shipper.models import FileUploat
from shipper.tasks import import_file,read_excel


class UploadForm(forms.ModelForm):
    class Meta:
        model = FileUploat
        fields = ['name']

    def save(self, commit=True):
        file = super(UploadForm, self).save()
        import_file.delay(file.id)
        read_excel.delay(file.id)

        return file