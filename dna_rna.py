class Dna:
  complement_dict = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
  transcription_map = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}  

  def __init__(self, dna_seq):        
    self.dna_seq = dna_seq
    

  def __iter__(self):
    self.current_pos = 0
    return self

  def __next__(self):
    if (self.current_pos < len(self.dna_seq)):
      self.current_pos += 1
      return self.dna_seq[self.current_pos - 1]
    else: 
      raise StopIteration

  def __eq__(self, other):
    return self.dna_seq == other.dna_seq

  def gc_content(self):
    return round((self.dna_seq.count('G') + self.dna_seq.count('C')) * 100 / len(self.dna_seq))

  def reverse_complement(self):
    return ''.join([self.complement_dict[base] for base in self.dna_seq[::-1]])

  def transcribe(self):
    rna_seq = ''.join([self.transcription_map[base] for base in self.dna_seq])
    return Rna(rna_seq)

class Rna:
  complement_dict = {'A': 'U', 'C': 'G', 'G': 'C', 'U': 'A'}

  def __init__(self, rna_seq):        
    self.rna_seq = rna_seq
    

  def __iter__(self):
    self.current_pos = 0
    return self

  def __next__(self):
    if (self.current_pos < len(self.rna_seq)):
      self.current_pos += 1
      return self.rna_seq[self.current_pos - 1]
    else: 
      raise StopIteration

  def __eq__(self, other):
    return self.rna_seq == other.rna_seq

  def gc_content(self):
    return round((self.rna_seq.count('G') + self.rna_seq.count('C')) * 100 / len(self.rna_seq))

  def reverse_complement(self):
    return ''.join([self.complement_dict[base] for base in self.rna_seq[::-1]])


print('=================> Eq')
dna1 = Dna('ACGG')
dna2 = Dna('ACGG')
print(dna1 == dna2)
print('=================> Eq')
dna3 = Dna('ACGG')
dna4 = Dna('ACGT')
print(dna3 == dna4)
print('=================> Iter')
for base in dna4:
  print(base)
print('=================> Gc content')
dna5 = Dna('ACTGGCA')
print(dna5.gc_content())
print('=================> Transcribe')
print(dna5.transcribe().rna_seq)


print('=================> Eq')
rna1 = Rna('UGACCGU')
rna2 = Rna('UGACCGU')
print(dna1 == dna2)
print('=================> Eq')
rna3 = Rna('UGACCGU')
rna4 = Rna('UGACCGA')
print(rna3 == rna4)
print('=================> Iter')
for base in rna4:
  print(base)
print('=================> Gc content')
rna5 = Rna('UGACCGUACG')
print(rna5.gc_content())

