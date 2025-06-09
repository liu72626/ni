from flask import Flask, request, jsonify
from flask_cors import CORS  # 解决跨域问题

app = Flask(__name__)
CORS(app)  # 允许前端跨域访问

@app.route('/chat', methods=['POST'])
def chat():
    # 获取前端发送的消息
    user_message = request.json.get('message', '')
    
    # 自动回复逻辑（可替换为更复杂的AI模型，如ChatGPT）
    bot_reply = f"已收到：{user_message}"  # 简单回显
    
    return jsonify({ 'reply': bot_reply })

if __name__ == '__main__':
    app.run(debug=True)  # 启动后端服务（默认端口5000）