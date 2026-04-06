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


---

## 🧩 Models

### TeaShop
- name
- location
- rating
- created_at

### TeaInventory
- tea_shop (ForeignKey)
- available_quantity
- price_per_cup

### Order
- tea_shop (ForeignKey)
- quantity
- total_price
- order_time
- status (PENDING / COMPLETED / CANCELLED)

---



