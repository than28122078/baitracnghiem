from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
# Danh sách các câu hỏi và đáp án đúng
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "correct": "Paris"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "correct": "4"
    }
    # Thêm nhiều câu hỏi khác ở đây
]

@app.route('/')
def home():
    return render_template('frontend.html')

@app.route('/get-quiz', methods=['GET'])
def get_quiz():
    return jsonify(quiz_data)

@app.route('/submit-quiz', methods=['POST'])
def submit_quiz():
    user_answers = request.json.get('answers', [])
    score = 0

    # Chấm điểm dựa trên câu trả lời đúng
    for i, answer in enumerate(user_answers):
        if i < len(quiz_data) and answer == quiz_data[i]['correct']:
            score += 1

    # Trả về kết quả dưới dạng JSON
    return jsonify({"score": score, "total": len(quiz_data)})

if __name__ == '__main__':
    app.run(debug=True)
