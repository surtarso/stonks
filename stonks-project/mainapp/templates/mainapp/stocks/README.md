# Index of `stocks`

- [Stock Picker](#stock-picker-page-documentation)
- [Stock Tracker](#stock-tracker-page-documentation)
- [Stock Graphs](#stock-graphs-page-documentation)

# Stock Picker Page Documentation
<p><img src="../../../../../shots/picker.png" width="50%" height="50%"></p>

The [stockpicker.html](stockpicker.html) page provides users with the ability to select and track stocks within a chosen market. This page allows users to choose specific stocks from a dropdown menu, enabling them to monitor the stock prices and relevant information.

## Contents

1. [Extending Base Template](#extending-base-template)
2. [Page Title](#page-title)
3. [Stock Picker Form](#stock-picker-form)
4. [Stock Selection](#stock-selection)
5. [Search Button](#search-button)

## Extending Base Template

```html
{% extends 'mainapp/basic.html' %}
```

The `stockpicker.html` page extends the base template `'mainapp/basic.html'`, ensuring consistent styling and layout throughout the application.

## Page Title

```html
{% block title %}
Stonks! - Picker
{% endblock title %}
```

The title of the `stockpicker.html` page is set to "Stonks! - Picker", which is displayed in the browser tab.

## Stock Picker Form

```html
<form class="form-control bg-light" action="/stocktracker">
```

The stock picker form initiates a request to the "/stocktracker" URL, where users can view the selected stocks' details and information.

## Stock Selection

```html
<select class="form-select form-select-lg mb-3" size="15" multiple aria-label="multiple select example" name="stockpicker">
    {% for i in stockpicker %}
    <option value="{{i}}">{{i}}</option>
    {% endfor %}
</select><br>
```

The dropdown menu allows users to select multiple stocks from the list of available tickers. The options are generated dynamically based on the stockpicker data. Users can choose which stocks they wish to track by selecting the respective options.

## Search Button

```html
<div class="d-grid gap-2">
    <input class="btn btn-primary" type="submit" value="Pesquisar">
</div>
```

The "Pesquisar" (Search) button enables users to submit their selected stock choices for tracking. When clicked, the button triggers the form submission, redirecting users to the "/stocktracker" page to view the selected stock information.

## Conclusion

The `stockpicker.html` page offers users a convenient way to select and track stocks within a chosen market. By extending the base template, it ensures consistent styling and layout. This documentation provides insights into how users can effectively use this page to select specific stocks for monitoring, enhancing their engagement and decision-making in stock tracking.

[Back to top](#index-of-stocks)

# Stock Tracker Page Documentation
<p><img src="../../../../../shots/tracker.png" width="50%" height="50%"></p>

The [stocktracker.html](stocktracker.html) page displays selected stocks along with their real-time market data, such as prices, changes, market cap, and more. This page offers users an organized and informative view of their chosen stocks for monitoring.

## Contents

1. [Extending Base Template and Loading Static Files](#extending-base-template-and-loading-static-files)
2. [Page Title](#page-title)
3. [Table Head](#table-head)
4. [Table Body](#table-body)
5. [Change Calculation and Styling](#change-calculation-and-styling)
6. [Historical Graph Button](#historical-graph-button)
7. [Create Alert Button](#create-alert-button)
8. [Websocket for Real-time Updates](#websocket-for-real-time-updates)
9. [jQuery and Datatables](#jquery-and-datatables)

## Extending Base Template and Loading Static Files

```html
{% extends 'mainapp/basic.html' %}
{% load static %}
```

The `stocktracker.html` page extends the base template `'mainapp/basic.html'` and loads necessary static files for styling and scripting.

## Page Title

```html
{% block title %}
{% load myfilters %}
Stonks! - Tracker
{% endblock title %}
```

The page title is set to "Stonks! - Tracker", which appears in the browser tab.

## Table Head

```html
<thead class="table-light">
  <tr>
    <!-- Column headings -->
  </tr>
</thead>
```

The table head contains column headings for the data that will be displayed in the table.

## Table Body

```html
<tbody>
  {% for key, value in data.items %}
  <tr>
    <!-- Data cells -->
  </tr>
  {% endfor %}
</tbody>
```

The table body contains rows of data, each corresponding to a selected stock. The stock data is retrieved from the `data` dictionary.

## Change Calculation and Styling

```html
<td id="{{key}}_change">
  <!-- Change calculation and styling script -->
</td>
```

The change in stock price is calculated using JavaScript and styled based on whether the change is positive or negative.

## Historical Graph Button

```html
<td>
  <form action='graph'>
    <button class="btn btn-primary btn-sm" name='ticker' value={{key}} type="submit">Gráfico</button>
  </form>
</td>
```

A button allows users to view a historical graph of the selected stock's performance over time.

## Create Alert Button

```html
<a class="btn btn-primary btn-sm d-grid gap-2" href="{% url 'create-alert' %}">Criar Alerta</a>
```

Users can create alerts for specific stocks using this button.

## Websocket for Real-time Updates

```html
{{ room_name|json_script:"room-name" }}
<script type="text/javascript" src="{% static 'mainapp/js/live-stocks.js' %}"></script>
```

A websocket script (`live-stocks.js`) provides real-time updates for stock data using Celery.

## jQuery and Datatables

```html
<script type="text/javascript" src="{% static 'mainapp/js/jquery-3.6.0.min.js' %}"></script>
<script type="text/javascript" charset="utf8" src="{% static 'mainapp/js/jquery.dataTables.js' %}"></script>
<script type="text/javascript" src="{% static 'mainapp/js/sort-table.js' %}"></script>
```

jQuery and Datatables scripts enhance the functionality of the stock table, including sorting and filtering options.

## Conclusion

The `stocktracker.html` page offers users a comprehensive view of their selected stocks' real-time market data. With organized tables, dynamic change calculations, historical graph options, and real-time updates, users can effectively monitor and analyze their chosen stocks' performance, supporting informed investment decisions.


[Back to top](#index-of-stocks)

# Stock Graph Page Documentation

The `graph.html` page is where users can view historical price data for a specific stock in the form of a candlestick chart. This page provides an interactive visualization of the stock's price movement over time.

## Contents

1. [Extending Base Template and Loading Static Files](#extending-base-template-and-loading-static-files)
2. [Page Title](#page-title)
3. [Graph Display](#graph-display)
4. [Error Handling](#error-handling)

## Extending Base Template and Loading Static Files

```html
{% extends 'mainapp/basic.html' %}
{% load static %}
```

The `graph.html` page extends the base template `'mainapp/basic.html'` and loads necessary static files for styling and scripting.

## Page Title

```html
{% block title %}
Stonks! - Graph
{% endblock title %}
```

The page title is set to "Stonks! - Graph", which appears in the browser tab.

## Graph Display

```html
<div class="container graph-container">
    <center><h2>{{ ticker }}</h2><center>
        
    {% if graph %}
        <div class="thegraph">
        {{ graph|safe }}
        </div>
    {% else %}

        <br><br>
        <p>An error has occurred.</p>

    {% endif %}

</div>
```

The graph container displays the title of the stock (`ticker`) and renders the candlestick chart using the `graph` variable. The graph is safely rendered using the `safe` filter to prevent any unintended HTML escaping.

## Error Handling

If there is an issue with rendering the graph data, an error message is displayed to the user.

## Conclusion

The `graph.html` page provides users with an interactive candlestick chart to visualize the historical price movement of a selected stock. Users can gain insights into price trends and patterns, helping them make more informed investment decisions based on the stock's historical performance.

[Back to top](#index-of-stocks)

- wallet
<p><img src="../../../../../shots/wallet.png" width="50%" height="50%"></p>
