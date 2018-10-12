# This file is part of trytond-stock_min_max module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.

from trytond.pool import Pool, PoolMeta
from trytond.model import ModelSQL, fields
from trytond.pyson import Eval
from trytond.modules.company.model import (
    CompanyMultiValueMixin, CompanyValueMixin)

__all__ = ['Product', 'Template', 'ProductMinMax']


class Template:
    __metaclass__ = PoolMeta
    __name__ = "product.template"

    uom_min = fields.Many2One('product.uom', 'UOM for min qty', states={
            'readonly': ~Eval('active'),
            },
        domain=[('category', '=', Eval('default_uom_category'))],
        depends=['active', 'default_uom_category'])
    uom_max = fields.Many2One('product.uom', 'UOM for max qty', states={
            'readonly': ~Eval('active'),
            },
        domain=[('category', '=', Eval('default_uom_category'))],
        depends=['active', 'default_uom_category'])


class Product(CompanyMultiValueMixin):
    __metaclass__ = PoolMeta
    __name__ = "product.product"

    quantity_min = fields.MultiValue(fields.Float('Min quantity limit'))
    quantity_max = fields.MultiValue(fields.Float('Max quantity limit'))
    quantities = fields.One2Many(
        'product.product.min_max', 'product', "Quantities")

    @classmethod
    def multivalue_model(cls, field):
        pool = Pool()
        if field in {'quantity_min', 'quantity_max'}:
            return pool.get('product.product.min_max')
        return super(Product, cls).multivalue_model(field)


class ProductMinMax(ModelSQL, CompanyValueMixin):
    "Product quantity min and max"
    __name__ = 'product.product.min_max'

    product = fields.Many2One(
        'product.product', "Product", ondelete='CASCADE', select=True)
    quantity_min = fields.Float('Min quantity limit')
    quantity_max = fields.Float('Max quantity limit')
