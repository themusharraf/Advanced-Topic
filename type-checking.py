"""
Python kuchli yozishga ega dinamik dasturlash tilidir. U dinamik ravishda terilganligi
va turlar dinamik ravishda chiqarilganligi sababli, Java kabi statik tarzda yoziladigan
dasturlash tillaridan farqli o'laroq, o'zgaruvchilar turini ko'rsatmasdan o'zgaruvchilar qiymatlarini o'rnatishingiz mumkin.
"""

str_value = 'hello'

int_value = 123

"""
type()
Python funktsiyasi type() o'zgaruvchilar turlarini aniqlash uchun ishlatilishi mumkin.
 Ish vaqti disk raskadrovka paytida dasturda aniq o'zgaruvchilar turlarini topish uchun type() funksiyasidan foydalaning.
"""

print(type(str_value))

print(type(int_value))

"""
Yuqoridagi kodning chiqishi "int" va "str" O'zgaruvchining ma'lumotlar turi butun son bo'lgani uchun uni aniqlash uchun "type()" dan foydalanish mumkin.

# isinstance()
Pythonning "insinstance("obj", "class")" funksiyasi ob'ekt sinfning namunasi yoki yo'qligini aniqlash uchun ishlatilishi 
mumkin. Faqat True yoki False bo'lishi mumkin bo'lgan mantiqiy chiqish qiymati qaytariladi.
"""

str_value = 'hello'

int_value = 123

print(isinstance(str_value, str))

print(isinstance(int_value, int))

"""
Yuqoridagi kodning natijasi haqiqatdir. O'zgaruvchining ma'lumotlar
turi qator bo'lgani uchun uni aniqlash uchun "isinstance()" dan foydalanish mumkin.
Siz misolni ham ko'rishingiz mumkin. Aytaylik, sizda mavjud bo'lgan o'zgaruvchida
raqamli qiymat bor yoki yo'qligini aniqlamoqchisiz.
"""


class TriangleChecker:
    def __init__(self, first, second, third):
        if isinstance(first, (float, int)) and isinstance(second, (float, int)) and isinstance(third, (float, int)):
            self.first = first
            self.second = second
            self.third = third
            print("checked")
        else:
            print("Error")


"""
subclass()
Agar talaba argumenti (birinchi argument) Human sinfining pastki sinfi bo'lsa, issubclass() funktsiyasi uning mavjudligini aniqlaydi.
"""


class Human:
    def __init__(polygonType):
        print('Polygon is a ', polygonType)


class Student(Human):
    def __init__(self):
        ...


print(issubclass(Student, Human))

"""
Typing
Yaxshi xabar shundaki, turdagi izoh Python-ga 3.5 versiyasida qo'shilgan.
Bu erda izohlari argument va qaytarish turlarini e'lon qiladigan oddiy funksiyaning tasviri:
"""


def info(age: int) -> int:
    return 'I am' + age


"""
Yuqoridagi misolda ko'rinib turganidek, turdagi izohga quyidagi bilan o'zgaruvchiga rioya qilish orqali erishiladi: 
Aytgancha, agar usul hech narsa qaytarmasa, qaytarish turi None bo'lishi kerak.
"""

"""
# Pydantic
Dasturingiz foydalanuvchilari kabi tashqi manbalardan olingan ma'lumotlar bilan ishlashda
statik turdagi tekshiruvlar foydasiz. turi shashka bu vaziyatda foydali bo'lishi mumkin. 
Pydantic ushbu vositalardan biri bo'lib, u ma'lumotlarni tekshirish uchun ishlatiladi. 
Taqdim etilgan ma'lumotlar turdagi ko'rsatma bilan e'lon qilingan turga mos kelmasa, tekshirish muammolari ko'tariladi.
"""
# pip install pydantic


from pydantic import BaseModel


class User(BaseModel):
    id: int
    name = 'Tad'
    friends: list[int] = []
