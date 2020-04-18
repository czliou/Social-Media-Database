from google.cloud import firestore
# Project ID is determined by the GCLOUD_PROJECT environment variable
db = firestore.Client()

community1_ref = db.collection(u'Community').document(u'community1')
community1_ref.set({
    u'ID': 1341,
    u'hashtag1': "#fun",
    u'hashtag2': "#furry",
    u'hashtag3': "#pet"
})

c1post1_ref = community1_ref.collection(u'Posts').document(u'post1')
c1post1_ref.set({
    u'ID': 1927,
    u'type': 'audio',
    u'data': 'http://',
    u'caption': "Summer in the Bahamas!",
    u'user': 'its.chris',
    u'likes': 2,
    u'userLikes': ['willy5060', 'hunchpunch'],
    u'comments': 1,
    u'userComments': {
        'willy5060': 'Amazing!'
    },
    u'hashtags': ['#fun', '#furry', '#pet', '#summer', '#bahamas']
})

user1_ref = db.collection(u'Users').document(u'User1')
user1_ref.set({
    u'username': 'its.chris',
    u'friends': ['willy5060'],
    u'communities': [1341]
})


users_ref = db.collection(u'Community')
docs = users_ref.stream()

for doc in docs:
    print(u'{} => {}'.format(doc.id, doc.to_dict()))