# reflektion-test

This Project is about API Test-Automation for the given URL.

"https://jsonplaceholder.typicode.com"

There are 6 test scripts associated to different HTTP verb calls.

1. GET --> test_get_service.py
2. POST --> test_post_service.py
3. PUT --> test_put_service.py
4. DELETE --> test_delete_service.py

Along with these scripts, "test_invalid_post_service.py" is to validate the POST request for invalid end point.

Assumptions: 
1. The project path is set at "PYTHONPATH"
2. Install the python packages using pip command
      - Execute the command : python pip install -r requirement.txt

How to run the script ?

Open cmd prompt(Windows) or Terminal(Linux)

Copy the below command in  the terminal

Template:
	python -v -m pytest --html=<Report Path> --self-contained-html <Test Script Folder path to execute test scripts associated to it.>

eg: 
	python -v -m pytest --html=reflektion-test/src/Test_Report/test_services.html --self-contained-html reflektion-test/src/Test_Scripts/

From the above example, you can find the report in "reflektion-test/src/Test_Report/" folder location.
