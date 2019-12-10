from plotapp import models
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT, TA_RIGHT
import time
import csv
from matplotlib import pyplot as plt
from uuid import uuid4
import math
import statistics
from django.conf import settings
import os
from django.core.files import File


def plot_scatter(points):
    plt.scatter([i for i in range(len(points))], points, alpha=0.5)
    plt.title('Scatter Plot')
    fn1 = os.path.join(settings.BASE_DIR, "temp", str(uuid4()) + ".png")
    plt.savefig(fn1)

    plt.clf()
    n, bins, patches = plt.hist(sorted(points), bins=100)
    fn2 = os.path.join(settings.BASE_DIR, "temp", str(uuid4()) + ".png")
    plt.savefig(fn2)

    return fn1, fn2


def plot():
    files = models.InputFile.objects.filter(
        status='queued'
    )

    for f in files:
        pdf_filename = os.path.join(settings.BASE_DIR, 'temp', str(uuid4()))
        with open(f.file.path, 'rt', newline='') as fp:
            reader = csv.reader(fp)
            points = list([float(row[0]) for row in reader])
            average = round(statistics.mean(points), 2)
            minimum = round(min(points), 2)
            maximum = round(max(points), 2)
            stdev = round(statistics.stdev(points), 2)

            fn1, fn2 = plot_scatter(points)

            doc = SimpleDocTemplate(pdf_filename, pagesize=letter,
                                    rightMargin=72, leftMargin=72,
                                    topMargin=72, bottomMargin=18)
            Story = []

            logo = "python_logo.png"
            magName = "TEST REPORT"
            test_date = "03/05/2010"
            csv_filename = 'Measurement_Data_20191023.csv'

            # im = Image(logo, 2*inch, 2*inch)
            # Story.append(im)

            styles = getSampleStyleSheet()

            styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
            styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER))

            ptext = '<font size=12>%s</font>' % magName

            Story.append(Paragraph(ptext, styles["Center"]))
            Story.append(Spacer(1, 12))

            # Create return address
            ptext = '<font size=12>Test Date: %s</font>' % test_date
            Story.append(Paragraph(ptext, styles["Normal"]))
            ptext = '<font size=12>CSV Filename: %s</font>' % csv_filename
            Story.append(Paragraph(ptext, styles["Normal"]))
            Story.append(Spacer(1, 12))

            ptext = '<font size=12>%s</font>' % 'Plot 1 (Actual Plot: time (x) vs measurement (y))'
            Story.append(Paragraph(ptext, styles["Normal"]))
            im1 = Image(fn1, 5*inch, 3*inch)
            Story.append(im1)
            Story.append(Spacer(1, 12))

            ptext = '<font size=12>%s</font>' % 'Plot 2 (Histogram)'
            Story.append(Paragraph(ptext, styles["Normal"]))
            im2 = Image(fn2, 5*inch, 3*inch)
            Story.append(im2)
            Story.append(Spacer(1, 12))
            ptext = '<font size=12>Ave: %s</font>' % average
            Story.append(Paragraph(ptext, styles["Normal"]))
            ptext = '<font size=12>Min: %s</font>' % minimum
            Story.append(Paragraph(ptext, styles["Normal"]))
            ptext = '<font size=12>Max: %s</font>' % maximum
            Story.append(Paragraph(ptext, styles["Normal"]))
            ptext = '<font size=12>STDEV: %s</font>' % stdev
            Story.append(Paragraph(ptext, styles["Normal"]))
            doc.build(Story)

            if os.path.exists(pdf_filename):
                f.status = 'done'
                with open(pdf_filename, 'rb') as source:
                    f.pdf_file.save(os.path.basename(
                        pdf_filename) + '.pdf', File(source), save=True)
