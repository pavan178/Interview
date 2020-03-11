
import cv2  #OpenCV to read and process the image file
import pytesseract  #pytersseract to use inbuilt character recognition library
#path for reading the image/pdf and using opencv to convert image to an array
imPath = cv2.imread(r'C:\Users\user\PycharmProject\interview\TASK2\TASK2.png')
#using pytesseract to extract text from the image which is rendered using opencv
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' #install pytesseract and copy the tesseract.exe path
text = pytesseract.image_to_string(imPath) #converting image to text
print(text) #printing the text
f = open('csvfile.csv','w') #opening a csv file
f.write(text+"\n") #Give csv text here.
# Python will convert \n to os.linesep
f.close() #closing the csv write

