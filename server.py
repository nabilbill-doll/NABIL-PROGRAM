from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Inventory API</h1>
    <p>Server berjalan dengan baik.</p>
    <p>Endpoint tersedia:</p>
    <ul>
        <li>/barang (GET)</li>
        <li>/barang (POST)</li>
    </ul>
    """

data_barang = []

@app.route("/barang", methods=["GET"])
def get_barang():
    return jsonify(data_barang)

@app.route("/barang", methods=["POST"])
def tambah_barang():
    data = request.json
    data_barang.append(data)
    return jsonify({"message": "Barang ditambahkan"})


if __name__ == "__main__":
    app.run(debug=True)
    
