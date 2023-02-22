from django.core.exceptions import ValidationError
from django.forms import ModelForm


class CategoryFormAdmin(ModelForm):
    def clean(self):
        parent = self.cleaned_data.get('parent')
        image = self.cleaned_data.get('image')

        if not parent:
            if not image:
                raise ValidationError(
                    'Не забудьте загрузить картинку категрии!'
                )
        elif parent:
            if parent.level == 1:
                raise ValidationError(
                    'Создание категории подкатегории - не предусматривается!'
                )
            if image:
                raise ValidationError(
                    'Загрузка картинки для подкатегории не предусматривается!'
                )

        return self.cleaned_data
