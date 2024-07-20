from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.image("./shirtificate.png", "C", 50, 175)
        self.set_font("helvetica", "", 55)
        self.cell(0, 30, "CS50 Shirtificate", align="C")
        self.ln(20)                                            #line break


def main():
    name = input("Name: ")
    pdf = PDF()
    pdf.add_page(orientation='portrait', format = 'a4')
    pdf.set_font("Times", size=30)
    pdf.set_text_color(255,255,255)
    pdf.cell(0, 200, f"{name} took CS50", align = "C")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
