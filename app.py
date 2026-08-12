import streamlit as st
import pandas as pd
import plotly.express as px

px.defaults.template = "plotly_white"

st.set_page_config(
    page_title="Factory Reallocation Dashboard",
    layout="wide"
)

st.markdown("""
<style>

/* ==============================
   MAIN BACKGROUND
   ============================== */

.stApp {
    background-color: #EEF3F8 !important;
}

[data-testid="stAppViewContainer"] {
    background-color: #EEF3F8 !important;
}


/* ==============================
   SIDEBAR
   ============================== */

[data-testid="stSidebar"] {
    background-color: #0B2545 !important;
}

[data-testid="stSidebar"] * {
    color: white !important;
}


/* ==============================
   SIDEBAR OPEN / CLOSE BUTTON
   ============================== */

/* Streamlit sidebar button */
[data-testid="stSidebarCollapsedControl"],
[data-testid="stSidebarCollapseButton"] {
    background-color: #0B2545 !important;
    border-radius: 8px !important;
    border: 1px solid #163B63 !important;
}

/* Button itself */
[data-testid="stSidebarCollapsedControl"] button,
[data-testid="stSidebarCollapseButton"] button {
    background-color: #0B2545 !important;
    color: white !important;
}

/* Arrow icon */
[data-testid="stSidebarCollapsedControl"] svg,
[data-testid="stSidebarCollapseButton"] svg {
    color: white !important;
    fill: white !important;
    stroke: white !important;
}


/* ==============================
   HEADINGS
   ============================== */

h1 {
    color: #102A43 !important;
}

h2, h3 {
    color: #102A43 !important;
}


/* ==============================
   KPI CARDS
   ============================== */

[data-testid="stMetric"] {
    background-color: white !important;
    border-radius: 12px !important;
    padding: 18px !important;
    border: 1px solid #D9E2EC !important;
    box-shadow: 0px 3px 10px rgba(0,0,0,0.08) !important;
}

[data-testid="stMetricLabel"] {
    color: #52606D !important;
}

[data-testid="stMetricValue"] {
    color: #102A43 !important;
}


/* ==============================
   DIVIDERS
   ============================== */

hr {
    border-color: #D9E2EC !important;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<h1 style="
    color:#102A43;
    font-size:38px;
    font-weight:700;
    margin-bottom:5px;
">
🏭 Factory Reallocation & Shipping Optimization System
</h1>

<p style="
    color:#52606D;
    font-size:18px;
    margin-top:0px;
    margin-bottom:5px;
">
📦 Nassau Candy Distributor Dashboard
</p>

<p style="
    color:#7B8794;
    font-size:14px;
    margin-top:0px;
">
Analyze Sales • Profit • Lead Time • Shipping • Risk • Factory Performance
</p>
""", unsafe_allow_html=True)

df = pd.read_excel("Final_Nassau_Candy_Predictions.xlsx")

st.success("✅ Dataset Loaded Successfully!")


st.sidebar.title("⚙ Dashboard Filters")

st.sidebar.markdown("---")

st.sidebar.markdown("### 📋 Project")

st.sidebar.info("""
Factory Reallocation &
Shipping Optimization

Nassau Candy Distributor
""")

selected_region = st.sidebar.selectbox(
    "Select Region",
    ["All"] + sorted(df["Region"].dropna().unique().tolist())
)

selected_factory = st.sidebar.selectbox(
    "Select Factory",
    ["All"] + sorted(df["Factory"].dropna().unique().tolist())
)

selected_shipmode = st.sidebar.selectbox(
    "Select Ship Mode",
    ["All"] + sorted(df["Ship Mode"].dropna().unique().tolist())
)

selected_year = st.sidebar.selectbox(
    "Select Order Year",
    ["All"] + sorted(df["Order Year"].dropna().unique().tolist())
)

filtered_df = df.copy()

if selected_region != "All":
    filtered_df = filtered_df[filtered_df["Region"] == selected_region]

if selected_factory != "All":
    filtered_df = filtered_df[filtered_df["Factory"] == selected_factory]

if selected_shipmode != "All":
    filtered_df = filtered_df[filtered_df["Ship Mode"] == selected_shipmode]

if selected_year != "All":
    filtered_df = filtered_df[filtered_df["Order Year"] == selected_year]

st.markdown(
"""
<h2 style="
color:#102A43;
font-size:22px;
font-weight:700;
margin-top:20px;
">
📊 Key Performance Indicators
</h2>
""",
unsafe_allow_html=True
)

total_orders = filtered_df["Order ID"].nunique()

total_sales = filtered_df["Sales"].sum()

total_profit = filtered_df["Gross Profit"].sum()

average_lead_time = filtered_df["Lead Time (Days)"].mean()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("📦 Total Orders", total_orders)

with col2:
    st.metric("💰 Total Sales", f"${total_sales:,.2f}")

with col3:
    st.metric("📈 Total Profit", f"${total_profit:,.2f}")

with col4:
    st.metric("⏱️ Avg Lead Time", f"{average_lead_time:.2f} Days")
st.divider()

st.markdown(
    """
    <div style="
        margin-top:8px;
        margin-bottom:14px;
        color:#102A43;
        font-size:22px;
        font-weight:700;
    ">
        📌 Key Insights
    </div>
    """,
    unsafe_allow_html=True
)

sales_region = (
    filtered_df.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

top_sales_region = sales_region.index[0]
top_sales_value = sales_region.iloc[0]

profit_factory = (
    filtered_df.groupby("Factory")["Gross Profit"]
    .sum()
    .sort_values(ascending=False)
)

top_profit_factory = profit_factory.index[0]
top_profit_value = profit_factory.iloc[0]

lead_factory = (
    filtered_df.groupby("Factory")["Lead Time (Days)"]
    .mean()
    .sort_values(ascending=False)
)

highest_lead_factory = lead_factory.index[0]
highest_lead_time = lead_factory.iloc[0]

slow_orders = (
    filtered_df[filtered_df["Shipping Speed"].astype(str).str.lower() == "slow"]
    ["Order ID"].nunique()
)

high_risk_orders = (
    filtered_df[filtered_df["Risk Level"].astype(str).str.lower() == "high"]
    ["Order ID"].nunique()
)

insight1, insight2 = st.columns(2)

with insight1:
    st.markdown(
        f"""
        <div style="
            background:#FFFFFF;
            border:1px solid #E2E8F0;
            border-left:4px solid #2563EB;
            border-radius:10px;
            padding:13px 16px;
            margin-bottom:10px;
        ">
            <div style="color:#102A43;font-weight:600;font-size:14px;">
                🏆 Sales Performance
            </div>
            <div style="color:#64748B;font-size:13px;margin-top:5px;">
                <b style="color:#1E3A5F;">{top_sales_region}</b>
                generates the highest sales in the current filtered data
                (${top_sales_value:,.2f}).
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with insight2:
    st.markdown(
        f"""
        <div style="
            background:#FFFFFF;
            border:1px solid #E2E8F0;
            border-left:4px solid #0F766E;
            border-radius:10px;
            padding:13px 16px;
            margin-bottom:10px;
        ">
            <div style="color:#102A43;font-weight:600;font-size:14px;">
                🏭 Profitability
            </div>
            <div style="color:#64748B;font-size:13px;margin-top:5px;">
                <b style="color:#1E3A5F;">{top_profit_factory}</b>
                records the highest gross profit
                (${top_profit_value:,.2f}).
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

insight3, insight4 = st.columns(2)

with insight3:
    st.markdown(
        f"""
        <div style="
            background:#FFFFFF;
            border:1px solid #E2E8F0;
            border-left:4px solid #D97706;
            border-radius:10px;
            padding:13px 16px;
            margin-bottom:10px;
        ">
            <div style="color:#102A43;font-weight:600;font-size:14px;">
                ⏱️ Lead Time Alert
            </div>
            <div style="color:#64748B;font-size:13px;margin-top:5px;">
                <b style="color:#1E3A5F;">{highest_lead_factory}</b>
                has the highest average lead time
                ({highest_lead_time:,.2f} days) and may require review.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with insight4:
    st.markdown(
        f"""
        <div style="
            background:#FFFFFF;
            border:1px solid #E2E8F0;
            border-left:4px solid #DC2626;
            border-radius:10px;
            padding:13px 16px;
            margin-bottom:32px;
        ">
            <div style="color:#102A43;font-weight:600;font-size:14px;">
                🚚 Shipping & Risk
            </div>
            <div style="color:#64748B;font-size:13px;margin-top:5px;">
                <b style="color:#1E3A5F;">{slow_orders:,}</b>
                slow-shipping orders and
                <b style="color:#1E3A5F;">{high_risk_orders:,}</b>
                high-risk orders are present in the current filtered data.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.header("📊 Sales & Profit Analysis")

chart1, chart2 = st.columns(2)

sales_by_region = (
    filtered_df.groupby("Region")["Sales"]
    .sum()
    .reset_index()
)

fig_region = px.bar(
    sales_by_region,
    x="Region",
    y="Sales",
    title="Sales by Region"
)

fig_region.update_traces(
    marker_color="#2563EB"
)
fig_region.update_traces(
    hovertemplate="<b>Region:</b> %{x}<br><b>Sales:</b> $%{y:,.2f}<extra></extra>"
) 

fig_region.update_layout(
    template="plotly_white",
    paper_bgcolor="#FFFFFF",
    plot_bgcolor="#FFFFFF",
    font=dict(
        family="Arial",
        size=13,
        color="#1F2937"
    ),
    title=dict(
        font=dict(
            family="Arial",
            size=19,
            color="#0F172A"
        ),
        x=0.02
    ),
    xaxis=dict(
        title="Region",
        title_font=dict(color="#374151"),
        tickfont=dict(color="#374151"),
        showgrid=False
    ),
    yaxis=dict(
        title="Sales",
        title_font=dict(color="#374151"),
        tickfont=dict(color="#374151"),
        gridcolor="#E5E7EB"
    ),
    margin=dict(l=20, r=20, t=60, b=30)
)

with chart1:
    st.plotly_chart(
        fig_region,
        use_container_width=True,
        config={"displayModeBar": False}
    )

profit_by_factory = (
    filtered_df.groupby("Factory")["Gross Profit"]
    .sum()
    .reset_index()
)

fig_factory = px.bar(
    profit_by_factory,
    x="Factory",
    y="Gross Profit",
    title="Gross Profit by Factory"
)

fig_factory.update_traces(
    marker_color="#315A8A"
)
fig_factory.update_traces(
    hovertemplate="<b>Factory:</b> %{x}<br><b>Gross Profit:</b> $%{y:,.2f}<extra></extra>"
)

fig_factory.update_layout(
    template="plotly_white",
    paper_bgcolor="#FFFFFF",
    plot_bgcolor="#FFFFFF",
    font=dict(
        family="Arial",
        size=13,
        color="#1F2937"
    ),
    title=dict(
        font=dict(
            family="Arial",
            size=19,
            color="#0F172A"
        ),
        x=0.02
    ),
    xaxis=dict(
        title="Factory",
        title_font=dict(color="#374151"),
        tickfont=dict(color="#374151"),
        showgrid=False
    ),
    yaxis=dict(
        title="Gross Profit",
        title_font=dict(color="#374151"),
        tickfont=dict(color="#374151"),
        gridcolor="#E5E7EB"
    ),
    margin=dict(l=20, r=20, t=60, b=30)
)

with chart2:
    st.plotly_chart(
        fig_factory,
        use_container_width=True,
        config={"displayModeBar": False}
    )

st.divider()

chart3, chart4 = st.columns(2)

sales_shipmode = (
    filtered_df.groupby("Ship Mode")["Sales"]
    .sum()
    .reset_index()
)

fig_shipmode = px.pie(
    sales_shipmode,
    names="Ship Mode",
    values="Sales",
    title="Sales by Ship Mode",
    color_discrete_sequence=[
    "#1E3A5F",
    "#2563EB",
    "#3B82F6",
    "#60A5FA"
]
)
fig_shipmode.update_traces(
    hovertemplate="<b>Ship Mode:</b> %{label}<br><b>Sales:</b> $%{value:,.2f}<extra></extra>"
)

fig_shipmode.update_layout(
    template="plotly_white",
    paper_bgcolor="#FFFFFF",
    plot_bgcolor="#FFFFFF",
    font=dict(
        family="Arial",
        size=13,
        color="#1F2937"
    ),
    title=dict(
        font=dict(
            family="Arial",
            size=19,
            color="#0F172A"
        ),
        x=0.02
    ),
    margin=dict(l=20, r=20, t=60, b=30)
)

with chart3:
    st.plotly_chart(
        fig_shipmode,
        use_container_width=True,
        config={"displayModeBar": False}
    )

risk_data = (
    filtered_df.groupby("Risk Level")
    .size()
    .reset_index(name="Count")
)

fig_risk = px.bar(
    risk_data,
    x="Risk Level",
    y="Count",
    title="Risk Level Distribution",
    color="Risk Level",
    color_discrete_map={
    "Low": "#60A5FA",
    "Medium": "#3B82F6",
    "High": "#1E3A5F"
}
)
fig_risk.update_traces(
    hovertemplate="<b>Risk Level:</b> %{x}<br><b>Orders:</b> %{y:,}<extra></extra>"
)

fig_risk.update_layout(
    template="plotly_white",
    paper_bgcolor="#FFFFFF",
    plot_bgcolor="#FFFFFF",
    font=dict(
        family="Arial",
        size=13,
        color="#1F2937"
    ),
    title=dict(
        font=dict(
            family="Arial",
            size=19,
            color="#0F172A"
        ),
        x=0.02
    ),
    xaxis=dict(
        title="Risk Level",
        title_font=dict(color="#374151"),
        tickfont=dict(color="#374151"),
        showgrid=False
    ),
    yaxis=dict(
        title="Number of Orders",
        title_font=dict(color="#374151"),
        tickfont=dict(color="#374151"),
        gridcolor="#E5E7EB"
    ),
    showlegend=False,
    margin=dict(l=20, r=20, t=60, b=30)
)

with chart4:
    st.plotly_chart(
        fig_risk,
        use_container_width=True,
        config={"displayModeBar": False}
    )

st.divider()

chart5, chart6 = st.columns(2)

recommendation_data = (
    filtered_df.groupby("Recommendation Status")
    .size()
    .reset_index(name="Count")
)

fig_recommendation = px.pie(
    recommendation_data,
    names="Recommendation Status",
    values="Count",
    title="Recommendation Status",
    color_discrete_sequence=[
    "#4A90E2",
    "#4B5F8F",
    "#F5C518"
]
)
fig_recommendation.update_traces(
    hovertemplate="<b>Status:</b> %{label}<br><b>Orders:</b> %{value:,}<extra></extra>"
)

fig_recommendation.update_layout(
    template="plotly_white",
    paper_bgcolor="#FFFFFF",
    plot_bgcolor="#FFFFFF",
    font=dict(
        family="Arial",
        size=13,
        color="#1F2937"
    ),
    title=dict(
        font=dict(
            family="Arial",
            size=19,
            color="#0F172A"
        ),
        x=0.02
    ),
    margin=dict(l=20, r=20, t=60, b=30)
)

with chart5:
    st.plotly_chart(
        fig_recommendation,
        use_container_width=True,
        config={"displayModeBar": False}
    )

leadtime_factory = (
    filtered_df.groupby("Factory")["Lead Time (Days)"]
    .mean()
    .reset_index()
)

fig_leadtime = px.bar(
    leadtime_factory,
    x="Factory",
    y="Lead Time (Days)",
    title="Average Lead Time by Factory"
)

fig_leadtime.update_traces(
    marker_color="#1E3A5F"
)
fig_leadtime.update_traces(
    hovertemplate="<b>Factory:</b> %{x}<br><b>Avg Lead Time:</b> %{y:.2f} days<extra></extra>"
)

fig_leadtime.update_layout(
    template="plotly_white",
    paper_bgcolor="#FFFFFF",
    plot_bgcolor="#FFFFFF",
    font=dict(
        family="Arial",
        size=13,
        color="#1F2937"
    ),
    title=dict(
        font=dict(
            family="Arial",
            size=19,
            color="#0F172A"
        ),
        x=0.02
    ),
    xaxis=dict(
        title="Factory",
        title_font=dict(color="#374151"),
        tickfont=dict(color="#374151"),
        showgrid=False
    ),
    yaxis=dict(
        title="Average Lead Time (Days)",
        title_font=dict(color="#374151"),
        tickfont=dict(color="#374151"),
        gridcolor="#E5E7EB"
    ),
    margin=dict(l=20, r=20, t=60, b=30)
)

with chart6:
    st.plotly_chart(
        fig_leadtime,
        use_container_width=True,
        config={"displayModeBar": False}
    )

st.markdown("""
<h2 style="
    color:#102A43;
    font-size:28px;
    font-weight:700;
    margin-top:25px;
    margin-bottom:18px;
">
🎯 Optimization Recommendation
</h2>
""", unsafe_allow_html=True)

high_risk_orders = filtered_df[
    filtered_df["Risk Level"] == "High"
].shape[0]

slow_shipping_orders = filtered_df[
    filtered_df["Shipping Speed"] == "Slow"
].shape[0]

current_avg_lead_time = filtered_df[
    "Lead Time (Days)"
].mean()

rec1, rec2, rec3 = st.columns(3)

with rec1:
    st.markdown(
        f'<div style="background:#FFFFFF;border:1px solid #E2E8F0;border-left:5px solid #DC2626;border-radius:12px;padding:18px 20px;box-shadow:0 3px 10px rgba(15,23,42,0.06);min-height:115px;">'
        f'<div style="color:#64748B;font-size:14px;font-weight:600;margin-bottom:8px;">🔴 High-Risk Orders</div>'
        f'<div style="color:#102A43;font-size:28px;font-weight:700;">{high_risk_orders:,}</div>'
        f'<div style="color:#94A3B8;font-size:12px;margin-top:5px;">Orders requiring attention</div>'
        f'</div>',
        unsafe_allow_html=True
    )

with rec2:
    st.markdown(
        f'<div style="background:#FFFFFF;border:1px solid #E2E8F0;border-left:5px solid #D97706;border-radius:12px;padding:18px 20px;box-shadow:0 3px 10px rgba(15,23,42,0.06);min-height:115px;">'
        f'<div style="color:#64748B;font-size:14px;font-weight:600;margin-bottom:8px;">🟠 Slow-Shipping Orders</div>'
        f'<div style="color:#102A43;font-size:28px;font-weight:700;">{slow_shipping_orders:,}</div>'
        f'<div style="color:#94A3B8;font-size:12px;margin-top:5px;">Orders with slow shipping</div>'
        f'</div>',
        unsafe_allow_html=True
    )

with rec3:
    st.markdown(
        f'<div style="background:#FFFFFF;border:1px solid #E2E8F0;border-left:5px solid #2563EB;border-radius:12px;padding:18px 20px;box-shadow:0 3px 10px rgba(15,23,42,0.06);min-height:115px;">'
        f'<div style="color:#64748B;font-size:14px;font-weight:600;margin-bottom:8px;">⏱ Average Lead Time</div>'
        f'<div style="color:#102A43;font-size:28px;font-weight:700;">{current_avg_lead_time:,.2f}</div>'
        f'<div style="color:#94A3B8;font-size:12px;margin-top:5px;">Current filtered average • Days</div>'
        f'</div>',
        unsafe_allow_html=True
    )

st.markdown(f"""
<div style="
    margin-top:18px;
    background:#FFF8E7;
    border:1px solid #F3D58A;
    border-left:5px solid #D97706;
    border-radius:10px;
    padding:16px 20px;
    color:#334155;
    font-size:14px;
    line-height:1.6;
">
    <b style="color:#92400E;">⚠ Attention Required</b><br>
    <span style="color:#475569;">
        {high_risk_orders:,} high-risk orders and 
        {slow_shipping_orders:,} slow-shipping orders were identified.
        These orders should be reviewed for possible factory reallocation
        and shipping optimization.
    </span>
</div>
""", unsafe_allow_html=True)


st.markdown("<div style='height:1px;'></div>", unsafe_allow_html=True)

st.markdown("<div style='height:8px;'></div>", unsafe_allow_html=True)

st.markdown(
    """
    <h2 style="
        color:#102A43;
        font-size:28px;
        font-weight:700;
        margin-bottom:6px;
    ">
        🔄 Factory Reallocation Scenario
    </h2>
    <p style="
        color:#64748B;
        font-size:14px;
        margin-top:0px;
        margin-bottom:18px;
    ">
        Compare the current factory with another factory to evaluate a potential
        reallocation scenario.
    </p>
    """,
    unsafe_allow_html=True
)

factory_options = sorted(df["Factory"].dropna().unique().tolist())

sim_col1, sim_col2 = st.columns(2)

with sim_col1:
    current_factory = st.selectbox(
        "Current Factory",
        factory_options,
        key="scenario_current_factory"
    )

with sim_col2:
    target_options = [
        f for f in factory_options
        if f != current_factory
    ]

    target_factory = st.selectbox(
        "Potential New Factory",
        target_options,
        key="scenario_target_factory"
    )

current_data = df[df["Factory"] == current_factory]
target_data = df[df["Factory"] == target_factory]

current_orders = current_data["Order ID"].nunique()
target_orders = target_data["Order ID"].nunique()

current_lead = current_data["Lead Time (Days)"].mean()
target_lead = target_data["Lead Time (Days)"].mean()

current_margin = current_data["Profit Margin %"].mean()
target_margin = target_data["Profit Margin %"].mean()


lead_time_change = current_lead - target_lead
margin_change = target_margin - current_margin

st.markdown("<div style='height:12px;'></div>", unsafe_allow_html=True)

sc1, sc2, sc3, sc4 = st.columns(4)

with sc1:
    st.markdown(
        f"""
        <div style="
            background:#FFFFFF;
            border:1px solid #E2E8F0;
            border-left:5px solid #1E3A5F;
            border-radius:12px;
            padding:16px 18px;
            min-height:105px;
            box-shadow:0 3px 10px rgba(15,23,42,0.06);
        ">
            <div style="color:#64748B;font-size:13px;font-weight:600;">
                📦 Current Orders
            </div>
            <div style="color:#102A43;font-size:26px;font-weight:700;margin-top:7px;">
                {current_orders:,}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with sc2:
    st.markdown(
        f"""
        <div style="
            background:#FFFFFF;
            border:1px solid #E2E8F0;
            border-left:5px solid #2563EB;
            border-radius:12px;
            padding:16px 18px;
            min-height:105px;
            box-shadow:0 3px 10px rgba(15,23,42,0.06);
        ">
            <div style="color:#64748B;font-size:13px;font-weight:600;">
                ⏱ Lead Time Change
            </div>
            <div style="color:#102A43;font-size:26px;font-weight:700;margin-top:7px;">
                {lead_time_change:+,.2f} days
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with sc3:
    st.markdown(
        f"""
        <div style="
            background:#FFFFFF;
            border:1px solid #E2E8F0;
            border-left:5px solid #0F766E;
            border-radius:12px;
            padding:16px 18px;
            min-height:105px;
            box-shadow:0 3px 10px rgba(15,23,42,0.06);
        ">
            <div style="color:#64748B;font-size:13px;font-weight:600;">
                📈 Margin Change
            </div>
            <div style="color:#102A43;font-size:26px;font-weight:700;margin-top:7px;">
                {margin_change:+,.2f}%
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with sc4:
    st.markdown(
        f"""
        <div style="
            background:#FFFFFF;
            border:1px solid #E2E8F0;
            border-left:5px solid #64748B;
            border-radius:12px;
            padding:16px 18px;
            min-height:105px;
            box-shadow:0 3px 10px rgba(15,23,42,0.06);
        ">
            <div style="color:#64748B;font-size:13px;font-weight:600;">
                🏭 Target Factory
            </div>
            <div style="
                color:#102A43;
                font-size:18px;
                font-weight:700;
                margin-top:10px;
            ">
                {target_factory}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<div style='height:16px;'></div>", unsafe_allow_html=True)

if lead_time_change > 0 and margin_change >= 0:

    st.success(
        f"Recommended Scenario: Reallocate selected orders from "
        f"**{current_factory}** to **{target_factory}**. "
        f"The target factory currently shows lower average lead time "
        f"and a comparable or better profit margin."
    )

elif lead_time_change > 0:

    st.info(
        f"Potential Shipping Improvement: **{target_factory}** shows a lower "
        f"average lead time than **{current_factory}**, but its average "
        f"profit margin is lower."
    )

elif margin_change > 0:

    st.info(
        f"Potential Profitability Improvement: **{target_factory}** shows "
        f"a better average profit margin, although its average lead time "
        f"is not lower."
    )

else:

    st.markdown(
        f"""
        <div style="
            background:#FFF8E7;
            border:1px solid #F3D58A;
            border-left:5px solid #D97706;
            border-radius:10px;
            padding:15px 20px;
            margin-top:10px;
            color:#334155;
            font-size:15px;
            line-height:1.6;
        ">
            <b style="color:#92400E;">⚠ No Clear Improvement</b><br>
            <span style="color:#475569;">
                No clear improvement was found for reallocating from
                <b style="color:#102A43;">{current_factory}</b>
                to
                <b style="color:#102A43;">{target_factory}</b>
                based on the current factory-level benchmarks.
            </span>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown(
    """
    <div style="
        color:#64748B;
        font-size:13px;
        margin-top:8px;
        margin-bottom:5px;
    ">
        ℹ Scenario results are benchmark estimates based on historical factory performance.
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

st.subheader("📋 Filtered Dataset")

st.markdown("""
<style>
[data-testid="stCheckbox"] label p {
    color: #102A43 !important;
    font-weight: 600 !important;
}
</style>
""", unsafe_allow_html=True)

show_data = st.checkbox("Show Filtered Data")

if show_data:
    st.dataframe(filtered_df, use_container_width=True)

csv_data = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Filtered Dataset",
    data=csv_data,
    file_name="Filtered_Nassau_Candy_Data.csv",
    mime="text/csv"
)

st.divider()

st.markdown("""
<div style="margin-top:30px; padding:18px 10px 12px 10px; border-top:1px solid #D9E2EC; text-align:center;">

<div style="color:#1E3A5F; font-size:14px; font-weight:600; margin-bottom:12px;">
Factory Reallocation & Shipping Optimization System
</div>

<div style="color:#64748B; font-size:12px; margin-bottom:7px;">
Developed using Python • Streamlit • Machine Learning • Power BI
</div>

<div style="color:#1E3A5F; font-size:12px; font-weight:600;">
Developed by Manya | B.Tech IT | GJUST
</div>

<div style="color:#94A3B8; font-size:11px; margin-top:5px;">
B.Tech IT Internship Project
</div>

</div>
""", unsafe_allow_html=True)
