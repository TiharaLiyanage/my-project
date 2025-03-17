from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample hotel data
hotels = [
    {"name": "Cinnamon Red Colombo", "location": "Kollupitiya, Colombo", "price": 15000, "status": "Available", "tags": ["In High Demand", "Great Value"]},
    {"name": "Fairway Colombo", "location": "Fort, Colombo", "price": None, "status": "Sold Out", "tags": ["In High Demand"]}
]

@app.route('/')
def index():
    return render_template('Online_Booking.html', hotels=hotels)

@app.route('/search', methods=['GET'])
def search_hotels():
    query = request.args.get('q', '').lower()
    filtered_hotels = [hotel for hotel in hotels if query in hotel['name'].lower() or query in hotel['location'].lower()]
    return jsonify(filtered_hotels)

if __name__ == '__main__':
    app.run(debug=True)
