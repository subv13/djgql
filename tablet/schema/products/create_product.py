# coding=utf-8
# future
from __future__ import absolute_import, unicode_literals

import graphene

from tablet.schema.products.types import Product
from tablet.services.product_services.create_product import create_product


class CreateProductMutation(graphene.Mutation):
    """
    # Создаёт продукт с двумя полями

    **Поля**
    1. Название
    1. Категория
    """

    class Arguments(object):
        name = graphene.String(required=True, description="Название продукта")
        category = graphene.String(required=True, description="Категория продукта")

    product = graphene.Field(Product)

    @staticmethod
    def mutate(_parent, _info, name, category):
        product = create_product(Product(name=name, category=category))

        return CreateProductMutation(product=product)
