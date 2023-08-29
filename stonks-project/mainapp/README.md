# Index

- [Templates Folder](templates/mainapp)
- [Views Folder](views)
- [Tasks Documentation](#tasks-documentation)
- [WebSocket Routing Documentation](#websocket-routing-documentation)
- [Forms Documentation](#forms-documentation)
- [URLs Documentation](#urls-documentation)

# Tasks Documentation

This section explains the tasks defined in the Django [tasks.py](tasks.py) file and their functionalities.

## Live Stocks Information Update Task

### Description:
The `update_stock` task is responsible for fetching real-time stock quotes for a list of selected assets (`stockpicker`) and updating the information to be displayed in the `stocktracker`. It uses the Celery library to perform asynchronous tasks and Channel Layer to communicate with clients in real-time.

### Parameters:
- `self` (implicitly bound): The task instance.
- `stockpicker` (List): A list of selected assets for which real-time quotes need to be fetched.

### Functionality:
1. Initialize necessary variables and import required libraries and modules.

2. Fetch the list of available stocks using the `tickers_ibovespa` function.

3. Filter out stocks from `stockpicker` that are no longer available.

4. Create multiple threads (one for each stock) to fetch real-time stock quotes concurrently.

5. For each thread, retrieve the stock quote using the `get_quote_table` function and store it in a queue.

6. Combine the fetched stock quotes from the queue into a `data` dictionary.

7. Send the updated stock information to the `stock_track` group in the Channel Layer, ensuring real-time updates for multiple users.

### Usage:
The `update_stock` task is designed to be executed asynchronously using Celery. It can be called from Django views or other parts of your application that require real-time stock information updates.

```python
from .tasks import update_stock

# Calling the task asynchronously
result = update_stock.delay(stockpicker)
print(result.get())  # Prints the task result ('update_stock() -> Done.')
```

# WebSocket Routing Documentation

This section explains the WebSocket routing configuration in Django using the provided [routing.py](routing.py) file.

## WebSocket Routing Configuration

The WebSocket routing configuration allows you to handle WebSocket connections and route them to appropriate consumers in your Django project. WebSocket connections are used for real-time communication between clients and the server.

### Import Statements

```python
from django.urls import re_path
from . import consumers
```

In this section, necessary import statements are made. The `re_path` function is used to define the WebSocket URL patterns, and the `consumers` module is imported, where the WebSocket consumer classes are defined.

### WebSocket URL Pattern

```python
websocket_urlpatterns = [
    re_path(r'ws/stock/(?P<room_name>\w+)/$', consumers.StockConsumer.as_asgi()),
]
```

The `websocket_urlpatterns` list defines the WebSocket URL patterns for your application. Each URL pattern maps a URL to a specific WebSocket consumer.

In the provided example, a single URL pattern is defined:
- `r'ws/stock/(?P<room_name>\w+)/$'`: This pattern matches WebSocket connections with URLs of the form `ws/stock/<room_name>/`, where `<room_name>` is a parameter that matches a sequence of word characters.
- `consumers.StockConsumer.as_asgi()`: This specifies the consumer class that will handle WebSocket connections for this URL pattern. In this case, the `StockConsumer` class from the `consumers` module is used.

## Summary

WebSocket routing in Django allows you to define URL patterns that correspond to WebSocket consumers. This enables real-time communication between clients and the server using WebSockets. The provided `routing.py` file demonstrates how to define a WebSocket URL pattern and associate it with a consumer class.

# Forms Documentation 
[forms.py](forms.py)
## Register Form: `SignUpForm`

A form for creating a new user account.

### Fields:
- `username`: User's name
- `email`: User's email
- `password1`: Password
- `password2`: Confirm password

### Description:
The `SignUpForm` is used for creating a new user account with a username, email, and password. It inherits from `UserCreationForm` and customizes the appearance of its fields.

## Room Create Message Form: `RoomForm`

A form for creating/editing a chat room.

### Fields:
- `name`: Room's title
- `description`: Room's content

### Description:
The `RoomForm` is used for creating or editing a chat room. It captures the room's title and content. The form is associated with the `Room` model and excludes the 'host' and 'participants' fields.

## Alert Form: `AlertForm`

A form for creating/editing price alerts.

### Fields:
- `email`: Email for alerts
- `ativo`: Ticker
- `compra`: Purchase price
- `venda`: Selling price
- `periodo`: Minutes between searches
- `duracao`: Operating days

### Description:
The `AlertForm` allows users to create or edit price alerts for specific assets. It captures details such as email, ticker, purchase and selling prices, search interval, and operating days.

## Carteira Form: `CarteiraForm`

A form for adding/editing an asset in the user's portfolio.

### Fields:
- `ativo`: Ticker
- `preco_medio`: Average price
- `quantidade`: Total quantity
- `nota`: Weight in the portfolio

### Description:
The `CarteiraForm` enables users to add or edit assets in their portfolio. It collects information about the asset's ticker, average price, quantity, and weight in the portfolio.
    

# URLs Documentation
[urls.py](urls.py)
## URL Configuration

This document outlines the URL patterns used in the Django project.

### Favicon Redirect

- Path: `/favicon.ico`
- Redirects to the favicon image using `staticfiles_storage.url()`

### Home

- Path: `/`
- View: `views.home`
- Name: `home`

### User Actions

- Path: `/login/`
- View: `views.loginPage`
- Name: `login`

- Path: `/logout/`
- View: `views.logoutUser`
- Name: `logout`

- Path: `/register/`
- View: `views.registerPage`
- Name: `register`

- Path: `/profile/<str:pk>/`
- View: `views.userProfile`
- Name: `user-profile`

### Forum Actions

- Path: `/forum/`
- View: `views.forum`
- Name: `forum`

- Path: `/room/<str:pk>/`
- View: `views.room`
- Name: `room`

- Path: `/create-room/`
- View: `views.createRoom`
- Name: `create-room`

- Path: `/update-room/<str:pk>/`
- View: `views.updateRoom`
- Name: `update-room`

- Path: `/delete-room/<str:pk>/`
- View: `views.deleteRoom`
- Name: `delete-room`

- Path: `/delete-message/<str:pk>/`
- View: `views.deleteMessage`
- Name: `delete-message`

### Alerts

- Path: `/alerts/`
- View: `views.alerts`
- Name: `alerts`

- Path: `/create-alert/`
- View: `views.createAlert`
- Name: `create-alert`

- Path: `/update-alert/<str:pk>/`
- View: `views.updateAlert`
- Name: `update-alert`

- Path: `/delete-alert/<str:pk>/`
- View: `views.deleteAlert`
- Name: `delete-alert`

### Stocks

- Path: `/stockpicker/<str:pk>`
- View: `views.stockPicker`
- Name: `stockpicker`

- Path: `/stocktracker`
- View: `views.stockTracker`
- Name: `stocktracker`

- Path: `/graph`
- View: `views.configGraph`
- Name: `graph`

- Path: `/carteira`
- View: `views.showCarteira`
- Name: `carteira`

- Path: `/create-carteira/`
- View: `views.createCarteira`
- Name: `create-carteira`

- Path: `/update-carteira/<str:pk>/`
- View: `views.updateCarteira`
- Name: `update-carteira`

- Path: `/delete-carteira/<str:pk>/`
- View: `views.deleteCarteira`
- Name: `delete-carteira`
