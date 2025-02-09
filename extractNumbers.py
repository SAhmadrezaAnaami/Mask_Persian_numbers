import re

text = "من 123 کتاب و سی و دو عدد خودکار دارم. سی و هفت هزارصد و دو میلیون"

basic_numbers = [
    "صفر",
    "یک",
    "دو", 
    "سه",
    "چهار", 
    "پنج", 
    "شش", 
    "هفت", 
    "هشت", 
    "نه", 
    "ده",
    "یازده", 
    "دوازده",
    "سیزده", 
    "چهارده", 
    "پانزده", 
    "شانزده", 
    "هفده", 
    "هجده", 
    "نوزده",

    ## two digits

    "بیست", 
    "سی", 
    "چهل", 
    "پنجاه", 
    "شصت", 
    "هفتاد", 
    "هشتاد", 
    "نود",

    ## three digits seprate 
    "دو یست",
    "سی صد",
    "پان صد",

    ## three digits combines 

    "صد", 
    "دویست", 
    "سیصد", 
    "چهارصد", 
    "پانصد", 
    "ششصد", 
    "هفتصد", 
    "هشتصد", 
    "نهصد",

    ## types

    "میلیارد",
    "سپتیلیارد",
    "سپتیلیون",
    "سکستیلیارد",
    "سکستیلیون",
    "کوانتینیارد",
    "کوینتیلیون",
    "کادریلیارد",
    "کوآدریلیون",
    "تریلیارد",
    "تریلیون",
    "بیلیارد",
    "بیلیون",
    "میلیارد",
    "میلیون",
    "هزار",

    ##decimal

    "دهم",
    "صدم", 
    "هزارم", 
    "ده هزارم"

    ## formations

    "شیش صد",
    "ششصد",
	"شش صد", 
    "ششصد",
	"هفت صد", 
    "هفتصد",
	"هشت صد", 
    "هشتصد",
	"نه صد", 
    "نهصد",
	"چارصد", 
    "چهارصد",
	"شیش‌صد", 
    "ششصد",
	"شش‌ضد", 
    "ششصد",
	"هفت‌صد", 
    "هفتصد",
	"هشت‌صد", 
    "هشتصد",
	"نه‌صد", 
    "نهصد",
	"یک‌صد", 
    "یکصد",
	"هزارمين", 
    "هزارمین",

]

pattern = f"({'|'.join(basic_numbers)})"
def extractNumbers(text , text_ent = None):

    numbers_in_words_alphabetic = re.findall(pattern, text)
    numbers_in_words_digits = re.findall(r'\d+', text)

    numbers = []
    for i , number in enumerate(numbers_in_words_alphabetic + numbers_in_words_digits):
        if text_ent:
            if number in text_ent.split(" "):
                text_ent = text_ent.replace(number , f"[NUM{i}]")
                numbers.append({
                    'label' : f"[NUM{i}]",
                    'text' : number
                })
        else :
            if number in text.split(" "):
                text = text.replace(number , f"[NUM{i}]")
                numbers.append({
                    'label' : f"[NUM{i}]",
                    'text' : number
                })
    if text_ent:
        return text_ent , numbers
    else:
        return text , numbers