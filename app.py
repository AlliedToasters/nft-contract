from flask import Flask, request, send_file, Response
import json

collection_name = "Unruggable"

description = f"""
The {collection_name}s is the first NFT collection made by the $WGMI (ERC-20) community. \n 
The collection consists of 888 unique {collection_name} pheonixes, which represent how we, as a community, rose from the ashes after the token was initially rugged by its creator. \n 
All royalties from secondary sales of NFTs in this collection will be directed towards supplying liquidity for the $WGMI token, via purchasing ETH/WGMI LP tokens and locking that liquidity away forever by burning those LP tokens.
"""

with open("./metadata.json", "r") as f:
    md = json.loads(f.read())

def get_metadata(id, md=md):
    if not 0 < int(id) < 889:
        return json.dumps({"error":"id is not between 1 and 888"})
    else:
        data = md[str(id)]
        #data["image"] = f"https://ipfs.io/ipfs/bafybeienvbzfs4gvasydbakejf7g2moz75kiqxj5wxso7wqkurworu2gpq/{id}.jpg"
        data["image"] = f"ipfs://bafybeienvbzfs4gvasydbakejf7g2moz75kiqxj5wxso7wqkurworu2gpq/{id}.jpg"
        data["description"] = description
        data["name"] = f"Unruggable #{id}"
        return json.dumps(data)

app = Flask(__name__)

@app.route('/healthcheck')
def healthcheck():
    return 'Healthy!'

@app.route('/metadata')
def metadata():
    id = request.args.get('id')
    data = get_metadata(id)
    return Response(data, mimetype="application/octet-stream")