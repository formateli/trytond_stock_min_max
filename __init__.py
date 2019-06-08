# This file is part of trytond-stock_min_max module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.

from trytond.pool import Pool
from . import product

def register():
    Pool.register(
        product.Template,
        product.Product,
        product.ProductMinMax,
        module='stock_min_max', type_='model')
