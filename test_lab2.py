import ecommerce_form
import logging

logging.basicConfig(
    level=logging.DEBUG,
    filemode='w',
    filename='test.log'
)


def test_purchase_itemzero():
    logging.info('TEST CASE 1')

    system = ecommerce_form.OnlinePurchase()

    cart = {
        'Laptop': 0,
        'Mouse': 2
    }

    cupon = 'DISCOUNT10'
    address = 'Av patria'
    result = system.process_purchase(cart, cupon, address)

    assert 'integer greater than 0' in result
    logging.info('TEST CASE FINISHED')


def test_coupon_invalid():
    logging.info('TEST CASE 2 RF3')

    system = ecommerce_form.OnlinePurchase()

    cart = {
        'Laptop': 1,
        'Mouse': 2
    }

    cupon = 'DISCOUNT30'
    address = 'Av patria'
    result = system.process_purchase(cart, cupon, address)

    assert 'The entered coupon code is not valid.' in result
    logging.info(f'The purchase result is:{result}')
    logging.info('TEST CASE FINISHED')

def test_coupon_valid():
    logging.info('TEST CASE 3 RF9')

    system = ecommerce_form.OnlinePurchase()

    cart = {
        'Laptop': 1,
        'Mouse': 2
    }

    cupon = 'DISCOUNT10'
    address = 'Av patria'

    result = system.process_purchase(cart, cupon, address)
    assert 'DISCOUNT10' in result
    assert '990' in result
    logging.info(f'The purchase result is:{result}')
    logging.info('TEST CASE FINISHED')

if __name__ == '__main__':
    test_coupon_valid
    logging.info('The purchase result')