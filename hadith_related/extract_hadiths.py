from bs4 import BeautifulSoup

from .other.funcs import get_hadith_dict
from .other.vars import books
from .other.vars import num_hadiths_to_display

def extract_hadiths(html_content: str):
    hadiths = []
    hadiths_ordered = []

    soup = BeautifulSoup(html_content, 'html.parser')
    hadith_divs = soup.find_all('div', class_='hadith')
    hadith_info_divs = soup.find_all('div', class_='hadith-info')
    
    # getting the hadiths out of the html elements
    for hadith_text, hadith_info in zip(hadith_divs, hadith_info_divs):
        hadith = get_hadith_dict(hadith_text, hadith_info)
        hadiths.append(hadith)

    # ordering the hadiths based on books
    for book in books:
        hadiths_in_book = [hadith for hadith in hadiths if book in hadith["المصدر"]]
        hadiths_ordered.extend(hadiths_in_book)

    # getting the link that is sent after the hadiths
    dorar_link = soup.find("a").get('href').replace(" ", "+")
    dorar_link = f"للإستزادة : \n{dorar_link}"

    # Making sure that x hadiths are sent everytime, x being the (num_hadiths_to_display) variable    
    if hadiths_ordered:
        if len(hadiths_ordered) < num_hadiths_to_display:
            hadiths_ordered.extend(hadiths[:num_hadiths_to_display - len(hadiths_ordered)])
            hadiths_ordered.append(dorar_link)
            return hadiths_ordered
        hadiths_ordered = hadiths_ordered[:num_hadiths_to_display]
        hadiths_ordered.append(dorar_link)
        return hadiths_ordered
    else:
        hadiths = hadiths[:num_hadiths_to_display]
        hadiths.append(dorar_link)
        return hadiths



