String.prototype.replaceAll = function(search, replacement) {
    var target = this;
    return target.split(search).join(replacement);
}
String.prototype.capitalize = function () {
  return this.charAt(0).toLocaleUpperCase('tr-TR') + this.slice(1).toLocaleLowerCase('tr-TR')
}
Array.prototype.insert = function (index, item) {
  this.splice(index, 0, item)
}
Array.prototype.unique = function () {
  var a = this.concat()
  for (var i = 0; i < a.length; ++i) {
    for (var j = i + 1; j < a.length; ++j) {
      if (a[i] === a[j]) { a.splice(j--, 1) }
    }
  }
  return a
}
String.prototype.gfl = function () {
  const dx = []
  this.split(' ').forEach(function (k) {
    dx.push(k.charAt(0).toUpperCase())
  })
  return dx.join('')
}

String.prototype.sfl = function(){
  let parts = this.split(' ')
  if (parts) {
    return parts[0] + ' ' + parts[parts.length-1]
  }
}

Number.prototype.round = function (places) {
  return +(Math.round(this + 'e+' + places) + 'e-' + places)
}

if (!String.prototype.startsWith) {
    Object.defineProperty(String.prototype, 'startsWith', {
        value: function(search, rawPos) {
            var pos = rawPos > 0 ? rawPos|0 : 0;
            return this.substring(pos, pos + search.length) === search;
        }
    });
}

if (!String.prototype.endsWith) {
	String.prototype.endsWith = function(search, this_len) {
		if (this_len === undefined || this_len > this.length) {
			this_len = this.length;
		}
		return this.substring(this_len - search.length, this_len) === search;
	};
}

Array.prototype.move = function (from, to) {
  this.splice(to, 0, this.splice(from, 1)[0])
}

String.prototype.format = function () {
  var i = 0, args = arguments
  return this.replace(/{}/g, function () {
    return typeof args[i] != 'undefined' ? args[i++] : ''
  })
}



/* eslint-enable */
