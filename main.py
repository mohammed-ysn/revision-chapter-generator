def comp_sci_topics():
  topics = {
    '1.1.1': ['a', 'b', 'c', 'd', 'e'],
    '1.1.2': ['a', 'b', 'c'],
    '1.1.3': ['a', 'b', 'c', 'd'],
    '1.2.1': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
    '1.2.2': ['a', 'b', 'c', 'd', 'e', 'f'],
    '1.2.3': ['a', 'b', 'c'],
    '1.2.4': ['a', 'b', 'c', 'd', 'e'],
    '1.3.1': ['a', 'b', 'c', 'd'],
    '1.3.2': ['a', 'b', 'c', 'd', 'e', 'f'],
    '1.3.3': ['a', 'b', 'c', 'd', 'e'],
    '1.3.4': ['a', 'b', 'c', 'd'],
    '1.4.1': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],
    '1.4.2': ['a', 'b', 'c'],
    '1.4.3': ['a', 'b', 'c', 'd', 'e'],
    '1.5.1': ['a', 'b', 'c', 'd'],
    '1.5.2': ['a'],
    '2.1.1': ['a', 'b', 'c', 'd'],
    '2.1.2': ['a', 'b', 'c', 'd'],
    '2.1.3': ['a', 'b', 'c', 'd'],
    '2.1.4': ['a', 'b', 'c'],
    '2.1.5': ['a', 'b'],
    '2.2.1': ['a', 'b', 'c', 'd', 'e', 'f'],
    '2.2.2': ['a', 'b', 'c', 'd', 'e', 'f'],
    '2.3.1': ['a', 'b', 'c', 'd', 'e', 'f'],
  }

def physics_topics():
  return 'Test'

def create_topics():
  return comp_sci_topics(), physics_topics()

print(create_topics())
