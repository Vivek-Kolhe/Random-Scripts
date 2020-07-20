import PyPDF2

pdf_list = [] # pass the path of PDFs
output = input("Name for the output PDF: ")

def combinePDF(pdf_list):
	merge = PyPDF2.PdfFileMerger()
	for pdf in pdf_list:
		merge.append(pdf)

	merge.write(output)

combinePDF(pdf_list)
print("All Done!")