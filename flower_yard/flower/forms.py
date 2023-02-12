from django.core.exceptions import ValidationError
from django.forms import ModelForm


class CategoryFormAdmin(ModelForm):
    def clean(self):
        parent = self.cleaned_data.get('parent')
        image = self.cleaned_data.get('image')

        if parent and parent.level == 1:
            if image:
                raise ValidationError(
                    'Загрузка картинки для подкатегории не предусматривается!!'
                )
            raise ValidationError(
                'Создание категории подкатегории - не предусматривается!'
            )
        return self.cleaned_data
