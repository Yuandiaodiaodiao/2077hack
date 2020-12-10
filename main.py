
from concurrent.futures import ThreadPoolExecutor
threadPool = ThreadPoolExecutor(max_workers=1, thread_name_prefix="exec")
from pynput.keyboard import Listener
def presskey(key):
   if key.char in ['1','2','3','4']:
      print(key.char)

if __name__ == '__main__':
   with Listener(on_press=presskey) as listener:
      listener.join()