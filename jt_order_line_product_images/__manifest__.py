# -*- coding: utf-8 -*-
##############################################################################
#
#    Jupical Technologies Pvt. Ltd.
#    Copyright (C) 2019-TODAY Jupical Technologies(<http://www.jupical.com>).
#    Author: Jupical Technologies Pvt. Ltd.(<http://www.jupical.com>)
#    you can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    GENERAL PUBLIC LICENSE (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Images produit voltere',
    'summary': 'Shows product images',
    'version': '16.0.1.0',
    'category': 'extra',
    'author':'Moh',
    'maintainer': 'Moh',
    'website': 'https://cv-lahrech-mohamed.onrender.com/',
    'license': 'AGPL-3',
    'depends': ['base','sale_management','purchase','account','mrp','stock','sale'],
    'data': [
        'views/sale_order_line_images.xml',
        'views/mrp_order_line_images.xml',
        'views/purchase_order_line_images.xml',
        'views/invoice_order_line_images.xml',
        'views/stock_order_line_images.xml',
        'reports/sale_report.xml',
        'reports/sale_qweb_template.xml',
    ],

}
