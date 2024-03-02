if __package__ is None or __package__ == '':
    from assistant.assistant import Assistant
    from assistant.io import IoCli
else:
    from .assistant import Assistant
    from .assistant import IoCli

NICE_LOGO = r"""
  ____            _____ _       _     
 |  _ \          /  __ \ |     | |    
 | |_) |_   _ ___| /  \/ |_   _| |__  
 |  _ <| | | / __| |   | | | | | '_ \ 
 | |_) | |_| \__ \ \__/\ | |_| | |_) |
 |____/\__,_|___/\____/_|\__,_|_.__/ 
                                        
"""


def main():
    io = IoCli()

    # nice and useless intro
    io.print(NICE_LOGO)
    io.print("Present\n")
    io.print("Personal assistant")

    assistant = Assistant(io)
    assistant.load()
    assistant.main_loop()
    assistant.save()


if __name__ == "__main__":
    main()
