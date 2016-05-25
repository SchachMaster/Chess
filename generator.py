while True:
        import random

        position = [ 'rbnqknbr', 'rnbkqbnr', 'rbnkqnbr', 'rbbkqnnr', 'rbbqknnr', 'rnnkqbbr', 'rnnqkbbr' ]


        option=raw_input('Press 1 for SFR, 2 for RQP, 3 for both, 4 to exit.')

        if option == '1':
                        print(random.choice(position))
        elif option == '2':
                                print random.randint(4, 8)
        elif option == '3':
                                print(random.choice(position))
                                print random.randint(4,8)
        elif option == '4':
                                quit()

        
        
    





