"""
Code shows if the greeting and response

RowSR - January 2025
"""

def main() -> None:
  name: str = ""
  monogram: str = ""
  test: str = int(input(""))
  for _ in range(test):
    names: int = int(input(""))
    for _ in range(names):
      name = input("")
      first, mid, last = name.split(" ")
      monogram = first[0].upper() + last[0].upper() + mid[0].upper()
      print(monogram)

if __name__ == "__main__":
  main()
