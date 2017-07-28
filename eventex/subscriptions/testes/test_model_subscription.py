from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription

class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Igor',
            cpf='12345678901',
            email='i@i.com.br',
            phone='987654321',
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_create_at(self):
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Igor', str(self.obj))

    def test_paid_default_to_false(self):
        self.assertEqual(False, self.obj.paid)
