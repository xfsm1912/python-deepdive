import itertools

flag = False

if flag:
    class TransactionID:
        def __init__(self, start_id):
            self.__start_id = start_id

        def next(self):
            self.__start_id += 1
            return self.__start_id


    class Account:
        transaction_counter = TransactionID(100)

        def make_transaction(self):
            new_trans_id = Account.transaction_counter.next()
            return new_trans_id


    a1 = Account()
    a2 = Account()

    print('method1')
    print(a1.make_transaction())
    print(a2.make_transaction())
    print(a1.make_transaction())

flag = False
if flag:
    # generator approach
    def transaction_ids(start_id):
        while True:
            start_id += 1
            yield start_id

    class Account:
        transaction_counter = transaction_ids(100)

        def make_transaction(self):
            new_trans_id = next(Account.transaction_counter)
            return new_trans_id


    a1 = Account()
    a2 = Account()

    print('method2')
    print(a1.make_transaction())
    print(a2.make_transaction())
    print(a1.make_transaction())

flag = True
if flag:
    class Account:
        transaction_counter = itertools.count(100)

        def make_transaction(self):
            new_trans_id = next(Account.transaction_counter)
            return new_trans_id


    a1 = Account()
    a2 = Account()

    print('method3')
    print(a1.make_transaction())
    print(a2.make_transaction())
    print(a1.make_transaction())