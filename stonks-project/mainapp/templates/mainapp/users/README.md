# Index of `users`

- [Login and Registration Page](#login-and-registration-page-documentation)
- [User Profile Page](#user-profile-page-documentation)

## Introduction

In this documentation, you'll find detailed information about key components that contribute to the functionality and user experience of your Django application. These components offer capabilities ranging from user authentication and registration to user profile management. By understanding and utilizing these components, you can create a rich and interactive environment for your application's users.

## Login and Registration Page (`login_register.html`)

The `login_register.html` page serves as the entry point for users to either log in to their existing accounts or register new user profiles. It presents input fields for users to enter their credentials and initiate either the login or registration process.

## User Profile Page (`profile.html`)

The `profile.html` page provides users with an overview of their profile information, offering different components based on whether they are viewing their own profile or another user's profile. It displays user-specific content such as topic filters, recent activity, alerts, and messages.

By delving into these sections, you'll gain a comprehensive understanding of how to leverage these components to create a feature-rich and engaging Django application.

[Back to top](#index-of-users)

# Login and Registration Page Documentation

The [login_register.html](login_register.html) page serves as a unified platform for user login and registration. It presents the necessary input fields for users to either log in to their existing accounts or register new user profiles.

## Contents

1. [Extending Base Template](#extending-base-template)
2. [Page Title](#page-title)
3. [Login Section](#login-section)
4. [Registration Section](#registration-section)

## Extending Base Template

```html
{% extends 'mainapp/basic.html' %}
```

The `login_register.html` page extends the base template `'mainapp/basic.html'`, ensuring consistent styling and layout throughout the application.

## Page Title

```html
{% block title %}
Stonks! - Login
{% endblock title %}
```

The title of the `login_register.html` page is set to "Stonks! - Login", which is displayed in the browser tab.

## Login Section

```html
{% if page == 'login' %}
    <!-- ... -->
{% else %}
    <!-- ... -->
{% endif %}
```

This section determines whether to display the login or registration fields based on the `page` variable. If `page` is set to `'login'`, the login fields are shown; otherwise, the registration fields are displayed.

### Login Fields

```html
<form method="POST" action="">
    {% csrf_token %}

    <label>Name:</label>
    <input type="text" name="username" placeholder="Enter username"/>

    <label>Password:</label>
    <input type="password" name="password" placeholder="Enter password"/>

    <input type="submit" value="Entrar" />
</form>
<br>
<p>Not yet registered?</p>
<a class="btn btn-primary" href="{% url 'register' %}">Register</a>
```

For the login section, this code presents the input fields for the user's username and password. Users can enter their credentials and click "Entrar" (Enter) to log in. If users are not yet registered, they are directed to the registration page via the "Register" button.

## Registration Section

```html
{% if page == 'login' %}
    <!-- ... -->
{% else %}
    <!-- ... -->
{% endif %}
```

In the registration section, the code also checks the `page` variable to determine whether to show the registration fields.

### Registration Fields

```html
<form class="container form-control" style="padding: 20px; margin-top: 20px" method="POST" action="">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Register" />
</form>

<div class="container form-control" style="padding: 20px">
    <p>Already registered?</p>
    <a class="btn btn-primary" href="{% url 'login' %}">Log in</a>
</div>
```

For registration, the form is displayed with the necessary fields for username, email, and password. Upon submitting, users are registered. If users are already registered, they can log in through the "Log in" link.

## Conclusion

The `login_register.html` page offers a user-friendly interface for both user login and registration. By extending the base template, it maintains a consistent style throughout the application. This documentation provides an understanding of how users can effectively use this page to either log in or register, enhancing the application's accessibility and user engagement.

[Back to top](#index-of-users)

# User Profile Page Documentation

The [profile.html](profile.html) page serves as a user profile page, displaying different components based on whether the user is viewing their own profile or another user's profile.

## Contents

1. [Extending Base Template](#extending-base-template)
2. [Page Title](#page-title)
3. [Profile Title](#profile-title)
4. [Components](#components)
   - [Topics Component](#topics-component)
   - [Feed Component](#feed-component)
   - [Alerts Component](#alerts-component)
   - [Activity Component](#activity-component)

## Extending Base Template

```html
{% extends 'mainapp/basic.html' %}
```

The `profile.html` page extends the base template `'mainapp/basic.html'`, ensuring consistent styling and layout throughout the application.

## Page Title

```html
{% block title %}
Stonks! Profile
{% endblock title %}
```

The title of the `profile.html` page is set to "Stonks! Profile", which is displayed in the browser tab.

## Profile Title

```html
<div class="profile_title bg-light">
    <h2 class="text-capitalize">{{user.username}}'s Profile</h2>
    <hr>
</div>
```

This section displays the title of the user's profile, indicating the username whose profile is being viewed.

## Components

The page is divided into three columns, each containing different components based on the user's access and viewing context.

### Topics Component

```html
<div class="topics_component">
    {% if request.user == user %}
        {% include 'mainapp/component/topics_component.html' %}
    {% endif %}
</div>
```

The **Topics Component** displays topic filters for the user to interact with. It is displayed only when the user is viewing their own profile.

### Feed Component

```html
<div class="feed_component d-grid gap-2 d-md-block">
    {% if request.user == user %}
        {% include 'mainapp/component/alerts_component.html' %}
    {% endif %}
    <br>
    {% include 'mainapp/component/feed_component.html' %}
</div>
```

The **Feed Component** acts as the central hub for displaying content. It includes the **Alerts Component** when users are viewing their own profile. Regardless of the user's identity, the **Feed Component** is always displayed.

### Alerts Component

The **Alerts Component** is embedded within the **Feed Component** and is shown when users are viewing their own profile. It centralizes the display of user alerts and allows interactions such as editing and deletion.

### Activity Component

```html
<div class="activity_component">
    {% if request.user == user %}
        {% include 'mainapp/component/activity_component.html' %}
    {% endif %}
</div>
```

The **Activity Component** shows recent activities, alerts, and messages. It is displayed only when the user is viewing their own profile.

## Conclusion

The `profile.html` page offers a user-friendly interface for user profiles, displaying different components based on whether the user is viewing their own profile or someone else's. By extending the base template, it maintains a consistent style throughout the application. This documentation provides insights into how users can effectively use this page to view profiles and interact with various components, enhancing user engagement and information management.

[Back to top](#index-of-users)
