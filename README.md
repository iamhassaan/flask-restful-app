# flask-restful-app

The Idea behind this app is to create a "Spanish Retail Store" rest api. With the abiity to create, read, update and delete Stores, Users, and Items in a database. 

The API has been created with "Object Oriented Programming" Architecture,
making sure all the resources and models (functions) remain seperate.

The API has been Secured by JWT Authentication and https. The external API is provided by Yandex (Translation API), it will help in translating spanish words into english or vice versa. More than 12 .py files have been made to complement the coding architecture in the rest api. The data gets stored in a SQlite database. 

To make best use of this API, Postman would be required.


Create User:
<POST /register>
Description:
CreateUser, creates a user in our SQLITE database, creates a JWT token, that can be used to access the list of stores


User Authentication:
<POST /auth>
Description:
copy the JWT request from the create user token and paste it and then enter it, to get access to the database

Create Store:
<POST /store/<name>>
Description:
Creates a store in the database, with the name of the store in the body tag.


Create Item:
<POST /items/<name>>
Description:
Creates an Item, inside a store, With a name and a price in the body tag.
 

Get all store name:
<GET /stores>
Description:
Get all stores entered in the database.
 
 
Get a specific store name:
<GET /store/name>
Description:
Gets the name of the specific store created  
 
 
Get an item name:
<GET items/<name>>
Description:
Gets the item from the 
  

Change an item:
<PUT /item/<name>>
Description:
changes an item properties in the database
  
  
Delete an item:
<DEL /item/name>>
Description:
deletes an item in the database.

Delete a store:
<DEL /store/name>>
Description:
Deleted a store in the database.


Using External API:
<POST translate/<word>>
Description:
Sends a request to external api to get the translation.
  
  
  
The translated word can be used to create a store or item name in the database.
  
 
 
Link to URL:
https://my-very-own-stores-api.herokuapp.com/    or
https://my-own-stores-api.herokuapp.com/  


If none of the link works (due to internal server error), I can also demonstrate the api in local host. 
  
  
  



  
