![image](https://github.com/user-attachments/assets/79066c50-a329-4743-a650-91556919d6f3)

The Electronic Commerce System is a platform designed for online merchandise transactions, integrating various functions such as vendor product listing and sales, buyer product browsing and purchasing, and post-sale communication between both parties. This system manages customer basic information, salesperson details, product data, purchase records, post-sale information, and customer service details. 

1. It features three user roles: customer, vendor, and administrator, each with a unique frontend interface for distinct functions:

- **Customers** can view and modify their basic information, browse product listings, place orders, manage their favorites, track order information, confirm deliveries, and rate their purchases. They can also raise post-sale queries about their purchases.

- **Vendors** can access and update their basic information, view, input, and modify (only within their store) product details. They can process orders and respond to post-sale queries.

- **Administrators** have the authority to conduct conditional queries, summaries, and sorting of customer, salesperson, product, order, and post-sale information. They also have editing privileges for certain data tables.

- The system also offers customer registration.

2. In terms of data requirements, the system design is informed by an analysis of real-world commercial transactions and existing e-commerce software. The data items and structures include:

- User Table: Contains all system login accounts, with data items including account ID, password, and role.

- Order Information Table: Holds data like order ID, customer ID, product ID, quantity, order status, order time, and customer ratings.

- Customer Information Table: Includes customer ID, account ID, name, contact number, delivery address, bank for payments, and bank card number.

- Administrator Information Table: Contains administrator ID, account, and phone number.

- Vendor Information Table: Holds vendor ID, account, responsible administrator ID, name, description, contact number, bank for receipts, and bank card number.

- Product Information Table: Details product ID, vendor ID, category ID, name, inventory, description, price, and status.

- Post-Sale Information Table: Includes post-sale message ID, corresponding order ID, sender account, and message content.

- Product Category Table: Contains category ID and name.

- Favorites Table: Holds customer ID and product ID.

3. The system design aims to:

- Utilize existing software and hardware environments, using Python as the programming language, MySQL for database management, and advanced e-commerce system development solutions to enhance the system's development and application.

- Comply with product purchase system management regulations, meeting the tripartite needs of customers, administrators, and vendors, ensuring an intuitive, convenient, safe, and user-friendly operation process.

- Adopt a C/S (Client/Server) architecture and modular program design for flexibility in system function combination and modification, facilitating system development and maintenance.
