# Chapter 1 - The Colltaz Conjecture

class Collatz:

    num_list = []
    xaxis = []

    def __init__(self) -> None:
        first_num = int(input("What number would you like to use?   "))
        self.num_list.append(first_num)
        self.first_num = first_num   
        if first_num % 2 == 0:
            first_result = first_num / 2
            self.num_list.append(first_result)
        else:
            first_result = (first_num * 3) + 1
            self.num_list.append(first_result)
        second_num = first_result
        self.apply_rule(second_num)
        self.print_steps()
        print(self)

    def __repr__(self) -> str:
        return f"Applying the Collatz Conjecture rule to {self.first_num} has a stopping time of {len(self.num_list)-1} (aka quantity of steps to reach 1)."

    def apply_rule(self, input) -> None:
        while input > 1:
            if input % 2 == 0:
                result = int(input / 2)
                self.num_list.append(result)
                input = result
            else:
                result = int((input * 3) + 1)
                self.num_list.append(result)
                input = result

    def print_steps(self) -> str:
        for i in range(len(self.num_list)):
            num = self.num_list[i]
            if i < max(range(len(self.num_list))):
                next_num = self.num_list[i+1]
                if num % 2 == 0:
                    print(f"{num} is even and when divded by 2 will equal {next_num}.")
                else:
                    print(f"{num} is odd and when multiplied by 3 and then had 1 added to it will equal {next_num}.")

    def create_xaxis(self):
        return [x for x in range(0, len(self.num_list))]

    def visualize_steps(self) -> None:
        xaxis = self.create_xaxis()
        graph_dict = zip(xaxis, self.num_list)


collatz = Collatz()
