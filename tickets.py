def tickets(people):
    ticket_price = 25
    register = {25: 0, 50: 0, 100: 0}

    for bill in people:
        if bill not in register.keys():
            return 'NO'

        change = bill - ticket_price

        if bill == 25:
            register[25] += 1

        if bill == 50:
            if register.get(25) >= 1:
                register[25] -= 1
                register[50] += 1
            else:
                return 'NO'

        if bill == 100:
            if register.get(50) >= 1 and register.get(25) >= 1:
                register[50] -= 1
                register[25] -= 1
                register[100] += 1
            elif register.get(25) >= 3:
                register[25] -= 3
            else:
                return 'NO'

    return 'YES'

print tickets([25, 25, 50]), "YES"
print tickets([25, 100]), "NO"
print tickets([25, 50, 50]), 'NO'