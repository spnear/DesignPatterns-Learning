from concrete_factory import DarkUIFactory, LightUIFactory
from abstract_factory import UIAbstractFactory

def client_code(factory: UIAbstractFactory):
    button = factory.create_button()
    textbox = factory.create_textbox()

    button.paint()
    textbox.paint()


def main():
    print("Generating Dark UI")
    client_code(DarkUIFactory())
    
    print("Generating Light UI")
    client_code(LightUIFactory())

if __name__ =='__main__':
    main()