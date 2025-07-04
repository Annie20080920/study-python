from services.order_service import (
    read_orders, 
    calculate_customer_totals, 
    calculate_product_quantities, 
    calculate_product_revenue
)
from views.report_view import (
    print_total_per_customer, 
    print_product_quantities, 
    print_product_revenues
)

orders = read_orders()

customer_totals = calculate_customer_totals(orders)
product_quantities = calculate_product_quantities(orders)
product_revenues = calculate_product_revenue(orders)

print_total_per_customer(customer_totals)
print_product_quantities(product_quantities)
print_product_revenues(product_revenues)
