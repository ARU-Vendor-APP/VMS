from django.test import TestCase
from .serializers import ProductSerializer, CategorySerializer, PricingSerializer, UserSerializer, FreeTrialSerializer, ReviewSerializer
def test_vendor_model(self):
    self.assertEqual(
        self.vendor.name,
        'vendor'
    )
    self.assertEqual(
        self.vendor.email,
        "vendor1@example.com"
    )
    self.assertEqual(
        self.vendor.phone,
        "+919876543210"
    )
    self.assertEqual(
        self.vendor.is_deleted,
        False
    )

def test_create_vendor(self):
    vendor = Vendor.objects.create_vendor(
        name='vendor',
        email = "vendor1@example.com",
        phone = "+919876543210",
        password = "password"
    )
    self.assertEqual(
        vendor.name,
        'vendor'
    )
    self.assertEqual(
        vendor.email,
        "vendor1@example.com"
    )
    self.assertEqual(
        vendor.phone,
        "+919876543210"
    )
    self.assertEqual(
        vendor.is_deleted,
        False
    )
    self.assertTrue(
        vendor.is_active
    )
    self.assertTrue(
        vendor.check_password('password')
    )
    self.assertFalse(
        vendor.check_password('wrong')
    )
    self.assertIsNotNone(
        vendor.date_joined
    )
    self.assertIsNotNone(
        vendor.last_login
    )
    self.assertIsNotNone(
        vendor.id
    )

def test_product_model(self):
    self.assertEqual(
        self.product.name,
        'product'
    )
    self.assertEqual(
        self.product.description,
        'description'
    )
    self.assertEqual(
        self.product.is_deleted,
        False
    )
    self.assertEqual(
        self.product.is_active,
        True
    )
    self.assertEqual(
        self.product.category,
        self.category
    )
    self.assertEqual(
        self.product.pricing,
        self.pricing
    )
    self.assertEqual(
        self.product.free_trial,
        self.free_trial
    )
def test_product_view(self):
    response = self.client.get('/product/')
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, 'product')
    self.assertContains(response, 'description')
    self.assertContains(response, self.category)
    self.assertContains(response, self.pricing)
    self.assertContains(response, self.free_trial)

def test_product_serializer(self):
    serializer = ProductSerializer(self.product)
    self.assertEqual(
        serializer.data,
        {
            'name': 'product',
            'description': 'description',
            'is_deleted': False,
            'is_active': True,
            'category': self.category,
            'pricing': self.pricing,
            'free_trial': self.free_trial
        }
    )
# Create your tests here.
