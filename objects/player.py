class Player:
    def __init__(self):
        self.location = "motel_room"
        self.inventory = []

    def act(self, command: str) -> str:
        if self.location == "motel_room":
            if command == "осмотреться":
                return "Ты видишь старую кровать, стол и диктофон."
            elif command == "взять диктофон":
                if "диктофон" not in self.inventory:
                    self.inventory.append("диктофон")
                    return "Ты взял диктофон. Он может пригодиться."
                return "У тебя уже есть диктофон."
            elif command == "выйти":
                self.location = "улица"
                return "Ты вышел на улицу. Холодный туман окутывает город..."
            else:
                return "Ничего не произошло..."
        elif self.location == "улица":
            if command == "осмотреться":
                return "Ты стоишь возле мотеля. Впереди — лес и дорога в центр."
            return "Ты слышишь далекий шум леса..."
        return "Ты не можешь этого сделать сейчас."
