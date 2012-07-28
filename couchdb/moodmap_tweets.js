{
    "_id": "_design/moodmap_tweets", 
    "_rev": "1-XXX",
    "language": "javascript", 
    "views": {
        "tweets": {
            "map": "function(doc) {\n  emit(doc.id, [doc.tweet, doc.rating]);\n}"
        }
    }
}
