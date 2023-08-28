import re

# using for loop
for i in range(int(input())):

    # taking the input credit card number
    card = input()
    try:
        assert re.search(r'^[456]', card)
        assert re.search(r'^(-?\d{4}){4}$', card)
        assert not re.search(r'(\d)(-?\1){3}', card)

    except:
        print('Invalid')
    else:
        print('Valid')
