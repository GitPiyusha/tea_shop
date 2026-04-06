# tea_shop
# 🍵 Tea Shop Management API

A RESTful backend system built using Django & Django REST Framework to manage multiple tea shops, their inventory, and customer orders.

---

## 📌 Features

### 🛠️ Admin APIs
- Create, update, delete tea shops
- Manage inventory (stock & price)

### 📦 Customer APIs
- View available tea shops
- Place tea orders
- Automatic price calculation
- Inventory reduction after order

---

## 🏗️ Tech Stack

- Python 3.12
- Django
- Django REST Framework (DRF)
- SQLite (default DB)

---

## 📂 Project Structure
tea_shop/
│── teaShop/
│ ├── models.py
│ ├── views.py
│ ├── serializers.py
│ ├── urls.py
│
│── tea_shop/
│ ├── settings.py
│ ├── urls.py
│
│── manage.py


## Assignment: Tea Shop Management API 

### Problem Statement: 
You are building a RESTful backend for a multi-branch tea shop system. The system 
allows admins to manage multiple tea shops, each offering tea with different stock levels, 
prices, and ratings. End users should be able to view available tea shops and place tea 
orders based on availability. 

 ##Requirements: 

️ Project Structure 
• Django project: tea_time 
• App: tea_shop 

## Models 
TeaShop: 
• id (AutoField) 
• name (CharField) 
• location (CharField) 
• rating (FloatField, 0 to 5) 
• created_at (DateTimeField) 
TeaInventory: 
• id (AutoField) 
• tea_shop (ForeignKey to TeaShop) 
• available_quantity (IntegerField – number of cups) 
• price_per_cup (FloatField) 
Order: 
• id (AutoField) 
• tea_shop (ForeignKey to TeaShop) 
• quantity (IntegerField) 
• total_price (FloatField – auto calculated) 
• order_time (DateTimeField) 
• status (CharField: choices – PENDING, COMPLETED, CANCELLED) 

## API Endpoints 

️ Admin APIs (CRUD): 
• GET /tea-shops/ → List all tea shops 
• POST /tea-shops/ → Create a new tea shop 
• PUT /tea-shops/<id>/ → Update a tea shop 
• DELETE /tea-shops/<id>/ → Delete a tea shop 
• GET /inventory/ → List inventory for all shops 
• POST /inventory/ → Add/update inventory for a shop 

 Customer APIs: 
• GET /available-tea/ → List tea shops with available quantity > 0, sorted by rating or 
price 
• POST /order/ 
o Request: { "tea_shop": 1, "quantity": 2 } 
o Checks if quantity is available 
o Responds with total price and order status 
o Reduces inventory if order is successful 
✨ Optional Enhancements (Bonus) 
• Add a view to scrape or generate ratings from a sample site (for tea reviews) 
• HTML template to show top 5 rated tea shops 
• Add basic Swagger API docs using drf-yasg 
✅ Deliverables: 
• Django project code (GitHub or ZIP) 
• README with setup instructions and example API calls 
• (Optional) Postman collection 
• Notes on what was implemented vs what's pending (if applicable) 
⏳ Deadline: 
• 5 May 2025 
Let me know if you want me to write up a sample README, Swagger sample, or initial 
project structure for this. 



