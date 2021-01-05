# auto-translation

auto-translation is a simple python library to translate any other
language or transform it to speech with google translation , all that
using the user's Chrome browser with selenium in hidden mode , mean time
to return the translation or speech 15 seconds

**Installation :**

| $ pip install auto-translation |

**Simple usage :**

| >>> from auto_browser.selenium_translation import Chrome |

| >>> test=Chrome()  |

| >>> print(
test.translate_text(text='*Bonjour*',from_lang='*fr*',to_lang='*fr*') )|

| >>> Good morning |


**Methods :**

| Methods                                                  | Return                              |
|:---------------------------------------------------------|:------------------------------------|
| translation_url(from_lang=str,to_lang=str)               | url of google translation (str)     |
| translation_text_url(text=str,from_lang=str,to_lang=str) | url of the translation needed (str) |
| translate_text(text=str,from_lang=str,to_lang=str)       | translation of text (str)           |
| text_2_speech(text=str, language=str)                    | None , text speech                  |
| translation_2_speech(text=str,from_lang=str,to_lang=str) | None , translation speech           |

**Note :**

Use language codes >>>
[ISO-639 Language Codes](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html)

example :  
Arabic:ar  
French:fr
