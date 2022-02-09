import os
import sys



BASE_DIR= os.path.dirname(os.path.dirname(__file__))


filepath=os.path.join(BASE_DIR,"blogs",sys.argv[1])
if filepath.find(".") !=-1 :
    print("Error")
else:
    with open(filepath) as blog_text:
        print(blog_text.read())
