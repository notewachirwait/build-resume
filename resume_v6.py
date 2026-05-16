from reportlab.lib.pagesizes import A4
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

OUTPUT = "/Users/note.wachirawit/resume/Wachirawit_Thongkaew_Resume.pdf"

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
FS_CONTACT = 7.5
FS_SECTION = 8
FS_BODY = 7
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
    fontName="Helvetica",
    fontSize=FS_SUBTITLE,
    leading=12,
    textColor=BLUE,
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
bullet_s = style(
    "bullet", fontSize=FS_BULLET, leading=9, leftIndent=8, firstLineIndent=-6
)
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


def bullet(text):
    return Paragraph(f"• {text}", bullet_s)


CW_DATE = 35 * mm
CW_MAIN = W - 12 * mm - 12 * mm - CW_DATE - 2 * mm


def exp_block(employer, title, date, bullets):
    date_col = [Paragraph(date, date_s)]
    main_col = [Paragraph(employer, employer_s), Paragraph(title, jobtitle_s)]
    for b in bullets:
        main_col.append(Paragraph(f"• {b}", bullet_s))
    t = Table([[main_col, date_col]], colWidths=[CW_MAIN, CW_DATE])
    t.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
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

# Highlights (4 cards)
story += section_header("Highlights")
story.append(
    highlights_row(
        [
            (
                "Test Suite Optimization",
                "Reduced test suite execution time, increasing overall efficiency.",
            ),
            (
                "Team Mentorship",
                "Improved QA automation by enhancing function logic efficiency, reducing regression execution time.",
            ),
            (
                "AI Adoption",
                "Leveraged AI to generate test scripts and test scenarios, accelerating automation coverage.",
            ),
            (
                "Production Investigation",
                "Collaborated with support teams to investigate production issues, performing RCA to resolve critical defects.",
            ),
        ]
    )
)

# Experience
story += section_header("Experience")
story.append(
    exp_block(
        "LSEG (London Stock Exchange Group)",
        "Senior QA Engineer",
        "11/2022 - Present",
        [
            "Coached and mentored QA team members on best practices for test automation to ensure high-quality standards before production deployment.",
            "Optimized test suites to reduce execution time and increase coverage for critical features.",
            "Designed load testing scripts in JMeter to simulate concurrent traffic on RESTful APIs.",
            "Configured GitLab CI/CD quality gates to block MRs failing Selenium/Playwright E2E paths.",
            "Implemented cloud testing strategies by automating AWS Lambda triggers and S3 validations.",
            "Developed Gherkin-based scripts for execution with Playwright/Selenium to validate RESTful API responses.",
        ],
    )
)
story.append(
    exp_block(
        "Zipmex Pte. Ltd",
        "Software Quality Engineer",
        "11/2021 - 11/2022",
        [
            "Tested web applications utilizing Cypress and Playwright; performed load testing with k6.",
            "Collaborated with international teams to perform Root Cause Analysis (RCA) on production issues.",
            "Translated user-reported bugs into technical tickets for the engineering team.",
        ],
    )
)
story.append(
    exp_block(
        "MAQE Bangkok Co., Ltd",
        "QA Automation Engineer",
        "07/2020 - 10/2021",
        [
            "Validated cross-platform mobile apps (Flutter) for iOS/Android and web apps with Cypress.",
            "Performed UI/UX testing against Figma prototypes and conducted load testing with k6.",
        ],
    )
)
story.append(
    exp_block(
        "Ascend Corporation",
        "Quality Assurance Engineer",
        "10/2019 - 06/2020",
        [
            "Designed test cases in Agile environments and coordinated with Product Owners on priorities.",
            "Conducted automated UI testing for web applications using Cypress.",
        ],
    )
)
story.append(
    exp_block(
        "Aware Technology",
        "Associate Software Test Engineer Automation",
        "03/2019 - 11/2019",
        [
            "Tested Android apps with Appium and developed Selenium regression scripts from manual cases.",
            "Executed and debugged automation scripts to ensure stability and accuracy.",
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
