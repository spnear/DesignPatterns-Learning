from context import PaymentProcessor
from strategy import PercentageCommission, FixedCommission


def main():
    amount = 100
    processor = PaymentProcessor(FixedCommission())
    payment = processor.process_payment(amount)
    print(payment)


    processor = PaymentProcessor(PercentageCommission())
    print(processor.process_payment(amount))

if __name__ == '__main__':
    main()