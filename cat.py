from glob import glob
from random import choice
glob('images/cat*.jp*g')

ch = choice(['images\\cat.jpg', 'images\\cat1.jpg', 'images\\cat2.jpg', 'images\\cat3.jpg', 
'images\\cat4.jpg', 'images\\cat5.jpg'])
print(ch)