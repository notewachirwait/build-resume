from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    HRFlowable,
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import KeepTogether

OUTPUT = "/Users/note.wachirawit/resume/Wachirawit_Thongkaew_Resume_edit.pdf"

# Page setup - tight margins for one page
doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=A4,
    leftMargin=12 * mm,
    rightMargin=12 * mm,
    topMargin=15 * mm,
    bottomMargin=10 * mm,
)

W, H = A4

# Colors
BLUE = colors.HexColor("#2E86C1")
BLACK = colors.HexColor("#1a1a1a")
GRAY = colors.HexColor("#555555")
LGRAY = colors.HexColor("#888888")
BG_GRAY = colors.HexColor("#F2F2F2")
WHITE = colors.white
DIVIDER = colors.HexColor("#CCCCCC")
TICK = colors.HexColor("#2E86C1")

FS_NAME = 18
FS_SUBTITLE = 8
FS_CONTACT = 8
FS_SECTION = 8
FS_BODY = 9
FS_BULLET = 8.5
FS_HIGHLIGHT = 7.5


def style(name, **kw):
    base = dict(
        fontName="Helvetica",
        fontSize=FS_BODY,
        textColor=BLACK,
        leading=10,
        spaceAfter=0,
        spaceBefore=0,
    )
    base.update(kw)
    return ParagraphStyle(name, **base)


name_s = style(
    "name",
    fontName="Helvetica-Bold",
    fontSize=FS_NAME,
    leading=24,
    textColor=BLACK,
    alignment=TA_CENTER,
    spaceAfter=3,
)
subtitle_s = style(
    "subtitle",
    fontName="Helvetica-Bold",
    fontSize=FS_SUBTITLE,
    leading=12,
    textColor=BLACK,
    alignment=TA_CENTER,
    spaceAfter=2,
)
contact_s = style(
    "contact",
    fontName="Helvetica",
    fontSize=FS_CONTACT,
    leading=11,
    textColor=GRAY,
    alignment=TA_CENTER,
    spaceAfter=4,
)
section_s = style(
    "section",
    fontName="Helvetica-Bold",
    fontSize=FS_SECTION,
    textColor=GRAY,
    alignment=TA_CENTER,
    spaceAfter=2,
    spaceBefore=4,
)
body_s = style("body", fontSize=FS_BODY, leading=9.5, alignment=TA_JUSTIFY)
bullet_dot_s = style("bullet_dot", fontSize=8.5, leading=11.5, textColor=BLACK)
bullet_s = style("bullet", fontSize=8.5, leading=11.5, alignment=TA_LEFT)
date_s = style(
    "date", fontSize=FS_BULLET, textColor=LGRAY, alignment=TA_RIGHT, leading=11
)
jobtitle_s = style(
    "jobtitle",
    fontName="Helvetica-Bold",
    fontSize=FS_BULLET,
    textColor=BLACK,
    leading=11,
)
employer_s = style(
    "employer", fontName="Helvetica-Bold", fontSize=9, textColor=BLUE, leading=12
)
expheader_s = style(
    "expheader",
    fontName="Helvetica-Bold",
    fontSize=FS_BULLET,
    textColor=BLACK,
    leading=12,
    spaceAfter=1,
)
highlight_label_s = style(
    "hl_label",
    fontName="Helvetica-Bold",
    fontSize=FS_HIGHLIGHT,
    textColor=BLACK,
    leading=9,
)
highlight_body_s = style("hl_body", fontSize=FS_HIGHLIGHT, textColor=GRAY, leading=9)
skill_key_s = style(
    "skill_key",
    fontName="Helvetica-Bold",
    fontSize=FS_BULLET,
    textColor=BLUE,
    leading=9,
)
skill_val_s = style("skill_val", fontSize=FS_BULLET, textColor=BLACK, leading=9)
interest_s = style(
    "interest",
    fontName="Helvetica-Bold",
    fontSize=FS_BULLET,
    textColor=BLACK,
    leading=9,
)
interest_v_s = style("interest_v", fontSize=FS_BULLET, textColor=GRAY, leading=9)


def hr(color=DIVIDER, thickness=0.4, before=1, after=2):
    return HRFlowable(
        width="100%",
        thickness=thickness,
        color=color,
        spaceAfter=after,
        spaceBefore=before,
    )


def section_header(text):
    return [
        hr(before=3, after=1),
        Paragraph(text, section_s),
        hr(after=2),
    ]


def make_bullet(text):
    DOT_W = 10
    BODY_W = CW_MAIN + CW_DATE - DOT_W
    t = Table(
        [[Paragraph("•", bullet_dot_s), Paragraph(text, bullet_s)]],
        colWidths=[DOT_W, BODY_W],
    )
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    return t


def bullet(text):
    return make_bullet(text)


CW_DATE = 35 * mm
CW_MAIN = W - 12 * mm - 12 * mm - CW_DATE - 2 * mm


def exp_block(employer, title, date, bullets):
    header_text = (
        f'<font color="#2E86C1"><b>{employer}</b></font>'
        f'<font color="#888888">  |  </font>'
        f'{title}'
        f'<font color="#888888">  |  </font>'
        f'<font color="#888888">{date}</font>'
    )
    items = [Paragraph(header_text, expheader_s)]
    for b in bullets:
        items.append(make_bullet(b))
    t = Table([[items]], colWidths=[CW_MAIN + CW_DATE])
    t.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    return t


# ── Highlight card ────────────────────────────────────────────────────────────
def highlight_card(label, body):
    content = [
        [Paragraph(f"✓  {label}", highlight_label_s)],
        [Paragraph(body, highlight_body_s)],
    ]
    t = Table(content, colWidths=[(W - 24 * mm) / 4 - 2 * mm])
    t.setStyle(
        TableStyle(
            [
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]
        )
    )
    return t


def highlights_row(cards):
    card_w = (W - 24 * mm) / len(cards) - 1.5 * mm
    cells = []
    for label, body in cards:
        inner = Table(
            [
                [Paragraph(f"✓  {label}", highlight_label_s)],
                [Paragraph(body, highlight_body_s)],
            ],
            colWidths=[card_w],
        )
        inner.setStyle(
            TableStyle(
                [
                    ("LEFTPADDING", (0, 0), (-1, -1), 5),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                    ("TOPPADDING", (0, 0), (-1, -1), 4),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ]
            )
        )
        cells.append(inner)
    row = Table([cells], colWidths=[card_w + 1.5 * mm] * len(cards))
    row.setStyle(
        TableStyle(
            [
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]
        )
    )
    return row


# ── Story ─────────────────────────────────────────────────────────────────────
story = []

# Header
story.append(Paragraph("WACHIRAWIT THONGKAEW", name_s))
story.append(
    Paragraph(
        "Senior QA Engineer",
        subtitle_s,
    )
)
story.append(
    Paragraph(
        "Email: wachirawit.th@ku.th •  LinkedIn: https://www.linkedin.com/in/wachirawit-thongkaew/  •  Phone: 0982705677",
        contact_s,
    )
)

# Summary section
story += section_header("Summary")
story.append(
    Paragraph(
        "Senior QA Engineer with a strong background across the Fintech and Banking sectors. Expert in designing "
        "and executing end-to-end automated and manual testing strategies to ensure product quality and reliability "
        "for high-performance financial platforms. Focused on driving testing innovation and enhancing frameworks "
        "within Agile environments to support rapid software delivery and robust system stability.",
        body_s,
    )
)

# # Highlights (4 cards)
# story += section_header("Highlights")
# story.append(
#     highlights_row(
#         [
#             (
#                 "Test Suite Optimization",
#                 "Reduced test suite execution time, increasing overall efficiency.",
#             ),
#             (
#                 "Team Mentorship",
#                 "Improved QA automation by enhancing function logic efficiency, reducing regression execution time.",
#             ),
#             (
#                 "AI Adoption",
#                 "Leveraged AI to generate test scripts and test scenarios, accelerating automation coverage.",
#             ),
#             (
#                 "Production Investigation",
#                 "Collaborated with support teams to investigate production issues, performing RCA to resolve critical defects.",
#             ),
#         ]
#     )
# )

# Experience
story += section_header("Experience")
story.append(
    exp_block(
        "LSEG (London Stock Exchange Group)",
        "Senior QA Engineer",
        "11/2022 - Present",
        [
            "Established test automation best practices and coding standards for the QA team, reducing defect escape rate before production deployment.",
            "Optimized automation test suite by consolidating redundant cases and refining execution logic, reducing overall regression run time by 50%.",
            "Built JMeter load testing scripts to stress-test RESTful APIs under concurrent traffic, identifying performance bottlenecks before production.",
            "Enforced zero-defect deployment standards by integrating Selenium/Playwright E2E quality gates into GitLab CI/CD, blocking non-compliant merges automatically.",
            "Extended test coverage to cloud infrastructure by validating serverless workflows and data integrity checks across critical cloud-dependent processes.",
            "Implemented Behavior-Driven Development (BDD) using Gherkin and Cucumber to align tests with business requirements and standardize feature documentation.",
        ],
    )
)
story.append(
    exp_block(
        "Zipmex Pte. Ltd",
        "Software Quality Engineer",
        "11/2021 - 11/2022",
        [
            "Validated end-to-end UI flows for ZipCard, a crypto-backed Visa debit card, using Cypress and Playwright to ensure payment accuracy and transaction reliability.",
            "Collaborated with international teams to perform Root Cause Analysis (RCA) on production issues.",
        ],
    )
)
story.append(
    exp_block(
        "MAQE Bangkok Co., Ltd",
        "QA Automation Engineer",
        "07/2020 - 10/2021",
        [
            "Led end-to-end QA for Com7's BananaIT (BNN) eCommerce platform migration from Magento to a custom-built solution across web and mobile (iOS/Android) using Cypress.",
            "Validated UI/UX implementation against Figma prototypes and stress-tested the BNN platform under high-traffic retail conditions using k6.",
        ],
    )
)
story.append(
    exp_block(
        "Ascend Corporation",
        "Quality Assurance Engineer",
        "10/2019 - 06/2020",
        [
            "Designed and prioritized test cases in Agile sprints for WeFresh, a grocery delivery platform integrating 7-Eleven, CP Freshmart, and Tesco Lotus Express into a single app.",
            "Built UI test coverage with Cypress to validate cart, checkout, and partner store integrations across the WeFresh platform.",
            "Investigated production issues on WeFresh, collaborating with support teams to perform Root Cause Analysis (RCA) and resolve live customer-impacting defects.",
        ],
    )
)
story.append(
    exp_block(
        "Aware Technology",
        "Associate Software Test Engineer Automation",
        "03/2019 - 11/2019",
        [
            "Built mobile test coverage for myAIS (AIS's all-in-one customer app) using Appium on Android, converting over 100 manual cases into a reusable regression suite.",
            "Maintained and debugged Selenium and Appium scripts across mobile and web to ensure stability of core myAIS features through each release cycle.",
        ],
    )
)

# Education
story += section_header("Education")
story.append(
    exp_block(
        "Kasetsart University",
        "Bachelor of Science in Computer Science",
        "01/2015 - 01/2019",
        [],
    )
)

# Skills
story += section_header("Skills")
skills_table = Table(
    [
        [
            Paragraph("Advanced:", skill_key_s),
            Paragraph(
                "Selenium · Cypress · Playwright · Postman/REST API · Cucumber",
                skill_val_s,
            ),
        ],
        [
            Paragraph("Intermediate:", skill_key_s),
            Paragraph(
                "SQL Script · Redis Command · Appium · Robot Framework · k6 · JMeter · Jenkins · GitHub Actions",
                skill_val_s,
            ),
        ],
    ],
    colWidths=[24 * mm, W - 24 * mm - 24 * mm],
)
skills_table.setStyle(
    TableStyle(
        [
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 1),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
        ]
    )
)
story.append(skills_table)

# Find me online
story += section_header("Find me online")
story.append(
    Paragraph(
        "Github  —  https://github.com/notewachirwait",
        style("gh", fontSize=FS_BULLET, textColor=BLACK, leading=9),
    )
)

# Interests
story += section_header("Interests")
interests = [
    (
        "AI & Automation:",
        "AI agents, multi-agent systems, and building custom Slack automations.",
    ),
    (
        "FinTech:",
        "Actively monitoring financial markets with a focus on AI-driven stock trends.",
    ),
    (
        "Fitness:",
        "Maintaining work-life balance through regular weight training and gym sessions.",
    ),
]
int_w = (W - 24 * mm) / 3 - 1.5 * mm
int_cells = []
for label, val in interests:
    inner = Table(
        [[Paragraph(label, interest_s)], [Paragraph(val, interest_v_s)]],
        colWidths=[int_w],
    )
    inner.setStyle(
        TableStyle(
            [
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )
    int_cells.append(inner)
int_row = Table([int_cells], colWidths=[int_w + 1.5 * mm] * 3)
int_row.setStyle(
    TableStyle(
        [
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ]
    )
)
story.append(int_row)

doc.build(story)
print("Done:", OUTPUT)
