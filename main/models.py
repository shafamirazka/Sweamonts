from django.db import models
from django.core.exceptions import ValidationError  # Tambahkan baris ini untuk mengimpor ValidationError


class ProductEntry(models.Model):
    name = models.CharField(max_length=255)
    time = models.DateField(auto_now_add=True)
    description = models.TextField()
    price = models.IntegerField()  # Harga produk (pastikan harga lebih dari 0)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)  # Menyimpan gambar produk

    def __str__(self):
        return self.name

    # Validasi untuk memastikan harga selalu positif
    def clean(self):
        if self.price <= 0:
            raise ValidationError('Harga produk harus lebih dari 0.')
