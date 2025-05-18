Django CRUD
1. Make sure you have setup the libraries and python
    
		-> make sure you have python install (this project using Python 3.7.4)
    
		-> pip install django (versioni 5.2.1)
2. This project using SQLite3
3. The most important file as below:
    
		->app.py to config the application name
    
		->model.py is to create a model for this application
   
	  ->view.py is to define function what to do and integration with the sql
      (this application using @csrf_exempt  # Disable CSRF just for this demo (not for production!) )
    
      ->url.py is to URL configruation for this application example [path('books/<int:book_id>/update/', views.book_update),]
4. To start the application you must type to the terminal/batch for example:

    -> Make the SQL lite enable by enable the migrations as below
 
   ![image](https://github.com/user-attachments/assets/79cfe964-1d0e-4f88-9267-ca7e2e492f2d)

    ->then start you server

    ![image](https://github.com/user-attachments/assets/c929e32a-a285-434a-a2b0-7e28d34a1cc5)
	
6. To test the CRUD you may use POSTMAN application as third parties.

   Example 1 (Create)
   ![image](https://github.com/user-attachments/assets/6e43d9ce-261a-4992-92be-d108ef36bb35)

   Example 2 (Read)
   
   
   ![image](https://github.com/user-attachments/assets/1b724953-0477-46eb-a7c8-b758ff47b5f2)


   Example 3 (Update)
   
   
   ![image](https://github.com/user-attachments/assets/d6887576-a224-4002-901c-fac3dbaadb76)

   Example 4 (Delete)
   
   ![image](https://github.com/user-attachments/assets/5f5e2547-2d14-4100-9643-ffdb357c929e)

   

