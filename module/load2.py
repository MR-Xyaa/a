import itertools
import threading
import time
import sys

done = False

#animasi loading
def animate():
    for c in itertools.cycle(['10', '20','30', '40','50','60','70', '80','90','10%']):
        if done:
            break
        sys.stdout.write('\rloading Tools MR-Xyaa ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rBerhasil 100')

t = threading.Thread(target=animate)
t.start()

#proses lama disini

time.sleep(30)
done = True

user_reply = input("Siapa Namamu? \n")
