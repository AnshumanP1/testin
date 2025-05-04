# module_name.py
from typing import List

def greet(name: str) -> str:
  return "Hello, " + name

def add(x: int, y: int) -> int:
  result: int = x + y
  return result

def process_data(data: List[int]) -> List[int]:
  # Imagine some complex processing
  processed: List[int] = [item * 2 for item in data if item > 0]
  return processed

class Calculator:
  def __init__(self):
    self.total: int = 0

  def add(self, value: int) -> None:
    self.total += value

  def get_total(self) -> int:
    return self.total

# Example usage (optional, mainly for context)
# if __name__ == "__main__":
#   print(greet("World"))
#   print(add(5, 3))
#   my_data = [1, -2, 3, 0, 5]
#   print(process_data(my_data))
#   calc = Calculator()
#   calc.add(10)
#   calc.add(5)
#   print(calc.get_total())
