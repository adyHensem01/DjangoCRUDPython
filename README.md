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
   
5. To test the CRUD you may use POSTMAN application as third parties.

   Example 1 (Create)
   ![image](https://github.com/user-attachments/assets/6e43d9ce-261a-4992-92be-d108ef36bb35)
