# Interview Task

Instructions:

Download the zip file from GIT and extract to desired location, open the extracted folder as a project on pycharm or any python IDE.

or you can use git clone to clone the git repo to your local machine.



Task1 : 

To run the Task 1 these are the required packages to install, you can use PIP install and run it in CMD :

pip install selenium
pip install time


Download Chromedriver and add the .exe path to the script where : chrome_driver_path = "PATH"

Now run the Selenium.py file



Task 2 :

Required packages :

pip install opencv-python
pip install pytesseract


add the path of the image/pdf to : imPath = cv2.imread("Path")

You need to download and install a third part pre built text recognition support file from 
https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.0.0-alpha.20200223.exe

Then add the tesseract.exe path to : pytesseract.pytesseract.tesseract_cmd = "Path"

Run the test.py file

A csv file will be generested after the convertion of image/pdf to text in the current project path




Task 3 :



Required packages:

pip install django



Open the cmd and go the location of Interview/Task3 

then run the following command


python manage.py runserver



the local host will be running with the django project


you can go the same local host address on your browser, you will be able to see a form with name, phone number and email fields, fill it and submit.


you will be able to see the entered fields in the command prompt in a List.



( I have added extra snippit where it is integrated with admin panel. You can login to adminpanel with /admin on the local host extenstion,

user name : user, password : 1234)



(you can access this extra snippet using /snippet as a user)



