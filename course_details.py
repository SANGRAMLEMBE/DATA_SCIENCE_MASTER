# here package is directory pwskills and the module is python file
# here we have to access the course from payment and payment from course
#    

import os,sys  # we use this packeges for connecting paths
from os.path import dirname , join, abspath


sys.path.insert(0, abspath(join(dirname(__file__),'..')))  #insert required index and object( index, object)

#from payment import payment_details

def course():
    print("this is my course")

#payment_details.payment()  # No module named 'payment' this is error is goena seen 
                            # because the moduls are untracked