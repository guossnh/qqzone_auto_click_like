// ==UserScript==
// @name         qqzone_auto_click_like
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @grant        none
// @include      http://user.qzone.qq.com/*
// @require      http://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js
// ==/UserScript==


function shua_xin_page()
{
   window.location.reload();
}

function qqclick_man(){
    var zan = document.getElementsByClassName("item qz_like_btn_v3");
    for (var i=0,len=zan.length; i<len; i++)
    {
        if (zan[i].text.indexOf("取消赞") === 0){
        continue;
        }
        else{
        zan[i].click();
        }
    }
    window.location.reload();
}

(function() {
    setTimeout(qqclick_man,90000);
})();

