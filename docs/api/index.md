# trade

trade is a Python module with functions and classes for the development
of investment applications in Python. It provides basic notions of assets,
operations, daytrades, cost deduction, asset accumulation and so on.

## Classes available:
+ trade.Asset  
  Representing assets.
+ trade.Operation  
  Representing operations with assets.
+ trade.Daytrade  
  Representing daytrade operations.
+ trade.OperationContainer  
  To identify daytrades, prorate comissions and apply taxes to operations.
+ trade.TaxManager  
  To get the right tax for each operation the OperationContainer identify.
+ trade.Accumulator  
  To accumulate the assets and calculate the result from the trades.
+ trade.Event  
  To change the asset's quantity and price on the accumulator.

## Functions available:
+ trade.daytrade_condition(operation_a, operation_b)
+ trade.average_price(quantity_1, price_1, quantity_2, price_2)
+ trade.same_sign(x, y)
+ trade.find_purchase_and_sale(operation_a, operation_b)

```python
import trade

# create the asset and the operation
asset = trade.Asset('some asset')
operation = trade.Operation(date='2015-09-18', asset=asset, quantity=20, price=10)

# create a container with some comissions associated with it
comissions = {
    'some comission': 1,
    'other comission': 3,
}
container = trade.OperationContainer(operations=[operation], comissions=comissions)

# identify common operations and daytrades,
# prorate the comissions and apply the taxes
container.fetch_positions()

# create an accumulator for the asset
accumulator = trade.Accumulator(asset)

# accumulate the operation
operation = container.common_operations[asset]
accumulator.accumulate_operation(operation)

print(accumulator.quantity)
#>>20

print(accumulator.price)
#>>10.2
# the original price (10) plus the comissions
# the OperationContainer prorated (default taxes are zero)

print(accumulator.price * accumulator.quantity)
#>>204
# 200 from the raw operation
# (20 quantity * 10 unitary price)
# + 4 from the total comissions

```

Check each module doc for more information.

## Modules in this package:
+ trade.accumulator (Accumulator, Event)
+ trade.operation (Asset, Operation, Daytrade)
+ trade.operation_container (OperationContainer)
+ trade.tax_manager (TaxManager)
+ trade.utils (all the functions)


Copyright (c) 2015 Rafael da Silva Rocha  
rocha.rafaelsilva@gmail.com  
http://github.com/rochars/trade  
http://trade.readthedocs.org  