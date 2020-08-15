function generatePage(link) {
    var goto = document.URL + "/";
    // test what type of link we are given
    var shareButtonIndex = link.indexOf('youtu.be');
    var regularLinkIndex = link.indexOf('?v=');
    if (shareButtonIndex > -1) {
        goto += link.substring(link.indexOf("b/") + 2);
    }
    else if (regularLinkIndex > -1) {
        goto += link.substring(regularLinkIndex + 3);
    }
    window.location.replace(goto);
}