




# Makefile for PH20 assignment 4

report4.pdf : p1.png 
	pdflatex report4.tex
	

p1.png:
	python hyunkim_ph20_week3.py 30000 1 0 0.001


clean : 
	rm -f *.pdf
	rm -f *.png
	