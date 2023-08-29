# Index of `views`
This guide provides in-depth explanations for various views within the project.

- [views_alert.py - Price Alerts](#price-alerts)
- [views_forum.py - Forum Message Board](#forum-message-board)
- [views_home.py - Home/Landing Page](#homelanding-page)
- [views_stocks.py - Stock Picker, Tracker, Graph, and Wallet](#stock-picker-tracker-graph-and-wallet)
- [views_user.py - User Login/Register Pages](#user-loginregister-pages)

## Price Alerts

The [views_alert.py](views_alert.py) module contains views related to price alerts for stocks. This includes creating, updating, and deleting price alerts for specific stock tickers. The views interact with the `Alerta` model and provide functionalities to set alert thresholds for buying and selling prices. Users can manage their price alerts through these views.

[Back to top](#index-of-views)

## Forum Message Board

The [views_forum.py](views_forum.py) module manages the forum message board feature of the project. It includes views for creating, viewing, updating, and deleting forum posts. Users can interact with the message board by posting messages, replying to threads, and managing their own posts. The views facilitate communication and engagement among users through the message board.

### Forum Views Documentation

#### `forum(request)`
View where users access existing chat rooms.

**Returns:**
- Template: forum.html
- Context: `rooms`, `topics`, `room_count`, `room_messages`

#### `room(request, pk)`
View to display a specific chat room.

**Args:**
- `pk`: Room ID

**Returns:**
- Template: room.html
- Context: `room`, `room_messages`, `participants`

#### `createRoom(request)`
View responsible for creating new chat rooms.

**Returns:**
- Template: room_form.html
- Context: Form for room creation

#### `updateRoom(request, pk)`
View for updating chat room details.

**Args:**
- `pk`: Room ID

**Returns:**
- Template: room_form.html
- Context: Pre-filled room form for editing

#### `deleteRoom(request, pk)`
View responsible for deleting chat rooms.

**Args:**
- `pk`: Room ID

**Returns:**
- Template: basic_delete.html
- Context: Room to be deleted

#### `deleteMessage(request, pk)`
View for deleting messages within chat rooms.

**Args:**
- `pk`: Message ID

**Returns:**
- Template: basic_delete.html
- Context: Message to be deleted

These views are part of the forum feature. They handle various aspects of the forum, including viewing chat rooms, entering specific rooms, creating rooms, updating and deleting rooms, as well as deleting messages within rooms. The views use authentication to ensure that users are logged in before accessing these functionalities. They interact with the `Room`, `Message`, and `Topic` models, along with associated forms. Additionally, error handling is incorporated using `ObjectDoesNotExist` exceptions and proper HTTP response codes.


[Back to top](#index-of-views)

## Home/Landing Page

The [views_home.py](views_home.py) module handles the main landing page of the application. It includes views that provide an overview of the project, showcase featured content, and offer navigation to various sections of the application. This page serves as the starting point for users to explore the project's functionalities.

### Home View

The `home` view renders the main home page of the web application.

#### Function Signature

```python
def home(request)
```

#### Parameters

- `request`: Represents the incoming HTTP request from the user's browser.

#### Behavior

The `home` view simply renders the 'home.html' template, which corresponds to the main landing page of the web application.

### 404 Error View

The `http_404_error` view handles 404 (Page Not Found) errors.

#### Function Signature

```python
def http_404_error(request, exception)
```

#### Parameters

- `request`: Represents the incoming HTTP request from the user's browser.
- `exception`: Represents the exception that triggered the 404 error.

#### Behavior

The `http_404_error` view renders the '404.html' template with an HTTP status code of 404. This template is displayed when a user tries to access a page that does not exist within the application.

[Back to top](#index-of-views)

## Stock Picker, Tracker, Graph, and Wallet

The [views_stocks.py](views_stocks.py) module encompasses a range of stock-related functionalities:

- Stock Picker: Provides a user interface for selecting stocks from a list and setting preferences.
- Stock Tracker: Displays real-time tracking of selected stocks' prices and updates.
- Graph: Generates graphical representations of stock price trends over time.
- Wallet: Allows users to manage their stock portfolio, including adding, updating, and removing stocks from their portfolio.

These views collectively enable users to monitor and manage their stock-related activities within the application.

### stockPicker View
- Allows users to select assets for price quotations.
- Receives the name of the market to present only assets belonging to that market.

### stockTracker View
- Receives selected assets from stockpicker for price research.
- Filters and validates valid tickers.
- Retrieves market data for the chosen assets.
- Uses multithreading to improve performance.

### configGraph View
- Displays graphs (using Plotly) for the chosen asset.
- Retrieves historical market data using the yfinance library.
- Generates candlestick and interactive range selectors.

### showCarteira View
- Displays the user's asset portfolio for tracking and balancing.
- Retrieves user-specific asset data and related market details.
- Creates pie charts to visualize asset distribution by notes and markets.

### createCarteira View
- Adds new assets to the user's balancing portfolio.
- Displays a form for adding assets to the portfolio.

### updateCarteira View
- Modifies information about assets added to the portfolio.
- Displays a form pre-filled with existing asset data for editing.

### deleteCarteira View
- Deletes an asset from the user's balancing portfolio.

[Back to top](#index-of-views)

## User Login/Register Pages

The [views_user.py](views_user.py) module handles user authentication and registration processes. It includes views for user login, registration, profile management, and password recovery. These views facilitate user account creation, authentication, and user-specific settings.

### loginPage - User Login

The `loginPage` view handles user authentication and redirects authenticated users to the forum page. Users can log in using their username and password. If the login is successful, the user is redirected to the forum; otherwise, an error message is displayed.

#### Functionality

- Authenticates user login
- Redirects authenticated users to the forum
- Displays error message on failed login attempt

### logoutUser - User Logout

The `logoutUser` view logs out the authenticated user and redirects them to the home page.

#### Functionality

- Logs out the authenticated user
- Redirects to the home page after logout

### registerPage - User Registration

The `registerPage` view manages user registration. It provides a form for users to register with a username, password, and email. If the registration is successful, the user is logged in automatically and redirected to the forum. If there are any errors, a registration error message is displayed.

#### Functionality

- Handles user registration
- Automatically logs in newly registered users
- Redirects to the forum on successful registration

### userProfile - User Profile

The `userProfile` view displays a user's profile page containing items created by the user. It requires the user to be logged in. The view retrieves information related to the user's rooms, room messages, topics, alerts, and market details. If the specified user profile doesn't exist, a 404 error page is displayed.

#### Functionality

- Displays a user's profile information
- Retrieves user-specific data such as rooms, messages, topics, alerts, and markets
- Handles non-existing user profiles with a 404 page

[Back to top](#index-of-views)

## Conclusion

Understanding these views and their functionalities will help you grasp the core features of our Django project. Feel free to explore each view's code to gain a deeper insight into their implementation.

If you have any questions or need assistance, please don't hesitate to ask!
