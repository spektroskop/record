class Base(tuple):

  def __new__(cls, *values):
    return tuple.__new__(cls, values)

  def __repr__(self):
    return self.__class__.__name__ + tuple.__repr__(self)

def Record(*slots):
  getitem = lambda i: lambda s: tuple.__getitem__(s, i)
  props = [(slot, property(getitem(i))) for i, slot in enumerate(slots)]
  return type('Record', (Base,), dict(props + [('slots', slots)]))
