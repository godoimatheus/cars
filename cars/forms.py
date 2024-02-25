from datetime import datetime

from django import forms

from cars.models import Car


class CarForm(forms.ModelForm):
    class Meta:  # pylint: disable=R0903
        model = Car
        fields = '__all__'

    @staticmethod
    def get_current_year():
        return datetime.now().year

    @staticmethod
    def exists(field):
        if field:
            return True
        return False

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if self.exists(value) and value <= 0:
            self.add_error(
                'value', 'Valor do carro não pode ser menor do que R$ 0,00'
            )
        return value

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        current_year = self.get_current_year()
        if self.exists(factory_year):
            if factory_year and factory_year < 1900:
                self.add_error(
                    'factory_year',
                    'Não é possível cadastrar carros com ano de fabricação anterior a 1900',
                )
            elif factory_year and factory_year > current_year:
                self.add_error(
                    'factory_year',
                    'O ano de fabricação não pode ser maior do que o ano atual',
                )
        return factory_year

    def clean_plate(self):
        plate = self.cleaned_data.get('plate')
        if not plate.isalnum():
            self.add_error(
                'plate',
                'Formato inválido: Somente são aceitos os formatos AAA1111 ou AAA1A11',
            )
        return plate
