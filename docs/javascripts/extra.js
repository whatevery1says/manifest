/* Handle visibility of scroll to top button */
var toTopBtn = document.getElementById('toTop')

var myScrollFunc = function() {
  var y = window.scrollY
  if (y >= 800) {
    toTopBtn.classList.add('show')
  } else {
    toTopBtn.classList.remove('show')
  }
}

window.addEventListener('scroll', myScrollFunc);

/* Handle click functionality of scroll to top button */
function scrollToTop() {
  const c = document.documentElement.scrollTop || document.body.scrollTop;
  if (c > 0) {
    window.requestAnimationFrame(scrollToTop)
    window.scrollTo(0, c - c / 16)
    document.getElementById('toTop').classList.remove('show')
  }
}

/* Create glossary links -- disabled */
/*
var context = '.md-main'
var exclude = ['code', '.no-gloss']
var terms = ['project', 'module']
var synonyms = {
    'project': 'projects',
    'module': 'modules'
}
var options = {
  'element': 'mark',
  'className': 'glossary',
  'separateWordSearch': true,
  'accuracy': 'exactly',
  'synonyms': synonyms,
  'caseSensitive': true,
  'exclude': exclude,
  'each': function (node) {
    var link = document.createElement('a')
    var glossAnchor = 'glossary/#' + node.innerText
    var url = new URL(window.location)
    url = url.href.split('getting_started/')[0] + 'getting_started/' + glossAnchor
    link.setAttribute('href', url)
    link.innerHTML = node.innerHTML
    node.innerHTML = link.outerHTML
  }
}
var instance = new Mark(context)
instance.mark(terms, options)
*/