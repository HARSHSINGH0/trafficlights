#one can perform this code in few line's but i want this to be in class
import time
class signallights:
    def on():
        while True:
            print("green")
            time.sleep(15)
            print("yellow")
            time.sleep(5)
            print("red")
            time.sleep(15)
s1=signallights
s1.on()
