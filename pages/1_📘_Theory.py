import streamlit as st

st.set_page_config(layout="wide")

st.title("Gas Ratio Interpretation Theory")
st.markdown("---")

st.header("Introduction")

st.write("""
The composition of entrained reservoir gas in mud is significant in 
determining the origin and value of a show. The Gas Composition Diagram is 
used to graphically represent the hydrocarbon distribution in the gas and to 
determine whether it corresponds to a gas or oil reservoir.

Gas composition diagrams are used to:
- Represent hydrocarbon distribution
- Identify gas, oil, or non-productive zones
""")

st.markdown("---")

st.header("2. Gas Ratio Triangular Plot")

### Gas Ratio Triangular Plot
st.write("""
The triangular diagram is constructed using three axes at 120°:
- C2/Total (Ethane)
- C3/Total (Propane)
- nC4/Total (Normal Butane)

Interpretation:
- Apex upward → Gas zone  
- Apex downward → Oil zone  
- Large triangle → Dry gas / low GOR oil  
- Small triangle → Wet gas / high GOR oil  
""")

st.subheader("Ratio Relationships")
st.write("""
The Triangular plot requires the calculation of the ratios C2, C3 and nC4 to the total of all gases detected (expressed as percentage). 
Lines representing those percentage are then drawn on a triangular grid.
Each side of the Triangle can now be used to plot ratios of:
""")
st.latex(r"1.\ \frac{C_2}{\sum C} \quad 2.\ \frac{C_3}{\sum C} \quad 3.\ \frac{nC_4}{\sum C}")

st.write("""
The Homocentric center of the triangle should fall inside the area delineated by the dotted line, which encircles compositions, which are "normal". If the triangle
area is outside this area the gas suggests that the reservoir is not exploitable and that the heavier hydrocarbo composition is "abnormal" 
(hydrocarbon chemically atlered or dys-migrated or gases with special compositions which are not associated with oil) and may indicate a dead show. 
The area of the triangle delineated as productive varies with the geochemical history of a given basin or sector. Thus the position of the homothetic center
is of minimal importance until an area trend is established.
""")

col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.image("assets/triangular_plot.png", width=800)

st.markdown("---")

### Gas Ratio Rectangular Plot
st.header("3. Rectangular (Pixler) Plot")

st.write("""
The Pixler Gas Ratio Plot represents ratios of methane to heavier hydrocarbons on semi-logarithmic grid:

- C1/C2
- C1/C3
- C1/C4
- C1/C5

The magnitude of the methane to ethane ratio determines if the reservoir contains gas or oil or if it is nonproductive.
""")

st.subheader("C1/C2 Interpretation")

st.table({
        "Range": ["< 2", "2 – 15", "15 – 65", "> 65"],
        "Interpretation": [
            "Non-productive zone",
            "Oil present",
            "Gas present",
            "Non-productive zone"
        ]
    })

st.subheader("Additional Interpretation Rules")

st.write("""
The slope of the line of the ratio plot indicates whether the reservoir will produce hydrocarbons or hydrocarbons with water.
- Positive slope → Hydrocarbon production  
- Negative slope → Water-bearing formation  
- Decreasing ratios → Non-productive  
""")

st.write("""
Several "rules of thumb" for rectangular plot are:

- Productive dry gas zones may show only C1, but abnormally high shows of C1 are usually indicative of salt water zones.
- If the ratio C1/C2 is low in the oil section and the ratio of C1/C4 is high in the gas section, the zone is probably non-productive.
- If any ratio (C1/C5 excepted in an oil based mud) is lower than the preceding ratio then the zone is probably non-productive.
- The ratios may not be definitive for zones of low permeability. Steep gas ratio plots may be indicative of tight zones.
""")

col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.image("assets/rectangular_plot.png", width=800)

st.markdown("---")

st.header("4. Gas Ratio Method")

st.write("""
Gas ratio method is a combination of three ratios, which when plotted toghther suggests a fluid character. The ratios are designed to be plotted on a depth log
(unlike the rectangular or triangular plots) and still provide interpretative results. They were designed for ditch gas values rather than steam-still or DST values.
""")

st.write(""" The following ratios are used:""")
st.latex(r"1.\ Wh = \frac{C2 + C3 + C4 + C5}{C1 + C2 + C3 + C4 + C5} \times 100")
st.latex(r"2.\ Bh = \frac{C1 + C2}{C3 + C4 + C5}")
st.latex(r"3.\ Ch = \frac{C4 + C5}{C3}")


st.subheader("Wetness (Wh) Analysis")

st.write("""Wetness (Wh) is the primary zone indicator and provides a measure of the relative proportion of heavier gases in the overall gas show. This ratio shows
         an increasing trend as gas and oil density increases, i.e. as the amount of heavy gas increaes proportionally against the lighter gases.
         """)

st.write(""" The interpretations are as follows:""")
st.table({
    "Wetness Range": ["< 0.5", "0.5 – 17.5", "17.5 – 40", "> 40"],
    "Interpretation": [
        "Light non-associated gas (low productivity)",
        "Potentially productive gas",
        "Potentially productive oil",
        "Heavy/residual oil with low productivity potential"
    ]
})

st.subheader("Balance (Bh) Analysis")

st.write("""Balance (Bh), which plots nearly the inverse of wetness, and wetness move closer together and eventually cross as reservoir hydrocarbon
        becomes denser in transition from gas to oil. """)
st.write("""
The interpretations are as follows:

- Bh > 100 → Very light, dry gas which is almost certainly non-productive  
- Bh < 100 → Increasing liquid content  
- Bh ≈ Wh → Transition zone  
""")

st.subheader("Character (Ch) Analysis")

st.write("""The character (Ch) is evaluated by excluding the lighter hydrocarbon components—methane (C1) and ethane (C2)—and focusing on the heavier fractions. 
        This approach helps confirm the presence of a denser hydrocarbon fluid and aids in distinguishing between a very wet gas and a high-gravity oil. 
        \nThe significance of comparing these heavier components lies in their distribution: propane (C3) is typically more dominant in gas reservoirs, 
        while butanes (C4) and pentanes (C5) are present only in trace or minimal amounts. As fluid density increases, the concentration of all heavier components rises.
        However, in the case of light oils, C4 and C5 tend to increase proportionally, providing a key indicator for fluid characterization.
        \nIf Ch< 0.5 With C3 the major component, the presence of a productive gas phase is confirmed, indicating either wet gas or gas condensate.
        \nIf Ch> 0.5, the presence of a productive liquid phase is confirmed, so that the gas indicated by the wetness ratio is associated with light oil.
         """)
st.table({
    "Condition": ["Ch < 0.5", "Ch > 0.5"],
    "Interpretation": [
        "Gas phase (wet gas / condensate)",
        "Liquid phase (oil)"
    ]
})

st.subheader("Combined Interpretation")

st.table({
    "Balance Ratio": [
        "> 100",
        "< 100",
        "Wh< Bh < 100",
        "Bh < Wh",
        "Bh < Wh",
        "Bh << Wh",
        ""
    ],
    "Wetness Ratio": [
        "",
        "< 0.5",
        "0.5- 17.5",
        "0.5- 17.5",
        "17.5 - 40",
        "17.5 - 40",
        "> 40"
    ],
    "Interpretation": [
        "Very light, dry gas Typically non-associated and non-productive such as the occurrence of high pressured methane, metagenic cracking out of the oil window, bacterial methane etc. ",
        "Possible production of light, dry gas ",
        "Productive gas, increasing in wetness as the curves are closer together",
        "Productive, very wet gas or condensate or high gravity oil with high GOR (Bh<Wh indicates liquid, but Wh still indicates gas) ",
        "Productive oil with decreasing gravity as the curve separation increases ",
        "Lower production potential of low gravity, low gas saturation oil",
        "Very low gravity or residual oil"
    ]
})
