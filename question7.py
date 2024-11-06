# Engine class
class Engine:
    def __init__(self):
        self.running = False

    def start(self):
        if not self.running:
            self.running = True
            print("Engine started.")
        else:
            print("Engine is already running.")

    def stop(self):
        if self.running:
            self.running = False
            print("Engine stopped.")
        else:
            print("Engine is already stopped.")

# Car class with an Engine instance
class Car:
    def __init__(self):
        self.engine = Engine()  # Composition: Car has an Engine

    def start_engine(self):
        self.engine.start()

    def stop_engine(self):
        self.engine.stop()

# Demonstration of controlling the engine through the Car class
my_car = Car()
my_car.start_engine()  # Expected output: "Engine started."
my_car.start_engine()  # Expected output: "Engine is already running."
my_car.stop_engine()   # Expected output: "Engine stopped."
my_car.stop_engine()   # Expected output: "Engine is already stopped."
