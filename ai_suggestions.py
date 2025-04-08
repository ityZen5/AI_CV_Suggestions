from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_improvement_suggestions(cv_data, job_description):
    # Combine CV sections for analysis
    cv_text = " ".join(cv_data['skills'] + cv_data['experiences'])
    
    # Vectorize CV and job description
    vectorizer = TfidfVectorizer()
    texts = [cv_text, job_description]
    tfidf_matrix = vectorizer.fit_transform(texts)
    
    # Calculate similarity score (0-100%)
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0] * 100
    
    # Find missing keywords
    feature_names = vectorizer.get_feature_names_out()
    important_keywords = feature_names[tfidf_matrix[1:2].toarray().argsort()[0][-10:]]  # Top 10 keywords
    
    missing_keywords = [kw for kw in important_keywords if kw not in cv_text.lower()]
    
    # Generate suggestions
    suggestions = {
        'similarity_score': round(similarity, 2),
        'missing_keywords': missing_keywords,
        'general_suggestions': []
    }
    
    if len(cv_data['skills']) < 10:
        suggestions['general_suggestions'].append("⚠️ Add more skills (aim for 10+).")
    
    if len(cv_data['experiences']) == 0:
        suggestions['general_suggestions'].append("⚠️ Include work experience with company names.")
    
    return suggestions