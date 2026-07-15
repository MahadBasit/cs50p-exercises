from fpdf import FPDF

name = input('Name: ')
pdf = FPDF(orientation='P', format= 'A4')
pdf.add_page()
pdf.set_font('Times', style='B', size=32)
pdf.cell(0, 10, "CS50 Shirtificate", align='C')
pdf.image("shirtificate.png", 90, 30, 33)
pdf.set_text_color(255, 255, 255)
pdf.set_xy(x=13, y=38)
pdf.set_font('Times', style='B', size=8)
pdf.cell(0, 10, f'{name} took CS50', align='C')
pdf.output("shirtificate.pdf")