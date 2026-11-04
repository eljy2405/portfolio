"""Regenerate the interview CV and 16:9 profile deck. Requires reportlab.
Content is based on the original supplied CV; update here when your experience changes.
"""
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import simpleSplit
from reportlab.lib.pagesizes import A4
ROOT = Path(__file__).resolve().parents[1]
NAVY, BLUE, GREY = '#102640', '#2458a0', '#4e6075'
NAME = 'Ethan Law Jun Yi'
TITLE = 'Global Markets, Corporate Sales Dealer'
LINK = 'https://www.linkedin.com/in/ethanlawjunyi/'

def text(c, x, y, content, size=10, color=GREY, width=490, font='Helvetica', leading=None):
    c.setFillColor(HexColor(color)); c.setFont(font, size)
    for line in simpleSplit(content, font, size, width):
        c.drawString(x, y, line); y -= leading or size * 1.45
    return y

def heading(c, y, title):
    y = text(c, 42, y, title.upper(), 9, BLUE, font='Helvetica-Bold')
    c.setStrokeColor(HexColor('#d9e2ed')); c.line(42, y+4, 553, y+4)
    return y-12

def cv():
    c = canvas.Canvas(str(ROOT / 'Ethan-Law-Jun-Yi-CV.pdf'), pagesize=A4)
    c.setTitle(f'{NAME} | Interview CV'); c.setAuthor(NAME)
    c.setFillColor(HexColor(NAVY)); c.rect(0, 716, 596, 126, fill=1, stroke=0)
    text(c, 42, 798, NAME, 25, '#ffffff', font='Helvetica-Bold')
    text(c, 42, 770, TITLE, 12, '#c7dcf8')
    text(c, 42, 745, 'ethanlawjy@gmail.com  |  +60 19-871 4078  |  LinkedIn profile', 9, '#ffffff')
    c.linkURL(LINK, (350, 733, 440, 750), relative=0)
    y=heading(c, 692, 'Profile')
    y=text(c,42,y,"Biomedical Engineering graduate from King's College London, building a career in Global Markets. Experience in foreign exchange and interest rate hedging support, equity research and private equity training. Combines quantitative analysis with clear communication and a client-focused approach.",9.5,width=510)-13
    y=heading(c,y,'Professional experience')
    y=text(c,42,y,'United Overseas Bank, Malaysia | FSTEP Trainee (Global Markets)',10,NAVY,font='Helvetica-Bold',width=510)
    y=text(c,42,y,'April 2026 - Present',8.5,BLUE)-3
    y=text(c,50,y,'• Support clients with foreign exchange and interest rate hedging considerations based on their requirements and access.',9.3,width=495)
    y=text(c,50,y,'• Coordinate with branches and business partners to increase treasury product sales and utilisation of approved trade lines.',9.3,width=495)-9
    y=text(c,42,y,'UOB Kay Hian, Malaysia | Equity Research Analyst',10,NAVY,font='Helvetica-Bold')
    y=text(c,42,y,'May 2024 - July 2024',8.5,BLUE)-3
    y=text(c,50,y,'• Analysed earnings releases, investor presentations and industry data to support sector outlook and valuation views.',9.3,width=495)
    y=text(c,50,y,'• Produced concise investment summaries for senior analysts; evaluated revenue drivers, margin trends and competitive positioning.',9.3,width=495)-13
    y=heading(c,y,'Education & training')
    y=text(c,42,y,"King's College London | BEng with Honours, Biomedical Engineering",10,NAVY,font='Helvetica-Bold',width=510)
    y=text(c,42,y,'Dissertation: Smart Sensing Sleeve for Continuous Monitoring of Urostomy Bag Fill-Level. Integrated hardware and software; applied statistical, machine learning and optimisation techniques.',9.3,width=510)-7
    y=text(c,42,y,'Imperial College Business School | Private Equity summer programme',10,NAVY,font='Helvetica-Bold',width=510)
    y=text(c,42,y,'Financing, Investing and Value Creation: case studies, commercial due diligence and investment screening.',9.3,width=510)-7
    y=text(c,42,y,'HELP International School | A-Levels',10,NAVY,font='Helvetica-Bold')
    y=text(c,42,y,'Physics A*, Biology A*, Mathematics A; Computer Science AS Level. Leadership Excellence scholarship.',9.3,width=510)-13
    y=heading(c,y,'Skills & leadership')
    y=text(c,42,y,'Tools: Bloomberg Terminal (BMC certified), Python, MATLAB, C++, Excel, PowerPoint.',9.3,width=510)
    y=text(c,42,y,'Leadership: University mixed ultimate frisbee captain; SHINE academic mentor; F1 in Schools team leader.',9.3,width=510)
    y=text(c,42,y,'Languages: English (native); Mandarin, Malay and Cantonese (conversational).',9.3,width=510)
    assert y>35, f'CV overflow: {y}'
    text(c,42,25,'linkedin.com/in/ethanlawjunyi',8,BLUE)
    c.linkURL(LINK,(42,22,240,35),relative=0)
    c.save()

def slides():
    w,h=960,540;c=canvas.Canvas(str(ROOT/'Ethan-Law-Jun-Yi-Slides.pdf'),pagesize=(w,h))
    c.setTitle(f'{NAME} | Global Markets Profile');c.setAuthor(NAME)
    pages=[
      ('PROFILE',NAME,[(TITLE,'A quantitative foundation. A client-focused markets perspective.'),('Connect','ethanlawjy@gmail.com | +60 19-871 4078')]),
      ('CAREER DIRECTION','Connecting markets with corporate needs', [('Corporate treasury','Foreign exchange and interest rate hedging considerations informed by client requirements.'),('Research discipline','Company fundamentals, industry context and concise investment summaries.'),('Quantitative foundation',"Biomedical Engineering at King's College London, with statistical analysis and technical problem solving.")]),
      ('EXPERIENCE','United Overseas Bank, Malaysia',[('FSTEP Trainee (Global Markets)','April 2026 - Present'),('Client needs','Support foreign exchange and interest rate hedging discussions based on requirements and access.'),('Collaboration','Work with branches and business partners to grow treasury product sales and utilisation of approved trade lines.')]),
      ('RESEARCH','UOB Kay Hian, Malaysia',[('Equity Research Analyst','May 2024 - July 2024'),('Evidence to insight','Analyse earnings releases, investor presentations and industry data to support sector outlook and valuation views.'),('Clear communication','Synthesise research for senior analysts. Evaluate revenue drivers, margins and competitive positioning.')]),
      ('EDUCATION & TOOLS','Engineering discipline. Financial curiosity.',[("King's College London",'BEng with Honours in Biomedical Engineering. Smart sensing prototype integrating hardware and software.'),('Imperial College Business School','Private Equity summer programme: investment screening, commercial due diligence and value creation.'),('Technical toolkit','Bloomberg Terminal (BMC certified), Python, MATLAB, C++, Excel and PowerPoint.')]),
      ('LET’S CONNECT','Ethan Law Jun Yi',[(TITLE,'Interested in opportunities in Global Markets and corporate treasury sales.'),('Email & phone','ethanlawjy@gmail.com | +60 19-871 4078'),('LinkedIn','linkedin.com/in/ethanlawjunyi')])]
    for i,(label,title,blocks) in enumerate(pages):
      c.setFillColor(HexColor('#f4f7fb'));c.rect(0,0,w,h,fill=1,stroke=0)
      c.setFillColor(HexColor(NAVY));c.rect(0,h-14,w,14,fill=1,stroke=0)
      text(c,52,482,label,11,BLUE,font='Helvetica-Bold',width=856)
      y=text(c,52,440,title,30,NAVY,width=850,font='Helvetica-Bold',leading=36)-20
      for key,body in blocks:
        y=text(c,52,y,key,15,BLUE,width=850,font='Helvetica-Bold')-3
        y=text(c,52,y,body,14,GREY,width=820,leading=21)-21
      assert y>52,(i,y)
      text(c,52,26,NAME+'  |  linkedin.com/in/ethanlawjunyi',9,BLUE,width=800)
      c.linkURL(LINK,(52,22,500,38),relative=0)
      text(c,865,26,f'{i+1} / {len(pages)}',9,GREY)
      c.showPage()
    c.save()
if __name__=='__main__':cv();slides()
