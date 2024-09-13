import Speech as sp
import Mouse as mo
import Brightness as br
import Sound as so
import PPT as pp
def Main():
    while True:
        a=sp.Speech()
        print(a)
        if(a=="volume"):
            so.Sound()
        if(a=="brightness"):
            br.Brightness()
        if(a=="Mouse"):
            mo.Mouse()
        if(a=="presentation"):
            pp.PPT()
Main()
