#!/usr/bin/python3

"""Defines a base model class."""
import json
import csv
import turtle

class Base:
    """Base class for managing id attribute."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor for Base class."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""

        from models.rectangle import Rectangle
        from models.square import Square

        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as file:
            json_str = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
            file.write(json_str)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with attributes set based on the provided dictionary."""

        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ == "Rectangle":
            dummy_instance = Rectangle(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = Square(1)
        else:
            raise ValueError("Unsupported class for create method")

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Return a list of instances based on the contents of a JSON file."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                json_content = file.read()
                dict_list = cls.from_json_string(json_content)
                return [cls.create(**item) for item in dict_list]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize objects to CSV and write to a file."""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    from models.rectangle import Rectangle
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    from models.square import Square
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize objects from CSV and return a list of instances."""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r', newline='') as file:
                reader = csv.reader(file)
                instances = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        from models.rectangle import Rectangle
                        instances.append(Rectangle(*map(int, row)))
                    elif cls.__name__ == "Square":
                        from models.square import Square
                        instances.append(Square(*map(int, row)))
            return instances
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw rectangles and squares using Turtle graphics."""
        screen = turtle.Screen()
        screen.bgcolor("white")

        # Function to draw a rectangle
        def draw_rectangle(rectangle):
            turtle.penup()
            turtle.goto(rectangle.x, rectangle.y)
            turtle.pendown()
            turtle.forward(rectangle.width)
            turtle.left(90)
            turtle.forward(rectangle.height)
            turtle.left(90)
            turtle.forward(rectangle.width)
            turtle.left(90)
            turtle.forward(rectangle.height)
            turtle.left(90)

        # Function to draw a square
        def draw_square(square):
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            for _ in range(4):
                turtle.forward(square.size)
                turtle.left(90)

        # Draw rectangles
        for rectangle in list_rectangles:
            draw_rectangle(rectangle)

        # Draw squares
        for square in list_squares:
            draw_square(square)

        turtle.done()
