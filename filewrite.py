from io import BytesIO


with open('sample.txt', 'a') as fh:
    sample_text = "Practicing file writes\n"
    fh.write(sample_text)
