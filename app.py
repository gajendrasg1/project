"""
Smart Question Paper Creator - Flask App
Generates question papers based on topics
"""
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


def expand_abbreviation(topic):
    """Expand common abbreviations to their full form"""
    abbreviations = {
        'ai': 'Artificial Intelligence',
        'ml': 'Machine Learning',
        'dl': 'Deep Learning',
        'dbms': 'Database Management System',
        'sql': 'Structured Query Language',
        'ds': 'Data Structures',
        'oops': 'Object Oriented Programming System',
        'dsa': 'Data Structures and Algorithms',
        'os': 'Operating System',
        'cn': 'Computer Networks',
        'cd': 'Compiler Design',
        'web': 'Web Development',
        'iot': 'Internet of Things',
        'api': 'Application Programming Interface',
        'http': 'HyperText Transfer Protocol',
        'json': 'JavaScript Object Notation',
        'rest': 'Representational State Transfer',
        'mvc': 'Model View Controller',
        'orm': 'Object Relational Mapping',
        'crud': 'Create Read Update Delete',
        'ci/cd': 'Continuous Integration/Continuous Deployment'
    }
    
    topic_lower = topic.lower().strip()
    return abbreviations.get(topic_lower, topic)


def generate_questions(topic):
    """Generate easy, medium, and hard questions for a topic"""
    # Expand abbreviations to full forms
    full_topic = expand_abbreviation(topic)
    
    easy_questions = [
        f"What is {full_topic}?",
        f"Define {full_topic}.",
        f"List the main characteristics of {full_topic}.",
        f"Explain the importance of {full_topic}.",
        f"What are the basic concepts of {full_topic}?"
    ]
    
    medium_questions = [
        f"Describe the key features and applications of {full_topic}.",
        f"Compare and contrast different aspects of {full_topic}.",
        f"Explain the working principle of {full_topic} with examples.",
        f"What are the advantages and disadvantages of {full_topic}?",
        f"How does {full_topic} relate to real-world scenarios?"
    ]
    
    hard_questions = [
        f"Analyze the complex relationships in {full_topic} and provide detailed explanations.",
        f"Design a solution using {full_topic} for a given problem scenario.",
        f"Evaluate different approaches to {full_topic} and justify your choice.",
        f"Critically examine the limitations and future scope of {full_topic}.",
        f"Create a comprehensive framework for implementing {full_topic} effectively."
    ]
    
    return easy_questions[:2], medium_questions[:2], hard_questions[:2]


@app.route('/', methods=['GET', 'POST'])
def index():
    """Serve the main page and handle form submission"""
    easy = None
    medium = None
    hard = None
    
    if request.method == 'POST':
        topic = request.form.get('topic', '').strip()
        if topic:
            easy, medium, hard = generate_questions(topic)
    
    return render_template('index.html', easy=easy, medium=medium, hard=hard)


@app.route('/api/hello')
def hello():
    """API endpoint that returns a greeting"""
    return jsonify(message="Hello from Flask!")


@app.route('/api/data')
def get_data():
    """API endpoint that returns sample data"""
    data = {
        "items": [
            {"id": 1, "name": "Item 1"},
            {"id": 2, "name": "Item 2"},
            {"id": 3, "name": "Item 3"}
        ]
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
