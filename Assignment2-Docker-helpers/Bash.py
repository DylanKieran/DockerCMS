import os

selection = 0
id = 0
while selection != 13:
    print("\n")
    print("Menu")
    print("Enter and Select a function")
    print("1. List Containers")
    print("2. List Running Containers")
    print("3. List Images")
    print("4. Inspect an Image")
    print("5. Delete all Containers")
    print("6. Delete Individual Container")
    print("7. Delete all Images")
    print("8. Delete Individual Image")
    print("9. Create a Container")
    print("10. Create an Image")
    print("11. Update Container")
    print("12. Update Image")
    print("13. Exit")
    print("\n")
    selection = int(raw_input("Select Function \n"))
    if selection == 13:
        break
    elif selection == 1:
        # List Containers
        os.system("curl -s -X GET -H 'Accept: application/json' http://35.205.181.127:8080/containers | python -mjson.tool")
    elif selection == 2:
        # List all Running containers
        os.system("curl -s -X GET -H 'Accept: application/json' http://35.205.181.127:8080/containers?state=running | python -mjson.tool")
    elif selection == 3:
        # List Images
        os.system("curl -s -X GET -H 'Accept: application/json' http://35.205.181.127:8080/images | python -mjson.tool")
    elif selection == 4:
        # Inspect an Image
        id = raw_input("Select Image ID\n")
        os.system("curl -s -X GET -H 'Accept: application/json' http://35.205.181.127:8080/containers/%s | python -mjson.tool" % id)
    elif selection == 5:
        # Delete all Containers
        os.system("curl -s -X DELETE -H 'Accept: application/json' http://35.205.181.127:8080/containers")
    elif selection == 6:
        # Delete Individual Container
        id = raw_input("Select Container ID to Delete\n")
        os.system("curl -s -X DELETE -H 'Accept: application/json' http://35.205.181.127:8080/containers/%s" % id)
    elif selection == 7:
        # Delete all Images
        os.system("curl -s -X DELETE -H 'Accept: application/json' http://35.205.181.127:8080/images")
    elif selection == 8:
        # Delete Individual Image
        id = raw_input("Select Image ID to Delete\n")
        os.system("curl -s -X DELETE -H 'Accept: application/json' http://35.205.181.127:8080/images/%s" % id)
    elif selection == 9:
        # Create a new Container
        id = raw_input("Input Image Name for Container to be made on\n")
        os.system(
            "curl -X POST -H 'Content-Type: application/json' http://35.205.181.127:8080/containers -d '{\"image\": \"%s\"}'" % id)
    elif selection == 10:
        # Create a new Image
        os.system("curl -H 'Accept: application/json' -F file=@Dockerfile http://35.205.181.127:8080/images")
    elif selection == 11:
        # Update a Container
        id = raw_input("Select a Container\n")
        while True:
            change = raw_input("Enter 1 to change to running, 2 to change to stopped")
            if change == '1':
                os.system(
                    "curl -X PATCH -H 'Content-Type: application/json' http://35.205.181.127:8080/containers/%s -d '{\"state\": \"running\"}'" % id)
                break
            elif change == '2':
                os.system(
                    "curl -X PATCH -H 'Content-Type: application/json' http://35.205.181.127:8080/containers/%s -d '{\"state\": \"stopped\"}'" % id)
                break
            else:
                print "Error unknown option entered"
    elif selection == 12:
        # Update an Image
        id = raw_input("Select an Image\n")
        os.system(
            "curl -s -X PATCH -H 'Content-Type: application/json' http://35.205.181.127:8080/images/%s -d '{\"tag\": \"test:1.0\"}'" % id)
