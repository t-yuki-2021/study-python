class Mama:
    def says(self):
        print("宿題をしなさい")

class Sister(Mama):
    def says(self):
        super().says()
        print("後宿題もしなさい")

Sister().says()