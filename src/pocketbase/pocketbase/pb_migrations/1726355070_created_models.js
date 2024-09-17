/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const collection = new Collection({
    "id": "a2fzai6k0uknqzn",
    "created": "2024-09-14 23:04:30.393Z",
    "updated": "2024-09-14 23:04:30.393Z",
    "name": "models",
    "type": "base",
    "system": false,
    "schema": [
      {
        "system": false,
        "id": "v5mrxuyb",
        "name": "model_lstm_btc",
        "type": "file",
        "required": false,
        "presentable": false,
        "unique": false,
        "options": {
          "mimeTypes": [],
          "thumbs": [],
          "maxSelect": 1,
          "maxSize": 5242880,
          "protected": false
        }
      }
    ],
    "indexes": [],
    "listRule": null,
    "viewRule": null,
    "createRule": null,
    "updateRule": null,
    "deleteRule": null,
    "options": {}
  });

  return Dao(db).saveCollection(collection);
}, (db) => {
  const dao = new Dao(db);
  const collection = dao.findCollectionByNameOrId("a2fzai6k0uknqzn");

  return dao.deleteCollection(collection);
})
