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
    KeepTogether,
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY

OUTPUT = "/Users/note.wachirawit/resume/Tanaporn_Karuhawanit_CV.pdf"

# Page setup - tight margins for one page
doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=A4,
    leftMargin=12 * mm,
    rightMargin=12 * mm,
    topMargin=14 * mm,
    bottomMargin=10 * mm,
)

W, H = A4

# Colors
BLUE = colors.HexColor("#2E86C1")
BLACK = colors.HexColor("#1a1a1a")
GRAY = colors.HexColor("#555555")
LGRAY = colors.HexColor("#888888")
DIVIDER = colors.HexColor("#CCCCCC")

FS_NAME = 18
FS_SUBTITLE = 8
FS_CONTACT = 8.5
FS_SECTION = 8
FS_BODY = 8.5
FS_BULLET = 8.5
FS_HIGHLIGHT = 7.5


def style(name, **kw):
    base = dict(
        fontName="Helvetica",
        fontSize=FS_BODY,
        textColor=BLACK,
        leading=11,
        spaceAfter=0,
        spaceBefore=0,
    )
    base.update(kw)
    return ParagraphStyle(name, **base)


# ── Typography ─────────────────────────────────────────────────────────────────
name_s = style(
    "name",
    fontName="Helvetica-Bold",
    fontSize=FS_NAME,
    leading=22,
    textColor=BLACK,
    alignment=TA_CENTER,
    spaceAfter=2,
)
subtitle_s = style(
    "subtitle",
    fontName="Helvetica-Bold",
    fontSize=FS_SUBTITLE,
    leading=11,
    textColor=BLACK,
    alignment=TA_CENTER,
    spaceAfter=1,
)
contact_s = style(
    "contact",
    fontSize=FS_CONTACT,
    leading=15,
    textColor=GRAY,
    alignment=TA_CENTER,
    spaceAfter=2,
)
body_s = style("body", fontSize=FS_BODY, leading=10.5, alignment=TA_JUSTIFY)

section_left_s = style(
    "section_left",
    fontName="Helvetica-Bold",
    fontSize=FS_SECTION + 1,
    textColor=BLACK,
    alignment=TA_LEFT,
    spaceAfter=1,
    spaceBefore=1,
)
license_val_s = style(
    "license_val",
    fontSize=FS_BULLET,
    textColor=BLACK,
    leading=10,
    fontName="Helvetica-Oblique",
)
lang_key_s = style(
    "lang_key",
    fontName="Helvetica-Bold",
    fontSize=FS_BULLET,
    textColor=BLACK,
    leading=10,
)
lang_val_s = style(
    "lang_val",
    fontSize=FS_BULLET,
    textColor=LGRAY,
    leading=10,
)
exp_company_s = style(
    "exp_company",
    fontName="Helvetica-Bold",
    fontSize=FS_BULLET,
    textColor=BLUE,
    leading=10,
)
exp_title_s = style(
    "exp_title",
    fontName="Helvetica-Bold",
    fontSize=FS_BULLET,
    textColor=BLACK,
    leading=10,
)
exp_date_s = style(
    "exp_date",
    fontSize=7.5,
    textColor=LGRAY,
    leading=10,
    alignment=TA_RIGHT,
)
skill_key_s = style(
    "skill_key",
    fontName="Helvetica-Bold",
    fontSize=FS_BULLET,
    textColor=BLUE,
    leading=10,
)
skill_val_s = style("skill_val", fontSize=FS_BULLET, textColor=BLACK, leading=10)

# Bullet styles — use firstLineIndent trick for clean hanging indent
BULLET_INDENT = 10  # points
bullet_s = style(
    "bullet",
    fontSize=FS_BULLET,
    leading=11,
    leftIndent=BULLET_INDENT,
    firstLineIndent=-BULLET_INDENT,
    alignment=TA_LEFT,
)

interest_title_s = style(
    "interest_title",
    fontName="Helvetica-Bold",
    fontSize=FS_BULLET,
    textColor=BLACK,
    leading=11,
)
interest_body_s = style(
    "interest_body",
    fontSize=FS_BULLET,
    textColor=GRAY,
    leading=11,
    alignment=TA_LEFT,
)


# ── Column widths ──────────────────────────────────────────────────────────────
CONTENT_W = W - 12 * mm - 12 * mm
LEFT_W = CONTENT_W * 0.64
RIGHT_PAD = 4 * mm  # left padding inside right column
RIGHT_W = CONTENT_W * 0.36 - 5 * mm - RIGHT_PAD
COL_GAP = 5 * mm


# ── Helpers ────────────────────────────────────────────────────────────────────
def make_bullet(text):
    """Hanging-indent bullet using Paragraph — no nested Table needed."""
    return Paragraph(f"• {text}", bullet_s)


def col_section_header(text, width):
    """Bold section title + full-width rule below it."""
    return [
        Paragraph(text.upper(), section_left_s),
        HRFlowable(
            width=width, thickness=0.8, color=BLACK, spaceAfter=3, spaceBefore=0
        ),
    ]


def row_table(cells, col_widths):
    """Helper: single-row Table with zero padding."""
    t = Table([cells], colWidths=col_widths)
    t.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )
    return t


# ── LEFT COLUMN ────────────────────────────────────────────────────────────────
def build_left_column():
    L = LEFT_W
    items = []

    # SUMMARY
    items += col_section_header("SUMMARY", L)
    items.append(
        Paragraph(
            "Experienced architect possessing three years of proficiency in conceptual design, "
            "detailed drafting, and construction site coordination. Demonstrates strong "
            "communication skills collaborating with contractors.",
            body_s,
        )
    )
    items.append(Spacer(1, 10))

    # LICENSE
    items += col_section_header("LICENSE", L)
    items.append(Paragraph("Associate Architect License", license_val_s))
    items.append(Spacer(1, 10))

    # EDUCATION
    items += col_section_header("EDUCATION", L)
    items.append(
        row_table(
            [
                Paragraph("Bachelor of Architecture", exp_title_s),
            ],
            [L * 0.68, L * 0.32],
        )
    )
    items.append(
        row_table(
            [
                Paragraph("Kasetsart University", exp_company_s),
                Paragraph("2017 - 2022", exp_date_s),
            ],
            [L * 0.68, L * 0.32],
        )
    )
    items.append(Spacer(1, 10))

    # EXPERIENCE
    items += col_section_header("EXPERIENCE", L)
    items.append(
        row_table(
            [
                Paragraph("Architect", exp_title_s),
            ],
            [L * 0.55, L * 0.45],
        )
    )

    items.append(
        row_table(
            [
                Paragraph("UNKNOWN SURFACE STUDIO", exp_company_s),
                Paragraph("08/2022 - 02/2026", exp_date_s),
            ],
            [L * 0.55, L * 0.45],
        )
    )
    items.append(Spacer(1, 2))

    bullets = [
        "<b>Design Award:</b> Led the design of Curvy Dining (2025), a 250 sq.m. freeform restaurant that received the Room SELECT Awards.",
        "<b>Project Leadership:</b> Overseeing the construction of Ministry Forest, a 1,000 sq.m. tropical garden-centered restaurant complex.",
        "<b>Boutique Renovation:</b> Managed the 30-room The Tan Hotel renovation, utilizing perforated aluminum facades to enhance privacy and modern identity.",
        "<b>Material Innovation:</b> Developed seamless, organic interiors for Craft Coffee Roaster and Nose Tea using CNC-cut foam panels and integrated fabric lighting.",
        "<b>Master Planning:</b> Designed a 24-unit Pool Villa in Khao Yai, coordinating master planning with health-focused communal facilities.",
        "<b>Technical Expertise:</b> Delivered high-fidelity 3D visualizations, architectural documentation, and on-site coordination.",
    ]
    for b in bullets:
        items.append(make_bullet(b))

    items.append(Spacer(1, 5))

    # ── Second experience ──────────────────────────────────────────────────────
    items.append(
        row_table(
            [
                Paragraph("Junior Architect", exp_title_s),
            ],
            [L * 0.55, L * 0.45],
        )
    )

    items.append(
        row_table(
            [
                Paragraph("ONION CO., LTD.", exp_company_s),
                Paragraph("06/2022 - 08/2022", exp_date_s),
            ],
            [L * 0.55, L * 0.45],
        )
    )

    items.append(Spacer(1, 2))

    bullets2 = [
        "<b>Design Development:</b> Assisted senior architects in developing schematic and design development drawings for residential and mixed-use projects.",
        "<b>3D Visualization:</b> Produced presentation-quality renderings using Rhino and Enscape to support client pitches and design approvals.",
        "<b>Site Coordination:</b> Attended site visits and coordinated with contractors to ensure construction aligned with architectural intent.",
    ]
    for b in bullets2:
        items.append(make_bullet(b))

    items.append(Spacer(1, 10))

    # TOOLS
    items += col_section_header("TOOLS", L)
    tools = [
        ("3D Model", "Rhino, Sketchup"),
        ("Render", "Enscape, D5Render"),
        ("Drawing", "AutoCad, Revit"),
    ]
    for i, (key, val) in enumerate(tools):
        items.append(Paragraph(key, skill_key_s))
        items.append(Paragraph(val, skill_val_s))
        if i < len(tools) - 1:
            items.append(
                HRFlowable(
                    width=L,
                    thickness=0.3,
                    color=DIVIDER,
                    spaceAfter=2,
                    spaceBefore=2,
                )
            )

    items.append(Spacer(1, 10))

    # LANGUAGES
    items += col_section_header("LANGUAGES", L)
    # Four equal columns: [lang] [level] [lang] [level]
    lang_table = Table(
        [
            [
                Paragraph("English", lang_key_s),
                Paragraph("Intermediate", lang_val_s),
                Paragraph("Thai", lang_key_s),
                Paragraph("Native", lang_val_s),
            ]
        ],
        colWidths=[L * 0.15, L * 0.35, L * 0.15, L * 0.35],
    )
    lang_table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 1),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
            ]
        )
    )
    items.append(lang_table)

    return items


# ── RIGHT COLUMN ───────────────────────────────────────────────────────────────
def build_right_column():
    R = RIGHT_W
    items = []

    items += col_section_header("INTERESTS", R)

    interest_items = [
        (
            "Residential & Public Architecture",
            "Highly interested in designing private residences, housing developments, and large-scale public buildings.",
        ),
        (
            "Scale & Complexity",
            "Seeking to apply architectural expertise to larger, more complex projects that challenge design and technical boundaries.",
        ),
    ]

    for i, (title, body) in enumerate(interest_items):
        items.append(Paragraph(title, interest_title_s))
        items.append(Paragraph(body, interest_body_s))
        if i < len(interest_items) - 1:
            items.append(Spacer(1, 5))

    return items


# ── Assemble two-column body ───────────────────────────────────────────────────
left_items = build_left_column()
right_items = build_right_column()

left_table = Table([[item] for item in left_items], colWidths=[LEFT_W])
left_table.setStyle(
    TableStyle(
        [
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ]
    )
)

right_table = Table([[item] for item in right_items], colWidths=[RIGHT_W])
right_table.setStyle(
    TableStyle(
        [
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), RIGHT_PAD),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ]
    )
)

two_col = Table(
    [[left_table, right_table]],
    colWidths=[LEFT_W + COL_GAP, RIGHT_W],
)
two_col.setStyle(
    TableStyle(
        [
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            # Subtle vertical divider between columns
            ("LINEAFTER", (0, 0), (0, -1), 0.3, DIVIDER),
        ]
    )
)

# ── Story ──────────────────────────────────────────────────────────────────────
story = []

story.append(Paragraph("TANAPORN KARUHAWANIT", name_s))
story.append(Paragraph("Architect", subtitle_s))
story.append(Paragraph("Email: tanaprnnn@gmail.com", contact_s))
story.append(
    HRFlowable(
        width="100%",
        thickness=1,
        color=BLACK,
        spaceAfter=5,
        spaceBefore=1,
    )
)
story.append(two_col)

doc.build(story)
print("Done:", OUTPUT)
