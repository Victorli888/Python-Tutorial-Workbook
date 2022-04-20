"""My cake shop is so popular, I'm adding some tables and hiring wait staff so folks can have a cute sit-down
cake-eating experience.

I have two registers: one for take-out orders, and the other for the other folks eating inside the cafe.
All the customer orders get combined into one list for the kitchen, where they should be handled first-come,
first-served.

Recently, some customers have been complaining that people who placed orders after them are getting their food first.
Yikes—that's not good for business!

To investigate their claims, one afternoon I sat behind the registers with my laptop and recorded:

"""

## Interview Cake solution
def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):
    take_out_orders_index = 0
    dine_in_orders_index = 0
    take_out_orders_max_index = len(take_out_orders) - 1
    dine_in_orders_max_index = len(dine_in_orders) - 1

    for order in served_orders:
        # If we still have orders in take_out_orders
        # and the current order in take_out_orders is the same
        # as the current order in served_orders
        if take_out_orders_index <= take_out_orders_max_index and order == take_out_orders[take_out_orders_index]:
            take_out_orders_index += 1

        # If we still have orders in dine_in_orders
        # and the current order in dine_in_orders is the same
        # as the current order in served_orders
        elif dine_in_orders_index <= dine_in_orders_max_index and order == dine_in_orders[dine_in_orders_index]:
            dine_in_orders_index += 1

        # If the current order in served_orders doesn't match the current
        # order in take_out_orders or dine_in_orders, then we're not serving first-come,
        # first-served.
        else:
            return False

    # Check for any extra orders at the end of take_out_orders or dine_in_orders
    if dine_in_orders_index != len(dine_in_orders) or take_out_orders_index != len(take_out_orders):
        return False

    # All orders in served_orders have been "accounted for"
    # so we're serving first-come, first-served!
    return True


"""
The goal of this program is to verify to make sure all orders placed through take-out and dine-in are accounted for
. The program must also verify orders being processed are following "First in First out". Whether the order is take-out
or dine-in the order that was placed first should be executed first.
"""

# My solution:
def FIFO(take_out, dine_in, queue):
    # Create your pointers
    take_out_index = 0
    dine_in_index = 0
    take_out_end = len(take_out) - 1  # this the max index for take-out
    dine_in_end = len(dine_in) - 1  # this is the max index for dine-in

    # Create the verifying process
    for order in queue:
        # IF our current take out index hasn't reached the end of our take_out array
        # AND order index is EQUAL to the value at or take_out_index.
        # move the take-out index forward
        if take_out_index <= take_out_end and order == take_out[take_out_index]:
            take_out_index += 1

        # IF our current dine-in index hasn't reached the end of our array
        # AND our order index value is equal to the dine_in[index value]
        # move the dine-in index forward
        elif dine_in_index <= dine_in_end and order == dine_in[dine_in_index]:
            dine_in_index += 1

        # IF the current order in the queue doesn't match the current orders in dine-in take-out,
        # That would mean it is not following FIFO
        else:
            return False
    #peform a check if we've processed all the orders in take_out and dine_in
    if dine_in_index != len(dine_in) or take_out_index != len(take_out):
       return False

    # All our orders have been processed and accounted for, this means we're following FIFO
    return True

# this is an alternate solution
def FIFO2(take_out,dine_in,queue):
    # init pointers
    take_out_pointer = 0
    dine_in_pointer = 0
    take_out_index_max = len(take_out)-1
    dine_in_index_max = len(dine_in)-1

    # Verify orders are being placed...
    for order in queue:
        take_out_exhausted = take_out_index_max < take_out_pointer
        dine_in_exhausted = dine_in_index_max < dine_in_pointer

        # IF take_out_index_max hasn't been reached AND take_out_pointer value == order then we can move our pointer
        # we expect to only move our pointer value if the order has indeed been processed
        if not take_out_exhausted and take_out[take_out_pointer] == order:
            take_out_pointer += 1

        # same IF for dine-in customers
        elif not dine_in_exhausted and dine_in[dine_in_pointer] == order:
            dine_in_pointer += 1

        # If both dine-in and take-out orders aren't exhausted  or the order values don't match then that means we are
        # not peforming FIFO so we need to return FALSE to show that our restaurant orders are not all accounted for
        else:
            return False

        # Consider this edge case, What if our queue has less values than our take_out & dine_in  lists, even if they're
        # exhausted and all the orders match something is wrong because we missing order in the queue that is not being
        # accounted for.

        # our lists are not exhausted and  the pointer values match so the for loop doesn't terminate, so we get a
        # return true value

        # we need to create a check to make sure all indexes in dine in and take out have been processed.
    if dine_in_pointer != len(dine_in) or take_out_pointer != len(take_out):
        return False

    return True
out = [1,3,5]
dine_in = [2,4,6]
served = [1,2,3,4,5,6]

x = FIFO(out,dine_in,served)
print(x)