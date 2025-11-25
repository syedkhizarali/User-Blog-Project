# 💬 User-Blog-Project (Created By: Syed Khizar Ali)
User-Blog-Project

## 💬 Description: User-Blog-Project
User-Blog-Project is a robust and scalable web application backend built with **FastAPI** that enables users to register, authenticate, and manage their own blog posts securely. The project includes full user authentication and authorization using **JWT (JSON Web Tokens)** and **OAuth2** schemas to protect sensitive endpoints and ensure secure login and registration flows.  

The application uses **Pydantic schemas** for strict data validation and **SQLAlchemy ORM models** to define relationships between users and their blogs, providing a clean and efficient interface for database operations. The backend connects to a **MySQL database** to store and fetch user credentials, blog posts, and related data.  

The project is structured modularly with dedicated files:  
- `user_routes.py` – Handles all user-related API endpoints (registration, login, profile).  
- `user_blogs.py` – Manages blog-related operations such as create, read, update, delete (CRUD).  
- `schemas.py` – Defines Pydantic schemas for request validation and response models.  
- `uploads.py` – Handles file uploads (e.g., blog images or attachments).  
- `config.py` – Centralized configuration for database connection, environment variables, and project settings.  

This project follows **best practices** for FastAPI development including dependency injection, modular routing, and clear separation of concerns. It is fully compatible with **uvicorn** for running ASGI servers, making it production-ready and highly performant.  

With this setup, developers can easily extend the project with additional features such as comments, likes, or notifications while keeping the core backend secure, fast, and maintainable.

---

## ⚙️ Technologies Used
- **Backend Framework:** FastAPI  
- **Server:** Uvicorn (ASGI server)  
- **Authentication & Security:** JWT, OAuth2, Password Hashing  
- **Database:** MySQL  
- **ORM & Data Validation:** SQLAlchemy, Pydantic  
- **Python Modules:** Databases, Typing, FastAPI Dependencies, Passlib  
- **File Handling:** Uploads via `uploads.py` module  
- **Configuration & Environment:** `.env` setup, Config module for central settings  
- **Project Architecture:** Modular, scalable, and maintainable folder structure  
<h2 align="center">📸 Project Screenshots</h2>

<p align="center">
  <img src="assets/screenshot1.png" width="600">
</p>

<p align="center">
  <img src="assets/screenshot2.png" width="600">
</p>
