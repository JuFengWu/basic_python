

state = "init"

def ini(inputAction,state):
    if inputAction == "inCargo":
        state = 'wait_pay'
    else:
        print("error1")
    return state

def wait_pay(inputAction,state):
    if inputAction == "pay":
        state = "shipping "
    elif inputAction == "not_pay":
        state = "finish"
    else :
        print("error2")
    return state

def shipping(inputAction,state):
    if inputAction == "ship":
        state == "get_cargo"
    else :
        print("error3")

def get_cargo(inputAction,state):
    if inputAction == "get_get_cargo":
        state = "finish"
    else :
        print("error4")

def do_action(inputAction, state):
    """if state == 'init':
        ini(inputAction, state)
    elif state == "wait_pay":
        wait_pay(inputAction, state)
    elif state == "shipping":
        shipping(inputAction, state)
    elif state == "get_cargo":
        get_cargo(inputAction,state)
    else:
        print("state error")
    """
    state_dic = {
        'init': ini,
        "wait_pay" : wait_pay,
        "shipping" : shipping,
        "get_cargo" : get_cargo
        }
    func = state_dic[state]
    func(inputAction,state)
    print(state)
    return state

state = do_action("inCargo",state)
state = do_action("pay",state)
