from django.db import models
from core.abstract.models import AbstractModel, AbstractManager


def product_directory_path(instance, filename):
    return "product_{0}/{1}".format(instance.public_id, filename)


class Category(AbstractModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ProductQuerySet(models.QuerySet):
    def active(self):
        """ Display only active products """
        return  self.filter(is_active=True, is_deleted=False)

    def by_price(self, price_code):
        """ Display only products by price code """
        return self.filter(pricing=price_code)

    def has_free_trial(self):
        """ Display only products with free trial """
        return self.filter(free_trials__in=['7D', '30D'])


class ProductManager(AbstractManager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def active(self):
        """ Display only active products """
        return self.get_queryset().active()

    def by_price(self, price_code):
        return self.get_queryset().by_price(price_code)

    def with_free_trial(self):
        return self.get_queryset().has_free_trial()


class Product(AbstractModel):

    PRICING_CHOICES = (
            ('BSC', 'Basic'),
            ('STD', 'Standard'),
            ('PRM', 'Premium')
    )

    FREE_TRIALS_CHOICES = (
            ('NONE', 'No Free Trial'),
            ('7D', '7 days'),
            ('30D', '30 days')
    )

    author = models.ForeignKey(
        to='core_user.User',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    pricing = models.CharField(max_length=3, choices=PRICING_CHOICES, default='BSC', blank=True, null=True)
    free_trials = models.CharField(max_length=4, choices=FREE_TRIALS_CHOICES, default='NONE', blank=True, null=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )
    image_url = models.ImageField(max_length=2083, upload_to=product_directory_path, blank=True, null=True)
    description = models.TextField()
    video_url = models.URLField(max_length=2083, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    link = models.URLField(max_length=2083)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    statistics = models.JSONField()
    report_file = models.FileField(upload_to=product_directory_path, blank=True, null=True)
    is_deleted = models.BooleanField(default=False, db_index=True)
    is_active = models.BooleanField(default=True, db_index=True)
    edited = models.BooleanField(editable=False)

    objects = ProductManager()

    def __str__(self):
        return f'{self.author.name} added {self.title}'

    class Meta:
        db_table = 'core.product'
