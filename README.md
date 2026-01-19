# PY175: Networked Applications with Python

**Repository:** [https://github.com/christinelinster/ls-py175](https://github.com/christinelinster/ls-py175)

This course builds the bridge between raw networking concepts and modern web application development. Starting from first principles, we manually handle HTTP requests via TCP sockets to understand the underlying "magic" of the web. The curriculum then transitions to **Flask**, a lightweight web framework, to build dynamic, data-driven applications that persist state and interact with the file system.

## Core Concepts Mastered

### Server-Side Fundamentals
* **The Request/Response Cycle:** Manually parsing HTTP request lines, headers, and bodies, and constructing raw HTTP responses.
* **WSGI (Web Server Gateway Interface):** Understanding the standard interface between Python web applications and web servers.
* **Statelessness:** Overcoming the stateless nature of HTTP using Cookies, Sessions, and Flash messages.


### The Flask Framework
* **Routing & View Functions:** Mapping URLs to Python functions and handling variable route parameters (e.g., `/users/<username>`).
* **Templating (Jinja2):** Separating logic from presentation using templates, layouts, loops, and custom filters.
* **Static Assets:** Serving CSS, JavaScript, and images efficiently within an application context.
* **Request Processing:** utilizing `before_request` hooks and handling redirection (HTTP 302).

### Deployment & Security
* **Production Deployment:** Configuring applications for cloud hosting platforms like **Render** using Gunicorn.
* **Security Best Practices:** Sanitizing user input to prevent XSS and securing user sessions.
* **Authentication:** Implementing simple password hashing (bcrypt) and restricted access decorators.

## Projects

### Echo Server (`echo_server.py`)
A foundational exercise in network programming.
* **Focus:** Creating a simple TCP server that listens on a port, accepts client connections, and reflects the data sent back to the client.
* **Key Concept:** Understanding sockets and the anatomy of a raw data stream.

### Users and Interests (`/user_and_interests`)
A dynamic information application that serves different content based on URL parameters.
* **Focus:** Routing and data structures.
* **Features:** A navigation menu that highlights the active user and dynamic generation of pages based on a YAML data source.

### File-Based CMS (Book Viewer)
A Content Management System that uses the file system as its database.
* **Focus:** File I/O, robust testing, and CRUD operations.
* **Features:**
    * **Reading:** Parsing and rendering Markdown files into HTML.
    * **Editing:** Allow users to update content via web forms.
    * **Search:** Implementing search functionality to filter content.
    * **Authentication:** restricting edit access to signed-in users.

### Todos Application
A comprehensive Task Management application (often hosted in a separate repository).
* **Focus:** Complex state management and session persistence.
* **Features:** Creating, editing, and deleting Todo lists and individual tasks, with user feedback provided via Flash messages.

## Repository Structure

```text
ls-py175/
├── echo_server.py          # Raw TCP server implementation
├── example_app/            # Basic Flask application setup
├── user_and_interests/     # Project: Dynamic routing with data structures
└── book_viewer_starter/    # Project: File-based Content Management System
```

## Key Takeaways
* Deep understanding of how web servers process requests before they reach the application code.
* Proficiency in building MVC-style applications using Flask.
* Ability to implement Authentication and Authorization from scratch.
* Experience deploying Python applications to a production environment.

## License
MIT
