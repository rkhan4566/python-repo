##put and delete
## working with API's--json

from flask import Flask, jsonify,request
app = Flask(__name__)

##initial data in my to do list
items= [
    {"id": 1, "name": "item1", "description": "this is my item 1"},
    {"id": 2, "name": "item2", "description": "this is my item 2"}
]

@app.route('/')
def home():
    return "welcome to this sample to DO List App"

#get and retreive all items 
@app.route('/items',methods=['GET'])
def get_items():
    return jsonify(items)

## get: retireve a specific item by id
@app.route('/items/<int:item_id>',methods=['GET'])
def get_item(item_id):
    item=next((item for item in items if item["id"]==item_id),None)
    if item is None:
        return jsonify({"error":"item not found"})
    return jsonify(item)

#post :create a new task-API
@app.route('/items',methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error": "items not found"})
    new_item={
         "id": items[-1]["id"] + 1 if items else 1,
         "name":request.json['name'],
         "description":request.json["description"]

    }
    items.append(new_item)
    return jsonify(new_item)

#put : update an existing item
@app.route('/items<int:item_id>',methods=['PUT'])
def update_item(item_id):
    item =next((item for item in items if item["id"] == item_id),None)
    if item is None:
        return jsonify({"error": "item not found"})
    item['name']= request.json.get('name',item['name'])
    item['description']= request.json.get('description',item ['description'])
    return jsonify(item)

##DELETE: delete an item 
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items= [ item for item in items if item["id"] !=item_id]
    return jsonify({"result": "item deleted"})




if __name__=='__main__':
    app.run(debug=True)






