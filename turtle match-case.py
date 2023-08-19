import turtle

t = turtle.Turtle()

def uitvoeren(regel):
    commando = regel[0]
    argument = regel[1:]
    match commando:
        case 'f':
            t.forward(int(argument))
        case 't':
            t.up()
        case _:
            pass


uitvoeren('t')
uitvoeren('f100')

turtle.mainloop()