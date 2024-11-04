import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from datetime import datetime

# Set page configuration
st.set_page_config(
    page_title="SAS Analytics Tools Explorer",
    page_icon="📊",
    layout="wide"
)

# Define the main tools and their descriptions
sas_tools = {
    "SAS Base": {
        "description": "The core module of SAS, providing extensive data manipulation techniques and sophisticated statistical algorithms.",
        "key_features": ["Data Management", "Statistical Analysis", "Report Writing", "Programming Interface"],
        "use_cases": ["Data Cleaning", "Basic Statistics", "Custom Reports", "Data Transformation"]
    },
    "SAS Enterprise Guide": {
        "description": "A user-friendly, point-and-click Windows client interface for quick access to SAS analytics.",
        "key_features": ["Visual Interface", "Workflow Designer", "Built-in Tasks", "Project Organization"],
        "use_cases": ["Business Reports", "Statistical Analysis", "Data Exploration", "Process Automation"]
    },
    "SAS Visual Analytics": {
        "description": "A visual analytics software for creating interactive dashboards, reports, and data visualizations.",
        "key_features": ["Interactive Dashboards", "Mobile Support", "Data Discovery", "Smart Visualizations"],
        "use_cases": ["Executive Dashboards", "Self-service Analytics", "Performance Monitoring", "Data Storytelling"]
    },
    "SAS Viya": {
        "description": "A cloud-based platform for artificial intelligence, machine learning, analytics, and data management.",
        "key_features": ["Cloud Native", "Open Source Integration", "Scalable Processing", "Modern Architecture"],
        "use_cases": ["Enterprise AI", "Cloud Analytics", "Real-time Decisions", "Distributed Computing"]
    }
}

def main():
    # Header
    st.title("🔍 SAS Analytics Tools Explorer")
    st.markdown("---")

    # Sidebar
    st.sidebar.title("Navigation")
    page = st.sidebar.radio(
        "Choose a section:",
        ["Overview", "Tool Explorer", "Features Comparison", "Industry Applications", "Demo Analytics"]
    )

    if page == "Overview":
        show_overview()
    elif page == "Tool Explorer":
        show_tool_explorer()
    elif page == "Features Comparison":
        show_features_comparison()
    elif page == "Industry Applications":
        show_industry_applications()
    elif page == "Demo Analytics":
        show_demo_analytics()

def show_overview():
    st.header("SAS Data Analytics Platform Overview")
    st.write("""
    SAS (Statistical Analysis System) is a comprehensive data analytics platform that provides
    a wide range of tools for data management, statistical analysis, and business intelligence.
    """)

    # Key benefits
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Key Benefits")
        benefits = [
            "📊 Comprehensive Statistical Analysis",
            "🎯 Advanced Data Visualization",
            "🤖 Integrated Machine Learning",
            "☁️ Cloud-Based Deployment",
            "🔄 Open Source Interoperability"
        ]
        for benefit in benefits:
            st.write(benefit)

    with col2:
        st.subheader("Industry Applications")
        industries = [
            "💼 Business Intelligence",
            "⚠️ Risk Management",
            "🌍 Environmental Analytics",
            "📱 Social Media Analytics",
            "🏥 Healthcare Analytics"
        ]
        for industry in industries:
            st.write(industry)

def show_tool_explorer():
    st.header("SAS Tools Explorer")
    
    selected_tool = st.selectbox("Select a SAS tool to explore:", list(sas_tools.keys()))
    
    if selected_tool:
        tool_info = sas_tools[selected_tool]
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.subheader(f"About {selected_tool}")
            st.write(tool_info["description"])
            
            st.subheader("Key Features")
            for feature in tool_info["key_features"]:
                st.write(f"• {feature}")
        
        with col2:
            st.subheader("Common Use Cases")
            for use_case in tool_info["use_cases"]:
                st.write(f"📌 {use_case}")

def show_features_comparison():
    st.header("Features Comparison")
    
    # Create comparison matrix
    features = ["Statistical Analysis", "Data Visualization", "Machine Learning", 
                "Cloud Support", "Open Source Integration"]
    
    comparison_data = {
        "SAS Base": [True, False, False, False, False],
        "SAS Enterprise Guide": [True, True, False, False, False],
        "SAS Visual Analytics": [True, True, False, True, True],
        "SAS Viya": [True, True, True, True, True]
    }
    
    df_comparison = pd.DataFrame(comparison_data, index=features)
    
    # Display interactive comparison
    st.dataframe(df_comparison.style.applymap(lambda x: 'background-color: #90EE90' if x else 'background-color: #FFB6C1'))

def show_industry_applications():
    st.header("Industry Applications")
    
    industries = {
        "Business Intelligence": {
            "icon": "💼",
            "applications": ["Data Warehousing", "ETL Processes", "Reporting", "Analytics"],
            "popularity": 85
        },
        "Risk Management": {
            "icon": "⚠️",
            "applications": ["Credit Risk", "Market Risk", "Operational Risk", "Compliance"],
            "popularity": 75
        },
        "Environmental Analytics": {
            "icon": "🌍",
            "applications": ["Deforestation Monitoring", "Climate Analysis", "Resource Management"],
            "popularity": 60
        },
        "Social Media Analytics": {
            "icon": "📱",
            "applications": ["Sentiment Analysis", "Trend Monitoring", "Engagement Tracking"],
            "popularity": 70
        }
    }
    
    # Create and display industry popularity chart
    industry_data = pd.DataFrame({
        "Industry": industries.keys(),
        "Popularity": [ind["popularity"] for ind in industries.values()]
    })
    
    fig = px.bar(industry_data, x="Industry", y="Popularity",
                 title="Industry Adoption of SAS Analytics",
                 labels={"Popularity": "Adoption Rate (%)"},
                 color="Industry")
    
    st.plotly_chart(fig)
    
    # Display detailed information
    for industry, details in industries.items():
        with st.expander(f"{details['icon']} {industry}"):
            st.write("Common Applications:")
            for app in details["applications"]:
                st.write(f"• {app}")

def show_demo_analytics():
    st.header("Demo Analytics Dashboard")
    
    # Generate sample data
    dates = pd.date_range(start="2024-01-01", end="2024-12-31", freq="M")
    data = pd.DataFrame({
        "Date": dates,
        "Sales": np.random.normal(1000, 200, len(dates)),
        "Customers": np.random.normal(500, 100, len(dates)),
        "Satisfaction": np.random.uniform(3.5, 5, len(dates))
    })
    
    # Interactive charts
    metric_choice = st.selectbox("Select metric to visualize:", 
                               ["Sales", "Customers", "Satisfaction"])
    
    fig = px.line(data, x="Date", y=metric_choice,
                  title=f"{metric_choice} Trend Analysis")
    st.plotly_chart(fig)
    
    # Summary statistics
    st.subheader("Summary Statistics")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Average Sales", f"${data['Sales'].mean():,.0f}")
    with col2:
        st.metric("Total Customers", f"{data['Customers'].sum():,.0f}")
    with col3:
        st.metric("Avg Satisfaction", f"{data['Satisfaction'].mean():.1f}/5.0")

if __name__ == "__main__":
    main()
