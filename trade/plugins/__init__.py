"""trade: Tools For Stock Trading Applications.

trade.plugins
-----------------------------------------------------------------------
This module provides the default plugins for the trade module.

Plugins are used to extend the trade module functionality. They can:

- Create new types of assets
- Create new types of operations
- Create new types of events
- Add functionalities to the OperationContainer
- Add functionalities to the Portfolio

The default plugins are:

- options
  provides the Option class, a subtype of asset.Derivative
  provides the Exercise class, a subtype of operation.Operation
  provides the fetch_exercises() task to the OperationContainer
  provides the get_exercise_premium() task to the Portfolio

- daytrades
  provides the Daytrade class, a subtype of operation.Operation
  provides the fetch_daytrades() task to the OperationContainer

- events
  provides the StockSplit class, a subtype of event.Event
  provides the ReverseStockSplit class, a subtype of event.Event

You may add the default plugins to your application or use them as a
base to create your own plugins.

-----------------------------------------------------------------------

Copyright (c) 2015 Rafael da Silva Rocha

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

from __future__ import absolute_import

from .events import StockSplit, ReverseStockSplit
from .options import Option, Exercise, fetch_exercises
from .daytrades import (
    Daytrade,
    fetch_daytrades,
    daytrade_condition,
    extract_daytrade,
    find_purchase_and_sale,
)
