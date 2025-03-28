/* Allows redirect back to artist's own page from
the artist's 'add_an_artwork' page upon
hitting the cancel link (button-styled) */

var full_url = window.location.pathname;
var url_array = full_url.split('/');
var id = url_array[url_array.length-2];

function updateHref() {
    const link = document.getElementById("back-to-artist-page");
    let artistId = id;
    link.href = `/artworks/artist/${artistId}/`;
}

document.addEventListener("DOMContentLoaded", updateHref);