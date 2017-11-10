text = "X-DSPAM-Confidence:    0.8475";
pop=text.find(':')
find=text[pop+1:].strip()
print (float(find))

