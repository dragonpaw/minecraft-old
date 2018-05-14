from django.db import models
from django.utils.translation import ugettext as _
from collections import defaultdict
from decimal import Decimal

# Create your models here.
class Item(models.Model):
    name = models.CharField('Name', max_length=80, unique=True)
    ingredients = models.ManyToManyField('self', through='Ingredient', symmetrical=False)
    slug = models.SlugField(max_length=80)
    batch_size = models.SmallIntegerField(default=1)

    class Meta:
        verbose_name = _('Item')
        verbose_name_plural = _('Items')
        ordering = ('name',)

    def __unicode__(self):
        return self.name

    def __lt__(self, other):
        return self.name < other.name

    @models.permalink
    def get_absolute_url(self):
        return ('dpminecraft.apps.minecraft.views.item_detail', [self.slug])

    def raw_materials(self):
        if self.ingredients.count() == 0:
            return {self: 1}
        else:
            mats = defaultdict(int)
            for i in Ingredient.objects.filter(makes=self):
                # Zero mats don't recurse, as they are not consumed.
                if i.quantity == 0:
                    mats[i.item] += i.quantity
                else:
                    sub_mats = i.item.raw_materials()
                    for mat in sub_mats:
                        mats[mat] += sub_mats[mat] * Decimal(i.quantity) / Decimal(self.batch_size)
            return mats

class Ingredient(models.Model):
    makes = models.ForeignKey('Item')
    quantity = models.DecimalField(_('Quantity'), max_digits=5, decimal_places=2, default=1)
    item = models.ForeignKey('Item', related_name='makes')

    class Meta:
        verbose_name = _('Ingredient')
        verbose_name_plural = _('Ingredients')
        ordering = ('makes', 'item',)

    def __unicode__(self):
        return u"{0}x {1}".format(self.quantity, self.item.name)

    def quantity_each(self):
        return Decimal(self.quantity) / Decimal(self.makes.batch_size)
