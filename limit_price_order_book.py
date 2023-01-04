class Order:
    def __init__(self, price, quantity, side):
        self.price = price
        self.quantity = quantity
        self.side = side  # "buy" or "sell"

class OrderBook:
    def __init__(self):
        self.buy_orders = []  # list of buy orders, sorted in descending order by price
        self.sell_orders = []  # list of sell orders, sorted in ascending order by price

    def add_order(self, order):
        if order.side == "buy":
            self.buy_orders.append(order)
            self.buy_orders.sort(key=lambda x: -x.price)
        elif order.side == "sell":
            self.sell_orders.append(order)
            self.sell_orders.sort(key=lambda x: x.price)

    def match(self):
        """Match buy and sell orders with the same price, until either the buy or sell queue is empty."""
        while self.buy_orders and self.sell_orders:
            buy_order = self.buy_orders[0]
            sell_order = self.sell_orders[0]
            if buy_order.price < sell_order.price:
                break  # no more matching orders
            # matched orders have the same price
            quantity = min(buy_order.quantity, sell_order.quantity)
            buy_order.quantity -= quantity
            sell_order.quantity -= quantity
            if buy_order.quantity == 0:
                self.buy_orders.pop(0)  # remove fully filled buy order
            if sell_order.quantity == 0:
                self.sell_orders.pop(0)  # remove fully filled sell order

# Example usage
order_book = OrderBook()
order_book.add_order(Order(100, 10, "buy"))
order_book.add_order(Order(90, 5, "buy"))
order_book.add_order(Order(110, 15, "sell"))
order_book.add_order(Order(105, 10, "sell"))
order_book.match()
