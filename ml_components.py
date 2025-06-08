import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
import os

class MLJobAnalyzer(JobAnalyzer):
    def __init__(self, model_path='models'):
        super().__init__()
        self.model_path = model_path
        os.makedirs(model_path, exist_ok=True)
        self.vectorizer = TfidfVectorizer(max_features=1000)
        self.exp_classifier = None
        self.skill_ner_model = None
        self.load_or_train_models()
        
    def load_or_train_models(self):
        """Load existing models or train new ones"""
        try:
            self.exp_classifier = joblib.load(f'{self.model_path}/exp_classifier.pkl')
            self.vectorizer = joblib.load(f'{self.model_path}/vectorizer.pkl')
            print("Loaded pre-trained models")
        except:
            print("Training new models...")
            self.train_experience_classifier()
            
    def train_experience_classifier(self):
        """Train or retrain the experience level classifier"""
        # Sample labeled data (in practice, use a real dataset)
        data = [
            ("0-2 years of experience required", "entry"),
            ("junior developer position", "entry"),
            ("3-5 years in software development", "mid"),
            ("senior engineer with 5+ years", "senior"),
            ("VP of Engineering", "executive")
        ]
        df = pd.DataFrame(data, columns=['text', 'level'])
        
        # Vectorize text
        X = self.vectorizer.fit_transform(df['text'])
        y = df['level']
        
        # Train classifier
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        self.exp_classifier = RandomForestClassifier()
        self.exp_classifier.fit(X_train, y_train)
        
        # Save models
        joblib.dump(self.exp_classifier, f'{self.model_path}/exp_classifier.pkl')
        joblib.dump(self.vectorizer, f'{self.model_path}/vectorizer.pkl')
        
    def ml_determine_experience_level(self, text):
        """Use ML model to predict experience level"""
        if not self.exp_classifier:
            return self.determine_experience_level(text)
            
        vec = self.vectorizer.transform([text])
        return self.exp_classifier.predict(vec)[0]
    
    def extract_skills_with_ml(self, text):
        """Enhanced skill extraction using ML/NER"""
        doc = nlp(text)
        skills = set()
        
        # Pattern-based extraction (original)
        skills.update(super().extract_skills(text))
        
        # NER-based extraction
        for ent in doc.ents:
            if ent.label_ in ["SKILL", "TECH"]:  # Assuming custom NER model
                skills.add(ent.text)
                
        # Filter and clean
        return [s for s in skills if len(s.split()) <= 3 and not any(w in self.stop_words for w in s.split())]