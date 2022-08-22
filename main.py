from elasticsearch import Elasticsearch

from flask_cors import CORS

from flask import Flask

app = Flask(__name__)
cors = CORS(app)

es = Elasticsearch(
    cloud_id="YuvalElastic:dXMtZWFzdC0yLmF3cy5lbGFzdGljLWNsb3VkLmNvbTo0NDMkYjhlOTE3ZjVhMzA0NDg1ZWE2MDVmNWUyNDg4Y2VkMTYkZDYxZWIwZThjMjJlNDgxYWEyY2VmYzc4OGI5NWYyNzc=",
    http_auth=('elastic', 'Gs2YuMmOCM9v03uMlR3J093m')
)


@app.route('/')
@app.route('/clients', methods=['GET'])
def all_clients():
    resp = es.search(index="clients")
    _clients = []
    for i in resp['hits']['hits']:
        clients_dict = i['_source']
        clients_dict['id'] = i['_id']
        _clients.append(clients_dict)
        print(i)
    return _clients


@app.route('/clients/<id>', methods=['GET'])
def all_vehicles(id):
    resp = es.search(index="vehicles", body={
        'query': {
          'match': {
              'company_id': id
        }
    }
})
    _vehicles = []
    for i in resp['hits']['hits']:
        vehicles_dict = i['_source']
        vehicles_dict['_id'] = i['_id']
        _vehicles.append(vehicles_dict)
        print(i)
    return _vehicles


if __name__ == "__main__":
    app.run(debug=True)



