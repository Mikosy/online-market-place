# OMP

Online Market Place

Project description:
An online marketing website that enables customer purchase items from sellers.

## project's Models:
* CustomUser
* Conversation
* ConversationMessage
* Category
* Product
* Order
* OrderItem
* Transaction



## Pages:
### Dashboard
* Dashboard
  * analytics
  * Supplier
  * General setting
* Frontend
  * Customer
  * Support
  * item
  * Item family
  * login
  * invoice-in
  * invoince-out

## Language:
  Django framework
  Python >=3.8
  Sql
  
## How to install it:
  1. Install python>=3.8
  2. Install Django
   `pip install django`
  3. Clone the Grocsale repository
   `git clone https://github.com/EmadAlamoudi/Grocsale.git`
  4. Install dependencies
   `pip install -r requirements.txt`
   `sudo apt install libcairo2`
   `sudo apt-get install libgl1`
    For for Windows:
   `pip install pipwin`
   `pipwin install cairocffi`
    Run the server
   `python manage.py runserver`
  5. If you encounter an error while installing all packages using the requirements.txt file, try installing each package independently without specifying a version number.
     For example, instead of running `pip install django==4.0.0`, use `pip install django`.
