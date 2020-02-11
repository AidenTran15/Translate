from translate import Translator

content = input('> ')
translator = Translator(to_lang="zh")
translation = translator.translate(content)
print(translation)