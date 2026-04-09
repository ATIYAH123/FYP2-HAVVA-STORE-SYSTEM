# 🌸 Havva Store System - User Manual & Guide

Welcome to the **Havva Store Grocery** system. This guide provides instructions on how to access and test the platform's key features.

---

## 🔑 Login Credentials

The system is equipped with two primary roles for testing. Both use the default password: **`password`**.

### 🛠️ Administrator Account
Use this to manage categories, products, and monitor all store orders.
- **Email**: `admin@havva.com`
- **Password**: `password`
- **Dashboard Features**: Store metrics (Total Sales, Orders), Recent Transactions list.

### 🛍️ Customer Account
Use this to browse the store, add items to your basket, and track your orders.
- **Email**: `customer@havva.com`
- **Password**: `password`
- **Dashboard Features**: Personal Order History with real-time status tracking.

> [!NOTE]
> If you have created your own account, you can also use those details.

---

## 🏗️ Core System Workflows

### 1. The Shopping Experience
- **Browsing**: Visit the [Home Page](/) to see the "Pick Your Grocery" grid.
- **Cart**: Add items using the **"ADD TO CART"** button. A premium drawer will slide from the right side.
- **Checkout**: Click **"Proceed to Checkout"** from the cart drawer.

### 2. Testing the Payment Gateway (Dummy Mode)
We have implemented a **ToyyibPay Simulation** for testing without real money.
1. Fill in your delivery details on the Checkout page.
2. Ensure your phone number is entered (it will be saved to your profile).
3. Select **"Confirm & Pay"**.
4. You will be redirected to our **Havva Mock Payment Gateway**.
5. Click **"Pay Now"** (Success Simulation) or **"Cancel"** (Fail Simulation).

### 3. Order Tracking (Customer)
1. After a successful payment, go to your [/dashboard](/dashboard).
2. Look for the **"Mementos of Selection"** section.
3. You will see your order status as **"Processing"**.

### 4. Order Management (Admin)
1. Log in as an Admin.
2. Go to the [Dashboard](/dashboard) to see high-level stats.
3. Navigate to **"Products"** or **"Categories"** in the navigation bar to manage the catalog.
4. (Optional) Access the Admin Order list to update customer order statuses.

---

## 🎨 Aesthetics & Design
The system follows a **Luxury Store** aesthetic:
- **Serif Fonts**: Used for headers to give a premium feels.
- **Havva Pink & Stone**: Our signature color palette.
- **Micro-animations**: Smooth transitions when browsing and managing orders.

---
*Curated with Love by the Havva Development Team & Antigravity AI.*
