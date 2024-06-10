from concrete_component import PlainText
from concrete_decorator import HTMLDecorator


plain_text=PlainText('Hola Mundo')
print(f'Texto sin decorar: {plain_text.render()}')

decorated_text=HTMLDecorator(plain_text)
print(f'Texto sin decorar: {decorated_text.render()}')