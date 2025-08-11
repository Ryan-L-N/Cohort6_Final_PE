class Automatron:

    def __init__(self, dough_units, pizza_shape, pizza_measurement, pizza_quantity):
        self.dough_units = dough_units
        self.pizza_shape = pizza_shape
        self.pizza_measurement = pizza_measurement
        self.pizza_quantity = pizza_quantity
        self.area = 0

    def calculate_area(self):
        if self.pizza_shape == 'circle':
            self.area = 3.141592653589793 * (self.pizza_measurement / 2) **2
            return (3.141592653589793 * (self.pizza_measurement / 2) **2 ) * self.pizza_quantity
        elif self.pizza_shape == 'triangle':
            self.area = (self.pizza_measurement * self.pizza_measurement * 0.4330127018922193)
            return (self.pizza_measurement * self.pizza_measurement * 0.4330127018922193) * self.pizza_quantity
        elif self.pizza_shape == 'square':
            self.area = (self.pizza_measurement * self.pizza_measurement)
            return (self.pizza_measurement * self.pizza_measurement) * self.pizza_quantity

        else:
            return 'Invalid shape'

    # Returns the area per unit
    def calculate_area_per_unit(self):
        return self.area / self.dough_units
