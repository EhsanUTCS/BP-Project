from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.ImageField()
    def save(self, commit=True):
        instance = super(UploadFileForm, self).save(commit=False)
        instance.save(black_and_white=True)  # call model save method from here
        return instance