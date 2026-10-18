import os
import pymupdf # PyMuPDF

pdf_conversions = [
    ("assets/certificates/Copy of Aqua Science Certificate.pdf", "assets/certificates/Aqua Science Certificate.jpg"),
    ("assets/certificates/Copy of InspiritAI_AI_Scholars_Certificate_AadyaAgarwal.pdf", "assets/certificates/InspiritAI_AI_Scholars_Certificate.jpg"),
    ("assets/certificates/Copy of InspiritAI_AI_Ambassador_Certificate_AadyaAgarwal.pdf", "assets/certificates/InspiritAI_AI_Ambassador_Certificate.jpg"),
    ("assets/certificates/John Locke 2026 - High Commendation.pdf", "assets/certificates/John Locke 2026 - High Commendation.jpg"),
    ("assets/certificates/Scholastic_Poetry_Silver_Key_Certificate.pdf", "assets/certificates/Scholastic_Poetry_Silver_Key_Certificate.jpg"),
    ("assets/certificates/Copy of MATLAB_SimscapeOnramp_certificate.pdf", "assets/certificates/MATLAB_SimscapeOnramp_certificate.jpg"),
    ("assets/community/The Melvin Jones Fundraiser Flyer - Aadya Agarwal.pdf", "assets/community/The Melvin Jones Fundraiser Flyer.jpg"),
]

for pdf_path, out_jpg in pdf_conversions:
    if os.path.exists(pdf_path):
        try:
            doc = pymupdf.open(pdf_path)
            page = doc[0]
            # 2x zoom for crisp high-res image
            pix = page.get_pixmap(dpi=200)
            pix.save(out_jpg)
            print(f"Rendered: {out_jpg} ({pix.width}x{pix.height})")
            doc.close()
        except Exception as e:
            print(f"Error rendering {pdf_path}: {e}")
    else:
        print(f"Not found: {pdf_path}")
