import eel

class AUIRG_WebApp():
    def __init__(self):
        print("Webapp!")
        #TODO start up all the managers and such?? 
        # this creates a singleton interms of how everything will be managed..
        # but this should be fine for our specific use case because it shouldn't
        # scale that large.....????

    def initalize(self):
        eel.init('web')
        eel.start('hello.html', size=(300, 200))  # Start

        


@eel.expose                         # Expose this function to Javascript
def say_hello_py(x):
    print('Hello from %s' % x)
say_hello_py('Python World!')
#eel.say_hello_js('Python World!')   # Call a Javascript function



temp = AUIRG_WebApp()
temp.initalize()