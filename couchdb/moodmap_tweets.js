{
    "_id": "_design/moodmap_tweets", 
    "language": "javascript", 
    "views": {
        "tweets": {
            "map": "function(doc) {\n  emit(doc.id, [doc.tweet, doc.rating]);\n}"
        }
    },
    "validate_doc_update": "function(newDoc, oldDoc, userCtx) { if (userCtx.roles.indexOf('_admin') !== -1 || userCtx.name == \"moodmap\") { return; } else { throw({forbidden: 'You are not authorized to edit this db.'}); } }"
}
