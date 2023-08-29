# Index of `forum`

1. [Introduction](#introduction)
2. [Forum Page](#forum-page-documentation)
3. [Room Page](#room-page-documentation)
4. [Room Creation Form Page](#room-creation-form-page-documentation)

## Introduction

In this documentation, you'll find detailed information about key components that contribute to the functionality and user experience of your Django application. These components offer capabilities ranging from managing conversation rooms to creating new rooms and interacting with messages. By understanding and utilizing these components, you can create a rich and interactive environment for your application's users.

## Forum Page (`forum.html`)

The **Forum Page** serves as a central hub for users to access and engage with various conversation rooms. It integrates filtering by topics and displays recent activity using dedicated components.

## Room Page (`room.html`)

The **Room Page** allows users to view the content of a specific room, leave messages, delete their own messages, and see messages from other participants in the same room.

## Room Creation Form Page (`room_form.html`)

The **Room Creation Form Page** enables users to access a user-friendly form for creating a new room. Users can input room details and submit the form to create a room.

By delving into these sections, you'll gain a comprehensive understanding of how to leverage these components to create a feature-rich and engaging Django application.

[Back to top](#index-of-forum)

# Forum Page Documentation

The [forum.html](forum.html) page serves as a central hub for users to access and engage with various conversation rooms. It integrates filtering by topics and displays recent activity using dedicated components.

## Contents

1. [Extending Base Template](#extending-base-template)
2. [Forum Title](#forum-title)
3. [Page Structure](#page-structure)
   - [Left Column: Topics Component](#left-column-topics-component)
   - [Center: Feed Component](#center-feed-component)
   - [Right Column: Activity Component](#right-column-activity-component)

## Extending Base Template

```html
{% extends 'mainapp/basic.html' %}
```

The `forum.html` page extends the base template `'mainapp/basic.html'`, allowing consistent styling and layout across the entire application.

## Forum Title

```html
{% block title %}
Stonks! - Forum
{% endblock title %}
```

The title of the `forum.html` page is set to "Stonks! - Forum", which is displayed in the browser tab.

## Page Structure

```html
<div class="forums-container">
    <!-- coluna da esquerda -->
    <div class="topics_component">
        {% include 'mainapp/component/topics_component.html' %}
    </div>
    <!-- centro da pagina -->
    <div class="feed_component d-grid gap-2 d-md-block">
        {% include 'mainapp/component/feed_component.html' %}
    </div>
    <!-- coluna da direita -->
    <div class="activity_component">
        {% include 'mainapp/component/activity_component.html' %}
    </div>
</div>
```

The content of the `forum.html` page is structured into three main columns within a container.

### Left Column: Topics Component

The `topics_component` section includes the `topics_component.html` file, which provides topic filtering functionality. It allows users to filter messages based on topics within the conversation rooms.

### Center: Feed Component

The `feed_component` section includes the `feed_component.html` file, which centralizes the room listing and creation options. This section enables users to view all available rooms, as well as create new ones.

### Right Column: Activity Component

The `activity_component` section includes the `activity_component.html` file, which displays recent activities related to alerts, messages, and other interactions. This component keeps users informed about ongoing activities within the application.

## Conclusion

The `forum.html` page acts as a dynamic and interactive hub for users to engage with conversation rooms. By integrating the filtering of topics and showcasing recent activity, the page enhances user engagement and provides a comprehensive experience. The structure and components used in this page contribute to a well-organized and user-friendly environment for users to explore and interact with various features of the application.

[Back to top](#index-of-forum)

# Room Page Documentation

The [room.html](room.html) page allows users to view the content of a specific room, leave messages, delete their own messages, and see messages from other participants in the same room.

## Contents

1. [Extending Base Template](#extending-base-template)
2. [Page Title](#page-title)
3. [Room Content](#room-content)
4. [Comment Section](#comment-section)
   - [Displaying Messages](#displaying-messages)
   - [Message Deletion](#message-deletion)
   - [Message Input](#message-input)
5. [Participants](#participants)

## Extending Base Template

```html
{% extends 'mainapp/basic.html' %}
```

The `room.html` page extends the base template `'mainapp/basic.html'`, ensuring consistent styling and layout throughout the application.

## Page Title

```html
{% block title %}
Stonks! - Room
{% endblock title %}
```

The title of the `room.html` page is set to "Stonks! - Room", which is displayed in the browser tab.

## Room Content

```html
<div class="container">
    <!-- titulo do post -->
    <h2>{{ room.name }}</h2>
    <!-- conteudo do post -->
    <div class="container">
        <p class="message">{{ room.description }}</p>
    </div>
    <!-- ... -->
</div>
```

This section displays the title and content of the room. It showcases the room's name and description within a container.

## Comment Section

```html
<div class="comment-wrapper">
    <big>Comments</big>
    <div class="card">
        <!-- ... -->
    </div>
</div>
```

This section represents the comment area where users can view and interact with messages within the room.

### Displaying Messages

```html
{% for message in room_messages %}
    <!-- ... -->
{% endfor %}
```

This section iterates through the `room_messages` and displays each message. It shows the username, message creation time, message body, and a delete button (for the message owner) within a card.

### Message Deletion

```html
{% if request.user == message.user %}
    <a class="btn btn-outline-danger btn-sm msgdel-btn"
        href="{% url 'delete-message' message.id %}">Delete</a>
{% endif %}
```

If the currently logged-in user is the owner of the message, a delete button is displayed. Clicking this button triggers the deletion of the message.

### Message Input

```html
{% if request.user.is_authenticated %}
    <div class="input-group input-group-sm mb-3">
        <form class="input-group-text bg-light" method="POST" action="">
            <!-- ... -->
        </form>
    </div>
{% endif %}
```

If the user is authenticated, an input field is provided for typing new messages. Users can post messages within the room.

## Participants

```html
<!-- participantes -->
<div class="container card-participants">
    <h5>Participants</h5>
    <br>
    <div class="card">
        {% for user in participants %}
            <!-- ... -->
        {% endfor %}
    </div>
</div>
```

This section displays the list of participants in the room. It iterates through the `participants` and displays each participant's username within a card.

## Conclusion

The `room.html` page provides users with a comprehensive experience when viewing and interacting within a specific room. It showcases the room's details, presents messages and their authors, and offers the ability to leave messages and delete one's own messages. The documentation offers an understanding of how users can effectively navigate and engage with the content of a room, making the application more interactive and engaging.

[Back to top](#index-of-forum)

# Room Creation Form Page Documentation

The [room_form.html](room_form.html) page enables users to access a form for creating a new room.

## Contents

1. [Extending Base Template](#extending-base-template)
2. [Page Title](#page-title)
3. [Form Section](#form-section)
   - [Form Input](#form-input)

## Extending Base Template

```html
{% extends 'mainapp/basic.html' %}
```

The `room_form.html` page extends the base template `'mainapp/basic.html'`, ensuring consistent styling and layout throughout the application.

## Page Title

```html
{% block title %}
Stonks! - Create
{% endblock title %}
```

The title of the `room_form.html` page is set to "Stonks! - Create", which is displayed in the browser tab.

## Form Section

```html
<div class="container lil-space">
    <form class="form-control bg-light" method="POST" action=""> {% csrf_token %}
        <!-- ... -->
    </form>
</div>
```

This section represents the form area where users can input information to create a new room.

### Form Input

```html
{{ form.as_p }}
<input type="submit" value="Submit" />
```

The `{{ form.as_p }}` tag renders the form fields as paragraph elements, displaying the fields nicely. Users can input information such as the room name and description. The `<input type="submit" value="Submit" />` button submits the form data to create the room.

## Conclusion

The `room_form.html` page provides a user-friendly interface for users to create new rooms. By extending the base template, it maintains the application's consistent style. The form section allows users to input relevant information, and the "Submit" button triggers the room creation process. This documentation explains how users can effectively utilize the room creation form, enhancing the application's functionality and user engagement.
