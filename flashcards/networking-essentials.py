import genanki
import random

# Use a consistent, but unique, ID for the model and deck.
# Using fixed IDs ensures that if you re-run the script, Anki recognizes it as the same deck.
model_id = 2023112215
deck_id = 2023112216

my_model = genanki.Model(
  model_id,
  'System Design: Networking Flashcards',
  fields=[
    {'name': 'Question'},
    {'name': 'Answer'},
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Question}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
    },
  ])

my_deck = genanki.Deck(
  deck_id,
  'System Design: Networking Essentials')

# --- Flashcards from the Initial "Core Concepts" Set ---
initial_core_cards = [
    ('What are the three primary layers of the OSI model that are most relevant to a software engineer in a system design interview?', 
     'Layer 3 (**Network Layer**), Layer 4 (**Transport Layer**), and Layer 7 (**Application Layer**).'),
    ('What is the primary protocol at the Network Layer (Layer 3) and what is its main responsibility?', 
     'The **Internet Protocol (IP)**. It\'s responsible for addressing and routing packets of data from a source host to a destination host across a network.'),
    ('Explain the key difference between TCP and UDP at the Transport Layer (Layer 4).', 
     '**TCP (Transmission Control Protocol)** is connection-oriented, reliable, and ensures ordered delivery of data. **UDP (User Datagram Protocol)** is connectionless, unreliable, and provides no guarantees of delivery or order.'),
    ('When would you choose UDP over TCP for an application?', 
     'You would choose UDP for applications where low latency is more critical than reliability, such as **live video streaming, online gaming, and VoIP (Voice over IP)**.'),
    ('What is the purpose of the TCP three-way handshake?', 
     'It\'s a synchronization process that establishes a reliable connection between a client and a server before data transmission. The steps are **SYN**, **SYN-ACK**, and **ACK**.'),
    ('Name three common protocols at the Application Layer (Layer 7).', 
     '**HTTP/HTTPS**, **REST**, and **GraphQL** are mentioned in the article, but others like gRPC and WebSockets are also common.')
]

# --- Flashcards from the "Thinking-Beyond" Sets ---
thinking_beyond_cards = [
    ('You are designing a real-time chat application like Slack or Discord. Which protocol—TCP or UDP—would you use for the core messaging functionality and why?', 
     'You would use **TCP**. While real-time is important, reliability and ordering are paramount. A user expects their message to be delivered exactly once and in the correct sequence. Missing a message or receiving them out of order would be a poor user experience.'),
    ('Imagine you are building a new video streaming service. You\'ve decided to use UDP for the live streams to reduce latency. What are some of the additional features you would need to build on top of UDP to handle packet loss and ensure a reasonable quality of service?', 
     'You would need to implement application-level mechanisms to manage the unreliability of UDP. This could include: Forward Error Correction (FEC), Adaptive Bitrate Streaming (ABS), and Selective Repeat.'),
    ('A client sends a request to an API endpoint. Walk me through the entire journey of that request from the client\'s perspective to the server\'s response, touching on the roles of the Application, Transport, and Network layers.', 
     '1. **Application Layer**: The client\'s application forms an **HTTP request**. 2. **Transport Layer**: TCP breaks the data into smaller segments, adds its header, and initiates the **three-way handshake**. 3. **Network Layer**: The TCP segments are wrapped in **IP packets** with the source and destination IP addresses for routing. The process is reversed on the server side to handle the request and send back an HTTP response.'),
    ('You are asked to design a service that streams real-time stock market quotes to millions of clients. What protocol would you choose, and what\'s a key design challenge you would need to solve?',
     'You would likely choose a streaming protocol built on top of **TCP**, such as **WebSockets**. WebSockets provide a persistent, bi-directional connection, ideal for pushing frequent updates. A key challenge is **scalability**—managing millions of concurrent connections efficiently.'),
    ('A user complains that your website is "slow." How would you use your knowledge of the different networking layers to begin diagnosing the problem?',
     'I\'d start from the top (Application Layer) and work my way down. Check for slow server-side logic, large API responses (Application Layer). Then, check for high latency or packet loss with `ping` or `traceroute` (Transport/Network Layer). This systematic approach helps to isolate the root cause.')
]

# --- Flashcards from the "Avoiding Common Pitfalls" Set ---
pitfall_cards = [
    ('True or False: DNS is a protocol at the Network Layer (Layer 3).',
     '**False**. DNS (Domain Name System) operates at the **Application Layer (Layer 7)**. It\'s a protocol used by applications to resolve human-readable domain names into IP addresses.'),
    ('What is the difference between HTTP and HTTPS?',
     '**HTTPS** is the secure version of HTTP. It uses **SSL/TLS (Secure Sockets Layer/Transport Layer Security)** to encrypt the communication between the client and server.'),
    ('What is a "port" in the context of networking, and why is it necessary?',
     'A port is a number used by the Transport Layer to identify a specific application or service running on a host. An IP address gets the data to the correct machine, but the port number ensures the data is delivered to the correct process.')
]

# --- Flashcards from the "Complete Fundamentals" Set ---
complete_fundamentals_cards = [
    ('What is the layered architecture of networks, and which three layers are most crucial for system design interviews?',
     'It\'s a model that breaks down complex networking into distinct layers, each with a specific responsibility. The most crucial layers are: **Layer 3: Network Layer**, **Layer 4: Transport Layer**, and **Layer 7: Application Layer**.'),
    ('What is the primary protocol at the Network Layer (Layer 3), and what is its sole responsibility?',
     'The **Internet Protocol (IP)**. Its only job is to handle the addressing and routing of data packets to ensure they reach the correct destination machine.'),
    ('What are the two main protocols at the Transport Layer (Layer 4)?',
     '**TCP (Transmission Control Protocol)** and **UDP (User Datagram Protocol)**.'),
    ('Describe the key characteristics of TCP.',
     'It is **connection-oriented** (establishes a connection before sending data), **reliable** (guarantees data arrives), and ensures **ordered delivery** (data is reassembled in the correct sequence).'),
    ('What is the TCP "three-way handshake"?',
     'It\'s the process TCP uses to establish a reliable connection. **1. SYN**: The client sends a "synchronize" packet. **2. SYN-ACK**: The server sends a "synchronize-acknowledgement" packet. **3. ACK**: The client sends an "acknowledgement" packet, confirming the connection is established.'),
    ('Describe the key characteristics of UDP.',
     'It is **connectionless** (no handshake), **unreliable** (no delivery guarantee), and does not ensure order. Its main advantage is **low latency**.'),
    ('What is the function of a **port number** at the Transport Layer?',
     'A port is a number that identifies a specific application or service running on a machine. The IP address gets the data to the right computer; the port number gets it to the right application on that computer.'),
    ('What are the ideal use cases for UDP?',
     'Applications where speed is more critical than perfect reliability, such as **live video streaming, online gaming, and Voice over IP (VoIP)**.'),
    ('What is the function of the **Domain Name System (DNS)**, and at which layer does it operate?',
     'DNS translates human-readable domain names (e.g., `www.hellointerview.com`) into machine-readable IP addresses. It operates at the **Application Layer (Layer 7)**.'),
    ('What is the fundamental difference between **HTTP** and **HTTPS**?',
     '**HTTPS** is the encrypted version of HTTP. It uses **SSL/TLS** to secure the communication between the client and the server, protecting the data from being intercepted.'),
    ('What is a **RESTful API**?',
     'It\'s an architectural style for APIs that is **stateless** and uses standard **HTTP methods** (GET, POST, PUT, DELETE) to operate on resources. It\'s the default choice for most web APIs.'),
    ('What are the common data formats returned by a REST API?',
     'While it can return many formats, the most common are **JSON** and **XML**.'),
    ('What is the main advantage of using **GraphQL** over REST?',
     'GraphQL gives the client more power and flexibility. It allows the client to request **exactly the data it needs** in a single request, preventing the common REST problems of over-fetching (getting too much data) or under-fetching (needing multiple requests).'),
    ('In a simple web request, what is the first networking step that a browser takes?',
     'The first step is to perform a **DNS lookup** to convert the website\'s domain name into an IP address.')
]

# Combine all card lists into a single list
all_cards = initial_core_cards + thinking_beyond_cards + pitfall_cards + complete_fundamentals_cards

# Add each flashcard to the deck
for question, answer in all_cards:
    my_note = genanki.Note(
        model=my_model,
        fields=[question, answer]
    )
    my_deck.add_note(my_note)

# Save the Anki deck to a file
genanki.Package(my_deck).write_to_file('System_Design_Networking_Essentials_Complete.apkg')

print("Anki deck 'System_Design_Networking_Essentials_Complete.apkg' has been created successfully!")