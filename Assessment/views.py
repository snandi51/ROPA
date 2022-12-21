from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from fpdf import FPDF
import uuid
import imghdr
from email.message import EmailMessage
from django.contrib import messages
from django.contrib.auth.models import User
import warnings
from datetime import datetime
warnings.filterwarnings("ignore")
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, Frame, SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter


from PyPDF2 import PdfMerger
from openpyxl import load_workbook

from django.conf import settings
from django.core.mail import send_mail

from PyPDF2 import PdfFileWriter, PdfFileReader
import io



# Create your views here.

