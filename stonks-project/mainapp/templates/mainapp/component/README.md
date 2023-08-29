# Index of `component`

- [Activity Component](#activity-component-documentation)
- [Alerts Component](#alerts-component-documentation)
- [Feed Component](#feed-component-documentation)
- [Mercado Component](#mercado-component-documentation)
- [Topics Component](#topics-component-documentation)

# About Components Documentation

This documentation provides detailed insights into various Django components that enhance user interaction and functionality within a web application. Each component serves a specific purpose, contributing to a seamless user experience and effective information management. Let's summarize the key components discussed:

## Activity Component (`activity_component.html`)

The **Activity Component** is employed to showcase recent activities, such as alerts, messages, and forum posts, depending on the context. It includes:

- Displaying recent messages and user alerts.
- Providing options for users to view profiles, delete messages, and manage alerts.

## Alerts Component (`alerts_component.html`)

The **Alerts Component** focuses on presenting user alerts and enabling interactions with them. It offers:

- Displaying owned alerts.
- Buttons to edit and delete alerts, with dynamic modals for detailed alert information.

## Feed Component (`feed_component.html`)

The **Feed Component** centralizes room listing and creation functionalities. It facilitates:

- Displaying rooms, with room count and new room creation options.
- Allowing users to view profiles, edit, and delete rooms based on ownership.

## Mercado Component (`mercado_component.html`)

The **Mercado Component** specializes in listing and filtering alerts based on markets. It includes:

- Displaying available markets.
- Links to filter alerts by selected markets.

## Topics Component (`topics_component.html`)

The **Topics Component** streamlines filtering messages by topics and alerts by markets. It offers:

- Displaying available topics and markets.
- Links to filter content based on selected topics and markets.

## Conclusion

These components collectively contribute to a feature-rich and user-friendly Django application. By implementing these building blocks, developers can create a seamless experience for users to interact with messages, alerts, rooms, and more. The documentation provides clear insights into each component's purpose, functionality, and usage, ensuring developers can effectively integrate them into their applications. Whether it's presenting recent activities, managing alerts, or simplifying content filtering, these components enhance the application's functionality and user engagement.

[Back to top](#index-of-component)

# Activity Component Documentation

The [activity_component.html](activity_component.html) file is used as a reusable component on the FORUM, ALERTS, and PROFILE pages in a Django application. It serves as a way to display recent user activity, including alerts, messages, and general activity on the FORUM page (posts from other users).

## Contents

1. [Message and Alert Titles](#message-and-alert-titles)
2. [Recent Activity Display](#recent-activity-display)
3. [User Messages](#user-messages)
4. [Alerts Display](#alerts-display)

## Message and Alert Titles

```html
<!-- esconde titulo de mensagens na pagina de alertas e vice versa -->
{% if alerta and not room_messages %}
<h3 class="active-title">Recent</h3>
{% else %}
<h3 class="active-title">Activity</h3>
{% endif %}
```

This section controls the display of titles based on whether there are alerts (`alerta`) and whether there are room messages (`room_messages`). If there are alerts and no room messages, the title "Recent" is displayed; otherwise, the title "Activity" is displayed.

## Recent Activity Display

```html
<!-- MENSAGENS (atividade recente) -->
<div class="container">
    {% for message in room_messages %}
    <!-- message display -->
    <!-- ... -->
    {% endfor %}
</div>
```

This section iterates through `room_messages` and displays recent user messages. It includes details such as the time since the message was created, the associated room, and the message content. For messages sent by other users, a link to the sender's profile is displayed, and for messages sent by the logged-in user, a "Delete" button is provided.

## User Messages

```html
<!-- esconde link para profile para dono da mensagem -->
{% if request.user != message.user %}
<a class="btn btn-outline-secondary btn-sm" 
    href="{% url 'user-profile' message.user.id %}">@{{ message.user }}</a>
{% endif %}

<!-- adiciona botao de apagar para dono da mensagem -->
{% if request.user == message.user %}
    <a class="btn btn-outline-danger btn-sm" 
        href="{% url 'delete-message' message.id %}">Delete</a>
{% endif %}
```

For messages sent by other users, a link to the sender's profile is displayed. For messages sent by the logged-in user, a "Delete" button is provided to delete the message.

## Alerts Display

```html
<!-- ALERTAS (alertas recentes) -->
<div class="container">
    {% for alerta in alertas %}
    <!-- alert display -->
    <!-- ... -->
    {% endfor %}
</div>
```

This section iterates through `alertas` and displays recent alerts. It shows alerts authored by the logged-in user, including details such as the alert name, associated market, creation time, and additional information. For user-authored alerts, "Edit" and "Delete" buttons are provided for editing and deleting the alert.

## Modal

```html
<!-- MODAL -->
<div id="modal{{alerta}}" class="modal fade" tabindex="-1">
    <div class="modal-dialog modal-dialog-centered modal-sm">
        <div class="modal-content">
            <!-- alert details display -->
            <!-- ... -->
        </div>
    </div>
</div>
```

A modal dialog is used to display detailed information about each alert. The modal contains various details related to the alert, such as market, buy and sell prices, period, duration, and the email to send the alert to.

[Back to top](#index-of-component)

# Alerts Component Documentation

The [alerts_component.html](alerts_component.html) file serves as a central column on the ALERTS page. It lists the existing alerts for the logged-in user. This component is also utilized on the PROFILE page when accessed by the active user.

## Contents

1. [Component Title and New Alert Creation](#component-title-and-new-alert-creation)
2. [Displaying User Alerts](#displaying-user-alerts)
3. [Alert Cards](#alert-cards)
4. [Modal Display](#modal-display)

## Component Title and New Alert Creation

```html
<!-- titulo do componente -->
<div class="container">
    <h3 class="active-title">Alertas</h3>
    <br>
    <!-- botao para criar um novo alerta -->
    <a class="btn btn-outline-primary btn-sm d-grid gap-2" 
    href="{% url 'create-alert' %}">Criar Alerta</a>
</div>
```

This section includes the component title "Alertas" and a button to create a new alert using the URL linked to the "create-alert" view.

## Displaying User Alerts

```html
<div class="container">
    <div class="row row-cols-1 row-cols-md-4 g-4 ">
        {% for alerta in alertas %}
        <!-- mostra apenas alertas do usuario logado -->
        {% if request.user == alerta.host %}
        
        <!-- alert card and modal display -->
        <!-- ... -->

        {% endif %}
        {% endfor %}
    </div>
</div>
```

This section iterates through the list of `alertas` and displays alerts belonging to the logged-in user. It generates a grid layout to organize the alert cards.

## Alert Cards

```html
<div class="col card-wrapper">
    <div class="card bg-light card-box">
        <div class="card-body">
            <!-- nome do alerta (ticker) com link para MODAL -->
            <!-- ... -->
            <!-- mercado dono do ativo do alerta -->
            <p class="card-text">{{alerta.mercado}}</p>
            <!--  tempo desde a criacao/update do alerta -->
            <small>{{alerta.updated}}</small>
        </div>
        <div class="card-footer">
            <!-- botao para EDITAR alerta -->
            <a class="btn btn-warning btn-sm" href="{% url 'update-alert' alerta.id %}">Editar</a>
            <!-- botao para APAGAR alerta -->
            <a class="btn btn-outline-danger btn-sm" href="{% url 'delete-alert' alerta.id %}">Apagar</a>
        </div>
    </div>
</div>
```

This section represents an alert card within the grid. It displays the alert's name (ticker) with a link to a modal, the associated market, and the time since the alert was last updated. Additionally, it provides buttons for editing and deleting the alert.

## Modal Display

```html
<!-- MODAL -->
<div id="modal{{alerta}}" class="modal fade" tabindex="-1">
    <div class="modal-dialog modal-dialog-centered modal-sm">
        <div class="modal-content">
            <!-- alert details display -->
            <!-- ... -->
        </div>
    </div>
</div>
```

A modal dialog is used to display detailed information about each alert. The modal contains various details related to the alert, such as market, buy and sell prices, search period, duration, and the email to send the alert to.

[Back to top](#index-of-component)

# Feed Component Documentation

The [feed_component.html](feed_component.html) file is a versatile component used to list available chat rooms and provide options for creating new rooms. It is designed for the FORUM page but is also incorporated in the PROFILE page to display rooms owned by the logged-in user or others.

## Contents

1. [User-Specific Display and New Room Creation](#user-specific-display-and-new-room-creation)
2. [Displaying Available Chat Rooms](#displaying-available-chat-rooms)
3. [Room Cards](#room-cards)

## User-Specific Display and New Room Creation

```html
{% if request.user == user %}
<div class="container">
    <h3 class="active-title">Salas</h3>
    <br>
    <!-- mostra apenas numero de salas quando na pagina do forum -->
    {% if room_count %}
    <h5>{{ room_count }} sala(s) disponíveis</h5>
    {% endif %}
    <!-- botao para criar nova sala -->
    <a class="btn btn-outline-primary btn-sm d-grid gap-2"
        href="{% url 'create-room' %}">Criar Sala</a>
</div>
<br>
{% endif %}
```

This section checks if the logged-in user is the same as the provided user (`user`). If they match, it displays the title "Salas" (Rooms), the number of available rooms if in the FORUM page, and a button to create a new room using the URL linked to the "create-room" view.

## Displaying Available Chat Rooms

```html
<div class="container">
    <div class="row row-cols-1 row-cols-md-4 g-4">
        {% for room in rooms %}
        <!-- room card display -->
        <!-- ... -->
        {% endfor %}
    </div>
</div>
```

This section iterates through the list of `rooms` and displays available chat rooms. It organizes the rooms in a grid layout.

## Room Cards

```html
<div class="col card-wrapper">
    <div class="card bg-light card-box">
        <div class="card-body">
            <!-- nome da sala -->
            <!-- ... -->
            <!-- topico -->
            <p class="card-text">{{room.topic.name}}</p>
            <!-- data de criacao/modificacao -->
            <small>{{room.updated}}</small>
        </div>
        <div class="card-footer">
            <!-- adiciona botoes editar/apagar apenas para usuario dono da sala -->
            <!-- ... -->
            <!-- link para o profile do usuario dono da sala -->
            <!-- ... -->
        </div>
    </div>
</div>
```

This section represents a card for each chat room. It displays the room's name, associated topic, and the date of creation or modification. Depending on whether the logged-in user owns the room or not, it provides buttons for editing and deleting the room and a link to the profile of the room's owner.

[Back to top](#index-of-component)

# Mercado Component Documentation

The [mercado_component.html](mercado_component.html) file is a component designed for the ALERTAS (Alerts) page. It provides a list of available market options for setting filters on alerts. Clicking on a specific market option filters the displayed alerts based on that market.

## Contents

1. [Component Title](#component-title)
2. [View All Alerts](#view-all-alerts)
3. [Filter by Markets](#filter-by-markets)

## Component Title

```html
<h3 class="active-title">Mercados</h3>
<br>
```

This section displays the title "Mercados" (Markets) with styling applied by the "active-title" class.

## View All Alerts

```html
<div>
    <a class="btn btn-secondary btn-sm d-grid gap-2"
        href="{% url 'alerts' %}">Todos</a>
</div>
```

This section provides a button labeled "Todos" (All) that links to the ALERTAS page. Clicking this button directs the user to their personal alerts page with no specific market filter applied.

## Filter by Markets

```html
{% for mercado in mercado %}
<div>
    <a class="btn btn-secondary btn-sm d-grid gap-2" 
        href="{% url 'alerts' %}?q={{ mercado }}">{{ mercado.name }}</a>
</div>
{% endfor %}
```

This section iterates through the list of available markets (`mercado`) and presents them as clickable buttons. Each button's link is dynamically generated to the ALERTAS page with a query parameter (`q`) set to the name of the selected market. This allows users to filter alerts based on the chosen market.

## Usage

The `mercado_component.html` component can be embedded within the ALERTAS page to offer users a convenient way to filter and view alerts based on different markets. The component displays the available markets and enables users to click on specific markets to narrow down the alerts they wish to view.

[Back to top](#index-of-component)

# Topics Component Documentation

The [topics_component.html](topics_component.html) file serves as a component on the FORUM and PROFILE pages. It provides filters for messages by topic and alerts by market.

## Contents

1. [Component Title](#component-title)
2. [View All Rooms (Forums)](#view-all-rooms-forums)
3. [Filter by Topics](#filter-by-topics)
4. [View All Personal Alerts](#view-all-personal-alerts)
5. [Filter by Markets](#filter-by-markets)

## Component Title

```html
<h3 class="active-title">Tópicos</h3>
<br>
```

This section displays the title "Tópicos" (Topics) with styling applied by the "active-title" class.

## View All Rooms (Forums)

```html
<div>
    <a class="btn btn-outline-warning btn-sm d-grid gap-2" 
        href="{% url 'forum' %}">Salas</a>
</div>
```

This section provides a button labeled "Salas" (Rooms) that links to the FORUM page. Clicking this button directs the user to the forum page displaying all available rooms.

## Filter by Topics

```html
{% for topic in topics %}
<div>
    <a class="btn btn-secondary btn-sm d-grid gap-2" 
        href="{% url 'forum' %}?q={{ topic.name }}">{{ topic.name }}</a>
</div>
{% endfor %}
```

This section iterates through the list of available topics (`topics`) and presents them as clickable buttons. Each button's link is dynamically generated to the FORUM page with a query parameter (`q`) set to the name of the selected topic. This allows users to filter messages based on the chosen topic.

## View All Personal Alerts

```html
<div>
    <a class="btn btn-outline-warning btn-sm d-grid gap-2" 
        href="{% url 'alerts' %}">Alertas</a>
</div>
```

This section provides a button labeled "Alertas" (Alerts) that links to the ALERTAS page. Clicking this button directs the user to their personal alerts page displaying all available alerts.

## Filter by Markets

```html
{% for mercado in mercado %}
<div>
    <a class="btn btn-secondary btn-sm d-grid gap-2" 
        href="{% url 'alerts' %}?q={{ mercado }}">{{ mercado.name }}</a>
</div>
{% endfor %}
```

This section iterates through the list of available markets (`mercado`) and presents them as clickable buttons. Each button's link is dynamically generated to the ALERTAS page with a query parameter (`q`) set to the name of the selected market. This allows users to filter alerts based on the chosen market.

## Usage

The `topics_component.html` component can be incorporated within the FORUM and PROFILE pages. It offers users convenient ways to filter messages by topic and alerts by market. Users can click on specific topics or markets to narrow down the content they wish to view.

[Back to top](#index-of-component)
