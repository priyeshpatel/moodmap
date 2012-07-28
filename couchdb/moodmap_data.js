{
    "_id": "_design/moodmap_data", 
    "_rev": "1-XXX",
    "language": "javascript", 
    "views": {
        "words": {
            "map": "function(doc) {\n  emit(doc[\"word\"], doc[\"value\"]);\n}"
        }
    }
}
