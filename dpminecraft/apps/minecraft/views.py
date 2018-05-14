import math

from django.shortcuts import render, get_object_or_404

from models import Item, Ingredient

def item_index(request):
    return render(request, 'minecraft/index.html', {
        'items': Item.objects.all(),
    })

def item_detail(request, slug):
    item = get_object_or_404(Item, slug=slug)

    materials = item.raw_materials()
    final_mats = list()
    for x in sorted(materials.keys()):
        final_mats.append([
            x, int(math.ceil(materials[x])), materials[x]
        ])

    return render(request, 'minecraft/item_detail.html', {
        'item': item,
        'ingredients': item.ingredient_set.all(),
        'materials': final_mats,
        'uses': Ingredient.objects.filter(item=item),
    })
