{
    "_id": "_design/moodmap_data", 
    "language": "javascript", 
    "views": {
        "words": {
            "map": "function(doc) {\n  emit(doc[\"word\"], doc[\"value\"]);\n}"
        }
    }
}
