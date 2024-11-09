from django.test import TestCase, Client
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import ProductEntry


class ProductEntryTest(TestCase):
    
    def test_product_creation(self):
        """Test untuk memastikan produk dapat dibuat dengan harga yang valid"""
        product = ProductEntry.objects.create(
            name="Produk Test",
            description="Deskripsi produk test",
            price=100,  # Harga yang valid
        )
        self.assertEqual(product.name, "Produk Test")
        self.assertEqual(product.price, 100)
    
    def test_product_creation_invalid_price(self):
        """Test untuk memastikan produk tidak dapat dibuat dengan harga yang tidak valid"""
        with self.assertRaises(ValidationError):
            product = ProductEntry.objects.create(
                name="Produk Test Invalid",
                description="Deskripsi produk test",
                price=-1,  # Harga tidak valid
            )
            product.full_clean()  # Memicu validasi sebelum menyimpan ke database
    
    def test_product_str_method(self):
        """Test untuk memastikan metode __str__() bekerja dengan benar"""
        product = ProductEntry.objects.create(
            name="Produk Test",
            description="Deskripsi produk test",
            price=100,
        )
        self.assertEqual(str(product), "Produk Test")

    # Test untuk URL dan template
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/skibidi/')
        self.assertEqual(response.status_code, 404)
