# python-ecommerce-cls

# 🛒 Python E-commerce (Console Application)

Bu loyiha Python’da yozilgan **console-based e-commerce tizimi** bo‘lib,
foydalanuvchilar mahsulotlarni ko‘rish, savatchaga qo‘shish va buyurtma berish
imkoniyatiga ega bo‘ladi.

Loyiha **OOP**, **Service Layer**, va **Clean Architecture** tamoyillari asosida
yaratiladi va keyinchalik **JSON yoki Database** bilan ishlashga tayyor.

---

## 🎯 Loyihaning maqsadi

- Backend arxitektura tushunchalarini amaliyotda qo‘llash
- Real e-commerce tizimining mantiqiy modelini qurish
- Keyinchalik FastAPI yoki Django’ga oson ko‘chirish

---

## 📌 Asosiy funksiyalar

- Foydalanuvchini ro‘yxatdan o‘tkazish (register)
- Login / logout
- Mahsulotlar bilan ishlash
- Savatcha (Cart) boshqaruvi
- Buyurtma (Order) yaratish
- Ma’lumotlarni JSON faylda saqlash

---

## 📂 Loyiha strukturasi

```text
ecommerce/
│
├── main.py
│
├── core/
│   ├── __init__.py
│   ├── database.py
│   └── utils.py
│
├── models/
│   ├── __init__.py
│   ├── user.py
│   ├── product.py
│   ├── cart.py
│   ├── cart_item.py
│   ├── order.py
│   └── order_item.py
│
├── services/
│   ├── __init__.py
│   ├── auth_service.py
│   ├── cart_service.py
│   └── order_service.py
│
├── data/
│   ├── users.json
│   ├── products.json
│   ├── carts.json
│   └── orders.json
│
└── README.md

## 🧠 Arxitektura yondashuvi

Loyiha **3 qatlamli arxitektura** asosida quriladi:

### 1️⃣ Models (Data Layer)
- Faqat ma’lumotlarni ifodalaydi
- Business logika yo‘q
- JSON, input, print ishlatilmaydi

### 2️⃣ Services (Business Logic Layer)
- Barcha harakat va mantiq shu yerda
- Model’lar bilan ishlaydi
- JSON bilan o‘qish / yozish qiladi

### 3️⃣ Main (Presentation Layer)
- Foydalanuvchi bilan muloqot (CLI)
- Service’larni chaqiradi
- Input / output faqat shu qatlamda

### ✅ Ushbu yondashuv afzalliklari
- Kod toza va tartibli bo‘ladi
- Test yozish osonlashadi
- Database yoki API qo‘shish yengillashadi

---

## 📦 Papkalar va fayllar vazifasi

---

## ▶️ `main.py`

**Vazifasi:**
- Dastur ishga tushadigan asosiy fayl
- Foydalanuvchi menyusi (CLI)
- Service layer bilan ishlash

**Bu yerda bo‘ladi:**
- `input()`
- `print()`
- menu va flow boshqaruvi

**❌ Bu yerda bo‘lmaydi:**
- Model yozish
- Business logika yozish

---

## ⚙️ `core/` – infratuzilma qatlami

### `core/database.py`

**Vazifasi:**
- JSON fayllar bilan ishlash
- Ma’lumotlarni o‘qish (read)
- Ma’lumotlarni yozish (write)

**Kelajakda:**
- PostgreSQL yoki boshqa DB bilan almashtiriladi

**Mas’ul funksiyalar:**
- `load_users()`
- `save_users()`
- `load_products()`
- `save_orders()`

---

### `core/utils.py`

**Vazifasi:**
- Yordamchi funksiyalar
- ID generator
- Validatsiya (bo‘sh qiymat, manfiy son va h.k.)

---

## 🧩 `models/` – Data (Model) qatlami

📌 Bu papkada **faqat class va fieldlar** bo‘ladi.  
📌 Bu yerda **JSON, input, print** ishlatilmaydi.

---

### `models/user.py`
**Foydalanuvchi modeli**

**Fieldlar:**
- `id`
- `username`
- `password`
- `first_name`
- `last_name`

📌 Login yoki register bu yerda yozilmaydi.

---

### `models/product.py`
**Mahsulot modeli**

**Fieldlar:**
- `id`
- `name`
- `category`
- `price`
- `sale`
- `stock`
- `description`

---

### `models/cart_item.py`
**Savatchadagi bitta mahsulot**

**Fieldlar:**
- `product`
- `quantity`

---

### `models/cart.py`
**Savatcha modeli**

**Fieldlar:**
- `user`
- `cart_items` (list)

**Mas’uliyati:**
- Umumiy narxni hisoblash

---

### `models/order_item.py`
**Buyurtmadagi bitta mahsulot**

**Fieldlar:**
- `product`
- `quantity`

---

### `models/order.py`
**Buyurtma modeli**

**Fieldlar:**
- `user`
- `order_items`
- `total_price`

📌 Order — bu tarix, u keyin o‘zgarmaydi.

---

## 🔧 `services/` – Business Logic qatlami

📌 Bu qatlamda **hamma amaliy mantiq yoziladi**.

---

### `services/auth_service.py`
**Mas’uliyati:**
- Register
- Login
- Logout
- User’larni JSON’dan o‘qish va saqlash

---

### `services/cart_service.py`
**Mas’uliyati:**
- Savatcha yaratish
- Mahsulot qo‘shish
- Mahsulot o‘chirish
- Cart ma’lumotlarini JSON’da saqlash

---

### `services/order_service.py`
**Mas’uliyati:**
- Cart → Order aylantirish
- Total price hisoblash
- Order’ni JSON’da saqlash
- Cart’ni tozalash

---

## 💾 JSON bilan ishlash (Data Layer)

Loyiha quyidagi JSON fayllardan foydalanadi:

```text
data/
├── users.json
├── products.json
├── carts.json
└── orders.json
