
### Snowman Challenge

Create and explore tourist spots on a map.  
Create a RESTful API for the app.  


##### API requirements  
1.1 - API RESTful  
1.2 - Python with Flask  


##### Rules  
2.1 - Anonymous users can only see things.  
2.2 - Initial Categories are "Park", "Museum", "Theater", "Monument"  
2.3 - anonymous user  
    2.3.1 - explore tourist spots (consume)  
    2.3.2 - sign up using Facebook account (register)  
    2.3.3 - sign in using Facebook account (consume)  
2.4 - logged user   
    2.4.1 - register a tourist spot (picture, name, geographical location, category) 
    2.4.1.1 - converter the picture into a string long
    2.4.2 - explore tourist spots (consume)  
    2.4.3 - tourist spots in a 5 km radius from a given location (consume)  
    2.4.4 - search for tourist spots by name  
    2.4.5 - comment about a tourist spot (search the spot and comment it)   
    2.4.6 - see comments about a tourist spot (search the spot and print comments)   
    2.4.7 - add pictures to a tourist spot (various pictures for each spot)   
    2.4.8 - remove pictures I added to a tourist spot  
    2.4.9 - favorite a tourist spot  
    2.4.10 - remove a tourist spot from my favorites  
    2.4.11 - upvote a tourist spot   
    2.4.12 - see the tourist spots I registered  
    2.4.15 - create new categories  



##### Deliverables  
3.1 - The source code in a public git repository  
3.2 - A public live demo  
3.3 - An OpenAPI 3.0 document  
3.4 - Instructions how to run the development environment  
3.5 - Instructions how to deploy    
3.6 - A Postman collection   


##### Comments
4.1 - All tourist spots are associated with some user
4.1 - Not all users are associated with come tourist spot (new users)
4.3 - There are two ways to register a tourist spot
4.3.1 - user
4.3.2 - admin


##### Endpoints

POST /user {name:}
POST /user/<string:name>/tourist-spot  {picture:, name:, gps:, category:}

GET /user/<string:name> 
GET /user/<string:name>/tourist-spot/<string:name>


POST /admin/tourist-spots {picture:, name:, gps:, category:}

GET /user/<string:name>/tourist-spot/<string:name>
/users/tourist-spot/commits

/users/<string:tourist-spot>/<tuple:gps_cords>                  2.4.3 
/users/<sting:tourist-spot>/<integer:upvote>                   2.4.11
/users/<string:tourist_spot_name>/commits              2.4.6

/tourist-spots/<string:name>        2.4.4 


