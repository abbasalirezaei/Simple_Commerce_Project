# Commerce_Project

> [!NOTE]
> - python3 -m venv .venv 
> - pip3 install -r requeriments.txt
> - python3 manage.py makemigrations and migrate
> - python3 manage.py createsuperuser
> - python3 manage.py runserver

# About the Project
This project contains 3 apps
1. product
   - models.py
     - Category
     - Product
   - views.py
     - Home 
1. cart
   - models.py
     - Cart
     - Order
   - views.py
     - add_to_cart
     - remove_from_cart
     - decreaseCart
     - CartView 

1. checkout
   - models.py
     - BillingAddress
   - views.py
     - checkout
     - payment
     - charge
     - oderView
