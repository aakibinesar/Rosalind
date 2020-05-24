from Bio import Entrez

def genbank(genus, dtstart, dtend):
	Entrez.email = "adelq@sas.upenn.edu"
	term = '%s[Organism] AND (%s[Publication Date] : %s[Publication Date])' % (genus, dtstart, dtend)
	handle = Entrez.esearch(db="nucleotide", term=term)
	record = Entrez.read(handle)
	return record["Count"]

# Tests
print (genbank("Olea", "2002/12/13", "2008/09/22"))