import itertools
import numbers
from datetime import timedelta, datetime
from collections import namedtuple
import unittest
from Project_1.Transactions import TimeZone, Account

class TestAccount(unittest.TestCase):
    # We also have the option of defining setup and tear down functionality -
    # these are just methods that will be executed before each test method, and right after.
    def setUp(self) -> None:
        print('Running setup...')
        self.account_number = 'A100'

    def tearDown(self) -> None:
        print('Running tear down...')

    # def test_1(self):
    #     self.account_number = 'A200'
    #     self.assertTrue('A200', self.account_number)
    #
    # def test_2(self):
    #     self.assertTrue('A100', self.account_number)

    # test timezone class
    def test_create_timezone(self):
        tz = TimeZone('ABC', -1, -30)
        self.assertEqual('ABC', tz.name)
        self.assertEqual(timedelta(hours=-1, minutes=-30), tz.offset)

    def test_timezones_equal(self):
        tz1 = TimeZone('ABC', -1, -30)
        tz2 = TimeZone('ABC', -1, -30)
        self.assertEqual(tz1, tz2)

    def test_timezones_not_equal(self):
        tz = TimeZone('ABC', -1, -30)

        test_timezones = (
            TimeZone('DEF', -1, -30),
            TimeZone('ABC', -1, 0),
            TimeZone('ABC', 1, -30)
        )
        for i, test_tz in enumerate(test_timezones):
            with self.subTest(test_number=i):
                self.assertNotEqual(tz, test_tz)

    # test account class
    def test_create_account(self):
        account_number = 'A100'
        first_name = 'FIRST'
        last_name = 'LAST'
        tz = TimeZone('TZ', 1, 30)
        balance = 100.00

        # test whether the attributes are set up as expected.
        a = Account(account_number, first_name, last_name, tz, balance)
        self.assertEqual(account_number, a.account_number)
        self.assertEqual(first_name, a.first_name)
        self.assertEqual(last_name, a.last_name)
        self.assertEqual(first_name + ' ' + last_name, a.full_name)
        self.assertEqual(tz, a.timezone)
        self.assertEqual(balance, a.balance)

    # One last piece of unit testing functionality, is handling exceptions
    # when they are expected, for example creating an account with an empty
    # first name should result in a ValueError exception.
    # We can write a unit test that will test this expected exception,
    # and which will fail if the exception is not encountered
    # (or is a different exception).
    def test_create_account_blank_first_name(self):
        account_number = 'A100'
        first_name = ''
        last_name = 'LAST'
        tz = TimeZone('TZ', 1, 30)
        balance = 100.00

        with self.assertRaises(ValueError):
            a = Account(account_number, first_name, last_name, tz, balance)

    # If self._balance is not validated, we are not raising an exception!
    # That's a bug in our code.
    def test_create_account_negative_balance(self):
        account_number = 'A100'
        first_name = 'FIRST'
        last_name = 'LAST'
        tz = TimeZone('TZ', 1, 30)
        balance = -100.00

        with self.assertRaises(ValueError):
            a = Account(account_number, first_name, last_name, tz, balance)

    def test_account_deposit_ok(self):
        account_number = 'A100'
        first_name = 'FIRST'
        last_name = 'LAST'
        balance = 100.00

        a = Account(account_number, first_name, last_name, initial_balance=balance)
        conf_code = a.deposit(100)
        self.assertEqual(200, a.balance)
        self.assertIn('D-', conf_code)

    def test_account_deposit_negative_amount(self):
        account_number = 'A100'
        first_name = 'FIRST'
        last_name = 'LAST'
        balance = 100.00

        a = Account(account_number, first_name, last_name, initial_balance=balance)
        with self.assertRaises(ValueError):
            conf_code = a.deposit(-100)

    def test_account_withdraw_ok(self):
        account_number = 'A100'
        first_name = 'FIRST'
        last_name = 'LAST'
        balance = 100.00

        a = Account(account_number, first_name, last_name, initial_balance=balance)
        conf_code = a.withdraw(20)
        self.assertEqual(80, a.balance)
        self.assertIn('W-', conf_code)

    def test_account_withdraw_overdraw(self):
        account_number = 'A100'
        first_name = 'FIRST'
        last_name = 'LAST'
        balance = 100.00

        a = Account(account_number, first_name, last_name, initial_balance=balance)
        conf_code = a.withdraw(200)
        self.assertIn('X-', conf_code)
        self.assertEqual(balance, a.balance)