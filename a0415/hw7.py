class WordFilter:
  def __init__(self,words):
    self.words = words
  
  def filter_words(self):
    for word in self.words:
      if len(word) >= 5:
        print(word)

wf = WordFilter(["hi", "hello", "python", "sun", "banana"])
wf.filter_words()
