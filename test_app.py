import io
import unittest
from unittest.mock import patch

import openpyxl
import app


def source(**changes):
    order = dict(order_number='TEST-01', status='processing', payment_method='cod',
                 order_total=250, order_currency='EGP', shipping_first_name='Test',
                 shipping_last_name='Customer', shipping_phone='', billing_phone='01000000000',
                 shipping_address_1='Test street', shipping_address_2='Unit 2',
                 shipping_country='EG', shipping_state='EGC', shipping_city='مدينه نصر',
                 line_item_1='name:Bricks|quantity:2|total:180', shipping_total=70)
    order.update(changes)
    book = openpyxl.Workbook()
    book.active.append(list(order))
    book.active.append(list(order.values()))
    stream = io.BytesIO()
    book.save(stream)
    return stream.getvalue()


class ConversionTests(unittest.TestCase):
    def parse(self, **changes):
        with patch.object(app, 'sender_settings', return_value={}):
            return app.parse_workbook(source(**changes))

    def test_shipping_phone_city_and_cod(self):
        row = self.parse()['rows'][0]
        self.assertEqual(row[2], '01000000000')
        self.assertEqual(row[4:6], ['القاهرة', 'مدينة نصر'])
        self.assertEqual(row[21], '250')  # Shipping is already included.
        self.assertEqual(row[7], 'Test street / Unit 2')
        self.assertEqual(row[6], '')  # Do not fabricate an area.

    def test_paid_order_no_collection(self):
        self.assertEqual(self.parse(payment_method='card', paid_date='2026-10-10')['rows'][0][21], '0')

    def test_uncertain_payment_blocks_export(self):
        row = self.parse(payment_method='card')['rows'][0]
        self.assertEqual(row[21], '')
        self.assertTrue(any('COD amount' in e for e in app.validate([row])))

    def test_multiple_products(self):
        row = self.parse(line_item_2='name:Flower|quantity:1')['rows'][0]
        self.assertEqual(row[16], 'Bricks × 2; Flower × 1')

    def test_refund_and_wrong_country_rejected(self):
        for changes in [dict(refund_items='refund'), dict(shipping_country='US')]:
            with self.assertRaises(ValueError):
                self.parse(**changes)

    def test_cancelled_not_exported(self):
        with self.assertRaises(ValueError):
            self.parse(status='cancelled')

    def test_missing_area_blocks_export(self):
        with self.assertRaises(ValueError):
            app.export_xls(self.parse()['rows'])

    def test_valid_xls_and_negative_amount(self):
        row = self.parse()['rows'][0]
        row[6] = 'Test area'
        row[8:15] = ['Test sender', '01000000000', '', 'القاهرة', 'مدينة نصر', 'Test area', 'Test street']
        self.assertEqual(app.validate([row]), [])
        self.assertTrue(app.export_xls([row]).startswith(bytes.fromhex('d0cf11e0')))
        row[21] = '-1'
        self.assertTrue(app.validate([row]))


if __name__ == '__main__':
    unittest.main()
