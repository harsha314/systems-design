import genanki
import random

# --- Model Definition ---
# A unique ID for the model. It's good practice to generate a random one.
MODEL_ID = random.randrange(1 << 30, 1 << 31)

# Model for the Anki cards
SYSTEM_DESIGN_MODEL = genanki.Model(
  MODEL_ID,
  'System Design API Model',
  fields=[
    {'name': 'Question'},
    {'name': 'Answer'},
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '<div style="font-family: Arial; font-size: 20px; text-align: center;">{{Question}}</div>',
      'afmt': '{{FrontSide}}<hr id="answer"><div style="font-family: Arial; font-size: 16px;">{{Answer}}</div>',
    },
  ])

# --- Card Data ---
# List of questions and answers, structured by article section and expanded
CARD_DATA = [
    # -----------------------------------------------------------
    # Section: API Protocols
    # -----------------------------------------------------------
    # Sub-section: REST (5 cards)
    ("What is the core philosophy behind RESTful API design?",
     "REST is a **resource-oriented** architectural style. It focuses on using standard HTTP methods to perform operations on named resources, which are objects or entities."),
    ("When is REST the most suitable choice for an API?",
     "REST is a great choice for public-facing APIs due to its simplicity, broad support, and use of familiar HTTP standards. It's the default choice for most web-based services."),
    ("In REST, what is a 'resource' and how should its URL be named?",
     "A resource is any object or data entity (e.g., a user, a product). Its URL should be a **plural noun** representing a collection (e.g., `/users`, `/products`)."),
    ("What are the key principles of a RESTful API? (Based on the article)",
     "A RESTful API should be:<br>1. **Resource-oriented:** Focus on nouns, not verbs.<br>2. **Stateless:** The server does not store client state between requests.<br>3. **Uses HTTP methods:** Uses standard verbs for actions (`GET`, `POST`, `PUT`, `DELETE`)."),
    ("Scenario: You are designing an API for a new mobile photo-sharing application. Why would REST be a good starting point?",
     "REST is a good starting point because it is a simple and well-understood protocol that fits the needs of a typical CRUD (Create, Read, Update, Delete) application. It leverages existing HTTP infrastructure, making it easy for both the server and client to implement."),

    # Sub-section: GraphQL (5 cards)
    ("What is the primary problem GraphQL solves that REST often struggles with?",
     "GraphQL solves the problems of **over-fetching** (retrieving more data than needed) and **under-fetching** (needing multiple requests to get all the data)."),
    ("How does GraphQL enable clients to be more efficient with data fetching?",
     "It allows the client to specify exactly what data they need from a single endpoint, reducing the number of requests and the amount of data transferred over the network."),
    ("What is a key difference between a GraphQL endpoint and a REST endpoint?",
     "A GraphQL API typically has only **one endpoint** (e.g., `/graphql`), while a REST API has multiple endpoints, each corresponding to a specific resource."),
    ("When is GraphQL a less suitable choice for an API?",
     "It's less suitable for simple APIs where data requirements are well-defined and don't change often. The added complexity of implementation might not be worth the benefit in such cases."),
    ("Scenario: An app needs to display a list of authors and, for each author, their name and the titles of their last five books. How would GraphQL be more efficient than REST?",
     "With GraphQL, the client can make a single query to get exactly the author names and book titles they need. In REST, this might require a series of requests: one for the authors, then one for each author's books."),

    # Sub-section: RPC (5 cards)
    ("What is the main philosophy behind RPC (Remote Procedure Call)?",
     "RPC is **action-oriented**. It focuses on calling a function or procedure on a remote server as if it were a local function call."),
    ("What is a primary use case for RPC in system design?",
     "RPC is best suited for high-performance, low-latency communication between **internal microservices** where efficiency is more critical than a uniform interface."),
    ("What is one major advantage of RPC over REST for internal communication?",
     "RPC can be more performant as it often uses binary serialization and does not have the overhead of HTTP semantics or complex data parsing."),
    ("Give a conceptual example of an RPC call versus a RESTful call for the same task.",
     "RPC: `createProduct(name, price, stock)`. REST: `POST /products` with a JSON body `{ \"name\": \"...\", \"price\": \"...\", \"stock\": \"...\" }`."),
    ("Scenario: Two services, `payment-service` and `shipping-service`, need to communicate a single event (`onPaymentReceived`). What protocol might be a good fit and why?",
     "RPC would be a good fit because it's an action-oriented protocol designed for direct, high-speed communication between internal services. The communication is a simple, direct function call."),

    # -----------------------------------------------------------
    # Section: Designing REST APIs
    # -----------------------------------------------------------
    # Sub-section: Resource Modeling (5 cards)
    ("How would you represent a collection of users in a RESTful API URL?",
     "As a plural noun, for example, `/users`."),
    ("How would you represent a specific user with ID `123`?",
     "By using a path parameter, for example, `/users/123`."),
    ("How should you name a resource for a blog post owned by a user?",
     "As a nested resource, such as `/users/{user_id}/posts`."),
    ("Why is it considered a bad practice to use verbs in a RESTful URL?",
     "Verbs in the URL (e.g., `/getAllUsers`) are redundant. The HTTP method itself should define the action being performed on the noun (resource)."),
    ("Scenario: You are designing an API for a forum with threads and replies. How would you model the API endpoint for getting all replies for a specific thread?",
     "You would model it as a nested resource: `GET /threads/{thread_id}/replies`."),

    # Sub-section: HTTP Methods (5 cards)
    ("Explain the purpose of the `PUT` and `PATCH` HTTP methods.",
     "**`PUT`** is for **replacing** a resource entirely with a new representation. **`PATCH`** is for making a **partial** update to a resource."),
    ("Which HTTP methods are considered idempotent?",
     "**`GET`**, **`PUT`**, and **`DELETE`** are idempotent because applying the operation multiple times has the same effect as applying it once."),
    ("What is the purpose of the `POST` method?",
     "`POST` is used to create a new resource on the server. It is not idempotent."),
    ("What HTTP method would you use to get a list of all products in a category?",
     "You would use the **`GET`** method, such as `GET /products?category=electronics`."),
    ("Scenario: A user wants to submit their profile photo. What HTTP method should be used and why?",
     "`PUT` or `PATCH` could be used. If the user is uploading a new photo that replaces the old one, `PUT /users/{id}/photo` is appropriate. If the photo is part of a larger profile object, `PATCH /users/{id}` with the photo data in the request body would work."),

    # Sub-section: Passing Data (5 cards)
    ("What are query parameters used for in a RESTful API?",
     "Query parameters are used for optional filters, sorting, or pagination (e.g., `/products?color=blue&sort=price`)."),
    ("How would you send a complex JSON payload in a request?",
     "It should be sent in the **request body**, typically using the `POST`, `PUT`, or `PATCH` methods."),
    ("When is a path parameter appropriate for a request?",
     "A path parameter is appropriate when a value is **required** to uniquely identify a specific resource."),
    ("How would you design a `GET` endpoint to find all products with a minimum rating and a maximum price?",
     "By using query parameters: `GET /products?min_rating=4.5&max_price=100`."),
    ("Scenario: A user wants to create a new post with a title and a body. How would you structure this request?",
     "You would use a `POST` request to an endpoint like `/posts`, with a JSON object containing the title and body in the request body."),

    # -----------------------------------------------------------
    # Section: Common API Patterns
    # -----------------------------------------------------------
    # Sub-section: Pagination (5 cards)
    ("What is the main purpose of pagination?",
     "Pagination is used to manage and retrieve large datasets in smaller, more manageable chunks. "),
    ("What is offset-based pagination and what is its main drawback?",
     "Offset-based pagination uses `limit` and `offset` to retrieve pages of data. Its main drawback is that it can lead to missing or duplicate items in a rapidly changing dataset."),
    ("What is cursor-based pagination and why is it often preferred for dynamic data?",
     "Cursor-based pagination uses a unique token (`cursor`) to mark the last item from the previous page. It's preferred because it provides a stable reference point and is not affected by changes to the dataset's order."),
    ("What API pattern would you use for an infinite scroll feed on a social media site?",
     "**Cursor-based pagination** is ideal for infinite scrolling because it provides a consistent, stable browsing experience."),
    ("Scenario: Your API has an endpoint that returns a list of user comments. The comments are sorted by creation time. Which pagination strategy is best and why?",
     "Cursor-based pagination is best because new comments are constantly being added to the dataset, which would break offset-based pagination."),

    # Sub-section: Versioning (5 cards)
    ("Why is API versioning a crucial practice in system design?",
     "It is essential to prevent breaking changes from disrupting existing clients and to allow new features to be introduced without backward compatibility issues."),
    ("Describe URL-based versioning and provide an example.",
     "The API version is included in the URL path, for example, `https://api.example.com/v2/users`."),
    ("Describe header-based versioning and provide an example.",
     "The API version is specified in a custom request header, such as `Accept: application/vnd.myapi.v2+json`."),
    ("What is a downside of URL-based versioning?",
     "It 'pollutes' the URL and can make it less clean. It also requires the client to change the entire endpoint URL for a new version."),
    ("Scenario: Your mobile app is deployed to a user's phone, but you need to introduce a breaking change to the user API. What is the best way to handle this?",
     "Create a new API version (e.g., `v2`). The app can be updated to use the new version, while the old version (`v1`) remains available for a deprecation period to support older versions of the app."),

    # Sub-section: Authentication & Authorization (5 cards)
    ("What is the difference between Authentication and Authorization?",
     "**Authentication** is the process of verifying who a user is. **Authorization** is the process of determining what that user is allowed to do."),
    ("What is the main use case for an API key?",
     "API keys are typically used to authenticate internal services or third-party applications. They are simple, secret tokens that are checked on the server side."),
    ("How does a JWT (JSON Web Token) work for authentication?",
     "A JWT is a self-contained, signed token that the server generates upon login. The client stores it and sends it with each request. The server can verify its authenticity and claims without a database lookup."),
    ("When would you use a JWT over an API key?",
     "You would use a JWT for user-facing applications after a user has logged in, as it is a more secure and flexible way to manage user sessions and permissions."),
    ("Scenario: A user needs to access their private data (e.g., messages) via an API. How would you secure this endpoint?",
     "You would use both authentication and authorization. First, the user would log in and receive a JWT. Then, on each request, the API would authenticate the user with the JWT and authorize their access to only their own resources."),

    # Sub-section: Rate Limiting (5 cards)
    ("What is the purpose of rate limiting?",
     "Rate limiting restricts the number of requests a user or client can make to an API in a given time frame. It prevents abuse, ensures fair usage, and protects the server from overload."),
    ("What HTTP status code should you return when a client is rate-limited?",
     "The standard status code is **429 Too Many Requests**."),
    ("What is a common strategy for rate-limiting?",
     "A common strategy is the **Token Bucket algorithm**, where a client is given a bucket of tokens that are refilled at a fixed rate. Each request costs one token."),
    ("Where would you typically implement rate limiting in a system?",
     "It is usually implemented at the API Gateway or a reverse proxy to protect the underlying services and provide a single point of enforcement."),
    ("Scenario: A single user IP address is sending millions of requests to your public API, causing performance issues. What would be the first step in mitigating this?",
     "Implement a rate-limiting policy on the API Gateway to restrict the number of requests per IP address to a reasonable limit, preventing a single client from monopolizing resources."),

    # -----------------------------------------------------------
    # Section: Cross-Section Questions (5 cards)
    # -----------------------------------------------------------
    ("Scenario: You are designing an API for an online music service. What is the best way to handle requests for a user's listening history with a large number of songs?",
     "You should use **REST** with **cursor-based pagination**. The endpoint would be `GET /users/{id}/listening_history`. Cursor-based pagination is ideal for this use case because it's a dynamic, growing list, and it prevents issues that could arise with offset-based pagination."),
    ("Scenario: An internal analytics service needs to receive a continuous stream of events from a front-end application. What API protocol and data transfer pattern would you use?",
     "You would use **RPC** with a **streaming** capability. A protocol like gRPC is well-suited for this, as it supports bidirectional streaming of binary data, providing a highly efficient way to send a constant flow of events."),
    ("Scenario: A client is trying to update a user's password but their requests are failing on a retry. What is a likely cause and how can it be fixed?",
     "The `PUT` request for the password update is likely not **idempotent**. It should be redesigned to be so. A possible solution is to ensure the server generates a unique password reset token that is only valid for one use, or to use an idempotency key."),
    ("Scenario: An endpoint to create a new user (`POST /users`) is failing on a retry. How can you make this operation idempotent?",
     "You can use an **Idempotency Key**. The client sends a unique key in the request header. The server checks if a user with that key has already been created. If so, it returns the previous successful response without creating a new user."),
    ("Scenario: Design a complete REST API for a simple blog system with users, posts, and comments. Include resource naming, methods, and a plan for versioning and security.",
     "The API would have endpoints like:<br>- `GET /v1/users` (list all users)<br>- `POST /v1/posts` (create a post)<br>- `GET /v1/posts/{post_id}/comments` (get comments for a post)<br>Security would involve a **JWT** for user authentication and authorization, and a **rate limiter** to protect against abuse. Versioning would be handled via the URL (`/v1`)."),
]


# --- Deck Generation ---
def create_anki_deck():
    """Generates an Anki deck from the card data."""
    # Create the deck
    deck = genanki.Deck(
        random.randrange(1 << 30, 1 << 31),
        'System Design - API Concepts'
    )

    # Add notes (cards) to the deck
    for question, answer in CARD_DATA:
        note = genanki.Note(
            model=SYSTEM_DESIGN_MODEL,
            fields=[question, answer]
        )
        deck.add_note(note)

    # Save the deck to an .apkg file
    output_file = 'system_design_api_deck.apkg'
    genanki.Package(deck).write_to_file(output_file)
    print(f"Successfully generated Anki deck with {len(CARD_DATA)} cards.")
    print(f"File saved as: {output_file}")


# --- Main Execution ---
if __name__ == "__main__":
    create_anki_deck()
