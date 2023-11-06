import re

def remove_duplicates(hadiths: list[str]) -> list[str]:
    non_duplicates = []
    for hadtih in hadiths:
        if hadtih not in non_duplicates:
            non_duplicates.append(hadtih)

    return non_duplicates


def get_text(html_element, strip=True):
    return html_element.get_text(strip=strip)


def get_hadith_dict(hadith, hadith_info):
    hadith_text = re.sub(r'\d', '', hadith.get_text(strip=False)).replace(" - ", "")
    info_spans = hadith_info.find_all("span")
    hadith_dict = {}
    hadith_dict["الحديث"] = hadith_text
    key = None

    for i in range(len(info_spans) - 1):
        key = info_spans[i].get_text(strip=True).replace(":","")
        next_text = info_spans[i].find_next_sibling(text=True).strip()
        hadith_dict[key] = next_text

    # last item is in another span, unlike the previous ones.
    hadith_dict[key] = info_spans[-1].get_text(strip=True)

    return hadith_dict