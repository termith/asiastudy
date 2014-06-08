$.fn.highlight = function (b, k) {
 function l() {
     $("." + c.className).each(function (c, e) {
         var a = e.previousSibling,
             d = e.nextSibling,
             b = $(e),
             f = "";
         a && 3 == a.nodeType && (f += a.data, a.parentNode.removeChild(a));
         e.firstChild && (f += e.firstChild.data);
         d && 3 == d.nodeType && (f += d.data, d.parentNode.removeChild(d));
         b.replaceWith(f)
     })
 }

 function h(b) {
     b = b.childNodes;
     for (var e = b.length, a; a = b[--e];)
         if (3 == a.nodeType) {
             if (!/^\s+$/.test(a.data)) {
                 var d = a.data,
                     d = d.replace(m, '<span class="' + c.className + '">$1</span>');
                 $(a).replaceWith(d)
             }
         } else 1 == a.nodeType && a.childNodes && (!/(script|style)/i.test(a.tagName) && a.className != c.className) && h(a)
 }
 var c = {
     split: "\\s+",
     className: "highlight",
     caseSensitive: !1,
     strictly: !1,
     remove: !0
 }, c = $.extend(c, k);
 c.remove && l();
 b = $.trim(b);
 var g = c.strictly ? "" : "\\S*",
     m = RegExp("(" + g + b.replace(RegExp(c.split, "g"), g + "|" + g) + g + ")", (c.caseSensitive ? "" : "i") + "g");
 return this.each(function () {
     b && h(this)
 })
};
$(function () {
$('#Analyze').click(function () {
    var settings = {};
    var pattern = $('#pattern').val();
    $("#right").prop("checked") && (settings.strictly = true);
    pattern && $("div").highlight(pattern, settings)
})
})