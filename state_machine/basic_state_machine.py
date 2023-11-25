
class StateMachine:
    def __init__(self):
        self.state = "init"

    def input_action(self, inputAction):
        if self.state == 'init':
            if inputAction == "inCargo":
                self.state = 'wait_pay'
            else:
                print("error")
        elif self.state == "wait_pay":
            if inputAction == "pay":
                self.state = "shipping "
            elif inputAction == "not_pay":
                self.state = "finish"
            else :
                print("error")
        elif self.state == "shipping":
            if inputAction == "ship":
                self.state == "get_cargo"
            else :
                print("error")
        elif self.state == "get_cargo":
            if inputAction == "get_get_cargo":
                self.state = "finish"
            else :
                print("error")
        else:
            print("state error")
    def get_state(self):
        return self.state

shopping = StateMachine()
shopping.input_action("inCargo")
print(shopping.get_state())
shopping.input_action("pay")
print(shopping.get_state())
