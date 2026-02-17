from supabase import create_client
import plotly.graph_objects as go

# Your Supabase credentials
url = "https://gilvijxmudywgcaslfxz.supabase.co"
key = "sb_publishable_3QYyHIXrfZJb5s-DBjnrDg_qSDRVBRd"

# Connect to database
supabase = create_client(url, key)

# Fetch all courses from the table
response = supabase.table("courses").select("*").execute()
courses = response.data

# Extract titles for chart
titles = [course['title'] for course in courses]
counts = [1] * len(titles)  # Simple count (1 per course for now)

# Create bar chart
fig = go.Figure(data=[
    go.Bar(x=titles, y=counts, marker_color='#3ECF8E')
])

fig.update_layout(
    title="Courses in Database",
    xaxis_title="Course Title",
    yaxis_title="Count",
    template="plotly_white"
)

# Save as HTML file
fig.write_html("course_dashboard.html")
print("Dashboard saved as course_dashboard.html")