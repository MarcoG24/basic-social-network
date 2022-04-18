fetch('/data-user')
.then(response => response.json())
.then((data) => {
    if (data['type_user'] === 'user') {
        document.getElementById("adminusers").style.display = "none";
    }
}
);

fetch('/get-post')
.then(response => response.json())
.then((posts) => {

    var hits = 0
    var post_top = posts['data'][0]
    posts['data'].forEach(element => {
        if (element['hits'] > hits) {
            hits = element['hits']
            post_top = element
        }
    });
    var section_top = document.getElementById('top-post')
    var full_article_top = document.createDocumentFragment();
    const article_top = create_article(post_top, true);
    full_article_top.appendChild(article_top)
    section_top.appendChild(full_article_top)

    var section  = document.getElementById('posts');
    var fullArticle = document.createDocumentFragment();
    posts['data'].forEach(element => {
        const article = create_article(element, false);
        fullArticle.appendChild(article);

    });
    section.appendChild(fullArticle);
    
}
);

function create_article(element, isTop) {
    
    if (!element['hits']) {
        element['hits'] = 0;
    }
    var article = document.createElement('article');

    var title_post = document.createElement('h3');
    var title_text = element['id'] + '.- ' + element['title_post']
    title_post.appendChild(document.createTextNode(title_text));

    var subtitle = document.createElement('p');
    subtitle.appendChild(document.createTextNode(element['subtitle']));

    var note = document.createElement('p');
    note.appendChild(document.createTextNode(element['note']));

    var hits = document.createElement('h5');
    var hit_element = element['id'] + 'hit'
    hits.setAttribute('id', hit_element);
    hits.appendChild(document.createTextNode(element['hits']+'+'));

    article.appendChild(title_post);
    article.appendChild(hits)
    article.appendChild(subtitle);
    article.appendChild(note);

    if (!isTop) {
        var id_element = element['id'] + '-' + element['hits']
        var ulNote = document.createElement('ul');
        ulNote.setAttribute('class', 'actions');
        var liNote = document.createElement('li');
        var a_note = document.createElement('a');
        
        a_note.setAttribute('class', 'button');
        a_note.setAttribute('id', id_element);
        a_note.setAttribute('onclick', 'updateHits('+element['id']+', '+element['hits']+')');
        a_note.appendChild(document.createTextNode('+1'));

        liNote.appendChild(a_note);
        ulNote.appendChild(liNote)

        article.appendChild(ulNote);
    }
    

    
    return article
}

function updateHits(id, hits) {
    $.ajax({
        url: '/update-hits',
        type: 'POST',
        data: {
            id: id,
            hits: hits+1
        },
        success: function (response) {
        },
        error: function (response) {
        }
    });
    var id_element = id + '-' + hits
    document.getElementById(id_element).style.display = "none";
    window.location.reload();

}