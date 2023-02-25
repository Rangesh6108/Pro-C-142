from flask import Flask, jsonify , request

from storage import all_articles, liked_articles, not_liked_articles
from demographic_filtering import output
from content_filtering import get_recommendations

app=Flask(__name__)


@app.route("/get-article")
def get_articles():
    article_data={
        'url':all_articles[0][11],
        'title':all_articles[0][12] ,
        'text':all_articles[0][13] ,
        'lang':all_articles[0][14],
        'total_events':all_articles[0][15]
    }
    return jsonify({
        "data":article_data,
        "status":"success"
    })

@app.route("/liked-article", methods=["POST"])
def liked_article():
    article = all_articles[0]
    liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/not_liked-article",methods=['POST'])
def not_liked_article():
    article=all_articles[0]
    not_liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status":"success"
    }),201

@app.route('/popular-article')
def popular_article():
    popular_article_data=[]

    for i in output:
        data={
            "url":i[0],
            "title":i[1],
            "text":i[2],
            "lang":i[3],
            "total_events":i[4]
        }
        popular_article_data.append(data)
    return jsonify({
        "data":popular_article_data,
        "status":"success"
    }),200

@app.route("/recommended-article")
def recommended_articles():
    all_recommended = []
    for i in liked_articles:
        output = get_recommendations(i[4])
        for data in output:
            all_recommended.append(data)
    import itertools
    all_recommended.sort()
    all_recommended = list(all_recommended for all_recommended,_ in itertools.groupby(all_recommended))
    article_data = []
    for i in all_recommended:
        _d = {
            "url": i[0],
            "title": i[1],
            "text": i[2],
            "lang": i[3],
            "total_events": i[4]
        }
        article_data.append(_d)
    return jsonify({
        "data": article_data,
        "status": "success"
    }),200
    
if __name__ == "__main__":
    app.run()