{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":1,"position":1,"stack":[[{"start":{"row":97,"column":0},"end":{"row":115,"column":20},"action":"insert","lines":["@app.route('/update_recipe_rating/<recipe_id>', methods=['POST'])","def update_recipe_rating(recipe_id):","   ","    recipe = mongo.db.recipes","    ","    this_recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})","    ","    number_of_votes = int(this_recipe['number_of_votes'])","    print('number_of_votes is: ', number_of_votes)","    ","    initial_recipe_rating = int(this_recipe['recipe_rating'])","    print('initial recipe rating is: ',  initial_recipe_rating)","    ","    latest_recipe_rating = int(request.json['recipe_rating'])","    print('latest recipe rating posted is: ', latest_recipe_rating)","    ","  ","    ","    return ('', 204)"],"id":54}],[{"start":{"row":97,"column":0},"end":{"row":97,"column":2},"action":"insert","lines":["# "],"id":55},{"start":{"row":98,"column":0},"end":{"row":98,"column":2},"action":"insert","lines":["# "]},{"start":{"row":100,"column":0},"end":{"row":100,"column":2},"action":"insert","lines":["# "]},{"start":{"row":102,"column":0},"end":{"row":102,"column":2},"action":"insert","lines":["# "]},{"start":{"row":104,"column":0},"end":{"row":104,"column":2},"action":"insert","lines":["# "]},{"start":{"row":105,"column":0},"end":{"row":105,"column":2},"action":"insert","lines":["# "]},{"start":{"row":107,"column":0},"end":{"row":107,"column":2},"action":"insert","lines":["# "]},{"start":{"row":108,"column":0},"end":{"row":108,"column":2},"action":"insert","lines":["# "]},{"start":{"row":110,"column":0},"end":{"row":110,"column":2},"action":"insert","lines":["# "]},{"start":{"row":111,"column":0},"end":{"row":111,"column":2},"action":"insert","lines":["# "]},{"start":{"row":115,"column":0},"end":{"row":115,"column":2},"action":"insert","lines":["# "]}]]},"ace":{"folds":[],"scrolltop":1314,"scrollleft":0,"selection":{"start":{"row":114,"column":4},"end":{"row":114,"column":4},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":207,"mode":"ace/mode/python"}},"timestamp":1564163789653,"hash":"b7f74ca4491a7a9d8d799baabcb7b12d641c2db3"}