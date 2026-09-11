# 🚗 Car Sales Recommendation & Management System

> A Python-based intelligent car sales and inventory management system that helps customers find suitable vehicles based on their budget, preferred model, and mileage requirements while automating sales tracking, inventory updates, and customer email notifications.

---

## 📌 Project Overview

The **Car Sales Recommendation & Management System** is designed to streamline the process of searching, recommending, and selling used cars. The system analyzes customer requirements such as budget, preferred vehicle model, and maximum kilometers driven to identify the most suitable cars from the available inventory.

Once a purchase is completed, the system automatically:

✅ Calculates the final selling price based on ownership history

✅ Sends a purchase confirmation email to the customer

✅ Records transaction details

✅ Updates inventory by removing sold vehicles

✅ Maintains a complete sales history database

This project demonstrates practical applications of **Python programming**, **data processing**, **business logic implementation**, **automation**, and **customer communication systems**.

---

# ✨ Key Features

## 🔍 Smart Vehicle Search

* Search vehicles by model name
* Budget-based filtering
* Mileage (KM) based filtering
* Intelligent recommendation matching
* Quick vehicle comparison

---

## 💰 Dynamic Pricing System

The system automatically calculates the final selling price based on vehicle ownership history.

### Pricing Logic

| Previous Owners | Discount Applied |
| --------------- | ---------------- |
| 1 Owner         | 5% Discount      |
| Multiple Owners | 7.5% Discount    |

This simulates a real-world dealership pricing strategy.

---

## 🤖 Recommendation Engine

The recommendation engine filters vehicles using:

* Customer budget range
* Preferred car model
* Maximum kilometers driven
* Ownership-based pricing adjustments

Only vehicles meeting all customer criteria are recommended.

---

## 📊 Inventory Management

The system maintains a live vehicle inventory.

### Features

* Tracks available vehicles
* Automatically removes sold vehicles
* Updates inventory in real-time
* Prevents duplicate sales
* Maintains inventory consistency

---

## 📧 Automated Email Notification System

After a successful purchase, the system automatically sends a confirmation email containing:

* Vehicle ID
* Vehicle Model
* Kilometers Driven
* Number of Previous Owners
* Final Purchase Price
* Purchase Date & Time

### Benefits

* Improves customer communication
* Provides purchase proof
* Automates dealership workflow
* Enhances customer experience

---

## 📝 Sales Record Management

Every completed purchase is stored for future reference.

### Stored Information

* Customer Email
* Vehicle ID
* Vehicle Model
* Vehicle Mileage
* Final Purchase Price
* Transaction Timestamp

This enables sales tracking and reporting.

---

## 📂 CSV-Based Database System

Instead of using a traditional database, this project uses CSV files for lightweight data management.

### Files Used

#### 🚘 cars.csv

Stores:

* Vehicle ID
* Model
* Kilometers Driven
* Previous Owners
* Vehicle Price

#### 📄 sold_cars.csv

Stores:

* Customer Email
* Vehicle Details
* Final Price
* Purchase Time

---

# 🏗️ System Workflow

```text
Customer Input
      │
      ▼
Budget Validation
      │
      ▼
Model Filtering
      │
      ▼
KM Filtering
      │
      ▼
Price Adjustment
      │
      ▼
Recommended Cars
      │
      ▼
Purchase Selection
      │
      ▼
Email Confirmation
      │
      ▼
Sales Record Update
      │
      ▼
Inventory Update
```

---

# 🛠️ Technologies Used

| Technology        | Purpose                  |
| ----------------- | ------------------------ |
| 🐍 Python         | Core Development         |
| 🐼 Pandas         | Data Processing          |
| 📧 SMTP           | Email Automation         |
| 📂 CSV Files      | Data Storage             |
| 🕒 Datetime       | Timestamp Management     |
| 🔄 Business Logic | Recommendation & Pricing |

---

# 📁 Project Structure

```text
Car-Sales-Management-System
│
├── data
│   ├── cars.csv
│   └── sold_cars.csv
│
├── src
│   └── main.py
│
├── screenshots
│
├── README.md
├── LICENSE
├── requirements.txt
├── sample.env
└── .gitignore
```

---

# 🚀 Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/car-sales-management-system.git
```

## 2️⃣ Navigate to Project Folder

```bash
cd car-sales-management-system
```

## 3️⃣ Install Dependencies

```bash
pip install pandas
```

---

# ⚙️ Configuration

Update the following values in the source code:

```python
DATA_FILE = "data/cars.csv"
SOLD_FILE = "data/sold_cars.csv"

SENDER_EMAIL = "your_email@gmail.com"
APP_PASSWORD = "your_app_password"
```

---

# ▶️ Run the Project

```bash
python src/main.py
```

---

# 📈 Skills Demonstrated

This project demonstrates:

* Python Programming
* Data Analysis Fundamentals
* Data Filtering Techniques
* Business Logic Implementation
* Inventory Management
* Automation Systems
* Email Integration
* CSV Data Handling
* Customer Data Management
* Recommendation Systems
* Sales Tracking Systems
* File Management
* Real-World Workflow Automation

---

# 🎯 Real-World Applications

* Used Car Dealership Management
* Vehicle Inventory Systems
* Automotive Sales Platforms
* Customer Relationship Systems
* Sales Tracking Applications
* Business Process Automation

---

# 🔮 Future Enhancements

### 🤖 Machine Learning Integration

* Car Price Prediction Model
* Vehicle Recommendation Model
* Customer Purchase Prediction
* Demand Forecasting

### 🌐 Web Application

* Django/Flask Web Portal
* Customer Dashboard
* Admin Dashboard

### 🗄️ Database Integration

* MySQL
* PostgreSQL
* MongoDB

### 📊 Analytics Dashboard

* Sales Reports
* Revenue Tracking
* Customer Insights
* Inventory Analytics

---

# 📸 Project Screenshots

Add screenshots inside the `screenshots/` folder and showcase:

* Vehicle Search
* Recommendation Results
* Purchase Process
* Email Confirmation
* Inventory Updates

---

# 📜 License

This project is licensed under the MIT License.

---

⭐ If you found this project useful, consider giving it a star on GitHub!
