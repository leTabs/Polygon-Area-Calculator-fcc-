class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # register the width & height 
        
    def set_width(self, width):
        self.width = width
        # creating the set_width method 
        
    def set_height(self, height):
        self.height = height
        # creating the set_height method
        
    def get_area(self):
        return self.width * self.height
        # creating the get_area method
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
        # creating the get_perimeter method
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
        # creating the get_diagonal method
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        picture = ""
        for i in range(self.height):
            picture += "*"*self.width + "\n"
        return picture
        # create the get_picture method
        
    def get_amount_inside(self, shape):
        if self.width < shape.width or self.height < shape.height:
            return 0
        width_ratio = self.width // shape.width
        height_ratio = self.height // shape.height
        return width_ratio * height_ratio
        # creating the get_amount_inside method 
        
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
        # creating the object's string version 


class Square(Rectangle):
    # creating the class as the child of the Rectangle
    def __init__(self, side):
        super().__init__(side, side)
        # register the parent's elements
        
    def set_side(self, side):
        self.width = side
        self.height = side
        # creating the set_side method
        
    def __str__(self):
        return f"Square(side={self.width})"
        # creating the object's string version 
