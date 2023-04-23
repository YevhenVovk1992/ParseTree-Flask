import json
import os
import dotenv

from flask import Flask, jsonify, request

from tree import TreeEditor


# Loading environment variables from .env file into the project
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
dotenv.load_dotenv(dotenv_path)

app = Flask(__name__)
app.secret_key = os.environ.get('SESSION_SECRET')


@app.route('/paraphrase', methods=['GET', ])
def paraphrase_text():
    query_params = request.args
    query_params.to_dict()
    tree_str = query_params.get('tree', None)
    limit = query_params.get('limit', None)

    # Check query parameters
    if not tree_str:
        return jsonify({"Error": "Missing required parameter --tree", "status": 400}), 400
    if limit and limit.isdigit():
        limit = int(limit)
    elif limit and not limit.isdigit():
        return jsonify({"Error": "Limit is not integer", "status": 400}), 400

    # Try to create parse tree
    try:
        handler = TreeEditor(tree_str)
    except ValueError:
        return jsonify({"Error": "The string has an invalid structure", "status": 400}), 400
    handler.create_combinations_from_tree(limit)
    trees_list = handler.to_json()
    return jsonify(json.loads(trees_list)), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=os.environ.get('DEBUG'))
