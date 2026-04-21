import unittest

from app import Payment, route_payment


class PaymentRoutingTests(unittest.TestCase):
    def test_cross_provider_route(self):
        payment = Payment("Asha", "Hassan", 25.0, "ZAAD", "Premier Bank")
        message = route_payment(payment)
        self.assertIn("UnifiedPay", message)
        self.assertIn("SUCCESS", message)

    def test_direct_route(self):
        payment = Payment("Ali", "Muna", 5.0, "EVC Plus", "EVC Plus")
        message = route_payment(payment)
        self.assertIn("direct ledger transfer", message)

    def test_invalid_amount(self):
        payment = Payment("Ali", "Muna", 0.0, "EVC Plus", "ZAAD")
        with self.assertRaises(ValueError):
            route_payment(payment)


if __name__ == "__main__":
    unittest.main()
