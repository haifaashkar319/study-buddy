from django.shortcuts import render, redirect
from .models import feed
# from .models import request
from django.http import JsonResponse
from django.http import HttpResponse
from django.contrib import messages
import mysql.connector
import mysql.connector
import json

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def create_feed(request):
    if request.method == 'GET':
        # Get the values from query parameters in the URL
        userId = request.GET.get('userId')
        details_value = request.GET.get('detailsValue')
        knowledge_level = request.GET.get('knowledgeLevel')
        selected_course = request.GET.get('selectedCourseSend')
        

            # Create a new FeedTable object and save it to the database
        feed_item = feed(
                Feed_Owner=userId,
                Description=details_value,
                Knowledge=knowledge_level,
                course=selected_course,
                isDeleted=False
            )
        
        feed_item.save(using='sign_up_pages_db')

        return redirect('/feed/') # Redirect to the feed page or another page
        

    return HttpResponse('Invalid request method')


# def CreateFeed(request,user_id, description, knowledge, course_id):
#     try:
#         # Establish a connection to the database
#         connection = mysql.connector.connect(
#         host='localhost',  # Replace with your database host
#         user='root',       # Replace with your database username
#         password='Thejocker21',  # Replace with your database password
#         database='userprofile'  # Replace with your database name
#     )



#         # Create a cursor object to execute SQL queries
#         cursor = connection.cursor()
        
    
        
#         # Insert a new feed into the Feed_Table
#         insert_feed_query = """
#         INSERT INTO Feed_Table (Feed_Owner, Description, Knowledge, Course, IsDeleted)
#         VALUES (%s, %s, %s, %s, %s)
#         """
#         cursor.execute(insert_feed_query, (user_id, description, knowledge, course_id, 0))  # 0 indicates not deleted

#         # Commit the changes to the database
#         connection.commit()

#         # Close the cursor and database connection
#         cursor.close()
#         connection.close()

#         print("Feed created successfully!")
#     except Exception as e:
#         print(f"An error occurred: {str(e)}")
        
        
def Feed(request, *args, **kwargs):
    # Get the currently logged-in user
    user_id = request.session.get('user_id')
    return render(request, "feed.html", {'username': user_id})



def id(request):
   user_id = request.session.get('user_id')
   return HttpResponse(user_id)


def Fetch(request, *args, **kwargs):
  

    connection = mysql.connector.connect(
        host='localhost',  # Replace with your database host
        user='root',       # Replace with your database username
        password='Thejocker21',  # Replace with your database password
        database='userprofile'  # Replace with your database name
    )



    cursor = connection.cursor()


    data_to_send = []
    data_to_send2 = []
    data_to_send3 = []
    data_to_send4 = []
    data_to_send5 = []

    query = "SELECT * FROM course_table;"
    cursor.execute(query)
    course_table_data = cursor.fetchall()
    data_to_send.append(course_table_data)
    

    query = "SELECT * FROM feedtable;"
    cursor.execute(query)
    feed_data = cursor.fetchall()
    data_to_send2.append(feed_data)


    query = "SELECT * FROM major_table;"
    cursor.execute(query)
    major_table_data = cursor.fetchall()
    data_to_send3.append(major_table_data)

     
    query = "SELECT * FROM requesttable;"
    cursor.execute(query)
    request_data = cursor.fetchall()
    data_to_send4.append(request_data)


    query = "SELECT * FROM sign_up_pages_user;"
    cursor.execute(query)
    user_data = cursor.fetchall()
    data_to_send5.append(user_data)
    
    
    user_id = request.session.get('user_id')
    
    cursor.close()
    connection.close()
    

    combined_data = {
        'course_table': data_to_send,
        'feedtable': data_to_send2,
        'major_table': data_to_send3,
        'requesttable':data_to_send4,
        'sign_up_pages_user': data_to_send5,
        'user_id' :user_id
    }

    return JsonResponse(combined_data)
    json_data = json.dumps(data_to_send)


    return JsonResponse(json_data, safe=False)
    
