import pymongo
import pymongo.errors
import logging

class MongoDBConnection():     
    def __init__(self, uri='mongodb+srv://joaofrugis:4293784@goappcluster.u5qlawa.mongodb.net/?retryWrites=true&w=majority&appName=GoAPPCluster', database_name='property-valuation'):
        self.client = pymongo.MongoClient(uri, server_api=pymongo.server_api.ServerApi('1'))
        self.db = self.client[database_name]
        self.logger = logging.getLogger(__name__ + '.' + self.__class__.__name__)
    
    def connect(self):
        try:
            self.client.admin.command('ping')
            self.logger.info('MongoDB Connection Successfully')
        except pymongo.errors.ConnectionFailure as error:
            self.logger.error(f'Connection with MongoDB Failure: {error}')
    
    def disconnect(self):
        self.client.close()
        self.logger.info('MongoDB Disconnect Successfully')

    def get_collection(self, collection: str):
        try:
            return self.db[collection]
        except pymongo.errors.CollectionInvalid as error:
            self.logger.error(error)

    def insert_one_data(self, collection, data):
        try: 
            return collection.insert_one(data)
        except pymongo.errors.OperationFailure as error:
            self.logger.error(f'Error to insert one data: {error}')