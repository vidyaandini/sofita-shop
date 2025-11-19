from django.forms import ModelForm, TextInput, Textarea, URLInput, NumberInput, Select, CheckboxInput
from main.models import Product
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "category", "thumbnail", "is_featured", "price"]
        widgets = {
            'name': TextInput(attrs={
                'class': 'block w-full rounded-md border-gray-300 shadow-sm focus:border-[#ba1666] focus:ring-[#ba1666] sm:text-sm',
                'placeholder': 'Masukkan nama produk'
            }),
            'description': Textarea(attrs={
                'class': 'block w-full rounded-md border-gray-300 shadow-sm focus:border-[#ba1666] focus:ring-[#ba1666] sm:text-sm',
                'rows': 5,
                'placeholder': 'Tulis deskripsi produkmu...'
            }),
            'thumbnail': URLInput(attrs={
                'class': 'block w-full rounded-md border-gray-300 shadow-sm focus:border-[#ba1666] focus:ring-[#ba1666] sm:text-sm',
                'placeholder': 'https://contoh.com/gambar-produk.jpg'
            }),
            'price': NumberInput(attrs={
                'class': 'block w-full rounded-md border-gray-300 shadow-sm focus:border-[#ba1666] focus:ring-[#ba1666] sm:text-sm',
                'placeholder': 'Contoh: 150000',
                'min': 0,
                'step': 1000
            }),
            'category': Select(attrs={
                'class': 'block w-full rounded-md border-gray-300 shadow-sm focus:border-[#ba1666] focus:ring-[#ba1666] sm:text-sm'
            }),
            'is_featured': CheckboxInput(attrs={
                'class': 'w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded'
            }),
        }

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)