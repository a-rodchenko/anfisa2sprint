from django.db import models

from core.models import PublishedModel


class Category(PublishedModel):
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    slug = models.SlugField(max_length=64, unique=True, verbose_name='Слаг')
    output_order = models.PositiveSmallIntegerField(default=100, verbose_name='Порядок отображения')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории' 

    def __str__(self):
        return self.title


class Topping(PublishedModel):
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    slug = models.SlugField(max_length=64, unique=True, verbose_name='Слаг')

    class Meta:
        verbose_name = 'топпинг'
        verbose_name_plural = 'Топпинги' 

    def __str__(self):
        return self.title


class Wrapper(PublishedModel):
    title = models.CharField(max_length=256, verbose_name='Заголовок')

    class Meta:
        verbose_name = 'обёртка'
        verbose_name_plural = 'Обёртки' 

    def __str__(self):
        return self.title


class IceCream(PublishedModel):
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    output_order = models.PositiveSmallIntegerField(default=100, verbose_name='Порядок отображения')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    wrapper = models.OneToOneField(
        Wrapper,
        on_delete=models.SET_NULL,
        related_name='ice_cream',
        null=True,
        blank=True,
        verbose_name='Обёртка'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='ice_creams',
        verbose_name='Категория'
    )
    toppings = models.ManyToManyField(Topping)
    is_on_main = models.BooleanField(default=False, verbose_name='На главной')

    class Meta:
        verbose_name = 'мороженое'
        verbose_name_plural = 'Мороженое'
        ordering = ('output_order', 'title')


    def __str__(self):
        return self.title
