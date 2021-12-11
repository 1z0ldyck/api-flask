
def convert_str_to_int(values):
  for value in values:
    if not value.isalpha():
      value = int(value)