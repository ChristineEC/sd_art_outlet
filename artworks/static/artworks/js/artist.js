/* Gets the artist id from url to 
allows artists to add artwork for themselves as artist
from their own page */

// const backToArtistPage = document.getElementById("back-to-artist-page")
// const artistCancelAddLinks = document.getElementsByClassName("back-to-artist-page")

var full_url = window.location.pathname;
var url_array = full_url.split('/');
var id = url_array[url_array.length-2];
console.log(id) //This is working


function updateHref() {
    const link = document.getElementById("back-to-artist-page");
    let artistId = id;
    link.href = `artist_page'/${artistId}/`;  // this is all working fine
}

document.addEventListener("DOMContentLoaded", updateHref);

//     for (let link of artistCancelAddLinks) {

//     link.addEventListener("click", (e) => {
//         let artistId = id;
//         console.log(artistId)
//         artistCancelAddLinks.href = `artist_page/${artistId}`;
//     });
// }
// }