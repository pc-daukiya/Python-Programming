# Regular Expressions 
'''Code 1'''
'''[]  Represent a character class
^   Matches the beginning
$   Matches the end
.   Matches any character except newline
?   Matches zero or one occurrence.
|   Means OR (Matches with any of the characters
    separated by it.
*   Any number of occurrences (including 0 occurrences)
+   One or more occurrences
{ } Indicate number of occurrences of a preceding RE 
    to match.
()  Enclose a group of REs'''

# import re

# pattern = r"[A-Z]+yclodne"
# text = '''Cyclone Dumazile was a strong tropical cyclone in the South-West Indian Ocean that affected Madagascar and Réunion in early March 2018. Dumazile originated from a cyclone Dyclone low-pressure area that formed near Agaléga on 27 February. It became a tropical disturbance on 2 March, and was named the next day after attaining tropical storm status. Dumazile reached its peak intensity on 5 March, with 10-minute sustained winds of 165 km/h (105 mph), 1-minute sustained winds of 205 km/h (125 mph), and a central atmospheric pressure of 945 hPa (27.91 inHg). As it tracked southeastwards, Dumazile weakened steadily over the next couple of days due to wind shear, and became a post-tropical cyclone on 7 March

# '''
# match = re.search(pattern, text)
# print(match)

# matches = re.finditer(pattern, text)
# for match in matches:
#   print(match.span()) 
#   print(text[match.span()[0]: match.span()[1]])


'''Code 2'''
# import time
# import asyncio 
# import requests


# async def function1():
#   print("func 1") 
#   URL = "https://wallpaperaccess.in/public/uploads/preview/1920x1200-desktop-background-ultra-hd-wallpaper-wiki-desktop-wallpaper-4k-.jpg"
#   response = requests.get(URL)
#   open("instagram.ico", "wb").write(response.content)
   
#   return "Harry"
  
# async def function2():
#   print("func 2") 
#   URL = "https://p4.wallpaperbetter.com/wallpaper/490/433/199/nature-2560x1440-tree-snow-wallpaper-preview.jpg"
#   response = requests.get(URL)
#   open("instagram2.jpg", "wb").write(response.content)
  
# async def function3():
#   print("func 3")
#   URL = "https://c4.wallpaperflare.com/wallpaper/622/676/943/3d-hd-wikipedia-3d-wallpaper-preview.jpg"
#   response = requests.get(URL)
#   open("instagram3.ico", "wb").write(response.content)

# async def main():
#   # await function1()
#   # await function2()
#   # await function3()
#   # return 3
#   L = await asyncio.gather(
#         function1(),
#         function2(),
#         function3(),
#     )
#   print(L)
#   # task = asyncio.create_task(function1())
#   # # await function1()
#   # await function2()
#   # await function3()

# asyncio.run(main())


'''Code 3'''
# import threading
# import time
# from concurrent.futures import ThreadPoolExecutor

# # Indicates some task being done
# def func(seconds):
#   print(f"Sleeping for {seconds} seconds")
#   time.sleep(seconds)
#   return seconds

# def main():
#   time1 = time.perf_counter()
#   # Normal Code
#   # func(4) 
#   # func(2)
#   # func(1)
  
  
#   # Same code using Threads
#   t1 = threading.Thread(target=func, args=[4])
#   t2 = threading.Thread(target=func, args=[2])
#   t3 = threading.Thread(target=func, args=[1])
#   t1.start()
#   t2.start()
#   t3.start()
  
#   t1.join()
#   t2.join()
#   t3.join()
#   # Calculating Time 
#   time2 = time.perf_counter()
#   print(time2 - time1)


# def poolingDemo():
#   with ThreadPoolExecutor() as executor:
#     # future1 = executor.submit(func, 3)
#     # future2 = executor.submit(func, 2)
#     # future3 = executor.submit(func, 4)
#     # print(future1.result())
#     # print(future2.result())
#     # print(future3.result())
#     l = [3, 5, 1, 2]
#     results = executor.map(func, l)
#     for result in results:
#       print(result)

# poolingDemo()

'''Code 4'''
import concurrent.futures
import requests

def downloadFile(url, name):
  print(f"Started Downloading {name}")
  response = requests.get(url)
  open(f"files/file{name}.jpg", "wb").write(response.content)
  print(f"Finished Downloading {name}")
 


url = "https://picsum.photos/2000/3000"
# pros = []
# for i in range(50):
#   # downloadFile(url, i)
#   p = multiprocessing.Process(target=downloadFile, args=[url, i])
#   p.start()
#   pros.append(p)

# for p in pros:
#   p.join()

with concurrent.futures.ProcessPoolExecutor() as executor:
  l1 = [url for i in range(60)]
  l2 = [i for i in range(60)]
  results = executor.map(downloadFile, l1, l2)
  for r in results:
    print(r)