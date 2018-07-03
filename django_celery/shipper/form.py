from django import forms
from shipper.models import FileUploat
from shipper.task_upload import import_file


class UploadForm(forms.ModelForm):
    class Meta:
        model = FileUploat
        fields = ['name']

    def save(self, commit=True):
        file = super(UploadForm, self).save()
        import_file.delay(file.id)
        return file