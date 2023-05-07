# Silver Leaf - Restaurant Web Application
A Restaurant Web Application with **Table Booking, Online Food Ordering and Delivery Tracking.**<br/>

# Brief Description
Silver Leaf is a web-based application that is operated on a web server with its data being retained in a database. It is designed to enable the registered customer to reserve a table at the restaurant at a specified time in accordance with its availability, view and order the offered food item of their choice, and track the delivery of their order. <br/> 
Since the Internet provides a wider range of customers, the application will provide the restaurant with a chance to increase their profits while customers can avail the restaurant's services at the comforts of their homes.

# How to install our project <br/>

First, clone this repository and create a virtual environment using:
```
python -m venv venv
```
Activate the virtual environment:
```
./venv/Scripts/activate
```
Install the required packages using: <br/>
```
pip install -r requirements.txt
```

Create an Authy Application and grab your API Key https://www.twilio.com/console/authy/applications <br/>
Edit `config.py` and update the API key with your application key. Create a secret key for managing sessions. <br/>

`cd` to the location of the cloned repository and run the command:
```
python run.py
```
Copy `http://127.0.0.1:5000/` and paste it in the address bar of a browser.

# Working of our Website 
The front-end portion of the web application has been developed using **HTML, CSS & JavaScript** while the backend portion has been developed using **Flask & SQLite**. The information regarding the users, food items, tables and orders are stored in a database created using **SQLite**. Through the use of **Flask**, the web app interacts with the database. To verify the user's phone number, we have used **Twilio Authy API** and the delivery tracking has been implemented using **Google Maps Javascript API** and **Google Directions API**

### Home Page
![home-page](https://user-images.githubusercontent.com/92647313/143268173-ff82236a-d49e-4ed1-85df-cb132b1be61f.png)

### Registration Page
![register](https://user-images.githubusercontent.com/92647313/143269562-8892a106-5d79-435d-8443-d0033de8d29d.png)

### Phone Number Verification
![otp page](https://user-images.githubusercontent.com/92647313/145669345-1664b46a-d8d8-4862-ae2e-65f2638bbc14.png)

### Login Page
![login](https://user-images.githubusercontent.com/92647313/143269879-8703fd51-d4f1-47ef-a82d-04ab302b3d00.png)

### Forgot Password Page
![forgot](https://user-images.githubusercontent.com/92647313/143270045-95554ba4-dcc2-4d69-8a96-bedd0872ff0a.png)

### Services Page
![services](https://user-images.githubusercontent.com/92647313/143269862-a9794ea5-e50d-4a6b-bfef-397fb30ac60f.png)

### Table Reservation Page
![table-reservation](https://user-images.githubusercontent.com/92647313/143269836-4c35eb47-ae86-41d9-90f1-6ea1b42ce566.png)

### Menu Page
![menu](https://user-images.githubusercontent.com/92647313/143270255-39b2aa04-6469-4fe2-a009-7361a1ee66f7.png)

### Cart Page
![cart](https://user-images.githubusercontent.com/92647313/143269901-21b84d5e-81d3-4ed8-a6be-42692c0ccc58.png)

### Order Confirmation Page
![congrats](https://user-images.githubusercontent.com/92647313/143270441-cb669f88-6d49-4f95-8540-5e5d7d1444f9.png)

### Delivery Tracking Page
![order-id-page](https://user-images.githubusercontent.com/92647313/143269971-bcb3e338-63f9-4440-9dbe-828314a88a0e.png)

![track](https://user-images.githubusercontent.com/92647313/143269928-a232bfc6-8307-4ae9-9aa7-f7e97575199d.png)

### About Us Page
![about-us](https://user-images.githubusercontent.com/92647313/143269712-70a96ef3-38d8-46f9-b361-8eb2e07a8c94.png)

### Contact Us Page
![contact-us](https://user-images.githubusercontent.com/92647313/143270006-6e1ab438-d112-44a0-be1e-a55a857a7dac.png)

# Developed by: <br/>
- [Vijay Lokith R R](https://github.com/vijaylokith)
- [Chinthala Ashish](https://github.com/AshishAsh01)
- [Elvis Theyo](https://github.com/avocadopelvis) 

If you would like to make any suggestions to improve the web application, feel free to contact any of the developers.
