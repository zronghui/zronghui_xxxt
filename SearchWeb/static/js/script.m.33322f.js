var e, n, t, r, o, i, a, c, u, s, l, d, m, f, p, y, g, v, h, _, S, q, b, L, E, k, w,
    x = document.querySelector(".search_form"), T = document.querySelector(".search_keywords"),
    M = document.querySelector(".search_options"), A = document.querySelector(".header_aside_slogan"),
    O = window.innerWidth <= 480, H = !!document.querySelector(".hero_search"), C = "//static.lookao.com";
A && (e = document.querySelector(".header_dropdown_modal"), A.onclick = function () {
    e.style.display = "none" === getComputedStyle(e).display ? "block" : "none"
}), x && (!function () {
    function e() {
        x.setAttribute("data-filled", !!T.value)
    }

    e(), T.addEventListener("input", function () {
        e()
    }), T.addEventListener("focus", function () {
        x.setAttribute("input-focus", !0)
    }), T.addEventListener("blur", function () {
        x.setAttribute("input-focus", !1)
    }), document.querySelector(".search_reset").addEventListener("mousedown", function (e) {
        e.preventDefault(), T.value = "", x.setAttribute("data-filled", !1)
    })
}(), n = x.querySelector("ul#suggestList"), t = x.querySelector(".engine_list_wrap"), r = x.querySelector(".suggest_tips"), o = x.querySelector(".active_tips"), i = x.querySelector(".active_engine"), a = {}, c = {}, d = l = s = u = "", p = f = !(m = []), y = function (e) {
    var n = !!e.match(/[一-龥]/), t = [];
    for (var r in a) a[r].grade = distance(n ? a[r].name : r, e), a[r].grade && t.push(a[r]);
    return t.sort(function (e, n) {
        return n.grade - e.grade
    }), 8 < t.length && (t.length = 8), t
}, g = function (e) {
    t.innerHTML = e.map(function (e) {
        var n = C + "/engine/favicons/" + e.shortname + ".png";
        return '<div class="engine_item"><img class="engine_icon" src="' + n + '"><span class ="engine_name">' + e.name + '</span><span class="engine_command">#' + e.shortname + "</span></div>"
    }).join("")
}, v = function () {
    g(m), o.style.display = "none", r.style.display = "block"
}, h = function (e) {
    T.value = "#" + e + " ", _(!1)
}, _ = function (e) {
    n.style.display = e ? "block" : "none"
}, S = function (e) {
    e.preventDefault(), x.removeEventListener("submit", S);
    var n = c.search;
    n = s ? n.replace(/\{key\}/g, encodeURI(s)) : c.hasOwnProperty("home") ? c.home : (n = n.split(/:\/\//, 2))[0] + "://" + n[1].replace(/\/.*$/, "") + "/", location.href = n
}, q = function () {
    var t, e = (u = T.value).indexOf(" ") + 1;
    if (s = e ? u.slice(e) : "", f = "#" === u[0]) {
        p || ((t = new XMLHttpRequest).open("GET", C + "/engine/engine.m.json", !0), t.onload = function (e) {
            for (var n in e = JSON.parse(t.response)) a[n] = e[n], a[n].shortname = n, m.push(a[n]);
            m.length = 8, v(), _(!0), p = !0
        }, t.send());
        var n = u.indexOf(" ");
        l = u.slice(1, -1 === n ? u.length : n), _(!(-1 !== n || !p)), l !== d ? (clearTimeout(y.Timer), y.Timer = setTimeout(function () {
            var e = y(l);
            e.length && (c = e[0], g(e), i.innerHTML = c.name, r.style.display = "none", o.style.display = "block")
        }, 20)) : c.hasOwnProperty("name") ? (c.name !== d && x.addEventListener("submit", S), s || l !== c.name && (l = c.name, h(l))) : x.removeEventListener("submit", S), l || "none" !== r.style.display || v(), d = l
    } else d = "", _(!(c = {})), x.removeEventListener("submit", S)
}, T.oninput = function () {
    q()
}, T.addEventListener("focus", function () {
    f && _(!0)
}), T.addEventListener("blur", function () {
    _(!1)
}), t.addEventListener("mousedown", function (e) {
    e.preventDefault();
    var n = e.target, t = "DIV" === n.tagName ? n : n.parentElement;
    d = t.querySelector(".engine_name").innerText, c = a[t.querySelector(".engine_command").innerText.slice(1)], h(d), x.addEventListener("submit", S)
}), H && !O && x.q.focus()), M && (b = !1, L = document.querySelector(".modular_results_count"), E = document.querySelector(".modular_filter"), k = document.querySelector(".select_time_range"), w = document.querySelector(".select_language"), document.querySelector(".current_time_range").innerHTML = k.options[k.selectedIndex].text, document.querySelector(".current_language").innerHTML = w.options[w.selectedIndex].text, document.querySelector(".option_filter").addEventListener("click", function () {
    L.style.display = b ? "block" : "none", E.style.display = b ? "none" : "block", b = !b
}), E.addEventListener("change", function () {
    var e = document.createElement("input"), n = M.querySelector("form");
    e.type = "hidden", e.name = M.querySelector(".option_category.active").name, e.value = 1, n.appendChild(e), n.submit()
})), function (e) {
    "use strict";

    function n(e, n, t) {
        var r, o, i = 0, a = function (e, n) {
            for (var t in n) n.hasOwnProperty(t) && (e[t] = n[t]);
            return e
        }({caseSensitive: !0}, t);
        if (0 === e.length || 0 === n.length) return 0;
        if (a.caseSensitive || (e = e.toUpperCase(), n = n.toUpperCase()), e === n) return 1;
        var c = Math.floor(Math.max(e.length, n.length) / 2) - 1, u = new Array(e.length), s = new Array(n.length);
        for (r = 0; r < e.length; r++) {
            var l = c <= r ? r - c : 0, d = r + c <= n.length - 1 ? r + c : n.length - 1;
            for (o = l; o <= d; o++) if (!0 !== u[r] && !0 !== s[o] && e[r] === n[o]) {
                ++i, u[r] = s[o] = !0;
                break
            }
        }
        if (0 === i) return 0;
        var m = 0, f = 0;
        for (r = 0; r < e.length; r++) if (!0 === u[r]) {
            for (o = m; o < n.length; o++) if (!0 === s[o]) {
                m = o + 1;
                break
            }
            e[r] !== n[o] && ++f
        }
        var p = (i / e.length + i / n.length + (i - f / 2) / i) / 3, y = 0;
        if (.7 < p) {
            for (; e[y] === n[y] && y < 4;) ++y;
            p += .1 * y * (1 - p)
        }
        return p
    }

    "function" == typeof define && define.amd ? define([], function () {
        return n
    }) : "object" == typeof exports ? module.exports = n : e.distance = n
}(this);