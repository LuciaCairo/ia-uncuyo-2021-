class Tree:
  def __init__(self, val = None):
    if val != None:
        self.val = val
    else:
        self.val = None
        
    self.left = None
    self.right = None
