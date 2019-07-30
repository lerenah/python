def is_first_come_first_served(take_out, dine_in, served_orders):
    for i in range(len(served_orders)):
        if len(take_out) and len(dine_in):
            if served_orders[i] == take_out[0]:
                take_out.pop(0)
            elif served_orders[i] == dine_in[0]:
                dine_in.pop(0)
            else:
                return False
        elif len(dine_in) and not len(take_out):
            if served_orders[i] == dine_in[0]:
                dine_in.pop(0)
            else:
                return False
        elif len(take_out) and not len(dine_in):
            if served_orders[i] == take_out[0]:
                take_out.pop(0)
            else:
                return False
        else:
            return False

    return True
