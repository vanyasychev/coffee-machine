class CoffeeMachine:
    @staticmethod
    def types_of_coffee(n):
        coffee = [
            {'name': 'espresso', 'money': 4, 'ingredients': {'water': -250, 'milk': 0, 'coffee_beans': -16,
                                                             'disposable_cups': -1}},
            {'name': 'latte', 'money': 7, 'ingredients': {'water': -350, 'milk': -75, 'coffee_beans': -20,
                                                          'disposable_cups': -1}},
            {'name': 'cappuccino', 'money': 6, 'ingredients': {'water': -200, 'milk': -100, 'coffee_beans': -12,
                                                               'disposable_cups': -1}}
        ]

        return coffee[n - 1]

    def buy(self):
        global materials

        print('\nWhat do you want to buy? 1 - espresso, 2 - latte, '
              '3 - cappuccino, back - to main menu:')
        answer = input()

        copy_of_materials = {key: val for key, val in materials.items()}

        if answer == 'back':
            return
        else:
            coffee = self.types_of_coffee(int(answer))

            for key_1, val_1 in coffee.items():
                if key_1 == 'ingredients':
                    for key_2, val_2 in val_1.items():
                        if materials[key_2] + val_2 > 0:
                            materials[key_2] += val_2
                        else:
                            print(f'Sorry, not enough {key_2}!')
                            materials = copy_of_materials
                            break
                    else:
                        materials['money'] += coffee['money']
                        print('I have enough resources, making you a coffee!')

    @staticmethod
    def fill():
        print('Write how many ml of water you want to add:')
        water = int(input())
        print('Write how many ml of milk you want to add:')
        milk = int(input())
        print('Write how many grams of coffee beans you want to add:')
        beans = int(input())
        print('Write how many disposable coffee cups you want to add:')
        cups = int(input())

        ingredient_list = [water, milk, beans, cups, 0]

        counter = 0
        for i in materials.keys():
            materials[i] += ingredient_list[counter]
            counter += 1

    @staticmethod
    def take():
        print(f'\nI gave you ${materials.get("money")}')
        materials['money'] = 0

    @staticmethod
    def remaining():
        print('\nThe coffee machine has:')
        print(materials.get('water'), 'of water')
        print(materials.get('milk'), 'of milk')
        print(materials.get('coffee_beans'), 'of coffee beans')
        print(materials.get('disposable_cups'), 'of disposable cups')
        print(materials.get('money'), 'of money')

    def options(self, option):
        if option == 'buy':
            self.buy()
        elif option == 'fill':
            self.fill()
        elif option == 'take':
            self.take()
        elif option == 'remaining':
            self.remaining()
        elif option == 'exit':
            return True

    def main(self):
        while True:
            action = input('Write action (buy, fill, take, remaining, exit):\n')

            if self.options(action):
                break

            print()


materials = {'water': 400, 'milk': 540, 'coffee_beans': 120, 'disposable_cups': 9, 'money': 550}

CoffeeMachine().main()
