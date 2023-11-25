

state = "init"

def do_action(inputAction, state):
    if state == 'init':
        if inputAction == "inCargo":
            state = 'wait_pay'
        else:
            print("error1")
    elif state == "wait_pay":
        if inputAction == "pay":
            state = "shipping "
        elif inputAction == "not_pay":
            state = "finish"
        else :
            print("error2")
    elif state == "shipping":
        if inputAction == "ship":
            state == "get_cargo"
        else :
            print("error3")
    elif state == "get_cargo":
        if inputAction == "get_get_cargo":
            state = "finish"
        else :
            print("error4")
    else:
        print("state error")

    print(state)
    return state

state = do_action("inCargo",state)
state = do_action("pay",state)
