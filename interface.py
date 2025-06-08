from flask import Flask, render_template, request, jsonify
import plotly.express as px
import pandas as pd
from datetime import datetime

app = Flask(__name__)

class JobDashboard:
    def __init__(self, pipeline):
        self.pipeline = pipeline
        self.data = None
        self.last_updated = None
        
    def update_data(self):
        self.data = self.pipeline.run(site_configs)
        self.last_updated = datetime.now()
        
    def get_filtered_jobs(self, filters):
        if not self.data:
            return []
            
        filtered = []
        for job in sum(self.data.values(), []):
            match = True
            if filters.get('experience'):
                match = match and (job.get('experience_level') == filters['experience'])
            if filters.get('skills'):
                match = match and any(skill in job.get('skills', []) for skill in filters['skills'])
            if match:
                filtered.append(job)
        return filtered
        
    def create_visualizations(self):
        df = pd.DataFrame(sum(self.data.values(), []))
        
        # Experience level distribution
        exp_fig = px.pie(df, names='experience_level', title='Experience Level Distribution')
        
        # Top skills
        all_skills = sum(df['skills'].tolist(), [])
        skill_counts = pd.Series(all_skills).value_counts().head(10)
        skill_fig = px.bar(skill_counts, title='Top 10 Required Skills')
        
        return {
            'experience': exp_fig.to_json(),
            'skills': skill_fig.to_json()
        }

# Initialize components
pipeline = JobScrapingPipeline()
dashboard = JobDashboard(pipeline)
dashboard.update_data()

@app.route('/')
def index():
    filters = {
        'experience': request.args.get('experience'),
        'skills': request.args.getlist('skills')
    }
    jobs = dashboard.get_filtered_jobs(filters)
    viz = dashboard.create_visualizations()
    return render_template('dashboard.html', 
                         jobs=jobs,
                         filters=filters,
                         visualizations=viz,
                         last_updated=dashboard.last_updated)

@app.route('/update', methods=['POST'])
def update_jobs():
    dashboard.update_data()
    return jsonify({"status": "success", "last_updated": str(dashboard.last_updated)})

if __name__ == '__main__':
    app.run(debug=True)