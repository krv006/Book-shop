# 📚 Self Study - Django REST Framework API

This project is built with **Django REST Framework (DRF)** and provides a robust backend system with authentication, e-commerce features, automated tasks, and external API integrations.

---

## 🚀 Features

- **Authentication & Authorization**
  - ✅ JWT-based authentication (login, register)
  - ✅ Admin login via email
  - ✅ One-time link for registration (expires in 3 days)
  - ✅ Celery for background tasks (email verification, notifications)
  - ✅ Account lockout after multiple failed login attempts (5 min block)

- **E-Commerce Functionalities**
  - ✅ **Models**: Book, Author, Cart, Wishlist, Order, OrderItem
  - ✅ **Wishlist & Cart APIs** (Add, Remove, List)
  - ✅ **Book Detail API** (Slug-based retrieval)
  - ✅ **Book Pricing** (Default in USD, adjusts based on user’s currency)
  - ✅ **Address Management**
    - Default billing & shipping addresses cannot be deleted
    - Addresses are sorted (default first, then alphabetically)
  - ✅ **Currency Exchange API Integration** (NBU, Bank.uz)

- **Background Tasks & Automation**
  - ✅ **Celery & Redis** for email sending, notifications
  - ✅ **Django Custom Commands**
    - Fake data generation (Faker, Django Seed)
    - Bulk data population (Authors, Books, Addresses)
  - ✅ **Database Backup** (Docker-based, requires a server)

- **Admin & Management**
  - ✅ **Django Custom Admin** with enhanced UI
  - ✅ **Django ORM Optimizations** (Query improvements)

- **Deployment & Monitoring**
  - ✅ **CI/CD Integration** (Automated deployment)
  - ✅ **Metabase for analytics & reports**
  - ✅ **Cron Jobs (Crontab) for scheduled tasks**
  - ✅ **Testing**: `pytest` & `unittest`

---

## 🛠 Tech Stack

| **Technology**   | **Purpose** |
|-----------------|------------|
| **Django** | Web framework |
| **Django REST Framework (DRF)** | API development |
| **PostgreSQL** | Database |
| **Redis** | Task queue |
| **Celery** | Background task execution |
| **Docker** | Containerization |
| **Metabase** | Data analytics & dashboards |
| **Crontab** | Automated scheduled tasks |
| **CI/CD (GitHub Actions)** | Automated deployment |
| **JWT Authentication** | Secure authentication |
| **Faker & Django Seed** | Dummy data generation |

---

## 📂 Project Structure

