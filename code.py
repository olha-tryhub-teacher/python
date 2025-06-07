class Vector3D:
    _instances = 0
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        Vector3D._instances += 1
    
    def __add__(self, other):
        new_vector_x = self.x + other.x
        new_vector_y = self.y + other.y
        new_vector_z = self.z + other.z
        return Vector3D(new_vector_x, new_vector_y, new_vector_z)
    
    def __sub__(self, other):
        new_vector_x = self.x - other.x
        new_vector_y = self.y - other.y
        new_vector_z = self.z - other.z
        return Vector3D(new_vector_x, new_vector_y, new_vector_z)
        
    def __mul__(self, n):
        new_vector_x = self.x * n
        new_vector_y = self.y * n
        new_vector_z = self.z * n
        return Vector3D(new_vector_x, new_vector_y, new_vector_z)
        
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z
    
    def __str__(self):
        return f"({self.x};{self.y};{self.z})"
        
    @staticmethod
    def get_count():
        return Vector3D._instances
    
    
    
